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



def read_one():
    pass


def update():
    pass

def delete():
    pass
