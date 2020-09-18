from save_spend_share import app
from save_spend_share import database

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


