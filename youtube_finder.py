import subprocess

def get_best_video(topic, mode="fast"):

    query = f"ytsearch5:{topic} tutorial"

    cmd = [
        "yt-dlp",
        query,
        "--print",
        "%(title)s|||%(duration)s|||%(webpage_url)s",
        "--no-download"
    ]

    try:
        result = subprocess.run(cmd, capture_output=True, text=True)
        lines = result.stdout.strip().split("\n")
    except Exception as e:
        print(f"Error running yt-dlp: {e}")
        return None

    fallback = None

    for line in lines:
        try:
            if not line.strip(): continue
            parts = line.split("|||")
            if len(parts) != 3: continue
            
            title, duration, url = parts
            duration = int(duration)
            
            video_data = {"title": title, "url": url}
            
            # Save the first valid video as fallback
            if fallback is None:
                fallback = video_data

            if mode == "fast" and duration <= 1200:
                return video_data

            if mode == "deep" and duration > 1200:
                return video_data

        except Exception:
            continue

    return fallback