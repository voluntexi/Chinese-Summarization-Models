# -*- coding: utf-8 -*-
from summarizer.bert_parent import BertParent
from summarizer.cluster_features import ClusterFeatures
from summarizer.sentence_handler import SentenceHandler
import jieba
class ModelProcessor(object):

    def __init__(self, bert_path=r'E:\Postgraduate\scientific\2022\model\bertmodel', min_length=40, max_length=256, pca_k=None, random_state=12345):
        """
        :param bert_path: The string path for the pretrained bert model.
        :param min_length: The minimum length a sentence should be to be considered.
        :param max_length: The maximum length a sentence should be to be considered.
        :param pca_k: If you want the features to be ran through pca, this is the components number.
        :param random_state: Random state.
        """
        self.model = BertParent(bert_path)
        self.sentence_handler = SentenceHandler(min_length, max_length)
        self.cluster_features = ClusterFeatures(pca_k, random_state)

    def cluster_runner(self, content, num_sentences, ratio):
        hidden = self.model(content)
        hidden_args = self.cluster_features(hidden, num_sentences, ratio)
        sentences = [content[j] for j in hidden_args]        
        return sentences

    def run(self, doc, num_sentences, ratio):   
        sentences = self.sentence_handler(doc)
        if sentences:
            sentences = self.cluster_runner(sentences, num_sentences, ratio)
        return '。'.join(sentences)

    def __call__(self, doc, num_sentences=None, ratio=0.1):
        return self.run(doc, num_sentences, ratio)