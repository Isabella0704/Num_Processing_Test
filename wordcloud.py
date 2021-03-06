#第一段，是对红楼梦的全文本分词，注意红楼梦.txt要保存为UTF-8编码格式，并与python文件保存在同一个文件夹下
#注意中文的词云要加入font_path="simsun.ttf"
import jieba
from wordcloud import WordCloud
import matplotlib.pyplot as plt
file1 = "a_dream_in_red_mansions.txt"
mytext = open(file1, encoding='utf-8',errors='ignore').read()
mytext = " ".join(jieba.cut(mytext))
wordcloud = WordCloud(font_path="simsun.ttf").generate(mytext)
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")

#第二段，是采用TF-IDF关键词频率算法，将常见词去除之后，保留专有词的结果
import jieba
import jieba.analyse
from wordcloud import WordCloud
import matplotlib.pyplot as plt
file1 = "a_dream_in_red_mansions.txt"
mytext = open(file1, encoding='utf-8',errors='ignore').read()
mytext = " ".join(jieba.analyse.extract_tags(mytext, topK=300))
wordcloud = WordCloud(font_path="simsun.ttf").generate(mytext)
#%pylab inline
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
