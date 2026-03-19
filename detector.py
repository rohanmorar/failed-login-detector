import os

failed_logins = {}
LOG_FILE = "auth.log"
THRESHOLD = 5
IP_INDEX = 12

if not os.path.exists(LOG_FILE):
    print(f"Error: {LOG_FILE} not found.")
    exit()

with open(LOG_FILE, "r") as file:
    for line in file:
        line = line.strip()

        if "Failed password" in line:
            parts = line.split()
            ip = parts[IP_INDEX] 
            timestamp = f"{parts[0]} {parts[1]} {parts[2]}"

            if ip not in failed_logins:
                failed_logins[ip] = {"count": 0, "timestamps": []}
            failed_logins[ip]["count"] += 1
            failed_logins[ip]["timestamps"].append(timestamp)

for ip, data in failed_logins.items():
    if data["count"] >= THRESHOLD:
        print(f"ALERT: {ip} has {data["count"]} failed login attempts")
        print(f"  First seen: {data["timestamps"][0]}")
        print(f"  Last  seen: {data["timestamps"][-1]}")

#line = "Jan 15 10:23:01 server sshd[1234]: Failed password for invalid user admin from 192.168.1.100 port 22 ssh2"

#def enumerate_log_line(line: str):
    #parts = line.split()

    #for index, word in enumerate(parts):
        #print(index, word)
