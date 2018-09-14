print("====Generate Math Quiz====")

import random
import datetime
from docx import Document
from docx.shared import Pt

now = datetime.datetime.now()

def quiz_add(quiz_no, add_no= 2, dig= 2, line_l= 80, q_per_l= 2, same_dig= False):
    '''
    For a given params, to generate math addition quizs
    :param quiz_no:  number of quiz
    :param add_no:  how many additions together
    :param dig:  digital number
    :param line_l: printable characters per line
    :param q_per_l: quiz to print per line
    :param same_dig:  True to add same digits numbers, False to add all possible positive numbers
    :return:
    '''
    cnt = 0
    with open('mathgen' + now.strftime("%Y-%m-%d") + '.txt', 'w') as file:
        file.write('===== Math Quiz by ' + str(now.strftime("%Y-%m-%d")) + ' =====\n\n')

        for i in range(int(quiz_no/q_per_l) +1):
            for j in range(q_per_l):
                quiz = []
                quiz.append('Q' + str(i*q_per_l+j+1) + ': ')
                for k in range(add_no):
                    if same_dig:
                        quiz.append(str(random.randint(10**(dig-1), 10 ** dig-1)))
                    else:
                        quiz.append(str(random.randint(1, 10 ** dig - 1)))
                    quiz.append(' + ')
                quiz[-1] = ' = '
                s = '%-' + str(int(line_l/q_per_l)) + 's'
                file.write(s % ''.join(quiz))
                cnt += 1
                if cnt == quiz_no:
                    file.write('\n\n\n\n')
                    return



def quiz_add_docx(quiz_no, add_no= 2, dig= 2, q_per_l= 2, same_dig= False, f_size=20):
    '''
    For a given params, to generate math addition quizs
    :param quiz_no:  number of quiz
    :param add_no:  how many additions together
    :param dig:  digital number
    :param q_per_l: quiz to print per line
    :param same_dig:  True to add same digits numbers, False to add all possible positive numbers
    :param f_size: font size in word file
    :return:
    '''
    cnt = 0
    fname = 'MathQuizGen_' + now.strftime("%m-%d_") + str(add_no) + 'x' + str(dig) + '-digitAdds'
    document = Document()
    document.add_heading(fname, 0)
    style = document.styles['Normal']
    font = style.font
    font.size = Pt(f_size)
    style.paragraph_format.space_after = Pt(f_size*1.25)

    table = document.add_table(rows=int(quiz_no/q_per_l) +1, cols=q_per_l)

    for i in range(int(quiz_no / q_per_l) + 1):
        for j in range(q_per_l):
            quiz = []
            quiz.append('Q' + str(i * q_per_l + j + 1) + ': ')
            # row_cells = table.add_row().cells
            for k in range(add_no):
                if same_dig:
                    quiz.append(str(random.randint(10 ** (dig - 1), 10 ** dig - 1)))
                else:
                    quiz.append(str(random.randint(1, 10 ** dig - 1)))
                quiz.append(' + ')
            quiz[-1] = ' = '
            table.rows[i].cells[j].text = ''.join(quiz)

            cnt += 1
            if cnt == quiz_no:
                document.save(fname + '.docx')
                return



def quiz_sub_docx(quiz_no, sub_no= 2, dig= 2, q_per_l= 2, same_dig= False, f_size=20):
    '''
    For a given params, to generate math addition quizs
    :param quiz_no:  number of quiz
    :param sub_no:  how many subtraction together
    :param dig:  digital number
    :param q_per_l: quiz to print per line
    :param same_dig:  True to sub same digits numbers, answer could be negative number. False to sub n-1 dig number, answer likely positive number.
    :param f_size: font size in word file
    :return:
    '''
    cnt = 0
    fname = 'MathQuizGen_' + now.strftime("%m-%d_") + str(sub_no) + 'x' + str(dig) + '-digitSubs'
    document = Document()
    document.add_heading(fname, 0)
    style = document.styles['Normal']
    font = style.font
    font.size = Pt(f_size)
    style.paragraph_format.space_after = Pt(f_size*1.25)

    table = document.add_table(rows=int(quiz_no/q_per_l) +1, cols=q_per_l)

    for i in range(int(quiz_no / q_per_l) + 1):
        for j in range(q_per_l):
            quiz = []
            quiz.append('Q' + str(i * q_per_l + j + 1) + ': ')
            # row_cells = table.add_row().cells
            for k in range(sub_no):
                if k==0:
                    quiz.append(str(random.randint(10 ** (dig - 1), 10 ** dig - 1)))
                else:
                    if same_dig:
                        quiz.append(str(random.randint(10 ** (dig - 1), 10 ** dig - 1)))
                    else:
                        quiz.append(str(random.randint(1, 10 ** (dig - 1))))
                quiz.append(' - ')
            quiz[-1] = ' = '
            table.rows[i].cells[j].text = ''.join(quiz)

            cnt += 1
            if cnt == quiz_no:
                document.save(fname + '.docx')
                return



quiz_add_docx(94, add_no=2, f_size=20, same_dig=True) #to generate  quiz
# quiz_add(quiz_no, add_no= 2, dig= 2, q_per_l= 2, same_dig= True)

quiz_sub_docx(94, sub_no=2, dig=2, f_size=20) #to generate quiz

print("====end====")

