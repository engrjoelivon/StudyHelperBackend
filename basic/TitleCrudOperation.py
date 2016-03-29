
from basic.crud_operations import CrudOperations
from basic.models import Titles,Actions,Base
from basic.ActionCrudOperations import ActionsOperation
from basic.VariesCrudOperation import generate_record,get_attributes_from_row_as_list

class TitlecrudOperation(CrudOperations,object):



      def get_whole_record(self):
        print("get whole record")
        self.set_row_as_list(Titles.objects.filter(username=self.username))


      #will accept a queryset iterate through the queryset,pass each each iteration to
      def set_row_as_list(self,query_set):
          for row in query_set:
            self.set_list_from_query_set(self.get_attributes_from_row_as_list(row))



      def get_attributes_from_row_as_list(self,this_row):
            """
           Row will always be different based on the table attribute for that reason the get_attributes_from_row_as_list has been seperated
           into the Varied crud operation module.get_attributes_from_row_as_list here will always call the Variaes crud operation
           get_attributes_from_row_as_list.
          """
            return get_attributes_from_row_as_list(this_row)



      def generate_record(self, list_holding_record):
          """
          Records attributes will always be different for that reason the generate_record has been seperated
          into the Varied crud operation module.Generate record here will always call the Variaes crud operation
          generate record.
          """
          return generate_record(list_holding_record,self.table_object)


      def insert_record(self, list_holding_record):

            key=list_holding_record[1]
            self.generate_record(list_holding_record)
            a_c_o=ActionsOperation(list_holding_record[0])
            a_c_o.set_inserted_actions(key,list_holding_record[2])
            return key

      def update_record(self,list_holding_record):
         key=list_holding_record[1]
         device_name=list_holding_record[2]
         try:

           if self.check_which_to_update(key,device_name):
            realkey=self.get_Real_key(key)
            record=Titles.objects.get(unique_key__icontains=realkey,username=self.username)
            self.generate_record(list_holding_record)
            self.notify_other_device_of_update(key,device_name)


         except:

             self.generate_record(list_holding_record)
         return list_holding_record[1]







      def check_which_to_update(self,key,device):
         print("check_which_to_update")
         update_or_dont_update=False
         try:
           realkey=key[key.find(" "):len(key)].strip()
           record=Actions.objects.get(username=self.username,deviceName=device,updated__icontains=realkey)
           key_from_device=record.updated
           timestamp_from_device=key[0:key.find(" ")].strip()
           timestamp_from_actions_table=key_from_device[0:key.find(" ")].strip()
           print("timestamp_from_device "+timestamp_from_device)
           print("timestamp_from_actions_table "+timestamp_from_actions_table)
           #if timestamp on device is greater then update was last made on the calling device so go ahead and update by setting update_or_dont_update as true
           if timestamp_from_device > timestamp_from_actions_table:
              record.delete()
              update_or_dont_update=True

         #if timestamp is lesser update_or_dont_update remains as false
         except:
           #key not found inside Actions table,so go ahead and update
           update_or_dont_update=True


         return update_or_dont_update



      def update_when_given(self,updated_record_list):

           """
           update the table when a record is given,accepts a list,this
           list holds the record the key and the device for the record.
           the order of insertion must be maintained from the client that initiated request
           returns the key or None if record does not exist

           :param updated_record_list: Accepts a list holding the attributes that have been updated
           :return: returns the key,if the record is succesfully updated,otherwise returns null
           """

           returnedvalue=None
           try:
               key=self.get_Real_key(updated_record_list[1])
               print(key," for update")

               title=self.table_name.objects.get(username=self.username,unique_key__icontains=key)
               title.no_of_time_accessed += 1
               title.given=1
               title.expiry=updated_record_list[3]
               title.save()
               #since the row was successfully updated notifyother device owned by this user.
               notifyothers=ActionsOperation(self.username)
               notifyothers.set_update_actions(updated_record_list[1],updated_record_list[4])
               returnedvalue=updated_record_list[1]


           except:
               """
               except would be called if there was an error because the key does not exist in the titletable
               this will mean the record has not been previously added
               """
               print("there is error")

           return returnedvalue










      #called when a record time has expired.returns the given column and expiry time to 0
      def update_single_record(self,record_to_update,key_for_record):
          title= Titles.objects.get(username=self.username,unique_key__icontains=self.get_Real_key(key_for_record[1]))
          title.given=0
          title.expiry=0
          return key_for_record




      def remove_single_record(self,key_for_record,devicename,type):
         realkey=self.get_Real_key(key_for_record)

         print(realkey)
         try:
             Titles.objects.get(unique_key__icontains=realkey,username=self.username).delete()#remove record from Titles table
             a_o=ActionsOperation(self.username)
             a_o.clear_table(realkey)#clear key from actions table
             a_o.add_actions(a_o.delete_attr,key_for_record,devicename)#add key to relevant row
         except:
             print("there is error")
             pass



      #If a row is successfully updated notifyother device owned by this user.
      def notify_other_device_of_update(self,key,devicename):

               notifyothers=ActionsOperation(self.username)
               notifyothers.set_update_actions(key,devicename)

      def get_updated_record(self,calling_devise):
          a_o=ActionsOperation(self.username)
          this_query=a_o.get_attribute(calling_devise,a_o.update_attr)
          for row in this_query:

              updated_key=row[0]
              print("there are columns in updated****************************",updated_key)
              if updated_key is not "":
                 try:
                     self.get_Real_key(updated_key)
                     this_row=Titles.objects.get(unique_key__icontains=self.get_Real_key(updated_key),username=self.username)
                     self.set_list_from_query_set(self.get_attributes_from_row_as_list(this_row))

                 except:
                     pass

          return self.get_list_from_query_set()



      def get_deleted_keys(self, calling_devise):
          a_o=ActionsOperation(self.username)
          this_query=a_o.get_attribute(calling_devise,a_o.delete_attr)
          for row in this_query:
              deleted_key=row[0]
              print("there are columns in deleted****************************",deleted_key)
              if deleted_key is not "":
                 try:
                    self.set_list_from_query_set(deleted_key)
                 except:
                     pass
          return self.get_list_from_query_set()




      def get_inserted_keys(self, calling_devise):
          a_o=ActionsOperation(self.username)
          this_query=a_o.get_attribute(calling_devise,a_o.insert_attr)
          for row in this_query:
              inserted_key=row[0]
              print("there are columns in inserted****************************",inserted_key)
              if inserted_key is not "":
                 try:
                     realkey=self.get_Real_key(inserted_key)
                     this_row=Titles.objects.get(unique_key__icontains=realkey,username=self.username)
                     self.set_list_from_query_set(self.get_attributes_from_row_as_list(this_row))
                 except:
                     pass
          return self.get_list_from_query_set()
