from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from basic.ActionCrudOperations import ActionsOperation
from basic.forms import Userinfo,Titlesform
from basic.crud_operations import CrudOperations
from basic.handle_requests import HandleJsonRequests,HandlePostRequests,HandleResponses
from basic.TitleCrudOperation import TitlecrudOperation
from django.views.decorators.csrf import csrf_exempt
import json
from basic.models import Titles,Groups,MyDevices,Actions
from basic.device import addDeviceInFile

def documentation(request):
    return render(request,"documentation/format.html")
# Create your views here.
value=False
titles=""
def home(request):


    return render(request,"studyhelper/base.html")




def signup(request):

    if request.method=="POST":
        userinfo=Userinfo(data=request.POST)
        if userinfo.is_valid():
            hashpass= userinfo.save(commit=False)
            hashpass.email=request.POST.get("username")
            hashpass.save()
            hashpass.set_password(hashpass.password)
            hashpass.save()

            return home(request)
        else:
            userinfo.errors
    else:
        userinfo=Userinfo()

    return render(request,"studyhelper/signup.html",{"userinfo":userinfo})


def log_in(request):
    x=False
    if request.method=="POST":
        print("request is post")
        username=request.POST.get("username")
        password=request.POST.get("password")
        userinfo=authenticate(username=username, password=password)
        if userinfo:
            print("username and password is correct")
            if userinfo.is_active:

                login(request,userinfo)

                #return HttpResponseRedirect("/")
                return HttpResponse("DONE")
            else:
                return HttpResponse("Your account has been deactivated")
        else:
            x=True



    return render(request,"studyhelper/login.html",{"x":x})


def logout(request):
    x=False
    if request.method=="POST":
        username=request.POST.get("username")
        password=request.POST.get("password")
        user=authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect("/")
            else:
                return HttpResponse("Your account has been deactivated")
        else:
            x=True



    return render(request,"studyhelper/login.html",{"x":x})


@login_required
def user_logout(request):
    a=request.user


    logout(request)
    #return HttpResponseRedirect("/")
    return HttpResponse(a)




def content_page(request):



    groupNames=Groups.objects.filter(userName=request.user)
    return render(request,"studyhelper/content.html",{"groupdatas":groupNames})


#renders titles name    responds to a matched request from titlelist
def grouplink(request,group_name_url):



    print(group_name_url)
    titlesList=Titles.objects.filter(slugGroups=group_name_url,username=request.user)#returns all the rows as list where each item on the list is
    #a python object.

    groupNames=Groups.objects.filter(userName=request.user) #returns  all the rows as List where username is of the logged in user

    return render(request,"studyhelper/titles.html",{"titlesList":titlesList,
                                                            "groupNames":groupNames})








def titlecontent(request,title_name_url):


    try:
        groupNames=Groups.objects.filter(userName=request.user)


        titles=Titles.objects.get(slug=title_name_url,username=request.user) #returns titles object inside of the modal with the
        titlesList=Titles.objects.filter(groupname=titles.groupname,username=request.user)
        #the slug name or title name clicked
        #titlecontent=Titles.objects.all()




        titlename=titles.questions
        print("there was no exception")
    except Titles.DoesNotExist:
        print("there was an exception")
        pass
    value=True
    #return HttpResponseRedirect("/addcontent/")
    #HttpResponseRedirect("/addcontent/")
    return render(request,"studyhelper/titlescontent.html",{"titlename":titles,
                                                            "groupNames":groupNames,
                                                             "titlesList":titlesList

                                                            })

#this view is called for start after the user performs an operation it will update the number of times
def start(request):
    # titledatas=Titlesform()
    titles=Titles.objects.get(slug="slugify")
    if request.method == 'GET':
        abc= request.GET.get("title",False)
        idnumber=request.GET.get("id",False)


        if abc:
            try:
             print("before calling object")
             titleHandler=Titles.objects.get(id=idnumber)

             print("after calling object")


             titleHandler.no_of_time_accessed = titleHandler.no_of_time_accessed+1  # change field
             # this will update only
             titleHandler.save()


            except Titles.DoesNotExist:
                print("there was an exception")

        #called when the page loads the first time
        else:

            print(titles.id)


    return render(request,"studyhelper/start.html",{"titles":titles})



