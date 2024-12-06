from flask import Flask, request, jsonify
from flask_cors import CORS
from jira_service import JiraService

app = Flask(__name__)
CORS(app)

jira_service = JiraService()

@app.route('/api/extract-comments', methods=['POST'])
def extract_comments():
    try:
        data = request.json
        start_date = data.get('startDate')
        end_date = data.get('endDate')
        
        if not start_date or not end_date:
            return jsonify({'success': False, 'error': 'Start date and end date are required'}), 400
            
        result = jira_service.extract_comments(start_date, end_date)
        return jsonify(result)
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

if __name__ == '__main__':
    app.run(port=5000)