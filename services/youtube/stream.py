import pafy

YOUTUBE_VIDEO_URL = "https://www.youtube.com/watch?v="

def get(youtube_id):
    try:
        url = YOUTUBE_VIDEO_URL + youtube_id
        video = pafy.new(url)
        stream = video.getbestaudio()
        stream.video = video
        return stream
    except:
        # This lib is so weird its risky to assume the errors it can raise
        return None