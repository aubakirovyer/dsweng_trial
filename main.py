from datetime import datetime

def main():
    today = datetime.now()
    #today_formatted = today.strftime("%Y-%m-%d %H:%M")
    print(f"Hello, World! Today is {today}")


if __name__ == "__main__":
    main()