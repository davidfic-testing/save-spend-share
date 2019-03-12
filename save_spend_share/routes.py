from save_spend_share import app, api
from flask_restplus import Resource, Api
from database import get_kids

@app.route('/')
@app.route('/index')
def index():
    return "hello world"



@app.route('/add/<amount>')
def add_amount(amount):
    return amount

@app.route('/add/<name>')
def add_kid(name):
    #TODO error checking
    db.add_kid(name)

@app.route('/add/<kid>/<amount>/<bucket>')
def add_money(kid,amount,bucket):
    print(f'adding {amount} to {kid}s {bucket} bucket')
    return None


@api.route('/kids')
class Kids(Resource):
    def get(self):
        kids = db.get_kids()
        return {'name': kids[0], 'name': kids[1]}
