import yt_dlp

def get_best_video(topic, mode="fast"):
    """
    Searches for a video on YouTube using yt-dlp.
    'mode' was used for scoring in the old version, but with yt-dlp
    we can trust the search relevance for "topic + tutorial".
    We can add keywords to the query based on mode if needed.
    """
    
    query = f"{topic} tutorial"
    
    # Adjust query based on mode for better relevance
    if mode == "fast":
        query += " crash course"
    elif mode == "deep":
        query += " full course"

    ydl_opts = {
        'quiet': True,
        'extract_flat': True,  # Don't download, just get metadata
        'force_generic_extractor': False,
        'noplaylist': True,
        'playlist_items': '1', # Max 1 result needed
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            # ytsearchN:query searches for N results
            info = ydl.extract_info(f"ytsearch1:{query}", download=False)
            
            if 'entries' in info and info['entries']:
                video = info['entries'][0]
                return {
                    "title": video['title'],
                    "url": video['url'], # yt-dlp usually returns the video ID or full URL
                    "thumbnail": video.get('thumbnail')
                }
            else:
                return None
    except Exception as e:
        print(f"yt-dlp search failed: {e}")
        return None

