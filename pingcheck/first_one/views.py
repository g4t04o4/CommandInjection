import subprocess

from django.shortcuts import render
from .models import BlogPost
import datetime


# Create your views here.

def main_page(request):
    if request.method == 'POST':
        ipaddress = request.POST['ipaddress']
        result = subprocess.Popen('ping -w 5 ' + ipaddress, shell=True,
                                  stdout=subprocess.PIPE).stdout.read()

        return render(request, 'ping_result.html', {'result': result.decode('cp866')})
    else:
        posts = BlogPost.objects.all()
        return render(request, 'all_posts.html', {'result': posts})


def new_post(request):
    if request.method == 'POST':
        file = request.FILES['post_image']
        name = request.POST['post_name']
        text = request.POST['post_text']

        # TODO: save file, do some validation
        post = BlogPost(name=name,
                        text=text,
                        image='',
                        pub_date=datetime.datetime.now())
        post.save()
        return render(request, 'new_post.html')
    else:
        return render(request, 'new_post.html')
