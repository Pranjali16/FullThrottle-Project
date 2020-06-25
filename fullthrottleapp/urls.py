from django.conf.urls import url
from .views import *
urlpatterns = [
      url('user_activity/', UserActivityView.as_view(), name='login'),

]