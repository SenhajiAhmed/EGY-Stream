import subprocess

# URL of the .m3u8 playlist
m3u8_url = "https://s001.mogcdn.com/hls/777074f4-d33c-4262-a828-b3b4800f68ea/daf75db2-5248-4c3f-bd02-78317c7b6cdf-828.m3u8"

# Call mpv to play the stream
subprocess.run(["mpv", m3u8_url])
