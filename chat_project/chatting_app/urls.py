
from django.urls import path,include
from .views import messaging
app_name="chatting_app"

urlpatterns = [
    
    # path("",messaging, name = "chat_url"),
    path("",messaging, name = "chat_url"),

]
