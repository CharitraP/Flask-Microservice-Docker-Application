from flask import request,jsonify, Blueprint,abort
from .models import Retailer, Items
from .utils import addRetailers,calculatePoints
from app import create_app

bp=Blueprint('routes',__name__)


@bp.route("/")
def home():
    return "Welcome to the Fetch Take Away Assignment"
@bp.errorhandler(404)
def not_found_errors(e):
    return jsonify(error=str(e)), 404

@bp.errorhandler(400)
def missing_erros(e):
    return jsonify(error=str(e)), 400


"""The below method gets the response of the request in json format and later 
the data is extracted and created into an object and then id is generated for each receipt
if the receipt already exist it prints the same id"""

@bp.route('/receipts/process', methods=['POST'])
def process_receipts():

    receipt=request.get_json()
    if receipt is None:
      abort(404, description="Receipt not found")
    required_keys = ['retailer', 'purchaseDate', 'purchaseTime', 'total', 'items']
    for key in required_keys:
        if key not in receipt:
            abort(400, description=f"Missing required field: {key}")
    retailer_name = receipt['retailer']
    purchase_date = receipt['purchaseDate']
    purchase_time = receipt['purchaseTime']
    total = receipt['total']
    if not isinstance(receipt['items'], list) or not receipt['items']:
      abort(404, description="Items not found in the receipt")
    try:
        items = [Items(item['shortDescription'], item['price']) for item in receipt['items']]
    except KeyError as e:
        abort(400, description=f"Missing item field: {e}")
    retailer = Retailer(retailer_name, purchase_date, purchase_time, total, items)
    response={'id':addRetailers(retailer)}
    return jsonify(response)
    

@bp.route('/receipts/<id>/points', methods=['GET'])
def getPoints(id):
    if str(id) not in Retailer.allRetailers:
      abort(404,description="Receipt does not exist")
    response={'points':calculatePoints(id)}
    return jsonify(response)

    