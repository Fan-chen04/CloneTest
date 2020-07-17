import jieba
from wordcloud import WordCloud
import PIL.Image as image
import numpy as np

# 创建停用词列表
stopwords = [line.strip() for line in open('D:\works\stop_words.txt',encoding='UTF-8').readlines()]

# 对句子进行中文分词
def seg_depart(sentence):
    # 创建停用词列表
    stopwords = [line.strip() for line in open('D:\works\stop_words.txt',encoding='UTF-8').readlines()]
    # 对文档中的每一行进行中文分词
    sentence_depart = jieba.cut(sentence.strip())
    outstr = ''
    # 去停用词
    for word in sentence_depart:
        if word not in stopwords:
            if word != '\t':
                outstr += word
                outstr += " "
    return outstr

# 给出文档路径
filename = "D:\works\iGuo.txt"
outfilename = "D:\works\iGuo_clear.txt"
inputs = open(filename, 'r', encoding='utf-8')
outputs = open(outfilename, 'w', encoding='utf-8')

# 将清洗结果写入iGuo_clear.txt中
print("-------------------正在分词和去停用词-------------------")
for line in inputs:
    line_seg = seg_depart(line)
    outputs.write(line_seg + '\n')
outputs.close()
inputs.close()
print("删除停用词和分词成功！！！")

#将文本里的词汇做成词典，并记录频数
with open("D:\works\iGuo_clear.txt",encoding="utf-8") as fp:
    text = fp.read()
    word_list = jieba.lcut(text)
    counts = {}
    for word in word_list:           
        if word != ' ' and word != '\n':
            counts[word] = counts.get(word,0) + 1
    items = list(counts.items())
    items.sort(key=lambda x:x[1], reverse=True) 
#显示频数
#    for i in range(15):
#        word, count = items[i]
#        print ("{0:<10}{1:>5}".format(word, count))

    # 读入模板
    mask = np.array(image.open("D:\works\Logo.jpg"))
    wordcloud = WordCloud(
        # 添加遮罩层
        scale = 4,
        mask=mask,
        font_path = "C:\Windows\Fonts\SimHei.ttf",
        background_color='white')

    wordcloud.generate_from_frequencies(counts) #根据词频生成词云
    image_produce = wordcloud.to_image()
    image_produce.show()
    wordcloud.to_file('word_cloud.jpg') # 保存词云图片
