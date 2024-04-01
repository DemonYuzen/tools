### 0xSHALL
### Recoded By HaxorWorld
### SeoBarBar
### Usage: python file.py list.txt
import requests
import sys
from multiprocessing.dummy import Pool
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

listSite = sys.argv[1]
op = [i.strip() for i in open(listSite, "r").readlines()]

# ANSI escape sequences for colors
class colors:
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    ENDC = '\033[0m'

def check(site):
  try:
    r = requests.get(site + "/upload/server/php/", verify=False, timeout=10)
    ff = open("vuln.txt", "a+")
    if '{"files":[{"name":"' in r.text:
      print(colors.GREEN + site + "/upload/server/php/ -> Vuln" + colors.ENDC)
      ff.write(site + "/upload/server/php/\n")
    else:
      c = requests.get(site + "/admin/server/php/", verify=False, timeout=10)
      if '{"files":[{"name":"' in c.text:
        print(colors.GREEN + site + "/admin/server/php/ -> Vuln" + colors.ENDC)
        ff.write(site + "/admin/server/php/\n")
      else:
        b = requests.get(site + "/fileupload/server/php/", verify=False, timeout=10)
        if '{"files":[{"name":"' in b.text:
          print(colors.GREEN + site + "/fileupload/server/php/ -> Vuln" + colors.ENDC)
          ff.write(site + "/fileupload/server/php/\n")
        else:
          k = requests.get(site + "/server/php/", verify=False, timeout=10)
          if '{"files":[{"name":"' in k.text:
            print(colors.GREEN + site + "/server/php/ -> Vuln" + colors.ENDC)
            ff.write(site + "/server/php/\n")
          else:
              rx = requests.get(site + "/admin/tools/assets/jquery-file-upload/server/php/", verify=False, timeout=10)
    ff = open("vuln.txt", "a+")
    if '{"files":[{"name":"' in rx.text:
      print(colors.GREEN + site + "/admin/tools/assets/jquery-file-upload/server/php/ -> Vuln" + colors.ENDC)
      ff.write(site + "/admin/tools/assets/jquery-file-upload/server/php/\n")
    else:
        fx = requests.get(site + "/assets/jquery-file-upload/server/php/", verify=False, timeout=10)
    ff = open("vuln.txt", "a+")
    if '{"files":[{"name":"' in fx.text:
      print(colors.GREEN + site + "/assets/jquery-file-upload/server/php/ -> Vuln" + colors.ENDC)
      ff.write(site + "/assets/jquery-file-upload/server/php/\n")
    else:
        z = requests.get(site + "/assets/plugins/jquery-file-upload/server/php/", verify=False, timeout=10)
    ff = open("vuln.txt", "a+")
    if '{"files":[{"name":"' in z.text:
      print(colors.GREEN + site + "/assets/plugins/jquery-file-upload/server/php/ -> Vuln" + colors.ENDC)
      ff.write(site + "/assets/plugins/jquery-file-upload/server/php/\n")
    else:
      print(colors.YELLOW + site + " -> Not Vuln" + colors.ENDC)
  except:
    print(colors.RED + site + " -> Unknow Error" + colors.ENDC)
    
tod = Pool(200)
tod.map(check, op)
tod.close()
tod.join()
