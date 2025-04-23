import keyboard
import time
from datetime import datetime
import os

def setup_log_file():
    """Create a log file with timestamp in filename."""
    if not os.path.exists("keyboard_logs"):
        os.makedirs("keyboard_logs")
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    return os.path.join("keyboard_logs", f"keyboard_activity_{timestamp}.txt")

def main():
    log_file = setup_log_file()
    
    print(f"Keyboard monitoring started. Logs will be saved to: {log_file}")
    print("Press Ctrl+C to stop monitoring.")
    
    # Write initial entry to confirm log file is working
    with open(log_file, "a") as f:
        f.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}: Logging started\n")
    
    # Function to record keypress
    def on_key_press(key):
        try:
            with open(log_file, "a") as f:
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]
                
                # Get key name in a readable format
                if hasattr(key, 'name'):
                    key_name = key.name
                else:
                    key_name = str(key)
                    
                if len(key_name) == 1:
                    char_to_write = key_name
                else:
                    char_to_write = f"[{key_name}]"
                    
                f.write(f"{timestamp}: {char_to_write}\n")
                print(f"Key pressed: {char_to_write}")  # Debug output
        except Exception as e:
            print(f"Error logging key: {e}")
    
    # Register the callback for keyboard presses
    keyboard.on_press(on_key_press)
    
    try:
        # Keep the program running
        while True:
            time.sleep(0.1)
    except KeyboardInterrupt:
        print("\nKeyboard monitoring stopped.")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Error in main program: {e}")