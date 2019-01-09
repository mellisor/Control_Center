from django.http import HttpResponseRedirect

def check_login(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('dashboard/')
    return HttpResponseRedirect('accounts/login/')