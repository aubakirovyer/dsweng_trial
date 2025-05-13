from datetime import datetime
from add import adder

def main():
    today = datetime.now()
    #today_formatted = today.strftime("%Y-%m-%d %H:%M")
    print(f"Hello, World! Today is {today}")

    # change made by other person
    today_formatted = today.strftime("%Y-%m-%d %H:%M")
    print(f"Hello, World2! Today's formatter date is {today_formatted}")

    print(adder(5,3))
    print(adder(10,10))

    print(adder(100, 200))
    printer()

def printer():
    print("Hello from main branch")
    print("Hello from feature branch")

if __name__ == "__main__":
    main()
