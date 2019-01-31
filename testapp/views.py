from django.shortcuts import render, HttpResponse, redirect
from django.template.context_processors import csrf
from django.contrib.auth import get_user_model
from .models import Photo,CommentPhoto
from django.contrib import auth

User = get_user_model()

class Test:

    def test1(self,request):
        if not request.POST:
            return render(request,"testapp.html",{"user":auth.get_user(request).username})
        else:
            try:
                user = User.objects.create_user(username=request.POST.get('log', ""),
                                                email=request.POST.get('mail', ""),
                                                password=request.POST.get('pass', ""))
            except:
                user = None
            if user:
                auth.login(request, user)
                return redirect('test/test1/', {"user": auth.get_user(request).username})
            else:
                content = csrf(request)
                content['error'] = "Name is Busy"
                content['url'] = "test/test1/"
                return render(request, "testapp.html", content, {"user": auth.get_user(request).username})

    def main(self,request):
        return render(request,"Main.html",{"user":auth.get_user(request).username})

    def test2(self, request):
        return render(request, "testapp2.html",{"user":auth.get_user(request).username})

    def acc(self, request):
        return render(request, "MyAcc.html",{"user":auth.get_user(request).username})
    def test3(self, request):
        return render(request, "test.html",{"user":auth.get_user(request).username})

class Photos:

    def showall(request):
        # [[Photo,[(comment, user),(comment, user),(comm, user),.....]],[video,],[video,].......]
        photos = Photo.objects.all()
        content = []
        for pho in photos:
            photo_con = [pho, []]
            comments = CommentPhoto.objects.filter(Comment_Photo_id=pho.id)
            for com in comments:
                user = User.objects.get(id=com.Comment_User_id)
                photo_con[1].append((com, user))
            content.append(photo_con)
        return render(request, "Main.html", {"content": content, "user": auth.get_user(request).username})

test = Test()
photos = Photos()