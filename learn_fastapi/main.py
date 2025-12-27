from fastapi import FastAPI   #this imports FastAPI class from fastapi which you can use directly
#import fastapi  #this is the entire fastapi module where you have to always use the module name to access the classes like fastapi.FastAPI()

#1.this is the object of class FastAPI
app =  FastAPI()

"""
2. Endpoint creation(last part of the url)

different end point methods are:

I.GET -get an information
II.POST -  create something new like new user in a database
III.PUT- update the already existing data
IV.DELETE-remove information

USE OF DECORATORS:
---------------to add common behaviour to many functions wihtout rewriting them 
---------------in FastAPI-when someone visits a URL like:----/users the fastapi must detect the url,
---------------check http method(get,post),validate request,send response and doing this manually for every route would be tedious so using decorators becomes helpful

 """

@app.get("/")   #when someone sends a GET request to(homepage) /, run the funciton written just below this line
def home():
    return {"name":"First Data"}
