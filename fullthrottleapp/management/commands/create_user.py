from datetime import datetime

from django.core.management.base import BaseCommand
from django.utils.crypto import get_random_string


from fullthrottleapp.models import *


class Command(BaseCommand):
    help = 'Create random users'

    def add_arguments(self, parser):
        parser.add_argument('total', type=int, help='Indicates the number of users to be created')

    def handle(self, *args, **kwargs):
        total = kwargs['total']
        for i in range(total):
            date_obj = datetime.now()
            timezone_name = datetime.strftime(date_obj, "%Z")
            if timezone_name == "":
                timezone_name = "America/Los_Angeles"
            User.objects.create(name=get_random_string(), tz=timezone_name)
