from basic.models import MyDevices


def getDevise(user,devicename):
        addDeviceInFile(user,devicename)#tries to add the devise to devise list before obtaining device list
        deviseList=MyDevices.objects.filter(username=user).exclude(device_name=devicename)
        print(deviseList)
        return deviseList



#adddevice would be called from inside the file,Its purpose is to check if the devise already exist////////////
def addDeviceInFile(user,devise):
    added_or_not=False
    print("+++++++++++++++++++++++++++++++++++addDeviceInFile+++++++++++++++++++++++++++++++++++"
          "" + user + devise )


    if len(MyDevices.objects.filter(username=user,device_name=devise)) == 0:

            devises=MyDevices()
            devises.username=user
            devises.device_name=devise
            devises.save()
            added_or_not=True
            print("DOES NOT EXIST")






    return added_or_not