import pafy

# Create a video instance from a YouTube URL
url = input("Enter YouTube Link: ")
video = pafy.new(url)

# Prints the video title
print("\n" + "Title of Video: " + video.title + "\n")

print("Author of Video: " + video.author + "\n")

print("Total View Count: " + str(video.viewcount) + "\n")

print("Number of Likes: " + str(video.likes) + "\n")

# Function not working due to Youtube/Google API quota limit 
# print("Video Description: " + video.description + "\n")

print("Available streams for Video:")
streams = video.streams
for s in streams:
	print(s)
print()

# print("All Formats, file-sizes, and download URLS:")
# for s in streams: 
# 	print(s.resolution, s.extension, s.get_filesize(), s.url)
