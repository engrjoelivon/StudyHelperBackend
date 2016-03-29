
from abc import ABCMeta, abstractmethod
from basic.VariesCrudOperation import get_table_name,get_table_object


class CrudOperations(metaclass=ABCMeta):
    def __init__(self, user):
        self.table_name=get_table_name()
        self.table_object=get_table_object()
        self.username = user
        self.query_list = list()  # list that holds list of rows.Every row will be converted to a list,and the list added to this variable
        #********************attribute types*************************************#

        self.insert_attr=0 # this variables is defined as constants,they should not be changed
        self.update_attr=1 # this variables is defined as constants,they should not be changed
        self.delete_attr=2 # this variables is defined as constants,they should not be changed
    @abstractmethod
    def get_whole_record(self):
        raise NotImplementedError("Please Implement this method")

    # concrete method,that can be called from subclass,if a query is done on A TABLE to return more than one row,call this method to insert each row into a list
    # accepts a row as list
    def set_list_from_query_set(self, list_object):
        self.query_list.append(list_object)



        # will be defined by class that implements this class,
        # called to get all the rows present in the table,each row is represented in the list as a list.
        # return a list of rowlist.

    def get_list_from_query_set(self):
        return self.query_list

    # method should be overriden to generate records that will be passed over to client,attributes in the row will be appended to an array,the ordering should be in ascending order for attributes names in the table
    # row obtained by performing a get request on the table
    # should return a list holding the attributes in a row.
    @abstractmethod
    def get_attributes_from_row_as_list(self, row):
        raise NotImplementedError("Please Implement this method")


    @abstractmethod
    def generate_record(self, list_holding_record):
        """
     :param list_holding_record: A list will be sent from client,this list will hold all the record,the order should be maintained so that the right values can be extracted,or betterstill insert values into list in ascending order from a to z,         method should be overriden to generate record that will be inserted into A TABLE,     After generating a record call save to save row in table
     :param record: will accept a table name
        :return:
    """






    # Method should be overriden to update already existing record.
    # A list will be sent from client,this list will hold all the record,the order should be maintained so that the right values can be extracted,or betterstill insert values into list in ascending order from a to z
    # After generating a record call save to save row in table
    @abstractmethod
    def update_record(self, list_holding_record):
        raise NotImplementedError("Please Implement this method")



    @abstractmethod
    def insert_record(self,list_holding_record):
        """
        Method should be overriden to insert new record into the Table.
        A list will be sent from client,this list will hold all the record,the order should be maintained so that the right values can be extracted,or betterstill insert values into list in ascending order from a to z
        After generating a record call save to save row in table
        """




    @abstractmethod
    def update_single_record(self, record_to_update, key_for_record):
        """
        must be overriden,to update single records
        represent the record to update,the attribute name for the record will be defined in the class thats implements the record
        the unique key to search through the table for the record or row.
        class that overrides method can include a return value when necessary
        """
        raise NotImplementedError("Please Implement this method")






    # override method to delete a row from a table
    # uniquekey for record,will be used to query the table,if key exist delete the row.
    # method is defined as abstract,because model name must be explicitely defined
    @abstractmethod
    def remove_single_record(self, key_for_record,devicename,type):
        raise NotImplementedError("Please Implement this method")

    # concrete method to return a real key in the case where time stamp is added to the uniquekey
    def get_Real_key(self, key):
        return key[key.find(" "):len(key)].strip()

    # The function below will compare the timestamp appended to every key using the result from the comparism,it will decide if the server should be updated or the client should be updated
    # though the function is called by the client,if the timestamp on the server is higher than that on the client,it will not update the server,rather it will return send the record on the
    # server to the client so the client can be updated
    ##accepts a user,a key and a devicename
    ###returns a boolean.true will mean update server while false will mean update client

    @abstractmethod
    def check_which_to_update(self, key, device):
        """
        function to compare the timestamp appended to every key using the result from the comparism,it will decide if the server should be updated or the client
        though the function is called by the client,if the timestamp on the server is higher than that on the client,it will not update the server,rather it will return send the record on the
        #server to the client so the client can be updated
        :param key: accepts the key for the record
        :param device: calling device
        :return:boolean true means server should be updated otherwise update client
        """


    # function would be called to return all updated record present in the server,it will obtain the keys from a TABLE that holds such keys,using the key it extract the record and convert it into a list
    ##return a list of list holding all the records
    @abstractmethod
    def get_updated_record(self, calling_devise):
        pass

    # function would be called to return all deleted keys present in the server,it will obtain the keys from the Actions TABLE and enter the key into a  list.As it obtains this key it adds it to the querylist
    ##returns a list holding all the keys by calling getquerylist
    @abstractmethod
    def get_deleted_keys(self, calling_devise):
        pass



    # function would be called to return all inserted record present in the server,
    # it will obtain the keys from a TABLE that holds such keys,
    # using the key,it will extract the record from the table that holds the Records and convert it into a list
    ##return a list of list holding all the records
    @abstractmethod
    def get_inserted_keys(self, calling_devise):
        pass
