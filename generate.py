import tokens

def generate_list_of_words(code) -> list:
    temp='' # it will appent char when it end by space or \n or any operatory
    temp_next_char=''
    temp_list=[]
    word_list=[]
    double_char_opr=False
    string_flag=False
    comment_flag=False
    multi_line_comment=False
    single_line_comment=False
    
    for line in code:
        for char in enumerate(line):
            
            # if statement beging with // or /* its a comment
            # if char[1]=='/' or comment_flag: 
            #     temp_next_char=line[char[0]+1]
            #     if comment_flag and char[1]=='/':
            #         pass

            #     elif multi_line_comment and char[1]=='*':
            #         temp_next_char=line[char[0]+1]
            #         if temp_next_char=='/':
            #             temp+='*/'
            #             comment_flag=False
            #             multi_line_comment=False
            #             temp_list.append(temp)
            #             temp=''
            #             continue

            #     elif single_line_comment and char[1]=='\n':
            #         comment_flag=False
            #         single_line_comment=False
            #         temp_list.append(temp)
            #         temp=''
            #         continue

            #     elif temp_next_char=='/':
            #         comment_flag =True 
            #         single_line_comment=True

            #     elif temp_next_char=='*':
            #         comment_flag=True
            #         multi_line_comment=True

            # check if the characker is an op or not
            if not tokens.all_tokens.get(char[1],False):  
                temp+=char[1]

            # if statement begin with " its string, should be a unique element 
            elif char[1]=='"' and not comment_flag: 
                # pdb.set_trace()
                if string_flag:
                    temp+='"'
                    string_flag=False
                    temp_list.append(temp)
                    temp=''
                else:
                    string_flag=True
                    temp+='"'
            # if its not a word or string or coment, it an operator like(+ * - ....)
            # if space or \n in comment or string it will not ignored
            else: 
                if string_flag or comment_flag:
                    temp+=char[1]
                    continue
                # a word completed we added to list here 
                if temp: 
                    temp_list.append(temp)
                    temp=''
                # in case of space of \n ignore 
                if (char[1]== ' ' or char[1]=='\n' or double_char_opr):
                    double_char_opr=False
                    continue

                # if an operator is in compare like >= >> << ....
                # this will handle it
                temp+=char[1]
                if tokens.double_operator_tokens.get(char[1],False): 
                    temp_next_char=line[char[0]+1]          

                    # if its like >> << >= <= it mean it has two operator char
                    if tokens.double_operator_tokens.get(temp_next_char,False):
                        double_char_opr=True 
                        temp+=temp_next_char
                        temp_list.append(temp)
                        temp=''
                    else:
                        temp_list.append(temp)
                        temp=''
                else:
                    temp_list.append(temp)
                    temp=''
        if temp_list:
            word_list.append(temp_list)
            temp_list=[]

    return word_list


def generate_token(list_of_words):
    token_file={}
    block={}
    block_number=0
    for line in enumerate (list_of_words):
        for word in line[1]:
            if tokens.all_tokens.get(word,False):



