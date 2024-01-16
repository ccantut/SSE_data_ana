from pathlib import Path
import json, pandas as pd
list_1=[]
list_2=[]
s=s_j=''

# SSE record
f=Path("/Users/ann/Desktop/SSE_data_ana/response.txt") 
# export 檔案
output=Path("/Users/ann/Desktop/SSE_data_ana/output.txt") 
output_j=Path("//Users/ann/Desktop/SSE_data_ana/output_j.txt") 

txt=f.read_text(encoding="UTF-8")
txt=txt.split('\n')

#有 records 的資料存入 list_1
for i in txt:
	if 'data' in i :
		i=i.split('data: ')[1]
		if len(i)>0:
			# i=i[1:-1]
			list_1.append(i)

#把每一筆資料轉成json, 再存入list_2
for j in list_1:
	b=json.loads(j)
	list_2.append(b)

for k in list_2:
	# print(k)
	for l in k:
		l=str(l)
		s=s+l+'\n'+'---------------'+'\n'
		s_j=s_j+l+','

# export as output.txt 文字檔
output.write_text(s,encoding="UTF-8")

# export as output.txt json格式
s_j='['+s_j+']'
output_j.write_text(s_j,encoding="UTF-8")

