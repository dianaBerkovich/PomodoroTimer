from django.shortcuts import render


# Create your views here.
def main_page(request):
    title = 'pomodoro'
    my_country = None
    numbers = [ 6, 7, 8, 9, 'ten' ]
    return render(request, 'Main/mainpage.html', locals())


def test_page(request):

    return render(request, 'Main/testpage.html', locals())



