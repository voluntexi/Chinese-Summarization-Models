# Chinese-Summarization-Models
 The purpose of this repository is to better train,finetune and use text summary models in Chinese datasets

### Aiming to implement the following models

- [x] LED-3:一种抽取式摘要模型，其根据句子 在文章中的位置来抽取摘要。选取文本的前三句作为摘要。通常来说，文本摘要常出现在开 头。尽管 LEAD 算法简单，但通常能够概括文本 的主要信息。
- [x] Bert-extractive-summarizer:一种抽取式摘要模型，将文本分 割为句子，然后利用 Bert 生成句向量。接着使用 K-Means 算法对这些句向量进行聚类，在每个聚 类中选取与该聚类中心距离最近的句向量，将这 K 个句向量所对应的句子作为文本的摘要。

- [ ] BART+finetune
- [ ] CPT+finetune
- [ ] Pegasus+finetune