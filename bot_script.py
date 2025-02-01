import time
from googleapiclient.errors import HttpError

def perform_actions_on_videos(youtube_client, videos):
    """
    This function performs actions on the videos, including watching, liking, and commenting.
    """
    for video in videos:
        video_id = video['video_id']
        video_title = video['title']
        
        print(f"Processing video: {video_title} (ID: {video_id})")
        
        # Get video duration
        duration = get_video_duration(youtube_client, video_id)
        if duration:
            print(f"Video duration: {duration} seconds")
            
            # Simulate watching the video
            watch_video(duration)
            
            # Like the video
            like_video(youtube_client, video_id)
            
            # Comment on the video
            comment_on_video(youtube_client, video_id, "Super cool! Love the content.")
        else:
            print("Skipping video due to missing duration.")

def get_video_duration(youtube_client, video_id):
    """
    Retrieve the duration of a video in seconds.
    """
    try:
        request = youtube_client.videos().list(
            part='contentDetails',
            id=video_id
        )
        response = request.execute()
        
        if response['items']:
            duration_iso = response['items'][0]['contentDetails']['duration']
            # Convert ISO 8601 duration to seconds
            return iso_duration_to_seconds(duration_iso)
        else:
            return None
    except HttpError as e:
        print(f"Error retrieving video duration: {e}")
        return None

def iso_duration_to_seconds(duration):
    """
    Convert ISO 8601 duration format to seconds.
    """
    import isodate
    return int(isodate.parse_duration(duration).total_seconds())

def watch_video(duration):
    """
    Simulate watching a video by waiting for its duration.
    """
    print(f"Watching video for {duration} seconds...")
    time.sleep(duration)
    print("Finished watching the video.")

def like_video(youtube_client, video_id):
    """
    Like a video using the YouTube API.
    """
    try:
        youtube_client.videos().rate(
            id=video_id,
            rating='like'
        ).execute()
        print("Liked the video.")
    except HttpError as e:
        print(f"Error liking the video: {e}")

def comment_on_video(youtube_client, video_id, comment_text):
    """
    Post a comment on a video using the YouTube API.
    """
    try:
        youtube_client.commentThreads().insert(
            part='snippet',
            body={
                'snippet': {
                    'videoId': video_id,
                    'topLevelComment': {
                        'snippet': {
                            'textOriginal': comment_text
                        }
                    }
                }
            }
        ).execute()
        print("Commented on the video.")
    except HttpError as e:
        print(f"Error commenting on the video: {e}")
