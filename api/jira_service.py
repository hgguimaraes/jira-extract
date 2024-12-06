import requests
from datetime import datetime
from config import Config
from text_utils import normalize_text, extract_text

class JiraService:
    def __init__(self):
        Config.validate()
        self.domain = Config.JIRA_DOMAIN
        self.username = Config.JIRA_USERNAME
        self.api_token = Config.JIRA_API_TOKEN
        self.api_endpoint = f"{self.domain}/rest/api/3/search"
        
    def extract_comments(self, start_date, end_date):
        try:
            jql_query = f'created >= "{start_date}" AND created <= "{end_date}" OR updated >= "{start_date}" AND updated <= "{end_date}"'
            
            headers = {
                "Accept": "application/json",
                "Content-Type": "application/json",
            }
            
            payload = {
                "jql": jql_query,
                "fields": ["summary", "comment"],
                "maxResults": 50,
            }
            
            response = requests.post(
                self.api_endpoint,
                headers=headers,
                auth=(self.username, self.api_token),
                json=payload,
            )
            
            if response.status_code != 200:
                return {
                    'success': False,
                    'error': f'Jira API Error: {response.status_code}'
                }
                
            data = response.json()
            filename = self._save_to_csv(data, start_date, end_date)
            
            return {
                'success': True,
                'message': f'Data exported successfully to {filename}',
                'filename': filename
            }
            
        except requests.exceptions.RequestException as e:
            return {
                'success': False,
                'error': f'Network error: {str(e)}'
            }
        except Exception as e:
            return {
                'success': False,
                'error': f'Unexpected error: {str(e)}'
            }
            
    def _save_to_csv(self, data, start_date, end_date, filename="jira_filtered_comments.csv"):
        import csv
        from datetime import datetime
        
        start = datetime.strptime(start_date, "%Y-%m-%d")
        end = datetime.strptime(end_date, "%Y-%m-%d")
        
        with open(filename, mode="w", encoding="utf-8", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Issue Key", "Title", "Comment Date", "Comment"])
            
            for issue in data.get("issues", []):
                key = issue.get("key", "")
                title = normalize_text(issue["fields"].get("summary", ""))
                comments = issue["fields"].get("comment", {}).get("comments", [])
                
                for comment in comments:
                    comment_body = normalize_text(extract_text(comment["body"]))
                    comment_date = datetime.strptime(comment["created"][:10], "%Y-%m-%d")
                    
                    if start <= comment_date <= end:
                        formatted_date = comment_date.strftime("%d/%m/%Y")
                        writer.writerow([key, title, formatted_date, comment_body])
                        
        return filename