from django.shortcuts import render, HttpResponse, redirect
from django.template.context_processors import csrf
from django.contrib.auth import get_user_model
from .models import Photo,CommentPhoto
from django.contrib import auth

User = get_user_model()

class Test:


    sumn = 0

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

    def test3(self, request):
        return render(request, "testapp2.html",{"user":auth.get_user(request).username})

    def but1(self, request):
        print("but1 +1")
        print(self.sumn)
        self.sumn += 1
        return render(request, "testapp2.html",)

    def but2(self, request):
        print("but2 +2")
        print(self.sumn)
        self.sumn += 2
        return render(request, "testapp2.html",)

    def but3(self, request):
        print("but3 +10")
        print(self.sumn)
        self.sumn += 10
        return render(request, "testapp2.html",)


class Photos:

    def showall(request):
        print("go")
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