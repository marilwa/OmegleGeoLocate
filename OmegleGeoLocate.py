from geolite2 import geolite2
import socket, subprocess 

# My network adapter name was Wi-Fi, change this your yours accordingly. use ipconfig in windows and ifconfig in Linux to find your network adapter name.
cmd = r"C:\Program Files\Wireshark\tshark -i Wi-Fi"

process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
my_ip = socket.gethostbyname(socket.gethostname())
reader = geolite2.reader()

def get_ip_location(ip):
    location = reader.get(ip)
    
    try:
        country = location["country"]["names"]["en"]
    except:
        country = "Unknown"

    try:
        subdivision = location["subdivisions"][0]["names"]["en"]
    except:
        subdivision = "Unknown"    

    try:
        city = location["city"]["names"]["en"]
    except:
        city = "Unknown"
    
    return country, subdivision, city





for line in iter(process.stdout.readline, b""):
    columns = str(line).split(" ")
# try out printing this line if your code is not running . In any case your code should run till this point.
    # print(columns)

# Just change your ip address here. and the program will work like a charm. Depending upton the tshark setting , you might have to make some modification in this filter if code is halting.
    if "192.168.0.104" in columns and "UDP" in columns: 
        src_ip = columns[columns.index("UDP")-3]
        # print(src_ip)
        # print(my_ip)
      

        if src_ip == my_ip:
            continue


        try:
            country, sub, city = get_ip_location(src_ip)
            print(">>> " +"Country: "+ country + ", State:  " + sub + "City: " + city)
        except:
            try:
                real_ip = socket.gethostbyname(src_ip)
                country, sub, city = get_ip_location(real_ip)
                print(">>> " + country + ", " + sub + ", " + city)
            except:
                print("Not found")