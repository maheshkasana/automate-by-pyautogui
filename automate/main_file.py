import pyautogui
from termcolor import colored
import pickle
import os
import time

credential_dict = {}


def delete_facebook_account():
    global credential_dict
    print("Welcome To Remove Facebook user credentials ")
    username = input("Enter Username : ")
    credential_dict.pop(username, 0)
    os.remove("conqueror_credential")
    dbfile = open("conqueror_credential", "ab")
    pickle.dump(credential_dict, dbfile)
    dbfile.close()


def add_facebook_account():
    global credential_dict
    print("Welcome TO Add new Facebook user credentials ")
    username = input("Enter Username : ")
    password = input("Enter Password : ")
    if username in credential_dict:
        print(colored("Username Already Exits : ", "yellow"))
        return
    credential_dict[username] = password
    os.remove("conqueror_credential")
    dbfile = open("conqueror_credential", "ab")
    pickle.dump(credential_dict, dbfile)
    dbfile.close()


def load_credential_dict():
    global credential_dict
    dbfile = open("conqueror_credential", "rb")
    credential_dict = pickle.load(dbfile)
    dbfile.close()


def update_credentials():
    global credential_dict
    print("\nWelcome To Update Credentials of Facebook")
    username = input("Enter Username : ")
    password = input("Enter Password : ")
    credential_dict[username] = password
    os.remove("conqueror_credential")
    dbfile = open("conqueror_credential", "ab")
    pickle.dump(credential_dict, dbfile)
    dbfile.close()


def print_current_credentials():
    print("\n\nCurrently Present Username & Password")
    if len(credential_dict) == 0:
        print(colored("No Credentials Present :)", "red"))
        return
    i = 1
    for user, psw in credential_dict.items():
        print(colored(" {0} : {1} , {2}", "green").format(i, user, psw))
        i += 1


def logout_from_facebook():
    pyautogui.moveTo(1074, 108)
    pyautogui.click(1074, 108)
    time.sleep(2)
    pyautogui.moveTo(974, 404)
    pyautogui.click(974, 404)
    pyautogui.moveTo(974, 375)
    pyautogui.click(974, 375)


def send_friend_requests():
    print("\n\nWelcome to module to send friend requests")
    n = int(input(colored("How Many Requests You want to send : ")))
    time.sleep(10)
    """
    pyautogui.moveTo(679, 108)
    pyautogui.click(679, 108)
    time.sleep(5)
    pyautogui.moveTo(490, 358)
    pyautogui.click(490, 358)
    time.sleep(5)
    pyautogui.moveTo(819, 425)
    pyautogui.click(819, 425)
    time.sleep(5)
    """
    i = 0
    pyautogui.scroll(-1150)
    while i < n:
        pyautogui.moveTo(600, 341)
        pyautogui.click(pyautogui.position())
        time.sleep(1)
        # not suggest
        pyautogui.moveTo(877, 705)
        pyautogui.click(pyautogui.position())
        # close chat
        pyautogui.moveTo(1114, 406)
        pyautogui.click(pyautogui.position())
        # close cant send request pop up
        pyautogui.moveTo(1086, 406)
        pyautogui.click(pyautogui.position())
        # click confirm request send
        pyautogui.moveTo(848, 373)
        pyautogui.click(pyautogui.position())
        # Cancle request
        pyautogui.moveTo(785, 374)
        pyautogui.click(pyautogui.position())
        pyautogui.scroll(-115)
        if i % 30 == 0:
            pyautogui.scroll(-10)
            time.sleep(3)
        i += 1
        time.sleep(1)


def accept_all_friend_requests():
    print("\n\nWelcome to module to Accept All friend requests")
    n = int(input(colored("How Many Requests You want to accept : ")))
    time.sleep(5)
    # pyautogui.moveTo(924, 111)
    # pyautogui.click(924, 111)
    time.sleep(5)
    i = 0
    while i < n:
        pyautogui.click(pyautogui.position())
        pyautogui.scroll(-115)
        i += 1
        time.sleep(1)


