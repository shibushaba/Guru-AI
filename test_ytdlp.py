from yt_dlp import YoutubeDL

ydl_opts = {'quiet': True, 'extract_flat': True, 'force_generic_extractor': False}
with YoutubeDL(ydl_opts) as ydl:
    info = ydl.extract_info("ytsearch1:React tutorial", download=False)
    if 'entries' in info and info['entries']:
        print("Found:", info['entries'][0]['title'])
        print("URL:", info['entries'][0]['url'])
    else:
        print("No results")
