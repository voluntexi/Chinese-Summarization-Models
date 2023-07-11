import json
from tqdm import tqdm
from model_processors import ModelProcessor
if __name__ == '__main__':
    data=[]
    with open(r'..\data\example.json','r',encoding='utf-8') as f:
        for ff in f:
            data.append(json.loads(ff))
    for doc in tqdm(data):
        text=doc['text']
        target=doc['summary']
        summart=target
        summarizer = ModelProcessor()
        result=summarizer(text, 1)
        res={}
        res["summary"] = result
        res['target'] = summart
        new = json.dumps(res, ensure_ascii=False)
        with open('./result.json', "a", encoding="utf8") as jsonw:
            jsonw.write(new + "\n")