#this will be called when changes are made to an existing table,it will be a get request

def number_of_time_acc_cal(x):
    return x+1
#*****************************called by a new device and new user,checks if database already holds record if yes returns the record****************************
@csrf_exempt
def new_device(request):
    print("##########################new_device###########################")
    h_j_r=HandleJsonRequests(request)
    h_j_r=h_j_r.at_first_starting()
    t_crud_operation=TitlecrudOperation(h_j_r)
    t_crud_operation.get_whole_record()
    value=t_crud_operation.get_list_from_query_set()
    print("value is ",value)

    return HttpResponse(HandleResponses().get_json_as_map(value),content_type='application/json')

#**************the first time a new app runs it will call this function add devise with its name and username****************#
@csrf_exempt
def add_device(request):
    devicename=request.POST.get("devicename")
    user=request.POST.get("username")
    addDeviceInFile(user,devicename)
    return HttpResponse(devicename)

#*******************************************handle record insertions*******************************************************************************#

#accepts an array of data and generates a record based on the array,the order of insertion of the data must be known


#**********check if new records have been inserted at startup****
#request must be of type json containing the inserted records,username and devicename of the client.key for inserted record must be insertnew and value must be of type jsonArray,
#username and devicename key must be username and devicename respectively and they must be of value type string.
@csrf_exempt
def check_inserts(request):
    this_request=HandleJsonRequests(request)
    data=this_request.get_insert_data()
    user_name=this_request.get_user_name()
    device_name=this_request.get_device_name()
    t_c_o=TitlecrudOperation(user_name)
    keyList=[]
    myMaps=dict()
    for singledata in data:
                title_record=json.loads(singledata)
                res=t_c_o.insert_record(title_record)
                if res is not None:
                 keyList.append(res)
                 print(type(keyList))
    myMaps[this_request.return_key_from_server]=keyList
    myMaps[this_request.serverrecord]=t_c_o.get_inserted_keys(device_name)
    return HttpResponse(json.dumps(myMaps),content_type='application/json')





#function is called to insert a new record into db
#request must come as json string,containing a jsonArray with key newrecord
@csrf_exempt
def insert_records(request):
    this_request=HandleJsonRequests(request)
    data=this_request.get_insert_data()
    username=data[0]
    key=data[1]
    t_c_o=TitlecrudOperation(username)
    #res=call_generate_record(data)
    t_c_o.insert_record(data)
    handleresponse=HandleResponses()
    print(handleresponse.get_json_as_map(key))
    return HttpResponse(handleresponse.get_json_as_map(key),content_type='application/json')



#Query accepts json string,json string will hold username with key username,device name with key device name and the inserted record key with newrecord
#When django recieves a query for checkinsert it will return all the new inserted record for the calling devise,after the calling devise adds this record to its db
# it will call this function to let django know the function has been added
#then django removes this record from Actions Table
@csrf_exempt
def remove_inserted_key(request):
    print("remove inserted key")
    this_request=HandleJsonRequests(request)
    inserted_record_list=this_request.get_insert_data()
    username=this_request.get_user_name()
    device_name=this_request.get_device_name()
    for my_key in inserted_record_list:
        a_c_p=ActionsOperation(username)
        a_c_p.remove_row(a_c_p.insert_attr,my_key,device_name)
    return HttpResponse("done")








#***********************************************************delete records*****************************************************************#
@csrf_exempt
def deleteRecord(request):
    thisrecord=HandlePostRequests(request)
    res=thisrecord.get_delete_data()
    key=res[0]
    print("this is key"+key)
    t_c_o=TitlecrudOperation(thisrecord.get_username())
    t_c_o.remove_single_record(key,thisrecord.get_device_name(),t_c_o.delete_attr)
    return HttpResponse(key)




