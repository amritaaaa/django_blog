from django.shortcuts import render
from django.core.mail import send_mail

# Create your views here.
def sendmail(request):
    send_mail('hello from django',
    'hello there . this is an automated msg',
    'amritasinha.fnd@gmail.com',
    ['mzarakhan643@gmail.com'])

    return render(request,'emailview.html')
