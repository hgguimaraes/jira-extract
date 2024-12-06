import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    JIRA_DOMAIN = os.getenv('JIRA_DOMAIN')
    JIRA_USERNAME = os.getenv('JIRA_USERNAME')
    JIRA_API_TOKEN = os.getenv('JIRA_API_TOKEN')
    
    @staticmethod
    def validate():
        required_vars = ['JIRA_DOMAIN', 'JIRA_USERNAME', 'JIRA_API_TOKEN']
        missing = [var for var in required_vars if not getattr(Config, var)]
        
        if missing:
            raise ValueError(f"Missing required environment variables: {', '.join(missing)}")