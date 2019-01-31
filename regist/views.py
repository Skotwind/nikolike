from django.shortcuts import render, HttpResponse, redirect
from django.template.context_processors import csrf
from django.contrib.auth import get_user_model
User = get_user_model()
from django.contrib import auth


class Regist:
    def reg(self, request):
        if not request.POST:
            content = csrf(request)
            content["status"] = "Registration:"
            content['url'] = "/regist/regist/"
            return render(request, 'index.html', content,{"user":auth.get_user(request).username})
        else:
            try:
                user = User.objects.create_user(username=request.POST.get('login', ""),
                                                password=request.POST.get('password',""))
            except:
                user = None
            if user:
                auth.login(request, user)
                return redirect('/video/all/',{"user":auth.get_user(request).username})
            else:
                content = csrf(request)
                content["status"] = "Registration:"
                content['error'] = "Name is Busy"
                content['url'] = "/regist/regist/"
                return render(request, 'index.html', content,{"user":auth.get_user(request).username})

    def login(self, request):
        if not request.POST:
            content = csrf(request)
            content["status"] = "Login to account:"
            content['url'] = "/regist/login/"
            return render(request,"index.html", content,{"user":auth.get_user(request).username})
        else:
            user = auth.authenticate(username=request.POST['login'],
                                     password=request.POST['password'])
            if user:
                auth.login(request, user)
                content = csrf(request)
                content["status"] = "Login to account:"
                content['succ'] = "You are logged in as"
                return redirect('/video/all',content,{"user":auth.get_user(request).username})
            else:
                content = csrf(request)
                content["status"] = "Login to account:"
                content['error'] = "wrong login or password"
                content['url'] = "/regist/login/"
                return render(request,'index.html',content,{"user":auth.get_user(request).username})

    def logout(self, request):
        auth.logout(request)
        return redirect("/regist/login/",{"user":auth.get_user(request).username})

regist = Regist()



# Create your views here.
