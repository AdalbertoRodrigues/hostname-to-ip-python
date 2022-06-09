import  sys
import socket
import csv

def hostToIp(hostname):
    return socket.gethostbyname(hostname)

def main():

    try:
        filePath = sys.argv[1]
    except:
        return
        
    ips = []

    with open(filePath) as file:
        csv_reader = csv.reader(file, delimiter=",")
        for row in csv_reader:
            try:
                ip = hostToIp(row[0])
            except:
                ip = "-"
            ips.append("".join([row[0], ",", ip]))

    print("\n".join(ips))

main()






