__author__ = 'johnanderson1'
from basic.models import Titles,Groups
from django.shortcuts import render
from basic.grouplink_creator import creategroup_link


def addTitle(request):
    newtitlename=request.GET.get("newtitlename",False)
    groupname=request.GET.get("groupname",False)
    print(newtitlename);
    if newtitlename:
        print("is true");
        add_Title=Titles()  #will return a new row
        #insert columns to the row below
        newtitlename=newtitlename.strip()
        add_Title.title=newtitlename
        add_Title.username=request.user



       #add_group.title=" title for testing unique in ivonjoe"

        add_Title.groupname=groupname

        add_Title.slugGroups=creategroup_link(groupname)

        add_Title.save()

    return render(request,"studyhelper/start.html")


















#this view will be called to make changes to a title.because there can be more than on title
#in the db,we use the id attribute to obtain the get,the make the changes

def updateTitle(request):
    titles=Titles.objects.filter(slug="slugify")

    if request.method == 'GET':

        idnumber=request.GET.get("id",False)

        abc= request.GET.get("title",False)



        if abc:
            try:
             print("before calling object")
             titleHandler=Titles.objects.get(id=idnumber)

             print("after calling object")

             #now we can change the title to the new title
             titleHandler.title = abc  # change field
             # this will update only
             titleHandler.save()


            except Titles.DoesNotExist:
                print("there was an exception")
                pass
        else:
            pass

    return render(request,"studyhelper/start.html",{"titles":titles})
    pass


#will update the group
#how i intend to change the groupname,is using the dom to collect the value of the box that
#displays the item to be changed
#be
def updateGroup(request):
    print("in updateGroup ")
    titles=Titles.objects.get(slug="new-title")
    if request.method == 'GET':
        print("updateGroup  request is get")
        oldgroupname=request.GET.get("oldgrouname",False)

        newgroupname= request.GET.get("newgroupname",False)



        if oldgroupname:
            try:
             print("before calling object")
             print(oldgroupname)
             groupHandler=Titles.objects.filter(groupname=oldgroupname)
             print(len(groupHandler))


             print("after calling object")

             #now we can change the groups to the new title
             for group in groupHandler:
                 print("inside for loop")
                 newgroupname=newgroupname.strip()
                 group.groupname= newgroupname

                 if newgroupname.find(" "):
                     print("found space")

                     x=newgroupname.replace(" ","-")
                     y=x.lower()
                     group.slugGroups=y
                 else:
                     group.slugGroups=group
                 group.save()
               # change field
             # this will update only



            except Titles.DoesNotExist:
                print("there was an exception")
                pass
        else:
            pass

    return render(request,"studyhelper/start.html",{"titles":titles})





def addgroup(request):
    newgroupname=request.GET.get("newgroupname",False)
    if newgroupname:
        add_group=Groups()
        #add_group=Titles()

        newgroupname=newgroupname.strip()
        add_group.groupName=newgroupname
        add_group.userName=request.user
        #add_group.title=" testing for 10:48 "


        add_group.slugGroups=creategroup_link(newgroupname)
        add_group.save()

    return render(request,"studyhelper/start.html")





def addContent(request):
    newtitlename=request.GET.get("newtitlename",False)
    groupname=request.GET.get("groupname",False)
    if newtitlename:
        add_group=Titles()

        newtitlename=newtitlename.strip()
        add_group.title=newtitlename
        add_group.username=request.user
        groupname=groupname.strip()


       #add_group.title=" title for testing unique in ivonjoe"

        add_group.groupname=groupname
        if groupname.find(" "):
            print("found space")

            x=groupname.replace(" ","-")
            add_group.slugGroups=x
        else:
            add_group.slugGroups=groupname

        add_group.save()

    return render(request,"studyhelper/start.html")