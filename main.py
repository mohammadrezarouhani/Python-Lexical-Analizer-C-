import pdb
from . import tokens

def get_word_list(value:iter):
    temp=''
    temp_next_char=''
    temp_list=[]
    word_list=[]
    
    for line in value:
        for char in line:
            if not tokens.all_tokens.get(char,None):
                temp+=char
            else:
                if temp:
                    temp_list.append(temp)
                if char== ' ' or char=='\n':
                    continue
                temp=''
                temp+=char
                if tokens.compare_tokens.get(char,None):
                    temp_next_char=next(value)

                    if tokens.compare_tokens.get(temp_next_char,None):
                        temp+=temp_next_char
                        temp_list.append(temp)
                        temp=''
                else:
                    temp_list.append(temp)
                    temp=''
        word_list.append(temp_list)

    return word_list



if __name__=='__main__':
    file=''
    with open(".\compile\simple.cpp",'r') as file:
        file=file.readlines()

    get_word_list(iter(file))
        