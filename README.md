# Jira Comments Extractor

This application allows you to extract comments from Jira issues within a specified date range.

## Prerequisites

- Node.js (v16 or higher)
- Python (v3.7 or higher)
- Visual Studio Code (recommended)

## Setup Instructions

1. Clone the repository
2. Set up the backend:
   ```bash
   cd api
   cp .env.example .env  # Update with your Jira credentials
   python -m venv venv
   source venv/bin/activate  # On Windows use: .\venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. Set up the frontend:
   ```bash
   cp .env.example .env
   npm install
   ```

4. Start the development servers:
   ```bash
   # Terminal 1 - Backend
   npm run start-api

   # Terminal 2 - Frontend
   npm run dev
   ```

## Environment Variables

### Backend (.env)
- JIRA_DOMAIN - Your Jira domain (e.g., https://your-company.atlassian.net)
- JIRA_USERNAME - Your Jira email
- JIRA_API_TOKEN - Your Jira API token

### Frontend (.env)
- VITE_API_URL - Backend API URL (default: http://localhost:5000/api)

## Usage

1. Open the application in your browser
2. Enter the start and end dates in DD/MM/YYYY format
3. Click "Extract Comments"
4. The extracted comments will be saved to a CSV file

## Features

- Date range validation
- Error handling for network issues
- Progress indication during extraction
- Success/error notifications
- CSV export of comments