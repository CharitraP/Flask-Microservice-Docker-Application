import hashlib
""" This is a Model Class which represent the Database struture"""

class Items:
    def __init__(self,shortDesription, price):
      self.__shortDescription = shortDesription
      self.__price = price

    def getShortDescription(self):
      return self.__shortDescription

    def getPrice(self):
      return self.__price

class Retailer:
  allRetailers={}
  def __init__(self, retailer_name, purchaseDate, purchaseTime, total,items: Items):
      self.__retailer_name=retailer_name
      self.__purchaseDate=purchaseDate
      self.__purchaseTime=purchaseTime
      self.__total=total
      self.__items=[]
      for item in items:
        self.__items.append(item) 
  
  def get_retailer_name(self):
    return self.__retailer_name
  
  def get_purchaseDate(self):
    return self.__purchaseDate
  
  def get_purchaseTime(self):
    return self.__purchaseTime
  
  def get_total(self):
    return self.__total
  
  def get_items(self):
    return self.__items
  
  
  
  


    
    