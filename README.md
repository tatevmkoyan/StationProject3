Python Terminal Countdown Timer 
A robust, feature-rich command-line countdown timer written in Python. It features dynamic in-place updates, automatic time normalization, and comprehensive error handling.
Features
In-Place Terminal Updates: Ticks down smoothly on a single line using carriage returns (\r) rather than spamming new lines.

Automatic Time Normalization: Intelligently handles overflow values (e.g., if you input 90 seconds, it automatically converts it into 1 minute and 30 seconds).

Robust Error Handling:

Catches invalid non-numeric inputs (letters, special characters, or blank entries).

Prevents negative time values and zero-duration timers.

Gracefully handles user interruptions (Ctrl + C).

Clean Formatting: Displays time in a professional HH:MM:SS format with leading zeros.
