from django.shortcuts import render
from .models import *

from rest_framework.views import APIView
from rest_framework.response import Response

def index(request):
    return render(request, 'index.html')


class UserModelView(APIView):
    def get(self, request):
        data = {"ok": True, 'members': []}

        user_list = UserModel.objects.all()
        for obj in user_list:
            user_data = {
                'id': obj.id,
                'real_name': obj.real_name,
                'tz': obj.time_zone,
                'activity_periods': []
            }

            for activity_period in obj.activityperiodmodel_set.all():
                activity_period_data = {
                    'start_time': activity_period.start_time.strftime("%b %d %Y %-I:%M%p") ,
                    'end_time': activity_period.end_time.strftime("%b %d %Y %-I:%M%p"),
                }
                user_data['activity_periods'].append(activity_period_data)
            data['members'].append(user_data)

        return Response(data)
