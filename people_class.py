# -*- coding: utf-8 -*-
"""
Created on Sat Aug  1 20:40:16 2020

@author: Christo Lagali
"""

# Class 

from datetime import datetime

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

    # create a new person
    def createPerson(self, lname,fname):
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
        
    


if __name__ == '__main__':
    ppl = people_list()
    ppl.createPerson('lagali','chris' )
    
    ppl.createPerson('lagali','christo')
    
    print(ppl.searchPerson('lagali'))
    