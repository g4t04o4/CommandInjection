import subprocess

from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def ping(request):
    if request.method == 'POST':
        ipaddress = request.POST['ipaddress']

        result = subprocess.Popen('ping -w 5 ' + ipaddress, shell=True, stdout=subprocess.PIPE).stdout.read()

        # return HttpResponse('<pre>' + result.decode('cp866') + '</pre>')
        return render(request, 'ping_result.html', {'result': result.decode('cp866')})
    else:
        return render(request, 'ping_input.html')
