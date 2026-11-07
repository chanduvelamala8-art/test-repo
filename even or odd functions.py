number=int(input("enter a number:"))

def check_number(num):
    if num % 2 == 0:
        print("even number")
    else:
        print("odd number")

check_number(number)