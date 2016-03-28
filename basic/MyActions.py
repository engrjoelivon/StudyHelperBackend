from django.views.decorators.csrf import csrf_exempt

__author__ = 'johnanderson1'
from basic.models import Actions,MyDevices, Titles
import json
class MyActions:

    def __init__(self,request):
        received_json_data=request.body.decode('utf-8')
        data=json.loads(received_json_data)
        self.request_dic=data
    @csrf_exempt
    def insertRecords(self,request):
       print("in insert records")
       record=Titles()
       received_json_data=request.body.decode('utf-8')
       data=json.loads(received_json_data)
       print(type(data) )

       for key in data:


        if key == "username":

            record.username=data[key]
        elif key == "unique_key":
            record.unique_key=data[key]
        elif key == "title":
             record.title=data[key]
        elif key == "group":
             record.groupname=data[key]
        elif key == "question":
            record.questions=data[key]
        elif key == "answer":

            record.answer_text=data[key]
        elif key == "answer_image":
            pass
        elif key == "difficulty_level":

            record.difficulty=data[key]
        elif key == "priority_level":

            record.priority=data[key]
        elif key == "expiry":

            record.expiry=data[key]
        elif key == "number_time_given":
            record.no_of_time_accessed=data[key]
        elif key == "givenornot":

             record.given=data[key]
        elif key == "date_created":
            record.date_created=data[key]
        elif key == "time_last_given":
            record.time_last_given=data[key]
        elif key == "notifyinsert":
             self.insert(data[key])
               #the order must be maintained usernamefirst,keysecond,devicename last


        record.save()

    def insert(self,insert_values_list):

        print(type(insert_values_list))
        deviseList=json.loads(insert_values_list)
        print("username is ",deviseList[0])
        print("key is ",deviseList[1])
        print("devise name is ",deviseList[2])

        for device in self.getDevise(deviseList[0],deviseList[2]):
            print("there is device")

            action=Actions()
            action.deviceName=device
            action.inserted=deviseList[1]
            action.username=deviseList[0]
            action.save()


    def getDevise(self,user,devicename):
        deviseList=MyDevices.objects.filter(username=user).exclude(device_name=devicename)
        print(type(deviseList))
        return deviseList

#when ever a devise makes a query it checks if any record has been added,through its username and device name.If yes,django pulls the key and return the full record as json
    def getInserted(self,user,callingDevise):
        inserted_key=MyDevices.objects.filter(username=user,deviceName=callingDevise)
        return inserted_key

    def delete(self,key):
        pass
    def update(self,key):
        pass
    def deviseName(self,key):

        pass
    def enterKey(self):

        pass

