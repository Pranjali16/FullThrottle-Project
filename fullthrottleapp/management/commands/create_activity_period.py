from datetime import datetime, timedelta

from django.core.management.base import BaseCommand
from django.shortcuts import get_object_or_404

from fullthrottleapp.models import *


class Command(BaseCommand):
    help = 'Create random users'

    def add_arguments(self, parser):
        parser.add_argument('id', type=int, help='Indicates the id of user')

    def handle(self, *args, **kwargs):
        user_id = kwargs['id']
        user_obj = get_object_or_404(User, id=user_id)
        if user_obj:
            end_date = datetime.now()
            start_date = end_date + timedelta(days=-(2 * 7))
            end_time = datetime.strftime(end_date, "%b %d %Y %I:%M %p")
            start_time = datetime.strftime(start_date, "%b %d %Y %I:%M %p")
            ActivityPeriod.objects.create(user_id=user_obj, start_time=start_time, end_time=end_time)
        else:
            print("User is not available with this id, please enter valid id")

