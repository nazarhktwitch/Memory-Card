from PyQt5.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QGroupBox, QButtonGroup, QRadioButton, QPushButton, QLabel, QSpinBox # Імпортуємо необхідні бібліотеки
from PyQt5.QtCore import Qt # Імпортуємо ядро Qt

window = QWidget() # Створюємо вікно
window.setWindowTitle('Memory Card') # Встановлюємо назву вікна
card_width, card_height = 600, 500 # Встановлюємо розміри вікна (Змінні card_width, card_height)
window.resize(card_width, card_height) # Встановлюємо розміри вікна
window.move(900, 900) # Встановлюємо позицію вікна на екрані

card_layout = QVBoxLayout() # Створюємо вертикальний макет
window.setLayout(card_layout) # Встановлюємо макет в вікно

text = QLabel('Студент - ...') # Створюємо напис

ans1 = QRadioButton('Student') # Створюємо радіокнопку
ans2 = QRadioButton('Teacher') # Створюємо радіокнопку 2
ans3 = QRadioButton('Apple') # Створюємо радіокнопку 3
ans4 = QRadioButton('House') # Створюємо радіокнопку 4

right_answer = QLabel('Student') # Створюємо правильну відповідь

next = QPushButton('Відповісти') # Створюємо кнопку "Відповісти"
menu = QPushButton('Меню') # Створюємо кнопку "Меню"
rest = QPushButton('Відпочити') # Створюємо кнопку "Відпочити"
rest_time = QSpinBox() # Створюємо спінбокс для відпочинку

RadioGroupBox = QGroupBox('Варіанти:') # Створюємо групу радіокнопок

RadioGroup = QButtonGroup() # Створюємо групу радіокнопок

RadioGroup.addButton(ans1) # Додаємо відповідь в групу
RadioGroup.addButton(ans2) # Додаємо відповідь 2 в групу
RadioGroup.addButton(ans3) # Додаємо відповідь 3 в групу
RadioGroup.addButton(ans4) # Додаємо відповідь 4 в групу

AnsGroupBox = QGroupBox('Результат') # Створюємо групу результату
result = QLabel('') # Створюємо напис результату
correct = QLabel('') # Створюємо напис правильної відповіді

ans1_layout = QHBoxLayout() # Створюємо горизонтальний макет для відповіді 1
ans2_layout = QVBoxLayout() # Створюємо горизонтальний макет для відповіді 2
ans3_layout = QVBoxLayout() # Створюємо горизонтальний макет для відповіді 3

ans2_layout.addWidget(ans1) # Додаємо відповідь 1 в макет
ans2_layout.addWidget(ans2) # Додаємо відповідь 2 в макет
ans3_layout.addWidget(ans3) # Додаємо відповідь 3 в макет
ans3_layout.addWidget(ans4) # Додаємо відповідь 4 в макет

ans1_layout.addLayout(ans2_layout) # Додаємо макет відповіді 2 в макет відповіді 1
ans1_layout.addLayout(ans3_layout) # Додаємо макет відповіді 3 в макет відповіді 1
RadioGroupBox.setLayout(ans1_layout) # Встановлюємо макет відповіді 1 в групу радіокнопок

card_layout.addWidget(result, alignment=Qt.AlignLeft | Qt.AlignTop) # Додаємо напис результату в макет
card_layout.addWidget(correct, alignment=Qt.AlignHCenter, stretch=2) # Додаємо напис правильної відповіді в макет
AnsGroupBox.setLayout(card_layout) # Встановлюємо макет в групу результату
AnsGroupBox.hide() # Ховаємо групу результату