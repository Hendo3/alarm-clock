from youtube_dl import YoutubeDL

audio_downloader = YoutubeDL({"format":"bestaudio"})

while True:
    try:
        print("Youtuber Downloader".center(40, "_"))

        url = input("Enter youtube URL: ")
        audio_downloader.extract_info(url)
    except Exception as e:
        print(e)
        print("Error")
    
    finally:
        option = int(input("1- Download again\n2- Exit\n> "))
        if option !=1:
            break