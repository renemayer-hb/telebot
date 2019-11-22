Zur Installation
Registrieren des Bots bei Telegram

    Schreib @BotFather bei Telegram per PN an
    Mit dem Kommando /newbot legt ihr einen neuen Bot an
    Auf die Frage: „Alright, a new bot. How are we going to call it? Please choose a name for your bot.“ gebt ihr den Namen für euren Bot an.
    Danach einen Usernamen, mit dem ihr euren Bot später bei Telegram anschreiben könnt.
    Darauf hin erhaltet ihr einen HTTP API Key. Den brauchen wir später in den Konfigurationsdateien unseres telebots




Kurzanleitung zur Installation des telebot v3 (Python3):

	rpi-rw
	sudo apt-get install python3-pip python-pip
	sudo apt-get install python-rpi.gpio python3-rpi.gpio
	sudo pip3 install psutil telepot requests
	sudo pip install crudini
	in /home/pi-star
	git clone https://github.com/renemayer-hb/telebot.git
	cd telebot
	git checkout v3
	die config.py editieren
	sudo cp telebot.service /etc/systemd/system/telebot.service
	sudo systemctl enable telebot.service
	sudo systemctl start telebot.service

