from datetime import datetime


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
	
	"""
	"""
	
	return [PEOPLE[key] for key in sorted(PEOPLE.keys())]


def create(person):

    lname= person.get("lname", None)
    fname = person.get("fname", None)

    if lname not in PEOPLE and lname is not None:

        PEOPLE[lname] = {
            "lname" : lname,
            "fname" : fname,
            "timestamp" : get_timestamp()
        }

        return PEOPLE[lname],201
    
    else:
        abort(406, "Person with last name {lname} already exists".format(lname=lname))


def read_one(lname):
    
    if lname in PEOPLE:
        return PEOPLE.get(lname)
    else:
        abort(404, "Person you were looking for {lname} is not to be found! ".format(lname=lname))


def update(lname,person):
    
    if lname in PEOPLE:
        PEOPLE[lname]["fname"] = person.get("fname")
        PEOPLE[lname]["timestamp"] = get_timestamp()
        
        return PEOPLE[lname]
    else:
        abort(404,"Person with last name {lastname} not found".format(lastname=lname))


def delete(lname):
    
    
    if lname in PEOPLE:
        
        del PEOPLE[lname]
        return make_response("{lname} successfully deleted".format(lname=lname),200)
