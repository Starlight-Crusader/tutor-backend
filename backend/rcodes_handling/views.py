from django.shortcuts import render
from users import models
from rest_framework import generics, decorators, status, response
from datetime import datetime
from django.db.models import F
from datetime import datetime as time
import datetime


@decorators.api_view(['DELETE'])
def delete_expired(request):
    try:
        records = models.RecoveryCode.objects.all()
    except:
        return response.Response('There are no recovery codes.',
                                 status=status.HTTP_202_ACCEPTED)

    records = models.RecoveryCode.objects.filter(active_time__range=[time.now()-datetime.timedelta(days=360), time.now()]).delete()

    return response.Response('Expired codes were successfully deleted!')
