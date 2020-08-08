from datetime import datetime
import json
from django.core.management.base import BaseCommand, CommandError
from main.models import *

class Command(BaseCommand):
    help = 'Load dummy data into the database'

    def add_arguments(self, parser):
        parser.add_argument('filename', type=str, help='Indicates the selected file.')

    def handle(self, *args, **kwargs):
        filename = kwargs["filename"]
        file = open(filename)
        data = json.load(file)

        for member in data["members"]:
            user_obj = UserModel()
            user_obj.id = member['id']
            user_obj.real_name = member['real_name']
            user_obj.time_zone = member['tz']
            user_obj.save()

            for act_period in member['activity_periods']:
                obj = ActivityPeriodModel()
                obj.user = user_obj
                obj.start_time = datetime.strptime(act_period['start_time'] + ' '+ user_obj.time_zone, '%b %d %Y %I:%M%p' + ' ' + user_obj.time_zone)
                obj.end_time = datetime.strptime(act_period['end_time'] + ' '+ user_obj.time_zone, '%b %d %Y %I:%M%p' + ' ' + user_obj.time_zone)
                obj.save()

        self.stdout.write(self.style.SUCCESS('Data loaded from "%s"' % filename))
