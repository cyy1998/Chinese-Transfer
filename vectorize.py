import os

if __name__=='__main__':
    filenames=os.listdir('visualized_test')
    for file in filenames:
        name=file.split('.')[0]
        os.system("potrace -s --output svg/{0}.svg visualized_test/{0}.bmp".format(name))
        print(name+': OK')
