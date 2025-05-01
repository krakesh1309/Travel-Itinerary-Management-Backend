import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'travel_backend.settings')  # adjust if needed
django.setup()

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from itineraries.models import Itinerary


app = FastAPI()

itineraries_db = []

class IntinerarySchema(BaseModel):
    name:str
    nights:int
    region:str


@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI application! Use /docs for API documentation."}

@app.post("/itineraries")
def create_itinerary(itinerary:IntinerarySchema):
    if not(2<=itinerary.nights <= 8):
        raise HTTPException(status_code=400,detail= "Nights must be between 2 and 8.")
    itineraries_db.append(itinerary)
    return {"message":"Itinerary created successfully", "data":itinerary}



@app.get("/itineraries", response_model=List[IntinerarySchema])
def get_itineraries():
    itineraries = Itinerary.objects.all()
    return [
        {"name": itinerary.name, "nights": itinerary.nights, "region": itinerary.region}
        for itinerary in itineraries
    ]


@app.get("/recommendations")
def recommend_itineraries(nights: int):
    recommendations = [itinerary for itinerary in itineraries_db if itinerary.nights == nights]
    if not recommendations:
        raise HTTPException(status_code=404, detail="No itineraries found for the given number of nights.")
    return {"recommendations": recommendations}
