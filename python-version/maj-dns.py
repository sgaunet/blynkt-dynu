from blinkt import set_pixel, set_brightness, show, clear
import time
import json
import os
import subprocess
import requests
import os
import inspect

def realip():
    result= subprocess.check_output(['dig', '@ns1-1.akamaitech.net','ANY','whoami.akamai.net'," +short"])

    for ligne in result.decode('utf-8').splitlines():
        if not ligne.startswith(";;") and ligne.find("IN	A	") != -1 :
            ligne_with_ip=ligne

    return ligne_with_ip.split()[4]

def ip_of_dns(dns):
    #ip_dns=os.system("dig @8.8.8.8 ANY "+data["DNS"]+" +short | grep -v ':' | head -n1")
    result = subprocess.check_output(['dig', '@8.8.8.8','ANY',dns," +short"])

    for ligne in result.decode('utf-8').splitlines():
        if not ligne.startswith(";;") and ligne.find("IN	A	") != -1 :
            ligne_with_ip=ligne

    return ligne_with_ip.split()[4]

"""Call api.dynu.com to update the DNS

Returns:
    [type] -- [description]
"""
def update_dns(login,password,dyndns):
    url="https://"+login+":"+password+"@api.dynu.com/nice/updadte?hostname="+dyndns
    print("url to call : "+url)
    r = requests.get(url)
    print(r.text)
    return not r.text.find("good") == -1


"""blink every LED in green during one sec

Returns:
    None
"""
def init_blink():
    clear ()
    for i in range(0,8) :
        set_pixel (i, 0, 255, 0)
        set_brightness(0.1)
    show ()
    time.sleep (1)
    for i in range(0,8) :
        set_pixel (i, 0, 0, 0)

def which_pixel(i):
    i += 1
    if i > 7:
        i = 0
        clear ()
    return i


#print(os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe()))))
init_blink()

# Open the conf.json file and load the content
with open(os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))+'/conf.json') as json_file:
    data = json.load(json_file)

print(data["USER"])
print(data["PASSWORD"])
print(data["DNS"])
i = 0

while True:    
    try:
        ip_dns = ip_of_dns(data["DNS"])
        real_ip = realip()

        print(ip_dns)
        print(real_ip)

        if ip_dns != real_ip:
            print("Mise à jour")
            if update_dns(data["USER"],data["PASSWORD"],data["DNS"]):
                print("Mise à jour ok")
                set_pixel (i, 0, 0, 255)
                show ()
            else:
                print("probleme lors de la mise à jour")
                set_pixel (i, 255, 0, 0)
                show ()
        else:
            print("pas besoin de mise a jour")
            set_pixel (i, 0, 255, 0)
            show ()

        i=which_pixel(i)
        print(i)
        time.sleep(300)

    except Exception as e:
        print(e)
        time.sleep(300)

    
