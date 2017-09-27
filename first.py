import io,json
import subprocess
import pyrebase
config = {
    "apiKey": "AIzaSyDfxLk8_yivA0GOLreYUhFeIvO9G81q3oQ",
    "authDomain": "status-pi.firebaseapp.com",
    "databaseURL": "https://status-pi.firebaseio.com",
    "storageBucket": "status-pi.appspot.com",
}
firebase = pyrebase.initialize_app(config)
db = firebase.database()
status={
"basic":{
                "hostname" : "hostname -b",
                "distro_name":"uname -s",
                "kernel_version":"uname -v",
                "date":"date",
                "machine":"uname -m",
                "voltage":"vcgencmd measure_volts core |cut -c6-| sed 's/.$//'",
                "temperature":"vcgencmd measure_temp|cut -c6-| sed 's/..$//'",
                "firmware_version":"/opt/vc/bin/vcgencmd version"

},"network":{

                        x:{
                                "ip" : "/sbin/ifconfig "+x+" | grep 'inet addr:' | cut -d: -f2 | awk '{ print $1}'",
                                "ip_loopback": "hostname -i",
                                "bcast"  : "/sbin/ifconfig "+x+" | grep 'inet addr:' | cut -d: -f3 | awk '{ print $1}'",
                                "sub" : "/sbin/ifconfig "+x+" | grep 'inet addr:' | cut -d: -f4 | awk '{ print $1}'",
                                "mac"            :"/sbin/ifconfig "+x+" | grep 'HWaddr' | tr -s ' ' |cut -d' ' -f5",
                                "rx_packet"  :"/sbin/ifconfig "+x+" | grep 'RX packet' | cut -d: -f2 | awk '{ print $1}'",
                                "tx_packet"  :"/sbin/ifconfig "+x+" | grep 'TX packet' | cut -d: -f2 | awk '{ print $1}'",
                                "rx_bytes"   :"/sbin/ifconfig "+x+" | grep 'RX bytes' | cut -d: -f2 | awk '{ print $1$2$3}'",
                                "tx_bytes"       :"/sbin/ifconfig "+x+" | grep 'TX bytes' | cut -d: -f2 | awk '{ print $1$2$3}'"
                                } for x in ("eth0","lo","wlan0")
},"physical":{
                "ram":{"total":"free -m  | grep 'Mem' | tr -s ' ' |cut -d' ' -f2",
                        "used":"free -m  | grep 'Mem' | tr -s ' ' |cut -d' ' -f3",
                        "free":"free -m  | grep 'Mem' | tr -s ' ' |cut -d' ' -f4",
                        "shared":"free -m  | grep 'Mem' | tr -s ' ' |cut -d' ' -f5",
                        "buffefs":"free -m  | grep 'Mem' | tr -s ' ' |cut -d' ' -f6",
                        "cached":"free -m  | grep 'Mem' | tr -s ' ' |cut -d' ' -f7"
                },
                "harddisk":{"size":"df -h |grep 'root' | tr -s ' '|cut -d ' ' -f2 | sed 's/.$//'",
                        "used":"df -h |grep 'root' | tr -s ' '|cut -d ' ' -f3 | sed 's/.$//'",
                        "avail":"df -h |grep 'root' | tr -s ' '|cut -d ' ' -f4 | sed 's/.$//'",
                        "user":"df -h |grep 'root' | tr -s ' '|cut -d ' ' -f5 | sed 's/.$//'"
                },
                "cpu":{"current":"cat /sys/devices/system/cpu/cpu0/cpufreq/scaling_cur_freq",
                        "max":"cat /sys/devices/system/cpu/cpu0/cpufreq/scaling_max_freq"
                }
},"peripheral":{
                "hdmi":"tvservice -n",
                "camera":"vcgencmd get_camera | grep -o '.$'",
                "usb":"lsusb |tr -d ':'| awk '$4 > 3 { print $4$7$8$9$10}'"
}
}
#print(commands.getoutput(basic["Date"]))
#for key, value in status["basic"].items():
#       status["basic"][key]=commands.getoutput(status["basic"][key])
#print(basic)

#for key, value in status["network"]["eth0"].items():
#       status["network"]["eth0"][key]=commands.getoutput(status["network"]["eth0"][key])

#status={basic,network}
def check_pin(pin,type):                                                                                                                                                                             
        GPIO.setmode(GPIO.BOARD)                                                                                                                                                                     
        GPIO.setup(pin,type)                                                                                                                                                                         
        return GPIO.input(pin)

def split_usb(text):
    dic_usb={}
    for usb in text.split('\n'):
        dic_usb[usb[:3]]=usb[3:usb.find("\n")]
    return dic_usb

def runCommand(dic):
        for key, value in dic.items():
                if isinstance(value, dict):
                        runCommand(value)
                else:
                        #dic[key]=commands.getoutput(value)
                        dic[key]=subprocess.getoutput(value)
                        if dic[key] == '' : # Debug create empty obj in usb
                                continue
                        #print(value)
                        if key is "usb" :
                                dic[key]=split_usb(dic[key])

runCommand(status)
mac_connect=[]
for x in ['eth0','lo','wlan0']:
        result=status['network'][x]['mac']
        if  result.find("not found")<0 and result != "":
                mac_connect.append(result)

#print(mac_connect)
#with open('./test.json', 'w') as file:
#       json.dump(status, file)

#print(status)
total={mac_connect[0]:status}
db.update(total)
#print(total)
