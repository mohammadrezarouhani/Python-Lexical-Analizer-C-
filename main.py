import pdb






if __name__=='__main__':
    code_lines=[]
    with open(".\compile\complex.py",'r') as file:
        for i in file.readlines():
            code_lines.append(i.split(" "))

    for i in code_lines:
        print(i)
        