import time
import threading


class _FileMethods:
    def __init__(self, file_name, extension):
        self.file_name = file_name
        self.extension = extension
        self.text = ""

    def read_file(self):
        with open(f"{self.file_name}.{self.extension}", "r") as file:
            self.text = file.read()

    def print_data(self):
        print(self.text)
        time.sleep(1)

    def read_file_inf(self):
        while True:
            with open(f"{self.file_name}.{self.extension}", "r") as file:
                self.text = file.read()

    def print_data_inf(self):
        for i in range(30):
            print(self.text)
            time.sleep(1)


f_methods = _FileMethods(input("Enter the file name: "), input("Enter the extension: "))


def run():
    read = threading.Thread(target=f_methods.read_file, daemon=True)
    print_data = threading.Thread(target=f_methods.print_data)

    read.start()
    print_data.start()
    return f_methods.text


def run_inf():
    read = threading.Thread(target=f_methods.read_file_inf, daemon=True)
    print_data = threading.Thread(target=f_methods.print_data_inf)

    read.start()
    print_data.start()
