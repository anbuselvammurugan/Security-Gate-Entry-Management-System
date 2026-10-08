from django.urls import path
from . import views


urlpatterns = [

    path(
        'dash/',
        views.dashboard,
        name='dashboard'
    ),

    path(
        'visitors/',
        views.visitor_list,
        name='visitor_list'
    ),

    path(
        'visitor/register/',
        views.register_visitor,
        name='register_visitor'
    ),

    path(
        'visitor/<int:visitor_id>/checkout/',
        views.check_out,
        name='check_out'
    ),

]