from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

# def messaging(request):
#     return render(request,"chatting_app/message.html")

@login_required
def messaging(request):
    return render(request,"chatting_app/message.html")