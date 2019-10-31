import os

file=open('font_test.txt', 'w')

path=os.listdir('./sun')
for i in range(len(path)-3000, len(path)-1000):
    print(path[i].split('.')[0])
    file.write(path[i].split('.')[0]+'\n')

