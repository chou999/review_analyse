data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line.strip())
		count += 1 # count = count + 1
		if count % 1000 == 0:
			print(count)
print('檔案讀取完了，總共有', len(data), '筆資料')

sum_len = 0
for d in data:
	sum_len += len(d) # sum_len = sum_len + len(d)

print('留言的平均長度為', sum_len/len(data))

new = []
for d in data:
	if len(d) < 100:
		new.append(d)
print('一共有', len(new), '資料長度小於100')
print('new清單的第一筆資料為\n', new[0])
print('new清單的第十筆資料為\n',new[11])