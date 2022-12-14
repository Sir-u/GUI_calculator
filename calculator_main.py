import sys
from PyQt5.QtWidgets import *

tempFigure1 = 0
tempFigure2 = 0
tempOperation = ""
solution = 0

class Main(QDialog):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        main_layout = QVBoxLayout()

        ### 각 위젯을 배치할 레이아웃을 미리 만들어 둠
        layout_button = QGridLayout()
        layout_equation_solution = QGridLayout()

        ### 수식 입력과 답 출력을 위한 LineEdit 위젯 생성
        self.equation = QLineEdit("")

        ### layout_equation_solution 레이아웃에 수식, 답 위젯을 추가
        layout_equation_solution.addWidget(self.equation, 0, 0)

        ### =, clear, backspace 버튼 생성
        button_equal = QPushButton("=")
        button_clear = QPushButton("C")
        button_backspace = QPushButton("<-")

        ### =, clear, backspace 버튼 클릭 시 시그널 설정
        button_equal.clicked.connect(self.button_equal_clicked)
        button_clear.clicked.connect(self.button_clear_clicked)
        button_backspace.clicked.connect(self.button_backspace_clicked)

        ### =, clear, backspace 버튼을 layout_button 레이아웃에 추가
        layout_button.addWidget(button_equal, 5, 3)
        layout_button.addWidget(button_clear, 0, 2)
        layout_button.addWidget(button_backspace, 0, 3)

        ### 사칙연상 버튼 생성
        button_plus = QPushButton("+")
        button_minus = QPushButton("-")
        button_product = QPushButton("x")
        button_division = QPushButton("/")

        ### 사칙연산 버튼을 클릭했을 때, 각 사칙연산 부호가 수식창에 추가될 수 있도록 시그널 설정
        button_plus.clicked.connect(lambda state, operation = "+": self.button_operation_clicked(operation))
        button_minus.clicked.connect(lambda state, operation = "-": self.button_operation_clicked(operation))
        button_product.clicked.connect(lambda state, operation = "*": self.button_operation_clicked(operation))
        button_division.clicked.connect(lambda state, operation = "/": self.button_operation_clicked(operation))

        ### 사칙연산 버튼을 layout_button 레이아웃에 추가
        layout_button.addWidget(button_plus, 4, 3)
        layout_button.addWidget(button_minus, 3, 3)
        layout_button.addWidget(button_product, 2, 3)
        layout_button.addWidget(button_division, 1, 3)

        ### %, CE, C, 1/x, 제곱, 제곱근 버튼 생성
        button_percent = QPushButton("%")
        button_CE = QPushButton("CE")
        button_inverse = QPushButton("1/x")
        button_square = QPushButton("x²")
        button_square_root = QPushButton("√X")

        ### %, CE, C, 1/x, 제곱, 제곱근 버튼 클릭 시 시그널 설정
        button_percent.clicked.connect(self.button_percent_clicked)
        button_CE.clicked.connect(self.button_clear_clicked)
        button_inverse.clicked.connect(self.button_inverse_clicked)
        button_square.clicked.connect(self.button_square_clicked)
        button_square_root.clicked.connect(self.button_square_root_clicked)

        ### %, CE, C, 1/x, 제곱, 제곱근 버튼을 layout_button 레이아웃에 추가
        layout_button.addWidget(button_percent, 0, 0)
        layout_button.addWidget(button_CE, 0, 1)
        layout_button.addWidget(button_inverse, 1, 0)
        layout_button.addWidget(button_square, 1, 1)
        layout_button.addWidget(button_square_root, 1, 2)

        ### 숫자 버튼 생성하고, layout_button 레이아웃에 추가
        ### 각 숫자 버튼을 클릭했을 때, 숫자가 수식창에 입력 될 수 있도록 시그널 설정
        number_button_dict = {}
        for number in range(0, 10):
            number_button_dict[number] = QPushButton(str(number))
            number_button_dict[number].clicked.connect(lambda state, num = number:
                                                       self.number_button_clicked(num))
            if number > 0:
                x,y = divmod(number-1, 3)
                layout_button.addWidget(number_button_dict[number], x+2, y)
            elif number == 0:
                layout_button.addWidget(number_button_dict[number], 5, 1)

        ### 소숫점 버튼과 00 버튼을 입력하고 시그널 설정
        button_dot = QPushButton(".")
        button_dot.clicked.connect(lambda state, num = ".": self.number_button_clicked(num))
        layout_button.addWidget(button_dot, 5, 2)

        button_double_zero = QPushButton("00")
        button_double_zero.clicked.connect(lambda state, num = "00": self.number_button_clicked(num))
        layout_button.addWidget(button_double_zero, 5, 0)

        ### 각 레이아웃을 main_layout 레이아웃에 추가
        main_layout.addLayout(layout_equation_solution)
        main_layout.addLayout(layout_button)

        self.setLayout(main_layout)
        self.show()

    #################
    ### functions ###
    #################
    def number_button_clicked(self, num):
        equation = self.equation.text()
        equation += str(num)
        self.equation.setText(equation)

    def button_operation_clicked(self, operation):
        global tempFigure1
        global tempOperation
        tempFigure1 = self.equation.text()
        tempFigure1 = float(tempFigure1)
        tempOperation = operation
        self.equation.setText("")
        
    def button_equal_clicked(self):
        global tempFigure1
        global tempFigure2
        global tempOperation
        tempFigure2 = self.equation.text()
        tempFigure2 = float(tempFigure2)
        if tempOperation == "+":
            solution = tempFigure1 + tempFigure2
            self.equation.setText(str(solution))
        
        if tempOperation == "-":
            solution = tempFigure1 - tempFigure2
            self.equation.setText(str(solution))

        if tempOperation == "*":
            solution = tempFigure1 * tempFigure2
            self.equation.setText(str(solution))
        
        if tempOperation == "/":
            solution = tempFigure1 / tempFigure2
            self.equation.setText(str(solution))

    def button_clear_clicked(self):
        self.equation.setText("")

    def button_backspace_clicked(self):
        equation = self.equation.text()
        equation = equation[:-1]
        self.equation.setText(equation)

    def button_percent_clicked(self):
        equation = self.equation.text()
        if float(equation) > 100:
            equation = int(equation) / 100
            self.equation.setText(str(equation))
        elif float(equation) <= 100:
            equation = float(equation) / 100
            self.equation.setText(str(equation))
        
    def button_inverse_clicked(self):
        equation = self.equation.text()
        if float(equation) != 0:
            equation = 1 / float(equation)
            self.equation.setText(str(equation))
        else:
            self.equation.setText("0")

    def button_square_clicked(self):
        equation = self.equation.text()
        equation = float(equation) ** 2
        self.equation.setText(str(equation))

    def button_square_root_clicked(self):
        equation = self.equation.text()
        equation = float(equation) ** (1/2)
        self.equation.setText(str(equation))

    def check_dot(self):
        equation = self.equation.text()
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Main()
    sys.exit(app.exec_())