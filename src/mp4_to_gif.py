import moviepy.editor as mpy

class MP4ToGif:
    def __init__(self, mp4_path, gif_path):
        self.mp4_path = mp4_path
        self.gif_path = gif_path

    @staticmethod
    def convert(mp4_path, gif_path):
        clip = mpy.VideoFileClip(mp4_path)
        clip.resize(width=100).write_gif(gif_path)
        # clip.write_gif(gif_path)



