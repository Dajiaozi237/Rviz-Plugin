class NumberCalculator:
    def __init__(self):
        self.numbers = []

    def input_numbers(self):
        """提示用户输入数字，以空格分隔，回车结束"""
        input_str = input("请输入数字: ")
        try:
            self.numbers = [float(num) for num in input_str.split()]
        except ValueError:
            raise ValueError("输入必须为数字")

    def sum(self):
        return sum(self.numbers)

    def product(self):
        result = 1
        for num in self.numbers:
            result *= num
        return result

# 主程序
if __name__ == "__main__":
    calc = NumberCalculator()
    calc.input_numbers()
    print(f"和: {calc.sum()}")
    print(f"积: {calc.product()}")
