from __future__ import print_function

import datetime
import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/calendar.readonly', 'https://www.googleapis.com/auth/calendar.events']


def main():
    """Shows basic usage of the Google Calendar API.
    Prints the start and name of the next 10 events on the user's calendar.
    """
    creds = None
    to_be_del_ev = []
    cal_id = "3fd9jkhommgcej5b4g2r3t91rc@group.calendar.google.com"
    time_min = "2022-11-16T00:00:00+05:30"
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
    try:
        service = build('calendar', 'v3', credentials=creds)

        # Call the Calendar API
        page_token = None
        while True:
          events = service.events().list(calendarId=cal_id,timeMin=time_min, pageToken=page_token, singleEvents=True, orderBy="startTime").execute()
          for event in events['items']:
            print(f"{event['summary']} @ {event['id']}")
            to_be_del_ev.append(event['id'])
          page_token = events.get('nextPageToken')
          if not page_token:
            break
        for ev in to_be_del_ev:
            print("Deleting id: ",ev)
            res = service.events().delete(calendarId=cal_id, eventId=ev).execute()


    except HttpError as error:
        print('An error occurred: %s' % error)


if __name__ == '__main__':
    main()
