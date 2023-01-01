import tokens
import string
import pdb

def generate_list_of_words(code) -> list:
    temp='' # it will appent char when it end by space or \n or any operatory
    temp_next_char=''
    temp_prev_char=''
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
            #     temp_next_char='' if comment_flag else line[char[0]+1]
            #     if temp_next_char=='/':
            #         single_line_comment=True
            #         comment_flag=True
            #         temp+=char[1]

            #     elif temp_next_char=='*':
            #         multi_line_comment=True
            #         comment_flag=True
            #         temp+=char

            #     elif char=='/' and comment_flag and multi_line_comment:
            #         temp_prev_char=temp_next_char=line[char[0]-1]
            #         if temp_prev_char=='*':
            #             multi_line_comment=False
            #             comment_flag=False
            #             temp+=char[1]
            #             temp_list.append(temp)

            #             temp=''
                  
            #     elif comment_flag and char=='\n' and single_line_comment:
            #         single_line_comment=False
            #         comment_flag=False
            #         temp_list.append(temp)
            #         temp=''

            #     elif comment_flag:
            #         temp+=char[1]
                
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
                if string_flag:
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
        if temp_list :
            word_list.append(temp_list)
            temp_list=[]

    return word_list

def is_id(value):
    return True if value[0] in string.ascii_letters else False


def generate_token(list_of_words):
    token_dict={}
    temp_list=[]
    block_number=0
    last_block='Block(0)'
    line_detail=''
    block_stack=['Block(0)']

    for line in enumerate (list_of_words):
        line_detail="Line{}".format(line[0])
        for word in line[1]:
            token=tokens.all_tokens.get(word,False)
            if token:
                if word in tokens.block_start_list:
                    block_number+=1
                    last_block="Block({})".format(block_number)
                    block_stack.append(last_block)
                    temp=str(token)+" "+last_block
                    temp_list.append(temp)

                elif word in tokens.block_end_list:
                    temp=str(token)+" "+last_block
                    temp_list.append(temp)
                    block_stack.pop()
                    last_block=block_stack[len(block_stack)-1]
                else:
                    temp=str(token)+" "+last_block
                    temp_list.append(temp)
            else:
                if word.startswith('"'):
                    temp="String"+" "+last_block
                    temp_list.append(temp)
                elif word.startswith('//') or word.startswith('*/'):
                    temp="Comment"+" "+last_block
                    temp_list.append(temp)
                elif is_id(word):
                    temp="ID"+" "+last_block
                    temp_list.append(temp)
                else:
                    temp="Value"+" "+last_block
                    temp_list.append(temp)

        token_dict.update({line_detail:temp_list})
        temp_list=[]
    return token_dict 