#function expects a json request,this request should hold a list of all the deleted keys,the first and second item should be the username and the device name respectively
@csrf_exempt
def deleteRecord_atstartup(request):
    this_request=HandleJsonRequests(request)
    datalist=this_request.get_delete_data()
    key_list=[]
    myMaps=dict()
    user=datalist[0]
    t_c_o=TitlecrudOperation(user)
    device_name=datalist[1]
    new_data_list=datalist[2:len(datalist)]
    for deletedkey in new_data_list:
        key_list.append(deletedkey)
        t_c_o.remove_single_record(deletedkey,device_name,t_c_o.delete_attr)
    myMaps[this_request.return_key_from_server]=key_list
    myMaps[this_request.serverrecord]=t_c_o.get_deleted_keys(device_name)
    return HttpResponse(json.dumps(myMaps),content_type='application/json')



#view should be called to remove deleted keys from actions table,request should be initiated after the client delete the records from its db
#request should be of datatype json,json must contain KEY named deletedrecords and VALUE should be of type JSONARRAY,KEY names username value string and key named devicename value string
@csrf_exempt
def remove_deleted_keys(request):
    this_request=HandleJsonRequests(request)
    deleted_record_list=this_request.get_delete_data()
    print("updated key to remove",deleted_record_list)
    username=this_request.get_user_name()
    device_name=this_request.get_device_name()
    for my_key in deleted_record_list:
        a_c_p=ActionsOperation(username)
        a_c_p.remove_row(a_c_p.delete_attr,my_key,device_name)
    return HttpResponse("done")





#***************************************************update records*********************************************************************#
@csrf_exempt
def update_records_at_startup(request):
    this_request=HandleJsonRequests(request)
    array_data=this_request.get_update_data()
    username=this_request.get_user_name()
    devicename=this_request.get_device_name()
    print("***************************update_records_at_startup***********************"+ username + devicename )
    update_map=dict()
    key_list=[]
    t_c_o=TitlecrudOperation(username)#
    for key in array_data:
        title_list=json.loads(key)
        record_key=t_c_o.update_record(title_list)#
        key_list.append(record_key)#
    update_map["key"]=key_list
    update_map["serverrecord"]=t_c_o.get_updated_record(devicename)
    return HttpResponse(json.dumps(update_map) ,content_type="application/json")


@csrf_exempt
def update_records(request):
    this_request=HandleJsonRequests(request)
    updated_record_list=this_request.get_update_data()
    t_c_o=TitlecrudOperation(updated_record_list[0])
    key=t_c_o.update_record(updated_record_list)
    handleresponse=HandleResponses()
    return HttpResponse(handleresponse.get_json_as_map(key),content_type="application/json")




@csrf_exempt
def update_record_when_given(request):
    this_request=HandleJsonRequests(request)
    updated_record_list=this_request.get_update_data()
    t_c_o=TitlecrudOperation(updated_record_list[0]) #the first index of the list holds the username
    key=t_c_o.update_when_given(updated_record_list)#returns the key to be returned to the client
    print("update_record key is",key)
    handleresponse=HandleResponses()
    return HttpResponse(handleresponse.get_json_as_map(key),content_type="application/json")


#called after records have been updated on local device.it will remove the key from the actions table
@csrf_exempt
def remove_updated_keys(request):
    this_request=HandleJsonRequests(request)
    updated_record_list=this_request.get_update_data()
    print("updated key to remove",updated_record_list)
    username=this_request.get_user_name()
    device_name=this_request.get_device_name()
    for my_key in updated_record_list:
        a_c_p=ActionsOperation(username)
        a_c_p.remove_row(a_c_p.update_attr,my_key,device_name)
    return HttpResponse("done")





#function to return the real key
def get_real_key(key):
    return key[key.find(" "):len(key)].strip