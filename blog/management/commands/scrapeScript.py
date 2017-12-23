from django.core.management.base import BaseCommand, CommandError
from blog.models import Trackee, Tracker

import requests
import bs4
import os


import telegram
#"364600088"


class Command(BaseCommand):
    help = 'Runs through all recorded trackees, scrapes website and checks if the target price has been reached, notifies mobile and deletes table entry if so, otherwise null'

    def add_arguments(self, parser):
        pass
        #parser.add_argument('poll_id', nargs='+', type=int)
    
    def handle(self, *args, **options):
        token = '458733632:AAHzH3NtBMk2fvv4P0zb3Yr0qVUjnawew7k'
        bot = telegram.Bot(token=token)
        allTrackees = Trackee.objects.all()
        for i in range(len(allTrackees)):
            trackee = allTrackees[i]
            try:
                response = requests.get(trackee.url)
                soup = bs4.BeautifulSoup(response.text, "html.parser")
                priceTag = soup.find("span", { "class" : "price" } )
                price = float(priceTag.text[4:])
                if price < float(trackee.target):
                    self.stdout.write(trackee.url + " under target")
                    chatId = Tracker.objects.get(mobile=trackee.mobile).chatId
                    print(chatId)
                    text = "Yo! " + trackee.name + " has reached the target price of " + str(trackee.target)
                    bot.send_message(chat_id=chatId, text=text)
                    trackee.delete()
                else:
                    self.stdout.write(trackee.url + " not under target")
            except Exception as error:
                self.stdout.write(repr(error))
                self.stdout.write(trackee.url + " not valid")
                trackee.delete()

