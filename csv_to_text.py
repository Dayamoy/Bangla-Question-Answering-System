import pandas as pd

data = pd.read_csv('sust.csv')

ques = data['question']
ans = data['answer']

file = open("output.txt","w",encoding='utf-8')

print(data.shape)
sz = data.shape
print(sz)
for i in range(ques.size):
      file.write("---"+ques[i]+"\n")
      file.write("-"+ans[i]+"\n")


