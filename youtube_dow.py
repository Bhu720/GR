from pytube import YouTube
link = input("Enter Youtube link: " )
yt = YouTube(link)
videos = yt.streams
for i, video in enumerate(videos):
    print(f"{i}: {video}")
try:
    selection = int(input("Enter the number of the stream you want to download: "))
    if 0 <= selection < len(videos):
        videos[selection].download()
        print('Successfully downloaded.')
    else:
        print("Invalid selection. Please enter a valid number.")
except ValueError:
    print("Invalid input. Please enter a number.")
except Exception as e:
    print(f"An error occurred: {e}")
    print("Please try again.")
    




# from pytube import Playlist
# from pytube import YouTube
# bhu = Playlist("https://www.youtube.com/watch?v=pF-h1YCS5GE&list=PLu0W_9lII9agK8pojo23OHiNz3Jm6VQCH&index=1: ")
# print(f'Downloading: {bhu.title}')
# for video in bhu.videos:
#     video.streams.first().download()