import unittest
from app.game_logic import spin_reels, calculate_payout, calculate_multiplier, PAYOUTS

class TestGameLogic(unittest.TestCase):
    def setUp(self):
        # Set a fixed bet amount for all tests
        self.bet_amount = 10

    def test_spin_reels(self):
        """Test that spin_reels returns a list of symbols, a payout, and a multiplier."""
        result, payout, multiplier = spin_reels(self.bet_amount)
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 3)  # Assuming a 3-reel slot machine
        self.assertIsInstance(payout, int)
        self.assertIsInstance(multiplier, int)
        # Further checks can include validating that the symbols are from the expected set

    def test_calculate_payout(self):
        """Test the payout calculation based on different reel outcomes."""
        # Test with non-matching symbols, expecting no payout
        spin_result = ["🍒", "🍋", "🔔"]
        multiplier = calculate_multiplier(spin_result)
        self.assertEqual(calculate_payout(spin_result, self.bet_amount, multiplier), 0)

        # Test with matching symbols, using the payout defined in PAYOUTS
        # Ensure that the symbols used here are actually present in your SYMBOLS list
        matching_symbol = "🍒"
        spin_result = [matching_symbol, matching_symbol, matching_symbol]
        multiplier = calculate_multiplier(spin_result)
        expected_payout = PAYOUTS[matching_symbol] * self.bet_amount * multiplier
        self.assertEqual(calculate_payout(spin_result, self.bet_amount, multiplier), expected_payout)

        # Add more test cases as needed to cover various scenarios and edge cases

if __name__ == '__main__':
    unittest.main()
