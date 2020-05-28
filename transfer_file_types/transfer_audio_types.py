import pydub
# from pydub import AudioSegment

#####################Transfer one file
# 导入os模块
import os

# 定义输入文件路径（其中r是转义字符，为了让 \ 不起作用）
path_in = r'C:\Users\pc\Desktop\project\m4a\Record_sample.m4a'
# 定义输出文件路径
path_out = r'C:\Users\pc\Desktop\project\m4a\Record_sample.wav'
# 拼接cmd下的命令
cmd = 'C:/Users/pc/Downloads/ffmpeg-20200527-8b5ffae-win64-static/ffmpeg-20200527-8b5ffae-win64-static/bin/ffmpeg -i '+path_in+' '+path_out
# 执行cmd命令
os.system(cmd)

########################Transfer all files in a folder

import os
#folder path
m4a_path = "C:/Users/pc/Desktop/project/m4a/"

m4a_file = os.listdir(m4a_path)
#because here I have not added this root to the environment variable, so I use the absolute path here.
for i, m4a in enumerate(m4a_file):
    os.system("C:/Users/pc/Downloads/ffmpeg-20200527-8b5ffae-win64-static/ffmpeg-20200527-8b5ffae-win64-static/bin/ffmpeg -i "+ m4a_path + m4a 
    + " " + m4a_path + str(i) + ".wav" )# ffmpeg 可以用来处理视频和音频文件

