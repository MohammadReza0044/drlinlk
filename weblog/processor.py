from django.conf import settings
import datetime

from .models import Visitors

import socket
import random

def save_visitor_info(request):
    present_date = None
    try:
        #----- get visitor ip -----#
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')    
        #----- check if ip adress is valid -----#
        try:
            socket.inet_aton(ip)
            ip_valid = True
        except socket.error:
            ip_valid = False
        #----- check if ip adress is valid -----#
        if ip_valid:

            present_date = datetime.datetime.now()
            ref_date_1 = present_date - datetime.timedelta(days=1)
            ref_date_2 = present_date - datetime.timedelta(days=2)

            if Visitors.objects.filter(ip=ip, page=request.path, visit_time__gte=ref_date_1).count() == 0:
                new_Visitors = Visitors(
                ip = ip,
                page= request.path,
                visit_time= present_date)          
                new_Visitors.save()

            if Visitors.objects.filter(ip=ip, page=request.path, visit_time__gte=ref_date_1).count() == 1:
                visitor_info_obj = Visitors.objects.get(ip=ip, page=request.path, visit_time__gte=ref_date_1)
                visitor_info_obj.visit_time = present_date
                visitor_info_obj.save()
    except:
        pass

    context_nb_vistors = 0
    ref_date = present_date - datetime.timedelta(minutes=5) 
    context_nb_vistors = Visitors.objects.filter(visit_time__gte=ref_date).values_list('ip', flat=True).distinct().count()

    return {"context_nb_vistors":context_nb_vistors}