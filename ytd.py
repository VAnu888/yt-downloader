#import pytube
import pytube
#import sys for exit the program
import sys 

#Run the program continuously
while True:
  
  print()
  print("YouTube Video Downloader")
  print()
  continue_or_exit = input("Do you want to continue:(y/n) ")
  if continue_or_exit == "y":
    url = input("Enter the YouTube video URL: ")
    try:
      youtube = pytube.YouTube(url)

      #Download the video
      stream = video = youtube.streams.get_highest_resolution()

      #Display video informations
      print("Title:", youtube.title)
      print("Author:", youtube.author)
      print("Length:", youtube.length, "secoends")
      print("Rating:", youtube.rating)
      print("Views:", youtube.views)

      print("\nDownloading...")
      stream.download()

      print("Video downloaded successfully!")

    #Display the error
    except Exception as e:
      print("Error:", str(e))

  #Exit the program
  elif continue_or_exit == "n":
    print()
    print("Good Bye!")
    sys.exit()
