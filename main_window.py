from PyQt5.QtWidgets import QLabel, QPushButton, QWidget, QLineEdit, QHBoxLayout, QVBoxLayout

menu_win = QWidget()

question = QLabel('Введіть питання:')
right_ans = QLabel('Введіть правильну відповідь:')
wrong_ans1 = QLabel('Введіть неправильну відповідь:')
wrong_ans2 = QLabel('Введіть неправильну відповідь:')
wrong_ans3 = QLabel('Введіть неправильну відповідь:')

le_question = QLineEdit()
le_right_ans = QLineEdit()
le_wrong_ans1 = QLineEdit()
le_wrong_ans2 = QLineEdit()
le_wrong_ans3 = QLineEdit()

lb_header_stats = QLabel('Статистика:')
lb_header_stats.setStyleSheet('font-size: 20px; font-weight: bold;')

lb_stats = QLabel()

vl_labels = QVBoxLayout()
vl_labels.addWidget(question)
vl_labels.addWidget(right_ans)
vl_labels.addWidget(wrong_ans1)
vl_labels.addWidget(wrong_ans2)
vl_labels.addWidget(wrong_ans3)

vl_lineEdits = QVBoxLayout()
vl_lineEdits.addWidget(le_question)
vl_lineEdits.addWidget(le_right_ans)
vl_lineEdits.addWidget(le_wrong_ans1)
vl_lineEdits.addWidget(le_wrong_ans2)
vl_lineEdits.addWidget(le_wrong_ans3)

hl_label_lineEdits = QHBoxLayout()
hl_label_lineEdits.addLayout(vl_labels)
hl_label_lineEdits.addLayout(vl_lineEdits)

hl_question = hl_label_lineEdits

btn_back = QPushButton('Назад')
btn_add = QPushButton('Додати питання')
btn_clear = QPushButton('Очистити')

hl_buttons = QHBoxLayout()
hl_buttons.addWidget(btn_back)
hl_buttons.addWidget(btn_add)
hl_buttons.addWidget(btn_clear)

vl_res = QVBoxLayout()
vl_res.addLayout(hl_question)
vl_res.addLayout(hl_buttons)
vl_res.addWidget(lb_header_stats)
vl_res.addWidget(lb_stats)
vl_res.addWidget(btn_back)

menu_win.setLayout(vl_res)
menu_win.resize(600, 500)