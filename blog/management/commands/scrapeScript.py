from django.core.management.base import BaseCommand, CommandError
from blog.models import Trackee

import requests
import bs4
import os

def underTargetPrice(url, alertPrice):
    response = requests.get(url)
    soup = bs4.BeautifulSoup(response.text, "html.parser")
    priceTag = soup.find("span", { "class" : "price" } )
    price = float(priceTag.text[4:])
    if price < alertPrice:
        return True
    else:
        return False

class Command(BaseCommand):
    help = 'Runs through all recorded trackees, scrapes website and checks if the target price has been reached, notifies mobile and deletes table entry if so, otherwise null'

    def add_arguments(self, parser):
        pass
        #parser.add_argument('poll_id', nargs='+', type=int)

    def handle(self, *args, **options):
        allTrackees = Trackee.objects.all()
        for i in range(len(allTrackees)):
            trackee = allTrackees[i]
            try:
                if underTargetPrice(trackee.url, float(trackee.target)):
                    self.stdout.write(trackee.url + " under target")
                    trackee.delete()
                else:
                    self.stdout.write(trackee.url + " not under target")
            except:
                self.stdout.write(trackee.url + " not valid")
                trackee.delete()

