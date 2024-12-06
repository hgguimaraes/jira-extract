import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    JIRA_DOMAIN = os.getenv('https://sofintech.atlassian.net')
    JIRA_USERNAME = os.getenv('higor.guimaraes@sofintech.com.br')
    JIRA_API_TOKEN = os.getenv('ATATT3xFfGF0uZ9oTNE525ssnixOhbAGX05PsQ4czz6t7TrgxsFBWDWOjCC9TVl25zATWE_roh_LSahhzZhyJjSFrxoNH8O_yoslHhYoR-4F_K35azrR0pqyC8GhJjo7z2Iy45oyO9NA0dgZXCDgVMTlDhWAx0D_3ZcVS13IMCxh04lwuNJktPg=1F1DC2B3')
    
    @staticmethod
    def validate():
        required_vars = ['JIRA_DOMAIN', 'JIRA_USERNAME', 'JIRA_API_TOKEN']
        missing = [var for var in required_vars if not getattr(Config, var)]
        
        if missing:
            raise ValueError(f"Missing required environment variables: {', '.join(missing)}")
