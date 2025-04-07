from datetime import datetime

def main():
    today = datetime.now()
    #today_formatted = today.strftime("%Y-%m-%d %H:%M")
    print(f"Hello, World! Today is {today}")

    # change made by other person
    today_formatted = today.strftime("%Y-%m-%d %H:%M")
    print(f"Hello, World2! Today's formatter date is {today_formatted}")

    print(5+3)

if __name__ == "__main__":
    main()
