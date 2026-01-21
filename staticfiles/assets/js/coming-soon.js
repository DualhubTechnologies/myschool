// Configuration
const countdownConfig = {
    endDate: new Date("2026-08-25T23:59:59").getTime(), // Set your target END DATE and TIME
    autoReset: true,  // true = countdown will repeat infinitely, false = stop on completion
    cycleDurationDays: 10 // if autoReset is true, restart countdown for this many days
};

// Extracting the configuration values for easy use
let { endDate, autoReset, cycleDurationDays } = countdownConfig;

// Main function to update the countdown timer every second
function updateCountdown() {
    const now = new Date().getTime();
    let distance = endDate - now;

    // Check if the countdown has finished
    if (distance <= 0) {
        if (autoReset) {
            // If autoReset is enabled, add the cycle duration to the current time to restart
            const cycleDurationMs = cycleDurationDays * 24 * 60 * 60 * 1000; // Convert days to milliseconds
            endDate = new Date(now + cycleDurationMs).getTime(); // Set new endDate
            distance = endDate - now; // Recalculate remaining time
        } else {
            // If autoReset is disabled, show the "We Are Live!" message and stop the timer
            document.getElementById('countdown').innerHTML = "<h2>We Are Live!</h2>";
            clearInterval(timer); // Stop the interval to stop further updates
            return; // Exit the function
        }
    }

    const days = Math.floor(distance / (1000 * 60 * 60 * 24));
    const hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
    const minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
    const seconds = Math.floor((distance % (1000 * 60)) / 1000);

    document.getElementById('days').textContent = days.toString().padStart(2, '0');
    document.getElementById('hours').textContent = hours.toString().padStart(2, '0');
    document.getElementById('minutes').textContent = minutes.toString().padStart(2, '0');
    document.getElementById('seconds').textContent = seconds.toString().padStart(2, '0');
}

// Run the countdown immediately to show the first value without delay
updateCountdown();

// Update the countdown every 1000 milliseconds (1 second)
const timer = setInterval(updateCountdown, 1000);