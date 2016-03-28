from django.views.decorators.csrf import ensure_csrf_cookie
from basic.models import Titles,Groups
from django.shortcuts import render
from basic.grouplink_creator import creategroup_link
from django.http import HttpResponse
from basic.forms import Userinfo,Groupform,Titlesform
from django.views.decorators.csrf import csrf_exempt



def addMobileTitle(request):

    if request.method=="POST":
        print("it is post")
        a=request.POST

        for keys in a:
           ab=keys
           print(ab +"="+a[ab] )


        titleinfos=Titlesform(data=request.POST)
        if titleinfos.is_valid():
            print("info is valid")


            info=titleinfos.save(commit=False)
            print(info.id)
            #get_title=Titles()

            print(request.user)
            info.username=request.user
            info.slugGroups=creategroup_link(info.groupname)
            info.slug=creategroup_link(info.title)
            groups=Groups()

            info.save()

            print("DONE")

            return HttpResponse("DONE")
        else:
            print(titleinfos.errors)
            titleinfos.errors
            return HttpResponse("THERE WAS ERROR")
    else:
        userinfo=Userinfo()
    print("it is get")
    return render(request,"studyhelper/addmobiletitle.html",{"userinfo":userinfo})
    #return HttpResponse((ensure_csrf_cookie(addMobileTitle)))

