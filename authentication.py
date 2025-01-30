python
import os
from googleapiclient.discovery import build
import json

# Prompt user for the path to their credentials JSON file
def get_credentials_path():
    CLIENT_SECRET_FILE = input('Please enter the path to your Google API client secret JSON file (e.g., 
"client_secret.json"): ')
    return CLIENT_SECRET_FILE

# Retrieve credentials from user-provided JSON file
def get_credentials(client_secret_file):
    import google.auth
    credentials = google.auth.service_account.Credentials.from_service_account_file(client_secret_file)
    return credentials

# Main function to build the YouTube API client and execute program logic
def main():
    # Prompt user for path to their credentials JSON file
    CLIENT_SECRET_FILE = get_credentials_path()
    
    # Get credentials from user-provided JSON file
    credentials = get_credentials(CLIENT_SECRET_FILE)
    
    # Build the YouTube API client using user's credentials
    youtube_client = build('youtube', 'v3', credentials=credentials)
    
    # Execute your program logic here
    # For example, you could use the YouTube Data API to perform operations on videos or channels.
    # Note that this is just an example; replace it with your actual program logic.
    video_id = 'your-video-id'  # Replace with your desired video ID
    
    response = youtube_client.channels().list(
        part='contentDetails',
        id=video_id
    ).execute()
    
    print('Video details:')
    for item in response['items']:
        print(f'- Video Title: {item["snippet"]["title"]}')
        print(f'- Video Description: {item["snippet"]["description"]}')
        print(f'- Video Published At: {item["snippet"]["publishedAt"]}')
        print(f'- Video Duration: {item["contentDetails"]["duration"]}')
    
    # Replace the above example with your actual program logic.

if __name__ == '__main__':
    main()
