import json
from bert_score import score
import jieba
from rouge_chinese import Rouge
from tqdm import tqdm
data=[]
rouge=Rouge()
score1=[]
score2=[]
scorel=[]
refs=[]
with open(r'E:\Postgraduate\scientific\2022\baseline\LED-3\result.jsonl', 'r', encoding='utf-8') as f:
    for line in f:
        # data.append(line.replace(" ",""))
        datas=json.loads(line)
        data.append([datas['summary'],datas['target']])
for res in tqdm(data):
        hyp=' '.join(jieba.cut(res[0]))
        # hyp=' '.join(i for i in res[0])
        ref=' '.join(jieba.cut(res[1]))
        # ref=' '.join(i for i in res[1])
        score1.append(rouge.get_scores(hyps=hyp,refs=ref)[0]['rouge-1']['f'])
        score2.append(rouge.get_scores(hyps=hyp,refs=ref)[0]['rouge-2']['f'])
        scorel.append(rouge.get_scores(hyps=hyp,refs=ref)[0]['rouge-l']['f'])
print(f"Rouge-1:{sum(score1)/len(score1)}")
print(f"Rouge-2:{sum(score2)/len(score2)}")
print(f"Rouge-l:{sum(scorel)/len(scorel)}")
print(len(score1))
# P, R, F1 = score(data, refs, lang="zh", verbose=True)

# print(f"System level F1 score: {F1.mean():.3f}")