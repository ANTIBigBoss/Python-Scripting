import time
import pyinputplus as pyip
import datetime as dt
import tkinter as tk


def measure_execution_time():
    startTime = time.time()
    for i in range(100):
        for j in range(100):
            for k in range(100):
                k = j
    stopTime = time.time()
    codeTime = round(stopTime - startTime, 4)
    print(f"Execution Time: {codeTime} seconds")


def use_time_sleep():
    for i in range(3):
        print('tik'); time.sleep(1)
        print('tok'); time.sleep(1)


def user_login_simulation():
    userName = pyip.inputStr(prompt='Enter user name: ')
    password = pyip.inputPassword(prompt='Enter password: ')
    print('\nUser:', userName, 'login time & date:', time.ctime())


def display_current_datetime():
    print(dt.datetime.now())  # display current date and time
    custom_datetime = dt.datetime(2025, 9, 29, 14, 56, 23)
    print(custom_datetime)  # set custom date and time
    print('Year:', custom_datetime.year, 'Month:', custom_datetime.month, 'Day:', custom_datetime.day)
    print('Hour:', custom_datetime.hour, 'Minute:', custom_datetime.minute, 'Second:', custom_datetime.second)


def digital_clock_gui():
    def clkON():
        while flag.get():
            ctime = dt.datetime.now()
            strHour = f'{ctime.hour:02d}'
            strMin = f'{ctime.minute:02d}'
            strSec = f'{ctime.second:02d}'
            dispHour.config(text=strHour, fg='blue')
            dispMin.config(text=strMin, fg='blue')
            dispSec.config(text=strSec, fg='blue')
            time.sleep(1)
            win.update()
        flag.set(True)

    def clkOFF():
        flag.set(False)
        dispHour.config(text='00', fg='blue')
        dispMin.config(text='00', fg='blue')
        dispSec.config(text='00', fg='blue')

    win = tk.Tk()
    win.title('Clock')
    win.minsize(280, 50)
    flag = tk.BooleanVar(win)
    flag.set(True)

    dispHour = tk.Label(win, text='00', fg='blue', font='Consolas')
    dispHour.grid(column=1, row=0)
    dispMin = tk.Label(win, text='00', fg='blue', font='Consolas')
    dispMin.grid(column=2, row=0)
    dispSec = tk.Label(win, text='00', fg='blue', font='Consolas')
    dispSec.grid(column=3, row=0)

    clkBtn = tk.Button(win, text='ON', command=clkON)
    clkBtn.grid(column=0, row=1)
    quitBtn = tk.Button(win, text='OFF', command=clkOFF)
    quitBtn.grid(column=4, row=1)

    win.mainloop()


def compare_datetimes():
    halloween = dt.datetime(2023, 10, 31, 0, 0, 0)
    newyear = dt.datetime(2024, 1, 1, 0, 0, 0)
    print(halloween == newyear)
    print(halloween < newyear)


def work_with_timedelta():
    delta = dt.timedelta(days=1, hours=2, minutes=9, seconds=8)
    print(delta.total_seconds()/60, 'minutes')


def work_with_strftime():
    # Display datetime object as a string using strftime
    dt1 = dt.datetime.now()
    delta = dt.timedelta(days=-7)
    dt2 = dt1 + delta
    print(dt1, dt2, sep='\n')

    todaysDate = dt.datetime(2023, 3, 22, 16, 29, 0)
    print(todaysDate.strftime('%A, %B %d, %Y'))
    print(todaysDate.strftime('%I:%M %p'))


def convert_string_to_datetime():
    # Converting string to datetime object via function strptime
    dateStr = 'March 22, 2023'
    dateObj = dt.datetime.strptime(dateStr, '%B %d, %Y')
    print(dateObj)

    dateObj = dt.datetime.strptime('2019/10/21 16:29:00', '%Y/%m/%d %H:%M:%S')
    print(dateObj)


def implement_multithreading():
    # Implement multithreading
    import threading

    def takeANap():
        time.sleep(5)
        print('Wake up!\n')

    print('PROGRAM START')
    threadObj = threading.Thread(target=takeANap)
    threadObj.start()
    print('PROGRAM END')


def launch_other_programs():
    # Launching other programs from Python
    import subprocess as sp

    # Launching calculator on Windows
    sp.Popen(r'C:\Windows\System32\calc.exe')

    # Executing a Python script from a Python program
    sp.Popen(['python.exe', 'E:\\clock.py'])


def opening_websites_files():
    # Opening websites and files with default applications
    import webbrowser
    import subprocess as sp

    # Open a website
    webbrowser.open('canadorecollege.ca')

    # Open a file with the default application
    sp.Popen(['start', 'E:\\Provinces.csv'], shell=True)


def main_menu():
    while True:
        print("\nMenu:")
        print("0. Exit")
        print("1. Measure Execution Time")
        print("2. Use time.sleep()")
        print("3. User Login Simulation")
        print("4. Display Current DateTime")
        print("5. Digital Clock GUI")
        print("6. Compare Datetimes")
        print("7. Work with Timedelta")
        print("8. Work with strftime()")
        print("9. Convert String to Datetime")
        print("10. Implement Multithreading")
        print("11. Launch Other Programs")
        print("12. Open Websites and Files")

        choice = input("Enter your choice: ")

        if choice == '1':
            measure_execution_time()
        elif choice == '2':
            use_time_sleep()
        elif choice == '3':
            user_login_simulation()
        elif choice == '4':
            display_current_datetime()
        elif choice == '5':
            digital_clock_gui()
        elif choice == '6':
            compare_datetimes()
        elif choice == '7':
            work_with_timedelta()
        elif choice == '8':
            work_with_strftime()
        elif choice == '9':
            convert_string_to_datetime()
        elif choice == '10':
            implement_multithreading()
        elif choice == '11':
            launch_other_programs()
        elif choice == '12':
            opening_websites_files()
        elif choice == '0':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter a number between 0 and 12.")


if __name__ == "__main__":
    main_menu()
