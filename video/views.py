from django.shortcuts import render, HttpResponse, redirect
from .models import Video, Comment
from django.contrib.auth import get_user_model
User = get_user_model()

from .form import CommentForm
from django.template.context_processors import csrf
from django.contrib import auth

import json



def hello(request):
    if not request.POST and not request.GET:
        return render(request, "../regist/templates/index.html", csrf(request))

    elif request.POST:
        if 'check' in request.POST:
            print(request.POST['check'])
        else:
            print("do not check")
        if "comment" in request.POST:
            print(request.POST['comment'])
        if 'login' in request.POST:
            print(request.POST['login'])
        return HttpResponse("POST")
    elif request.GET:
        print(request.GET['login'])
        return HttpResponse("GET")



def showall(request):
    #[[video,[(comment, user),(comment, user),(comm, user),.....]],[video,],[video,].......]
    videos = Video.objects.all()
    content = []
    for vid in videos:
        video_con = [vid, []]
        comments = Comment.objects.filter(Comment_Video_id = vid.id)
        for com in comments:
            user = User.objects.get(id = com.Comment_User_id)
            video_con[1].append((com, user))

        content.append(video_con)
    return render(request, "all.html", {"form":CommentForm,"content":content,"user":auth.get_user(request).username})


def showone(request, video_id):
    args = {}
    args.update(csrf(request))
    video = Video.objects.get(id = video_id)
    comments = Comment.objects.filter(Comment_Video_id = video_id)
    com_content = []
    for com in comments:
        user = User.objects.get(id = com.Comment_User_id)
        com_content.append((com, user))
    args["video"] = video
    args["comments"] = com_content
    args["form"] = CommentForm
    return render(request, "showone.html", args)


def addcomm(request, video_id):
    print(request.path_info)
    if request.POST:
        comment = Comment()
        comment.Comment_Video = Video.objects.get(id=video_id)
        comment.Comment_text = request.POST['comment']
        comment.Comment_User = User.objects.get(id=request.user.id)
        comment.save()
    return redirect('/video/all')


def addlike(request):
    if request.GET:
        video = Video.objects.get(id=request.GET["video_id"])
        video.Video_likes += 1
        video.save()
    return HttpResponse(video.Video_likes)

def addlikecom(request):
    if request.GET:
        id_comm = request.GET['coment_id']
        comment = Comment.objects.get(id=id_comm)
        comment.Comment_likes += 1
        comment.save()
    return HttpResponse(comment.Comment_likes)

def addcommajax(request):
    if request.GET:
        comment = Comment()
        comment.Comment_Video = Video.objects.get(id=request.GET['idvideo'])
        comment.Comment_text = request.GET['text']
        comment.Comment_User = User.objects.get(id=request.user.id)
        comment.save()

        response_data = {}
        response_data['user'] = auth.get_user(request).username
        response_data['date'] = str(comment.Comment_date)
    return HttpResponse(json.dumps(response_data),
            content_type="application/json")
# Create your views here.
