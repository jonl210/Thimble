from django.urls import path
from . import views

app_name = 'groups'
urlpatterns = [
    path('', views.create),
    path('<group_type>', views.group_view),
    path('<group_id>/<profile_id>', views.add_member),
]