# 对比TextRank和Tf-idf
###
## 实验对比小数据下Text-rank和tf-idf的效果
### 
## 结果如下：
1. 使用text-rank：['文件', '词语', '数学公式', '例子', '频率', '母牛', '集里', '总数', '次数', '逆向']
2. 使用tf-idf['文件', '母牛', '词语', '词频', '份文件', '数学公式', '频率', '总数', '集里', '逆向']
3. 总结：结果发现在对单一的文档进行关键词提取的实验时，结果是差不多的，text-rank稍好一些。
4. 可能原因是在小样本数据中，text-rank不需要训练，自己迭代就可以产生关键字,Tf-idf需要大文本训练
