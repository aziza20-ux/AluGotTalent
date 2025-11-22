import re
from flask import flash

def convert_to_embed_url(url_string):
    """
    Converts YouTube watch URLs, short URLs, and Shorts URLs to embed format.
    """
    if not url_string:
        return ""

    # 1. Standard watch URL: ...?v=VIDEO_ID
    watch_match = re.search(r'v=([a-zA-Z0-9_-]{11})', url_string)
    if watch_match:
        video_id = watch_match.group(1)
        return f"https://www.youtube.com/embed/{video_id}"

    # 2. Short URL: https://youtu.be/VIDEO_ID
    short_match = re.search(r'youtu\.be/([a-zA-Z0-9_-]{11})', url_string)
    if short_match:
        video_id = short_match.group(1)
        return f"https://www.youtube.com/embed/{video_id}"

    # 3. YouTube Shorts URL: https://youtube.com/shorts/VIDEO_ID
    shorts_match = re.search(r'shorts/([a-zA-Z0-9_-]{11})', url_string)
    if shorts_match:
        video_id = shorts_match.group(1)
        return f"https://www.youtube.com/embed/{video_id}"

    # 4. Already an embed or unsupported
    flash('format not supported! and it will not show embed it or allow embed option', 'danger')

    return url_string
"""
if __name__ =='__main__':
    print(convert_to_embed_url('https://youtu.be/r1Fx0tqK5Z4?si=JrJzbhx5oKlQSs82'))
    print(convert_to_embed_url('https://youtu.be/LOpya2xwpx0'))
    print(convert_to_embed_url('https://youtube.com/shorts/tjxAHnbOEXA?si=chf039gPqMdaDs8H'))
    print(convert_to_embed_url(''))
"""
