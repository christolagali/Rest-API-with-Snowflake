from flask import(
	render_template,
    abort,
    make_response
)
from datetime import datetime
from people_class import people_list
import json

pclObj = people_list()
def get_timestamp():
	return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))


# data to serve

PEOPLE ={
    "Farrell": {
        "fname": "Doug",
        "lname": "Farrell",
        "timestamp": get_timestamp()
    },
    "Brockman": {
        "fname": "Kent",
        "lname": "Brockman",
        "timestamp": get_timestamp()
    },
    "Easter": {
        "fname": "Bunny",
        "lname": "Easter",
        "timestamp": get_timestamp()
    }
}
    
# creat the handler

def read_all():
    peopleList = pclObj.getAllPeople()
    
    if peopleList != None:
        json_string = json.dumps([ob.__dict__ for ob in peopleList])
        return json_string
    else:
        abort(406, "There seems to be no one registered!")
        
    


def create(person):

    lname= person.get("lname", None)
    fname = person.get("fname", None)
    
    (existingPerson,atIndex) = pclObj.searchPerson(lname)
    
    
    if existingPerson == None:
        pclObj.createPerson(lname,fname)
    
    else:
        abort(406, "Person with last name {lname} already exists".format(lname=lname))


def read_one(lname):
    
    (existingPerson,atIndex) = pclObj.searchPerson(lname)
    
    if existingPerson != None:
        
        #convert to JSON string
        jsonStr = json.dumps(existingPerson.__dict__)
        return jsonStr
    else:
        abort(404, "Person you were looking for {lname} is not to be found! ".format(lname=lname))


def update(lname,person):
    
    value = pclObj.updatePersonData(lname,person)
    if value != None:
        
        return make_response("{lname} successfully Updated".format(lname=value),200)
    
    else:
        abort(404, "Person you were looking for {lname} is not to be found! ".format(lname=value))
    
        
    
    
def delete(lname):
    
    deletedPerson = pclObj.delPerson(lname)
    
    if deletedPerson != None:
        return make_response("{lname} successfully deleted".format(lname=deletedPerson.lname),200)