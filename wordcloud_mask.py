"""
Masked wordcloud
================
Using a mask you can generate wordclouds in arbitrary shapes.
如果在jupyter notebook中运行，记得把alice文件放到同一目录下
"""

from os import path
#from PIL import Image #这一行隐藏了不影响效果，主要是这个库pip无法下载
import numpy as np
import matplotlib.pyplot as plt
import os

from wordcloud import WordCloud, STOPWORDS

# get data directory (using getcwd() is needed to support running example in generated IPython notebook)
d = path.dirname(__file__) if "__file__" in locals() else os.getcwd()

# Read the whole text.
#原先是open(path.join())，但由于这种方式无法加入encoding参数，改为直接open，由于图片文件在同一文件夹下，没有报错
text = open('a_dream_in_red_mansions.txt', encoding='utf-8').read() 

# read the mask image
# taken from
# http://www.stencilry.org/stencils/movies/alice%20in%20wonderland/255fk.jpg
#目前该网址已失效
alice_mask = np.array(Image.open(path.join(d, "alice_mask.png")))

stopwords = set(STOPWORDS)
stopwords.add("said")

wc = WordCloud(font_path="simsun.ttf", width=2000, height=1000,background_color="white", max_words=2000, mask=alice_mask,
               stopwords=stopwords, contour_width=0.2, contour_color='grey')

# generate word cloud
wc.generate(text)

# store to file
wc.to_file(path.join(d, "alice.png"))

# show
#plt.imshow(wc, interpolation='bilinear') #这种方式会输出两张图片，第一个其实没必要
plt.axis("off")
plt.figure(figsize=(15,15)) #增加了对图片大小的调节，默认的图片较小
plt.imshow(wc, cmap=plt.cm.gray, interpolation='bilinear') #cmap即colormap
plt.axis("off")
plt.show()
