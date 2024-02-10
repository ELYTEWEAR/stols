from . import db
from .models import User, Transaction
import random

# Define symbols and their base payouts
SYMBOLS = ["🍒", "🍋", "🔔", "🍉", "⭐", "🍇", "7️⃣"]
PAYOUTS = {
    "🍒": 2, "🍋": 3, "🔔": 4, "🍉": 5, "⭐": 8, "🍇": 10, "7️⃣": 15
}

# Special symbols
WILD = "🃏"
SCATTER = "💎"

# Define the reels
REELS = [
    SYMBOLS + [WILD, SCATTER] * 2,  # Increase the occurrence of special symbols
    SYMBOLS + [WILD, SCATTER] * 2,
    SYMBOLS + [WILD, SCATTER] * 2
]

def spin_reels(bet_amount):
    """Simulate spinning the reels and return the result."""
    result = [random.choice(reel) for reel in REELS]
    multiplier = calculate_multiplier(result)
    payout = calculate_payout(result, bet_amount, multiplier)
    return result, payout, multiplier

def calculate_multiplier(spin_result):
    """Calculate any multipliers based on special symbol combinations."""
    if WILD in spin_result and spin_result.count(WILD) == 3:
        return 10  # Example: 10x payout for 3 wilds
    if spin_result.count(SCATTER) >= 2:
        return 5  # Example: 5x payout for 2 or more scatters
    return 1  # No multiplier

def calculate_payout(spin_result, bet_amount, multiplier):
    """Calculate the payout based on the spin result, bet amount, and any multipliers."""
    if len(set(spin_result)) == 1 and spin_result[0] in PAYOUTS:  # All symbols match
        return PAYOUTS[spin_result[0]] * bet_amount * multiplier
    return 0  # No payout

def update_balance(user_id, payout):
    """Update user balance based on the payout and create a transaction record."""
    user = User.query.get(user_id)
    user.balance += payout  # Payout can be negative for a lost bet

    db.session.add(Transaction(user_id=user_id, amount=payout))
    db.session.commit()

def bonus_round(user_id):
    """Trigger a bonus round for the user."""
    bonus = 0
    if random.randint(1, 10) > 7:  # 30% chance to trigger a bonus round
        bonus = random.randint(50, 200)  # Bonus amount
        user = User.query.get(user_id)
        user.balance += bonus
        db.session.add(Transaction(user_id=user_id, amount=bonus))
        db.session.commit()
    return bonus
