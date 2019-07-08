import subprocess

from django.shortcuts import render


# Create your views here.

def ping(request):
    if request.method == 'POST':
        ipaddress = request.POST['ipaddress']
        result = subprocess.Popen('ping -w 5 ' + ipaddress, shell=True,
                                  stdout=subprocess.PIPE).stdout.read()
        return render(request, 'ping_result.html', {'result': result.decode('cp866')})
    else:
        return render(request, 'all_posts.html')


def new_post(request):
    if request.method == 'POST':
        return render(request, 'new_post.html')
    else:
        return render(request, 'new_post.html')