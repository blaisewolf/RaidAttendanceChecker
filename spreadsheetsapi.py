import os.path
import json

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

SCOPES = ["https://www.googleapis.com/auth/spreadsheets.readonly"]

def main():
    credentials = None
    if os.path.exists("token.json"):
        credentials = Credentials.from_authorized_user_file("token.json", SCOPES)
    if not credentials or not credentials.valid:
        if credentials and credentials.expired and credentials.refresh_token:
            credentials.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file("credentials.json", SCOPES)
            credentials = flow.run_local_server(port=0)
        with open("token.json", "w") as token:
            token.write(credentials.to_json())
    
    try:
        service = build("sheets", "v4", credentials=credentials)

        spreadsheet_data = None
        with open("spreadsheetData.json", "r") as json_file:
            spreadsheet_data = json.load(json_file)

        sheet = service.spreadsheets()
        result = sheet.values().get(spreadsheetId=spreadsheet_data["id"], range=spreadsheet_data["range"]).execute()
        values = result.get("values", [])
        if not values:
            print("No data")
            return
        for row in values:
            print(f"{row[0]}, {row[1]}")        

    except HttpError as error:
        print(error)

main()