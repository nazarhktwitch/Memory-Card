from PyQt5.QtWidgets import QApplication
from random import choice, shuffle

app = QApplication([])

from main_window import *
from menu_window import *

class Question:
    def __init__(self, question, answer, wrong_answer1, wrong_answer2, wrong_answer3):
        self.question = question
        self.answer = answer
        self.wrong_answer1 = wrong_answer1
        self.wrong_answer2 = wrong_answer2
        self.wrong_answer3 = wrong_answer3
        self.isAsking = True
        self.count_ask = 0
        self.count_right = 0
    def got_right(self):
        self.count_ask += 1
        self.count_right += 1
    def got_wrong(self):
        self.count_ask += 1

q1 = Question('Яблуко', 'apple', 'application', 'pinapple', 'apply')
q2 = Question('Дім', 'house', 'horse', 'hurry', 'hour')
q3 = Question('Миша', 'mouse', 'mouth', 'muse', 'museum')
q4 = Question('Число', 'number', 'digit', 'amount', 'summary')

radio_buttons = [ans1, ans2, ans3, ans4]
questions = [q1, q2, q3, q4]

def new_question():
    global cur_q
    cur_q = choice(questions)
    text.setText(cur_q.question)
    right_answer.setText(cur_q.answer)
    shuffle(radio_buttons)

    radio_buttons[0].setText(cur_q.wrong_answer1)
    radio_buttons[1].setText(cur_q.wrong_answer2)
    radio_buttons[2].setText(cur_q.wrong_answer3)
    radio_buttons[3].setText(cur_q.answer)

new_question()

def check():
    RadioGroup.setExclusive(False)
    for answer in radio_buttons:
        if answer.isChecked():
            if answer.text() == right_answer.text():
                cur_q.got_right()
                result.setText('Вірно!')
                answer.setChecked(False)
                break
    else:
        result.setText('Не вірно!')
        cur_q.got_wrong()

    RadioGroup.setExclusive(True)

def click_ok():
    if next.text() == 'Відповісти':
        check()
        text.hide()
        ans1.show()

        next.setText('Наступне запитання')
    else:
        new_question()
        text.show()
        ans1.hide()

        next.setText('Відповісти')

next.clicked.connect(click_ok)

def menu_generation():
    if cur_q.count_ask == 0:
        c = 0
    else:
        c = (cur_q.count_right / cur_q.count_ask) * 100

    text = f'Разів відповіли: {cur_q.count_ask}\n' \
            f'Вірних відповідей: {cur_q.count_right}\n' \
            f'Успішність: {round(c, 2)}%'
    lb_stats.setText(text)
    menu_win.show()
    window.hide()

menu.clicked.connect(menu_generation)

def back_menu():
    menu_win.hide()
    window.show()

btn_back.clicked.connect(back_menu)

def clear():
    le_question.clear()
    le_right_ans.clear()
    le_wrong_ans1.clear()
    le_wrong_ans2.clear()
    le_wrong_ans3.clear()

btn_clear.clicked.connect(clear)

def add_question():
    q_text = le_question.text()
    custom_question = Question(q_text, le_right_ans.text(), le_wrong_ans1.text(), le_wrong_ans2.text(), le_wrong_ans3.text())
    questions.append(custom_question)
    clear()

btn_add.clicked.connect(add_question)

window.show()
app.exec_()