from generate import generate_list_of_words,generate_token
from PyQt5.QtWidgets import *
from ui import App
import sys


if __name__=='__main__':
    file=''
    with open(".\compile\complex.cpp",'r') as file:
        file=file.readlines()

    result=generate_list_of_words(file)

    tocken_dict=generate_token(result)

    for i in result:
        print(i)

    app = QApplication(sys.argv)
    ex = App(tocken_dict)
    sys.exit(app.exec_())