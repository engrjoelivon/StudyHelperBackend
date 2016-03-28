__author__ = 'joel'
# one of the core important of this class is maintaining the same key with the client.
import json


class HandleJsonRequests:
    def __init__(self, request):
        self.new_device = "1"  # if a device is new,would make a request with value of 1
        self.this_request = request
        self.json_string = request.body.decode("utf-8")
        self.username = "username"
        self.devisename = "devicename"
        self.deleted_record_key="deleterecord"
        self.updated_record_key="updaterecord"
        self.serverrecord="serverrecord"#keys for records that are held by the server,that is supposedly no in the client table
        self.return_key_from_server="key" #keys for records that was sent by client.
        print(self.json_string)

    # called when the username is added to a request
    # returns the username,using username as its key.This key must be constant accross alll clients that calls this request
    def get_user_name(self):
        data = self.get_json_data()
        return data[self.username]


        # called when the devicename is added to a request

    # returns the device name,using devicename as its key.This key must be constant accross alll clients that calls this request
    def get_device_name(self):
        data = self.get_json_data()
        return data[self.devisename]

    # return a list holding the record as sent by the client,the key would be constant accross all clients that makes the request.The key should be newrecord
    def get_insert_data(self):
        print("getinsert")
        data = self.get_json_data()
        return json.loads(data["newrecord"])

    # return a list holding datas that have been updated by client,the key would be constant accross all clients that initiates the request.The key should be updaterecord
    def get_update_data(self):
        print("getupdate")
        data = json.loads(self.json_string)
        return json.loads(data["updaterecord"])

    # return a list holding datas that have been updated by client,the key would be constant accross all clients that initiates the request.The key should be updaterecord
    def get_delete_data(self):
        print("getupdate")
        data = json.loads(self.json_string)
        return json.loads(data[self.deleted_record_key])

    # will return the json data as a string
    def get_json_data(self):
        data = json.loads(self.json_string)
        return data

        # called first time a device runs an application to see if the client is up to date with server

    def at_first_starting(self):
        data = self.get_json_data()
        print("at_first_starting", data[self.username])
        return (data[self.username])







class HandlePostRequests:
    def __init__(self, request):
        self.username = "username"
        self.devisename = "devicename"
        self.request = request
        print("handle post request")

    # the keys used should be the same as the key that would be used from the device making the request for deletion
    def get_delete_data(self):
        print("get_delete_data")
        return (
        self.request.POST.get("deleterecord"), self.request.POST.get("username"), self.request.POST.get("devicename"))



    # called when the username is added to a request
    # returns the username,using username as its key.This key must be constant accross alll clients that calls this request
    def get_username(self):
        return self.request.POST.get("username")



    # called when the devicename is added to a request
    # returns the device name,using devicename as its key.This key must be constant accross alll clients that calls this request
    def get_device_name(self):
        return self.request.POST.get("devicename")






class HandleResponses:
    def __init__(self):
        self.list_value = list()

    def set_list(self, value):
        self.list_value.append(value)

    def get_json_as_map_of_list(self):
        return json.dumps({"keys": self.list_value})

    def get_json_as_map(self, value):
        return json.dumps({"key": value})
