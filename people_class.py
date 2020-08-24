# -*- coding: utf-8 -*-
"""
Created on Sat Aug  1 20:40:16 2020

@author: Christo Lagali
"""

# Class 

from datetime import datetime
from utils.db import Connect

class people:
    
    def __init__(self):
        self.lname = ''
        self.fname = ''
        self.timestamp =''
    

    def setValues(self, lname,fname,timestamp):
        self.lname = lname
        self.fname = fname
        self.timestamp = timestamp
        


class people_list:

    def __init__(self):
        self.lst = []
        self.p = people()
        self.connClass = Connect()
        self.conn = None

    # create a new person
    def createPerson(self, lname,fname):


        if self.conn ==None:
            ### establish connection
            self.conn = self.connClass.getSnowflakeConnection('christo77lagali','Snowflake@1234','xj19570.us-east-2.aws','ChOMPUTE_WH','DEMO_DB')
            query = "INSERT INTO RAW_PEOPLE_INFO(LNAME,FNAME,TIMESTAMP) VALUES({lname},{fname},{timestamp})".format(
                lname = lname,
                fname = fname
            )
            self.connClass.execute_Query(query,self.conn)
        
        else:
            self.p = people()
            self.p.setValues(lname,fname,datetime.now().strftime(("%Y-%m-%d %H:%M:%S")))

            self.lst.append(self.p)

        return self.lst
    
    # Search handler
    def searchPerson(self,lname):

        foundPerson = None
        foundIndex = None
        for ind,obj in enumerate(self.lst):
            
            if obj.lname == lname:
                foundPerson = obj
                foundIndex = ind
            
        return foundPerson,foundIndex
    
    # Delete a person
    def delPerson(self,lname):

        (deletePerson,atIndex) = self.searchPerson(lname)

        if deletePerson!= None:

            del self.lst[atIndex]
            return deletePerson
        
        else:
            return None
    
    def updatePersonData(self,lname,personObj):
        
        (foundPerson,atIndex) = self.searchPerson(lname)
        
        if foundPerson != None:
            self.lst[atIndex].setValues(personObj.get("lname"),personObj.get("fname"),datetime.now().strftime(("%Y-%m-%d %H:%M:%S")) )
            return lname
        
        else:
            return None


    def getAllPeople(self):
        
        if len(self.lst)>0:
            return self.lst
        
        else:
            return None
        
    


if __name__ == '__main__':
    ppl = people_list()
    ppl.createPerson('lagali','chris' )
    
    ppl.createPerson('lagali','christo')
    
    print(ppl.searchPerson('lagali'))
    