import randfacts
import winsound
import time
from time import sleep
import os
from plyer import notification

def send_notification (title, message) :

    notification.notify (

        title = "Random Fun Fact !!",
        message = f"{x}",
        timeout = 17
	)

if __name__ == "__main__" :

    os.system ("cls")

    x = str (randfacts.get_fact ().title ())

    while True :

        send_notification ("Random Fun Fact !!".title (), f"\n{x}".title ())

        sleep (420)
