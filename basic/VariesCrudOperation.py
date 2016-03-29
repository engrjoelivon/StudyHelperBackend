"""
Class to handle operations that vary  for different tables
"""
from basic.models import Titles
def generate_record(list_holding_record,record):

         try:

            key=list_holding_record[1]
            record.username=list_holding_record[0]
            record.unique_key=key
            record.groupname=list_holding_record[3]
            record.title=list_holding_record[4]
            record.questions=list_holding_record[5]
            record.answer_text=list_holding_record[6]
            record.difficulty=(list_holding_record[7])
            record.priority=(list_holding_record[8])
            record.date_created=(list_holding_record[9])
            record.expiry=(list_holding_record[10])
            record.no_of_time_accessed=(list_holding_record[11])
            record.given=(list_holding_record[12])
            record.time_last_given=(list_holding_record[13])
            record.save()
         except:
            print("already exist")
         return key


def get_attributes_from_row_as_list(this_row):
            this_list=list()
            this_list.append(this_row.answer_text)
            this_list.append(this_row.date_created)
            this_list.append(this_row.difficulty)
            this_list.append(this_row.expiry)
            this_list.append(this_row.given)
            this_list.append(this_row.groupname)
            this_list.append(this_row.no_of_time_accessed)
            this_list.append(this_row.priority)
            this_list.append(this_row.time_last_given)
            this_list.append(this_row.questions)
            this_list.append(this_row.title)
            this_list.append(this_row.unique_key)
            return   this_list



def get_table_name():
    return Titles


def get_table_object():

    return Titles()