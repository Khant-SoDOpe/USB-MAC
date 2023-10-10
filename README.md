# USB Drive Formatter for Mac OS

This Python script allows you to format a USB drive to Mac OS Extended (Journaled) and assign a name to it. It's a handy tool for creating bootable USB drives or preparing storage media for Mac-specific purposes.

## Prerequisites

- This script is designed for macOS.
- Ensure you have Python installed on your macOS system.

## Usage

1. Open a terminal window.

2. Navigate to the directory where you've saved the Python script.

3. Run the script by executing the following command:

   ```shell
   python script_name.py
   ```

4. You will be prompted to enter the name you want to assign to the USB drive after formatting it.

5. You will also be prompted to enter the USB location, which should be in the format `/dev/diskX`. Make sure to enter the correct location of your USB drive.

6. The script will format the USB drive to Mac OS Extended (Journaled) with the specified name.

7. If successful, your USB drive will be ready for use.

## Example

Here's an example of how you can use the script:

```shell
$ python script_name.py
What name would you like to assign to the USB drive after formatting it? : MyBootableUSB
Please enter the USB location : /dev/diskX
USB drive formatted successfully as Mac OS Extended (Journaled).
```

## Note

- Ensure that you have a backup of any important data on the USB drive before running this script, as it will erase all existing data.

- Replace `script_name.py` with the actual name of your Python script.

- Use this script responsibly and double-check the USB location to avoid formatting the wrong drive.

- This script can be especially useful for creating bootable USB drives for Mac OS installations.

- Feel free to modify the script to suit your specific needs.

Happy formatting!
