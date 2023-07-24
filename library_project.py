
#install schedule:{pip install schedule}

'''
import schedule
import time
def job():
        print("I'm working...")
schedule.every(4).seconds.do(job)
while True:
        schedule.run_pending()
        time.sleep(2)

'''
#_____________________________#
#download video from youtube:(in code file)
'''
from pytube import YouTube

def download_video(url, output_path=None):
    try:
        # Create a YouTube object
        yt = YouTube(url)

        # Get the highest resolution stream available
        stream = yt.streams.get_highest_resolution()

        # Set the output path if provided, otherwise use the default path
        output_path = output_path if output_path else "./downloads/"

        # Download the video
        print("Downloading...")
        stream.download(output_path)

        print("Download successful!")
    except Exception as e:
        print("An error occurred:", str(e))

if __name__ == "__main__":
    video_url = "https://www.youtube.com/watch?v=YDz6QwcnRdk&ab_channel=CodingCart"
    download_video(video_url)
'''
#_____________________________#

# create notification 
'''
from plyer import notification

def show_notification(title, message):
    notification.notify(
        title=title,
        message=message,
        app_icon=None,  # You can specify an icon file path if needed
        timeout=10  # Duration in seconds for how long the notification will stay visible
    )

if __name__ == "__main__":
    notification_title = "Sample Notification"
    notification_message = "This is a sample notification from Python using plyer."

    show_notification(notification_title, notification_message)
'''
#___________________________#
#notification + schedule:
'''
from plyer import notification
import schedule
import time
def job():
         notification.notify(
        title="اذكر الله",
        message="اللهم صل على محمد وعلى آله وصحبه وسلم")
schedule.every(100).seconds.do(job)
while True:
        schedule.run_pending()
        time.sleep(1)
'''



