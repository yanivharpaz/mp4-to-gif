#!/Users/yaniv/Dropbox/Yaniv_dev/oracle/video/mp4-to-gif/venv/bin/python3
from mp4_to_gif import MP4ToGif

input_file  = '../data/vid01.mp4'
output_file = '../output/vid01.gif'

MP4ToGif.convert(input_file, output_file)
