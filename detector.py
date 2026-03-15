failed_logins = {}
THRESHOLD = 5

with open("auth.log", "r") as file:
    for line in file:
        line = line.strip()

        if "Failed password" in line:
            parts = line.split()
            ip = parts[12]
            
            if ip not in failed_logins:
                failed_logins[ip] = 0
            failed_logins[ip] += 1

for ip, count in failed_logins.items():
    if count >= THRESHOLD:
        print(f"ALERT: {ip} has {count} failed login attempts")

line = "Jan 15 10:23:01 server sshd[1234]: Failed password for invalid user admin from 192.168.1.100 port 22 ssh2"

def enumerate_log_line(line: str):
    parts = line.split()

    for index, word in enumerate(parts):
        print(index, word)
