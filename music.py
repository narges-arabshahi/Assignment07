from moviepy import editor

video=editor.VideoFileClip('batel.mp4')
print("start")
video.audio.write_audiofile('batel.mp3')
print("end")
video.close()



