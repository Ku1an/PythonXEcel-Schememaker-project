# What im gonna do. Scheme of people working at a school. 
# Monday - Friday. Each person has 40 hours each week. Same week for 16 weeks but different 
# done mal for how the scheme is made. 
# some people work early and some not. Spread it out.
# The data should report it into an excel


import json

def getDataFromJsonSchemeTimes():
    jsonFile = open("./json/schemetimes.json","r")
    staffdict = json.loads(jsonFile.read())
    return staffdict

def getDataFromJsonStaff():
    jsonFile = open("./json/staff.json","r")
    stafflist = json.loads(jsonFile.read())
    return stafflist

