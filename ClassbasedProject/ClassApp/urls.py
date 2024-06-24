from django.urls import path
from .views import *
from django.contrib import admin

#create path here

urlpatterns = [
    path('register/', regclass.as_view(), name='register'),
    path('login/', logclass.as_view(), name='login'),
    path('studentreg/', studentreg.as_view(), name='studentreg'),
    path('studentdisplay/', studentdisplay.as_view(), name='studentdisplay'),
    path('delete/<pk>', delete_stud.as_view(), name='delete'),
    path('detail/<pk>', detail_stud.as_view(), name='detail'),
    path('update/<pk>', update_stud.as_view(), name='update'),

    path('fileupload/', fileupload.as_view(), name='fileupload'),
    path('displayfile/', displayfile.as_view(), name='displayfile'),
    path('deletefile/<pk>', deletefile.as_view(), name='deletefile'),
    path('detailfile/<pk>', detailfile.as_view(), name='detailfile'),
    path('updatefile/<pk>', updatefile.as_view(), name='updatefile')




]