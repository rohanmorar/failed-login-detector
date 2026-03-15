with open("auth.log", "r") as file:
    for line in file:
        if "Failed password" in line:
            parts = line.split()
            ip = parts[12]
            print(ip)




line = "Jan 15 10:23:01 server sshd[1234]: Failed password for invalid user admin from 192.168.1.100 port 22 ssh2"

def enumerate_log_line(line: str):
    parts = line.split()

    for index, word in enumerate(parts):
        print(index, word)
