from django.shortcuts import render


# Create your views here.

def timer_page(request):

    return render(request, 'Timer/timer.html', locals())



