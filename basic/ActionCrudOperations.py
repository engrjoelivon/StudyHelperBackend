__author__ = 'joel'
from basic.models import Actions
from basic.device import getDevise

#class designed to perform crud actions on the actions table
class ActionsOperation():
    #constructor accepts the user making the request
     def __init__(self,user):
         self.user=user
        #********************attribute types*************************************#

         self.insert_attr=0 # this variables is defined as constants,they should not be changed
         self.update_attr=1 # this variables is defined as constants,they should not be changed
         self.delete_attr=2 # this variables is defined as constants,they should not be changed
         #the idea is,the get_attribute will is the constants to decide which of the 3 attribute to return


    #function should be called when notifying other device of a new update.
     def set_update_actions(self,key,devicename):
         list_of_devices=getDevise(self.user,devicename)
         for device in list_of_devices:
               realkey=self.get_Real_key(key)
              #check the actions table if the key exist in either the updated and inserted column
            #would have used get but could not use the OR for get request
               record=Actions.objects.filter(username=self.user,updated__icontains=realkey ,deviceName=device)\
                      | Actions.objects.filter(username=self.user,inserted__icontains=realkey ,deviceName=device)
           #actions should be added only if it does not exist inside the updated or inserted attribute
               if len(record) is  0:
                   print("record added to actions()")

                   action=Actions()
                   action.deviceName=device
                   action.updated=key
                   action.old_updated_key=key
                   action.username=self.user
                   action.save()


     #call functions when new records are added to the record Table,so as to notify other device with the same username of a new record
     def set_inserted_actions(self,key,devicename):
         print("++++++++++++++++set insert record++++++++++++++++++++++++++")
         list_of_devices=getDevise(self.user,devicename)
         for device in list_of_devices:
             action=Actions()
             #check if key already exist
             try:
                 Actions.objects.get(inserted=key,deviceName=device,username=self.user)
             except:
                 #keys does not exist
                 action.deviceName=device
                 action.inserted=key
                 action.username=self.user
                 action.save()

     #concrete method to return a real key in the case where time stamp is added to the uniquekey
     def get_Real_key(self,key):
        return key[key.find(" "):len(key)].strip()



     #function should be called to remove a row from the actions table,these row could be from any of the column.
     #Accepts a list holding all the keys to remove
     def remove_row(self,type,key,device_name):
          succes=False

          if type==self.update_attr:
             print("------------------about to remove updated-------------------------")
             Actions.objects.filter(username=self.user,updated__icontains=key,deviceName=device_name).delete()
             succes=True
          elif type==self.delete_attr:
             print("------------------about to remove deleted-------------------------")
             Actions.objects.filter(username=self.user,deleted__icontains=key,deviceName=device_name).delete()
             succes=True
          elif type == self.insert_attr:
             print("------------------about to remove inserted-------------------------")
             Actions.objects.filter(username=self.user,inserted__icontains=key,deviceName=device_name).delete()
             succes=True

          return succes

     # After an a row has been deleted,it will be approprite to check all the other other attributes of the table so as to remove the key from the actions table
     def clear_table(self,key):
         realkey=self.get_Real_key(key)
         for returned_key in Actions.objects.filter(username=self.user,inserted__icontains=realkey)|Actions.objects.filter(username=self.user,updated__icontains=realkey):
             print("clear table record exist")
             returned_key.delete()






     #function should get one of the columns using the value_list query.
     #will accept the calling_device ie the device name,and the attribute type,this will be one of the attribute types defined inside the constructor
     #will return the query set updatained from the query
     def get_attribute(self,calling_device,attribute_type):

        if attribute_type == self.update_attr:
            return Actions.objects.values_list("updated","username","deviceName").filter(username=self.user,deviceName=calling_device).exclude(updated=None)
        elif attribute_type == self.delete_attr:
             return Actions.objects.values_list("deleted","username","deviceName").filter(username=self.user,deviceName=calling_device).exclude(deleted=None)
        elif attribute_type == self.insert_attr:
             return Actions.objects.values_list("inserted","username","deviceName").filter(username=self.user,deviceName=calling_device).exclude(inserted=None)



     # AddActions function should be called if an action needs to be added to the Actions Table
     def add_actions(self,type,key,devicename):
         if type == self.delete_attr:
             list_of_devices=getDevise(self.user,devicename)
             for device in list_of_devices:
                 print("there is device")
                 action=Actions()
                 action.deviceName=device
                 action.deleted=key
                 action.username=self.user
                 action.save()
