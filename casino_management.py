from . import db
from .models import User, Transaction

def get_all_transactions():
    return Transaction.query.all()

def get_user_balance(user_id):
    user = User.query.get(user_id)
    return user.balance

def adjust_user_balance(user_id, amount):
    user = User.query.get(user_id)
    user.balance += amount
    db.session.commit()
