import subprocess

def format_usb_to_macos_extended(device_path,name):
    try:
        # Construct the command to format the USB drive to Mac OS Extended (Journaled)
        command = ["diskutil", "eraseDisk", "JHFS+", name, device_path]

        # Run the command
        result = subprocess.run(command, capture_output=True, text=True, check=True)

        # Print the output for debugging purposes
        print("Output:", result.stdout)

        print("USB drive formatted successfully as Mac OS Extended (Journaled).")
    except subprocess.CalledProcessError as e:
        print("Error:", e)
    except Exception as e:
        print("An unexpected error occurred:", e)

if __name__ == "__main__":
    # Specify the path to your USB device (e.g., /dev/disk2)
    name = input("What name would you like to assign to the USB drive after formatting it? : ")
    usb_device_path = input('Please enter the USB location : ')  # Replace X with your actual disk number

    # Call the function to format the USB drive
    format_usb_to_macos_extended(usb_device_path,name)
