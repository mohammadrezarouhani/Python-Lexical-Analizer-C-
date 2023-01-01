import pdb
from generate import generate_list_of_words



if __name__=='__main__':
    file=''
    with open(".\compile\complex.cpp",'r') as file:
        file=file.readlines()

    result=generate_list_of_words(file)

    for line in result:
        print(line)
        