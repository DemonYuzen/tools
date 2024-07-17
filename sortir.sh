#!/bin/bash

# Leviathan Perfect Hunter
# Directory where the logs are located
LOG_DIR="."

# Output files
declare -A OUTPUT_FILES=(
    ["cpanel"]="cpanel.txt"
    ["admin"]="admin.txt"
    ["adminpanel"]="adminpanel.txt"
    ["wp-login"]="wp.txt"
    ["direct"]="hx3.txt"
    ["adminer"]="adminer.txt"
    ["phpmyadmin"]="phpmyadmin.txt"
    ["sqlpanel"]="sqlpanel.txt"
    ["plesk"]="plesk.txt"
    ["directadmin"]="directadmin.txt"
    ["cloudpanel"]="cloudpanel.txt"
    ["ispconfig"]="ispconfig.txt"
    ["vestacp"]="vestacp.txt"
    ["ajenti"]="ajenti.txt"
    ["aapanel"]="aapanel.txt"
    ["cyberpanel"]="cyberpanel.txt"
    ["webuzo"]="webuzo.txt"
    ["hestiacp"]="hestiacp.txt"
    ["virtualmin"]="virtualmin.txt"
    ["runcloud"]="runcloud.txt"
)

# Colors for display
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Header
echo -e "${BLUE}==============================================${NC}"
echo -e "${YELLOW}       HaxorNoname Tools Log Sorting Script      ${NC}"
echo -e "${BLUE}==============================================${NC}"

# Function to show loading animation
show_loading() {
    local pid=$!
    local delay=0.1
    local spinstr='|/-\'
    echo -n "Loading... "
    while [ "$(ps a | awk '{print $1}' | grep $pid)" ]; do
        local temp=${spinstr#?}
        printf " [%c]  " "$spinstr"
        local spinstr=$temp${spinstr%"$temp"}
        sleep $delay
        printf "\b\b\b\b\b\b"
    done
    echo -e "${GREEN}Done.${NC}"
}

# Function to separate processes with a line
separator() {
    echo -e "${BLUE}----------------------------------------------${NC}"
}

# Common function to process logs
process_logs() {
    local name=$1
    local pattern=$2
    local filter=$3
    echo -e "${YELLOW}Processing $name...${NC}"
    (find "$LOG_DIR" -type f -exec grep -E "$pattern" "{}" \; | sort -u $filter > "${OUTPUT_FILES[$name]}") & show_loading
    separator
}

# Patterns and filters for each type
declare -A PATTERNS=(
    ["cpanel"]='https?://[^/]*\.(go.th|ac.th|co.th|gov|edu|go.id|ac.id|co.id|sch.id|rumahweb.com|hostinger.com):208[37]'
    ["admin"]='https?://[^/]*\.(go.th|ac.th|co.th|gov|edu|go.id|ac.id|co.id|sch.id|rumahweb.com|hostinger.com)/administrator'
    ["adminpanel"]='https?://[^/]*\.(go.th|ac.th|co.th|gov|edu|go.id|ac.id|co.id|sch.id|rumahweb.com|hostinger.com)/admin'
    ["wp-login"]='https?://[^/]*\.(go.th|ac.th|co.th|gov|edu|go.id|ac.id|co.id|sch.id|rumahweb.com|hostinger.com)/wp-login\.php'
    ["direct"]='https?://[^/]*\.(go.th|ac.th|co.th|gov|edu|go.id|ac.id|co.id|sch.id|rumahweb.com|hostinger.com)'
    ["adminer"]='https?://[^/]*\.(go.th|ac.th|co.th|gov|edu|go.id|ac.id|co.id|sch.id|rumahweb.com|hostinger.com)/adminer\.php'
    ["phpmyadmin"]='https?://[^/]*\.(go.th|ac.th|co.th|gov|edu|go.id|ac.id|co.id|sch.id|rumahweb.com|hostinger.com)/phpmyadmin'
    ["sqlpanel"]='https?://[^/]*\.(go.th|ac.th|co.th|gov|edu|go.id|ac.id|co.id|sch.id|rumahweb.com|hostinger.com)/sql-panel'
    ["plesk"]='https?://[^/]*\.(go.th|ac.th|co.th|gov|edu|go.id|ac.id|co.id|sch.id|rumahweb.com|hostinger.com):8443'
    ["directadmin"]='https?://[^/]*\.(go.th|ac.th|co.th|gov|edu|go.id|ac.id|co.id|sch.id|rumahweb.com|hostinger.com):2222'
    ["cloudpanel"]='https?://[^/]*\.(go.th|ac.th|co.th|gov|edu|go.id|ac.id|co.id|sch.id|rumahweb.com|hostinger.com):8443'
    ["ispconfig"]='https?://[^/]*\.(go.th|ac.th|co.th|gov|edu|go.id|ac.id|co.id|sch.id|rumahweb.com|hostinger.com):8080'
    ["vestacp"]='https?://[^/]*\.(go.th|ac.th|co.th|gov|edu|go.id|ac.id|co.id|sch.id|rumahweb.com|hostinger.com):8083'
    ["ajenti"]='https?://[^/]*\.(go.th|ac.th|co.th|gov|edu|go.id|ac.id|co.id|sch.id|rumahweb.com|hostinger.com):8000'
    ["aapanel"]='https?://[^/]*\.(go.th|ac.th|co.th|gov|edu|go.id|ac.id|co.id|sch.id|rumahweb.com|hostinger.com):8888'
    ["cyberpanel"]='https?://[^/]*\.(go.th|ac.th|co.th|gov|edu|go.id|ac.id|co.id|sch.id|rumahweb.com|hostinger.com):8090'
    ["webuzo"]='https?://[^/]*\.(go.th|ac.th|co.th|gov|edu|go.id|ac.id|co.id|sch.id|rumahweb.com|hostinger.com):300[234]'
    ["hestiacp"]='https?://[^/]*\.(go.th|ac.th|co.th|gov|edu|go.id|ac.id|co.id|sch.id|rumahweb.com|hostinger.com):8083'
    ["virtualmin"]='https?://[^/]*\.(go.th|ac.th|co.th|gov|edu|go.id|ac.id|co.id|sch.id|rumahweb.com|hostinger.com):10000'
    ["runcloud"]='https?://[^/]*\.(go.th|ac.th|co.th|gov|edu|go.id|ac.id|co.id|sch.id|rumahweb.com|hostinger.com):8080'
)

# Process each type
for name in "${!PATTERNS[@]}"; do
    process_logs "$name" "${PATTERNS[$name]}" ""
done

echo -e "${GREEN}Sorting process completed.${NC}"
