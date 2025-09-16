#!/bin/bash
clear
ver="0.8"
echo "Eyescry $ver by Maxspells"

# Colors for terminal
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
CYAN='\033[0;36m'
NC='\033[0m' # No Color

# Logfile stuff
current_date=$(date "+%m-%d-%Y")
last_date="$current_date"
LOGFILE="/home/admin/sshlog/ssh_$current_date.log"


echo "I spy with my little eye: SSH login attempts..."

log_event() {
    local msg=$1
    echo -e "$msg" | tee -a "$LOGFILE"
}


journalctl -u ssh -f | while read -r line; do
    # Gets current date and current time, updates the logfile if the day rolls over
    current_time=$(date "+%H:%M:%S")
    current_date=$(date "+%m-%d-%Y")
    if [ "$current_date" != "$last_date" ]; then
        last_date="$current_date"
        LOGFILE="/home/admin/sshlog/ssh_$current_date.log"
        touch "$LOGFILE"
    fi

    # Checks the SSH logs
    if echo "$line" | grep -Eq "publickey"; then
        short=$(echo "$line" | grep -oP '(Postponed|Accepted) publickey for \S+ from (\d{1,3}\.){3}\d{1,3}')
        user=$(echo "$short" | grep -oP '(?<=for )\S+')
        ip=$(echo "$short" | grep -oP '(\d{1,3}\.){3}\d{1,3}')
        action=$(echo "$short" | grep -oP '^(Postponed|Accepted)')
        log_event "[$current_time]${GREEN}$action${NC} publickey for ${YELLOW}$user${NC} from ${CYAN}$ip${NC}"
    elif echo "$line" | grep -Eq "Disconnected from invalid user|Connection closed by invalid user"; then
        user=$(echo "$line" | grep -oP '(?<=invalid user )\S+')
        ip=$(echo "$line" | grep -oP '(\d{1,3}\.){3}\d{1,3}')
        log_event "[$current_time]${CYAN}$ip${NC} tried to log in as ${YELLOW}$user${NC}: Invalid User"
    elif echo "$line" | grep -Eq "Disconnected from authenticating user|Connection closed by authenticating user"; then
        user=$(echo "$line" | grep -oP '(?<=authenticating user )\S+')
        ip=$(echo "$line" | grep -oP '(\d{1,3}\.){3}\d{1,3}')
        log_event "[$current_time]${CYAN}$ip${NC} tried to log in as ${RED}$user${NC}: Authentication Failure"
    fi
done
