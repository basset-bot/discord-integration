import pafy

YOUTUBE_VIDEO_URL = "https://www.youtube.com/watch?v="

def get_stream(youtube_id):
    url = YOUTUBE_VIDEO_URL + youtube_id
    video = pafy.new(url)
    stream = video.getbestaudio()
    stream.video = video
    return stream