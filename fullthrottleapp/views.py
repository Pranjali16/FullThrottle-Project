from datetime import datetime, date, time, timedelta
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import *
from .models import ActivityPeriod

class UserActivityView(APIView):
    """
    Displays User details with activity period in respective json
    """
    def get(self, request):

        user_data = User.objects.all()
        members = []
        for obj in user_data:
            activity_objects = ActivityPeriod.objects.select_related('user_id').values('start_time', 'end_time').\
                filter(user_id=obj)
            new_dict = {
                "id": obj.id,
                "real_name": obj.name,
                "tz": obj.tz,
                "activity_periods": activity_objects
            }
            members.append(new_dict)
        return Response({"ok": 'true', "members": members}, status=status.HTTP_200_OK)
