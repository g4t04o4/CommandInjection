import subprocess, os, shutil
from django.shortcuts import render, redirect
from .models import BlogPost



# Create your views here.

def main_page(request):
    if request.method == 'POST':
        ipaddress = request.POST['ipaddress']
        result = subprocess.Popen('ping -w 5 ' + ipaddress, shell=True,
                                  stdout=subprocess.PIPE).stdout.read()

        return render(request, 'ping_result.html', {'result': result.decode('cp866')})
    else:
        posts = list(reversed(BlogPost.objects.all()))
        return render(request, 'all_posts.html', {'post_list': posts})


def new_post(request):
    if request.method == 'POST':

        file = request.FILES.get('post_image', False)
        name = request.POST['post_name']
        text = request.POST['post_text']

        if file == False or name in [None, '']:
            return render(request, 'new_post.html')

        post = BlogPost(name=name,
                        text=text,
                        image=file)
        post.save()
        return render(request, 'new_post.html')
    else:
        return render(request, 'new_post.html')


def clear(request):
    BlogPost.objects.all().delete()
    if os.path.isdir('image'):
        shutil.rmtree('image')
    return redirect('/')