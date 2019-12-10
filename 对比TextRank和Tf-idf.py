import jieba
import jieba.analyse
file_name = "test.txt"
content = open(file_name, 'r',encoding='utf-8').read()
# content = '酒店的床真不错，房间也合适'
# topK表示输出多少个关键词,withWeight表示是否输出权重，如果想要获取权重,for x,w并将withWeight=True
# allowPOS表示输出的词性
# print(content)
# 只保留名词
print('使用text-rank')
dic = jieba.analyse.textrank(content, topK=10, withWeight=False, allowPOS=('n'))
print(dic)
print('使用tf-idf')
content = open(file_name, 'r',encoding='utf-8').read()
# 10表示输出的前10个
tags = jieba.analyse.extract_tags(content, topK=10,withWeight=False,allowPOS=('n'))
print(tags)
