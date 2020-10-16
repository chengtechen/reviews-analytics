data = []
count = 0
with open('reviews.txt', 'r') as f:
    for line in f:
        data.append(line)
        count = count + 1
        if count % 1000 == 0:
            print(len(data)) 
print('總共有', len(data), '筆資料')   

wc = {} #word_count
for d in data:
    words = d.split() #預設空字串
    for word in words:
        if word in wc:
            wc[word] = wc[word] + 1
        else:
            wc[word] = 1

for word in wc:
    if wc[word] > 1000000:
        print(word, wc[word])

print('字典長度:', len(wc)) 

while True:
    word = input('想查的字(q離開):')
    if word == 'q':
        break
    if word in wc:
        print(word, '出現過的次數:', wc[word])
    else:
        print('沒有出現過')

print('程式結束')

'''
sum_len = 0
for d in data:
    sum_len = sum_len + len(d)

print('留言資料平均長度:', sum_len / count)

new = []
for d in data:
    if len(d) < 100:
        new.append(d)
print('總共有', len(new), '筆資料長度小於100')  
'''
