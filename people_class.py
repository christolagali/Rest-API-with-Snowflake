# -*- coding: utf-8 -*-
"""
Created on Sat Aug  1 20:40:16 2020

@author: Christo Lagali
"""

# Class 

from datetime import datetime
from utils.db import Connect
import json

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
        self.getAllPeople()

    # create a new person
    def createPerson(self, lname,fname):


        if self.conn ==None:
            ### establish connection
            self.conn = self.connClass.getSnowflakeConnection(configData['user'], configData['password'], configData['snow_account'], configData['warehouse'], configData['db'])

            #ts = '2020-08-24 22:13:07.902 -0700'

        # Insert person to Database
        lname = "'" + lname + "'"
        fname = "'" + fname + "'"
        query = "INSERT INTO RAW_PEOPLE_INFO(LNAME,FNAME,TIMESTAMP) VALUES({lname},{fname},current_timestamp())".format(
            lname = lname,
            fname = fname
        )
        self.connClass.execute_Query(query,self.conn)

        # Add person to the local people list
        self.p = people()
        self.p.setValues(lname, fname, datetime.now().strftime(("%Y-%m-%d %H:%M:%S")))

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

            # delete from the database
            lname = "'" + lname + "'"
            query = "DELETE FROM RAW_PEOPLE_INFO WHERE LNAME={lname}".format(
                lname = lname
            )
            self.connClass.execute_Query(query, self.conn)
            return deletePerson
        
        else:
            return None
    
    def updatePersonData(self,lname,personObj):
        
        (foundPerson,atIndex) = self.searchPerson(lname)

        # Person to be updated already exists
        if foundPerson != None:
            # Update the local list
            self.lst[atIndex].setValues(personObj.get("lname"),personObj.get("fname"),datetime.now().strftime(("%Y-%m-%d %H:%M:%S")) )

            # update the database
            lname = "'" + personObj.get("lname") + "'"
            fname = "'" + personObj.get("fname") + "'"
            query = "UPDATE RAW_PEOPLE_INFO SET FNAME ={fname} ,TIMESTAMP = CURRENT_TIMESTAMP() WHERE LNAME = {lname}".format(
                fname=fname,
                lname=lname
            )
            self.connClass.execute_Query(query, self.conn)

            return lname
        
        else:
            return None

    # Method gets invoked on startup to establish connection with snowflake and populate the People List
    def getAllPeople(self):
        
        if len(self.lst)>0:
            return self.lst
        
        else:

            # read config from file
            configData= None
            with open('config/config.json') as f:
                configData = json.load(f)

            print(configData)

            # Establish a connection
            query = "SELECT LNAME,FNAME,TIMESTAMP FROM RAW_PEOPLE_INFO"
            self.conn = self.connClass.getSnowflakeConnection(configData['user'], configData['password'], configData['snow_account'], configData['warehouse'], configData['db'])
            curr = self.connClass.execute_Query(query, self.conn)

            for row in curr:
                self.p = people()
                self.p.setValues( row[1],row[0], row[2])

                self.lst.append(self.p)
        
    


if __name__ == '__main__':
    ppl = people_list()
    ppl.createPerson('lagali','chris' )
    
    ppl.createPerson('lagali','christo')
    
    print(ppl.searchPerson('lagali'))
    