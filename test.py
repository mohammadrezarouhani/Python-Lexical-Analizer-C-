import pdb

if __name__=='__main__':
    file=''
    with open(".\compile\simple.cpp",'r') as file:
        file=file.readlines()

    for line in file:
        for i in enumerate(line):
            if '"'==i[1]:
                pdb.set_trace()
                print(i)