def send_friend_requests_conditional():
    print("\n\nWelcome to module to send friend requests to conditional Friend")
    n = int(input(colored("How Many Requests You want to send : ")))
    time.sleep(5)
    i = 1
    pyautogui.scroll(-920)
    while i < n:
        pyautogui.moveTo(657, 248)
        pyautogui.click(pyautogui.position())
        # time.sleep(1)
        # close chat
        pyautogui.moveTo(1114, 406)
        pyautogui.click(pyautogui.position())
        # close cant send request pop up
        pyautogui.moveTo(1086, 406)
        pyautogui.click(pyautogui.position())
        # close cant send request pop up type 2
        pyautogui.moveTo(1086, 427)
        pyautogui.click(pyautogui.position())
        # clisk confirm
        pyautogui.moveTo(848, 373)
        pyautogui.click(pyautogui.position())
        # clisk cancle
        pyautogui.moveTo(785, 374)
        pyautogui.click(pyautogui.position())

        """    
        pyautogui.moveTo(877, 705)
        pyautogui.click(pyautogui.position())

        """
        pyautogui.scroll(-115)
        if i % 30 == 0:
            pyautogui.scroll(-10)
            time.sleep(3)
        i += 1
        # time.sleep(1)

        if i % 15 == 0:
            pyautogui.moveTo(500, 46)
            pyautogui.click(500, 46)
            pyautogui.scroll(3000)
            pyautogui.hotkey("Enter")
            time.sleep(3)
            pyautogui.scroll(3000)
            # #for bandikui location current location
            # pyautogui.moveTo(790, 651)
            # pyautogui.click(790, 651)
            # #for bandikui location Hometown
            pyautogui.moveTo(790, 570)
            pyautogui.click(790, 570)
            time.sleep(3)
            pyautogui.scroll(1000)
            pyautogui.scroll(-920)


def send_friend_requests_mutual():
    print("\n\nWelcome to module to send friend requests to Mutual Friend Friend")
    n = int(input(colored("How Many Requests You want to send : ")))
    time.sleep(5)
    i = 1
    pyautogui.scroll(-920)
    while i < n:
        pyautogui.moveTo(657, 248)
        pyautogui.click(pyautogui.position())
        # time.sleep(1)
        # close chat
        pyautogui.moveTo(1114, 406)
        pyautogui.click(pyautogui.position())
        # close cant send request pop up
        pyautogui.moveTo(1086, 406)
        pyautogui.click(pyautogui.position())
        # close cant send request pop up type 2
        pyautogui.moveTo(1086, 427)
        pyautogui.click(pyautogui.position())
        # clisk confirm
        pyautogui.moveTo(848, 373)
        pyautogui.click(pyautogui.position())
        # clisk cancle
        pyautogui.moveTo(785, 374)
        pyautogui.click(pyautogui.position())
        pyautogui.scroll(-115)
        if i % 30 == 0:
            pyautogui.scroll(-10)
            time.sleep(3)
        i += 1
        if i % 10 == 0:
            pyautogui.moveTo(500, 46)
            pyautogui.click(500, 46)
            pyautogui.scroll(3000)
            time.sleep(1)
            pyautogui.hotkey("Enter")
            time.sleep(3)
            pyautogui.scroll(3000)
            # #for bandikui location current location
            # pyautogui.moveTo(790, 651)
            # pyautogui.click(790, 651)
            # #for bandikui location Hometown
            pyautogui.moveTo(790, 570)
            pyautogui.click(pyautogui.position())
            time.sleep(2)
            pyautogui.moveTo(830, 617)
            pyautogui.click(pyautogui.position())
            pyautogui.typewrite("Devnarayan Gurjar")
            pyautogui.hotkey("down")
            time.sleep(2)
            pyautogui.hotkey("Enter")
            pyautogui.moveTo(815, 617)
            pyautogui.click(pyautogui.position())
            pyautogui.typewrite("Devnarayan Gurjar")
            pyautogui.hotkey("down")
            time.sleep(2)
            pyautogui.hotkey("Enter")
            time.sleep(2)
            pyautogui.moveTo(788, 308)
            pyautogui.click(pyautogui.position())
            pyautogui.scroll(1000)
            time.sleep(1)
            pyautogui.scroll(-920)


