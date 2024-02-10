document.addEventListener('DOMContentLoaded', () => {
    const spinButton = document.getElementById('spinButton');
    const balanceElement = document.getElementById('balance');
    let balance = 100; // Starting balance for demonstration

    spinButton.addEventListener('click', () => {
        spinReels();
    });

    function spinReels() {
        // This would be replaced by more complex logic and possibly server requests
        const outcomes = ['🍒', '🍋', '🔔', '🍉', '⭐']; // Simple reel items
        const result = [];

        for (let i = 0; i < 3; i++) { // Assuming a 3-reel slot machine
            const randomIndex = Math.floor(Math.random() * outcomes.length);
            result.push(outcomes[randomIndex]);
            document.getElementById(`reel${i + 1}`).textContent = outcomes[randomIndex]; // Update reel display
        }

        updateGame(result);
    }

    function updateGame(result) {
        // Simplified win condition: all reels match
        if (result[0] === result[1] && result[1] === result[2]) {
            balance += 50; // Win: increase balance
            alert("You win! 🎉");
        } else {
            balance -= 10; // Lose: decrease balance
        }

        updateBalance();
    }

    function updateBalance() {
        balanceElement.textContent = `Balance: ${balance} Elyte Tokens`;
        if (balance <= 0) {
            spinButton.disabled = true;
            alert("Game over! Reload the page to play again.");
        }
    }
});
