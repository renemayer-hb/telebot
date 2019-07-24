# -*- coding: utf-8 -*-


#[General]
# prefered language
# translations available
# de = deutsch, en = english, sv = svenska, da = dansk, sl = Slovenski
language="de"
# api_key you got from @botfather for your bot
apikey = ""
# ACL for controll the repeater (your own ID should in here) (ID is NOT @username)
grant=[]
# Call of repeater
botcall="DL2RPM"
# ID des Repeaters
dmrid = "263305699"
# ID des Botowner / der Botowner (die bekommen Nachrichten über Statusänderungen)
owner=[]

#[Services]
# brandmeister api
bmapiactive=1
bmapi=""

# Liste of processes
prozesse=["MMDVMHost","DMRGateway","YSFGateway","ircddbgatewayd","YSF2DMR"]

# folder which contains mmdvm-logs
pistar_mmdvmlogs = "/var/log/pi-star"
mmdvmlogs = "/var/log/mmdvm"
mmprefix = "MMDVM"

# folder wich contains the dmr-gw logfiles
pistar_gwlogs = "/var/log/pi-star"
gwlogs = "/var/log/mmdvm"
gwprefix = "DMRGateway"

# how to start mmdvm
mmdvmaufruf = "/usr/bin/screen -d -m -S MMDVM /home/pi/MMDVMHost/MMDVMHost /home/pi/MMDVMHost/MMDVM-DB0SBN.ini"
# how to start dmrgw should it be active?
dmrgwaufruf = "/usr/bin/screen -d -m -S DMRGW /home/pi/DMRGateway/DMRGateway /home/pi/DMRGateway/DMRGateway.ini"
dmrgwaktiv = 0
# how to start ysfgw
ysfgw = "sudo /etc/init.d/YSFGateway.sh start"
ysfgwaktiv = 0
# how to start ircdbbgw
ircdbbgw = "sudo /etc/init.d/ircddbgateway start"
ircdbbgwaktiv = 0


logfile = "botlog.txt"
userfile = "users.csv"

# define pathes to 1-wire sensor data
sensors = [
  ["/sys/bus/w1/devices/28-24d329126461/w1_slave","KA 1"],
  ["/sys/bus/w1/devices/28-a78d29126461/w1_slave","KA 2"]
]

# define gpio ports
gpioactive = 1
gpioports = [
  # [gpio number,"name",invers]
  [11,"TX",0],
  [12,"RX",0],
  [13,"NS1",0],
]

#### SVXLink Settings
svxactive = 0
svxlogic = "/home/pi/remote/svx_pty.RepeaterLogic"

#### Pi-Star Kommandos aktivieren
ispistar = 0

backupfiles = ["/home/pi/software/telebot/config.py","/home/pi/software/telebot/commands.py","/etc/*","/var/log/*","/opt/*/*.ini"]