def send_friend_requests_mutual_profile():
    print("\n\nWelcome to module to send friend requests to Mutual Friend Friend")
    n = int(input(colored("How Many Requests You want to send : ")))
    time.sleep(5)
    pyautogui.moveTo(428, 187)
    input("Hit OK")
    i = 1
    time.sleep(3)

    while i < n:
        # left add req
        pyautogui.moveTo(428, 187)
        pyautogui.click(pyautogui.position())
        # time.sleep(1)
        # close chat
        pyautogui.moveTo(1114, 406)
        pyautogui.click(pyautogui.position())
        # Confirm
        pyautogui.moveTo(849, 376)
        pyautogui.click(pyautogui.position())
        # Close Button
        pyautogui.moveTo(1086, 406)
        pyautogui.click(pyautogui.position())
        pyautogui.moveTo(1086, 423)
        pyautogui.click(pyautogui.position())
        pyautogui.moveTo(830, 351)
        pyautogui.click(pyautogui.position())

        # Right add req
        pyautogui.moveTo(844, 187)
        pyautogui.click(pyautogui.position())
        # time.sleep(1)
        # close chat
        pyautogui.moveTo(1114, 406)
        pyautogui.click(pyautogui.position())
        # Confirm
        pyautogui.moveTo(849, 376)
        pyautogui.click(pyautogui.position())
        # Close Button
        pyautogui.moveTo(1086, 406)
        pyautogui.click(pyautogui.position())
        pyautogui.moveTo(1086, 423)
        pyautogui.click(pyautogui.position())
        pyautogui.moveTo(830, 351)
        pyautogui.click(pyautogui.position())

        pyautogui.scroll(-135)
        i += 1
        if i % 10 == 0:
            pyautogui.scroll(-5)


def suggest_friend():
    print("\n\nWelcome to module to Suggest friend")
    n = int(input(colored("How Many Friend you want to suggest: ")))
    time.sleep(5)
    # pyautogui.moveTo(924, 111)
    # pyautogui.click(924, 111)
    time.sleep(5)
    i = 0
    while i < n:
        pyautogui.click(pyautogui.position())
        pyautogui.scroll(-74)
        i += 1
        time.sleep(1)
        if i % 20 == 0:
            pyautogui.scroll(-5)


def login_to_facebook_account(flag):
    if flag != -1:
        print("\n\nWelcome To Login Module\nEnter The index relative to Username you want to login")
        print_current_credentials()
        option = int(input())
        if option > len(credential_dict) or option <= 0:
            print(colored("Enter index in limit, out of scope index entred", 'red'))
            return
        i = 1
        for username, password in credential_dict.items():
            if i == option:
                break
            i += 1

        print(colored("Please Go To New chrome Window, I Will Start Taking action after 10sec :"))
        time.sleep(10)
        pyautogui.moveTo(500, 46)
        pyautogui.click(500, 46)
        pyautogui.typewrite("https://www.facebook.com/")
        pyautogui.hotkey("Enter")
        time.sleep(20)
        pyautogui.moveTo(856, 135)
        pyautogui.click(856, 135)
        pyautogui.typewrite(username)
        pyautogui.moveTo(1014, 135)
        pyautogui.click(1014, 135)
        pyautogui.typewrite(password)
        pyautogui.moveTo(1139, 127)
        pyautogui.click(1139, 127)
        time.sleep(5)

    while True:
        print("\n\n\tWelcome To perform operation :\n\t0 : Logout & Exit\n\t1 : Send Friend Requests\n\t2 : Accept All Friend Requests\n\t3 : Send Requests To conditional friend\n"
              "\t4 : Send Request to Mutual Friend\n\t5 : Send Request To mutual by Profile\n\t6 : Suggest Friend\n")
        option = int(input("\t"))
        if option == 0:
            time.sleep(5)
            logout_from_facebook()
            break
        elif option == 1:
            send_friend_requests()
        elif option == 2:
            accept_all_friend_requests()
        elif option == 3:
            send_friend_requests_conditional()
        elif option == 4:
            send_friend_requests_mutual()
        elif option == 5:
            send_friend_requests_mutual_profile()
        elif option == 6:
            suggest_friend()


def main():
    global credential_dict
    try:
        dbfile = open("conqueror_credential", 'rb')
        try:
            credential_dict = pickle.load(dbfile)
            dbfile.close()
        except EOFError:
            credential_dict = {}
    except FileNotFoundError:
        dbfile = open("conqueror_credential", 'ab')
        pickle.dump(credential_dict, dbfile)
        dbfile.close()
    while True:
        print("\n\nWelcome To Main Menu :\n0 : Exit\n1 : Add New Facebook Account\n2 : Remove Facebook Account List"
              "\n3 : Print Credentials in list\n4 : Update The Credentials in list\n5 : Login To account\n-1 : Bypass Login Process")
        option = int(input())
        if option == 0:
            break
        elif option == 1:
            add_facebook_account()
            load_credential_dict()
        elif option == 2:
            delete_facebook_account()
            load_credential_dict()
        elif option == 3:
            print_current_credentials()
        elif option == 4:
            update_credentials()
        elif option == 5:
            login_to_facebook_account(5)
        elif option == -1:
            login_to_facebook_account(-1)


if __name__ == '__main__':
    # time.sleep(10)
    # send_friend_requests()
    main()
