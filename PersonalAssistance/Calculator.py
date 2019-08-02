
class Calculator:
    def calculate(self):
        self.result = 0
        str(input("Hello this is Eliana, Personal Assistant...\nTry typing \'math\' or \'calculate\' : "))
        self.first_operand = int(input("First Number: "))
        self.operator = input("Operator: ")
        self.second_operand = int(input("Second Number: "))
        operators = ['+', '-', '/', '*']
        for x in operators:
            if x != self.operator:
                print("Please enter valid operator")
                break
            else:
                pass
                if self.operator == "+":
                    self.result = self.first_operand + self.second_operand
                elif self.operator == "-":
                    self.result = self.first_operand - self.second_operand
                elif self.operator == "*":
                    self.result = self.first_operand * self.second_operand
                elif self.operator == "/":
                    self.result = self.first_operand / self.second_operand
                print(self.first_operand, "", self.operator, "", self.second_operand, "=", self.result)
                break

    def history(self):
        f = open("file.csv", "a+")
        recordhistory = self.first_operand, self.operator, self.second_operand, "=", self.result
        f.write(str(recordhistory))
        f.close()

    def viewHistory(self):
        history = input("Do you want to see calculation history? Y/N \n : ")
        if history == "Y":
            with open("file.csv", 'r') as viewFileOpen:
                data = viewFileOpen.read()
                data.format()
            print("Calculation History: \n", data)
        elif history == "N":
            print("Thank you!")
        else:
            print("Please type Y/N")

    def clearHistory(self):
        clearhistory = input("Type \"history clear\" if you want to clear the history \n : ")
        if clearhistory == "history clear":
            f = open('file.csv', 'r+')
            f.truncate(0)  
            print("History Cleared")
        else:
            print("Please type \"history clear\": ")


test = Calculator()
test.calculate()
test.history()
test.viewHistory()
test.clearHistory()
