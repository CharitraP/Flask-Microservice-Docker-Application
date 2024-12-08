from .models import Retailer,Items
import math
from datetime import datetime

def generate_id(retailer):
    items=retailer.get_items()
    retailer_id=f"{retailer.get_retailer_name()+retailer.get_purchaseDate()+retailer.get_purchaseTime()+retailer.get_total()}"
    for item in items:
      retailer_id+=item.getShortDescription()+item.getPrice()
    retailer_id=hash(retailer_id)%100000007
    return retailer_id

def addRetailers(retailer):
    retailer_id=str(generate_id(retailer))
    if retailer_id not in Retailer.allRetailers:
      Retailer.allRetailers[retailer_id]=retailer
    for id,retail in Retailer.allRetailers.items():
      print(id," ",retail)
    return retailer_id

def calculatePoints(retail_id):
  points=0
  retailer=Retailer.allRetailers[retail_id]
  retailer_name=retailer.get_retailer_name()
  for char in retailer_name:
    if char.isalnum():
      points+=1
  if math.ceil(float(retailer.get_total()))==float(retailer.get_total()):
    points+=50
  if float(retailer.get_total())%0.25==0:
    points+=25
  items=retailer.get_items()
  count_of_items=0
  for item in items:
      count_of_items+=1
      if len(item.getShortDescription())%3==0:
        points+=math.ceil(float(item.getPrice())*0.2)
  points+=((count_of_items//2)*5)
  purchasedDate=retailer.get_purchaseDate()
  purchaseTime=retailer.get_purchaseTime()
  date_obj=datetime.strptime(purchasedDate, "%Y-%m-%d")
  if date_obj.day%2==1:
    points+=6
  purchase_time = datetime.strptime(purchaseTime, "%H:%M").time()
  start_time = datetime.strptime("14:00", "%H:%M").time()
  end_time = datetime.strptime("16:00", "%H:%M").time()
  if start_time <= purchase_time <= end_time:
    points+=10
  print(points)
  return points

  
  

