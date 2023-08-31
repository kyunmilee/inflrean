# chapter09_02
# 파이썬 CSV 파일 읽기 및 쓰기

# CSV : MIME - text/csv

import csv

# 예제1
with open('./resource/test1.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader) #Header Skip(처음 헤더 출력 안되게)
    # 객체 확인
    print(reader)
    # 타입 확인
    print(type(reader))
    # 속성 확인
    print(dir(reader))  # __iter__
    print()
    
    for c in reader:
        print(c)
        # 타입 확인
        # print(type(c))
        # list to str
        print(''.join(c))
        
# 예제2
with open('./resource/test2.csv', 'r') as f:
    reader = csv.reader(f, delimiter='|')
    
    for m in reader:
        print(m)
print('-' * 19)
        
# 예제3
with open('./resource/test1.csv', 'r') as f:
    reader =  csv.DictReader(f)
    print(reader)
    print(type(reader))
    print(dir(reader))
    
    for c in reader:
        for k,v in c.items():
            print(k,v)
        print('-' * 19) 
        
# 예제4
w = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18], [19, 20, 21]]

with open('./resource/write1.csv', 'w', encoding = 'utf-8') as f:
    print(dir(csv))
    wt = csv.writer(f)  # wt는 csv의 writer에다가 위에서 list로감 
    # dir 확인
    print(dir(wt))
    # 타입 확인
    print(type(wt))
    
    for v in w:
        wt.writerow(v)
        
with open('./resource/write2.csv', 'w', encoding = 'utf-8') as f:
    # 필드명
    fields = ['one', 'two', 'three']
    # Dict Writer 선언
    wt = csv.DictWriter(f, fieldnames=fields)
    # Herder Write
    wt.writeheader()
    
    for v in w:
        wt.writerow({'one': v[0], 'two': v[1], 'three': v[2]})


        
    