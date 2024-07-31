from django.shortcuts import render

# Create your views here.


def set_cookie_view(request):
    response = render(request, 'app_cookie/set_cookie.html')
    response.set_cookie('info', 'This is a test cookie from the local server!')
    return response


def get_cookie_view(request):
    info = request.COOKIES.get('info', 'Guest')
    return render(request, 'app_cookie/get_cookie.html', {'info': info})


def delete_cookie_view(request):
    response = render(request, 'app_cookie/del_cookie.html')
    response.delete_cookie('info')
    return response
