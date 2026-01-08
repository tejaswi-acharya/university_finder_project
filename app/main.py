"""
Frontend
  ↓
FastAPI (/universities?country=Nepal)
  ↓
Hipolabs API (/search?country=Nepal)
  ↓
FastAPI (optional filtering)
  ↓
Frontend


"""


from fastapi.middleware.cors import CORSMiddleware

import requests
from fastapi import FastAPI, HTTPException 
from typing import Optional

base_url = f"http://universities.hipolabs.com/search"

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # allow frontend (dev only)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def Home():
    return {"Hi":"This is the home page"}
#https://............/universities?country=Nepal
@app.get("/universities")
def get_universities(country: str, name: Optional[str]=None):
    params={"country":country}

    if name:
        params['name']=name
    
    response = requests.get(base_url,params=params)
    if response.status_code!=200:
        raise HTTPException(status_code=response.status_code, detail="Failed to display Universities")
    

    return response.json()



