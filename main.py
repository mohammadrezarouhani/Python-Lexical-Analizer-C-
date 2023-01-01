import pdb
from generate import generate_list_of_words,generate_token



if __name__=='__main__':
    file=''
    with open(".\compile\complex.cpp",'r') as file:
        file=file.readlines()

    result=generate_list_of_words(file)


    re=generate_token(result)
    for i in re.items():
        print(i)