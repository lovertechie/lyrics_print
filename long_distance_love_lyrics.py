import time
import sys

def print_lyrics():
    if sys.platform =="win32":
         output_stream =open(sys.stdout.fileno(), mode='w', encoding='utf-8', buffering=1)
    else:
         output_stream =sys.stdout

    lyrics = [
        "Eto Shunnota, E Mone Rakhi Je Ami. ❤",
        "Dekhe Na Keu To Ar,🙃",
        "Bole Eshobi.. Paglami. 😅",
        "Kate Na Jamini,🌙",
        "Biroho Jeno Kete Jaye. 💕",
        "Thame Na... Borosha, 🌧",
        "Tomare Daki Je Ami.✨",

    ]

    delays = [1.0, 1.0, 0.8, 0.8, 0.9, 0.8, 0.8, 0.9, 0.3]
    print("Long Distance Love:\n")
    time.sleep(1.2)
    
    for i, line in enumerate(lyrics):
            for char in line:
                output_stream.write(char)
                output_stream.flush()
                time.sleep(0.068)
            print()
            time.sleep(delays[i])

print_lyrics()

