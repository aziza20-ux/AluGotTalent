import re
from flask import flash

def convert_to_embed_url(url_string):
    """
    Converts standard YouTube watch URLs or short URLs to the embed URL format.
    """
    if not url_string:
        return ""

    # 1. Check for the standard watch URL format: ...?v=VIDEO_ID
    watch_match = re.search(r'v=([a-zA-Z0-9_-]{11})', url_string)
    if watch_match:
        video_id = watch_match.group(1)
        return f"https://www.youtube.com/embed/{video_id}"

    # 2. Check for the short URL format: https://youtu.be/VIDEO_ID
    short_match = re.search(r'youtu\.be/([a-zA-Z0-9_-]{11})', url_string)
    if short_match:
        video_id = short_match.group(1)
        return f"https://www.youtube.com/embed/{video_id}"
    flash('format not supported!', 'danger')
    # 3. If it already looks like an embed URL, or other, return it as is.
    return url_string