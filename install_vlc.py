import requests
import hashlib
import os
import subprocess

# Step 1: Get the Expected Hash Value of the VLC Installer
expected_hash_value = 'your_expected_hash_value'  # Replace with the actual hash value from the VLC website

# Step 2: Download the VLC Installer
installer_url = 'https://download.videolan.org/pub/videolan/vlc/3.0.17.4/win64/vlc-3.0.17.4-win64.exe.sha256'  
resp_msg = requests.get(installer_url)

# Check if the download was successful
if resp_msg.status_code == requests.codes.ok:
    # Step 3: Verify the Integrity of the Downloaded VLC Installer
    file_content = resp_msg.content
    computed_hash_value = hashlib.sha256(file_content).hexdigest()
    
    if computed_hash_value == expected_hash_value:
        print("Hash verification succeeded.")
        
        # Step 4: Save the Downloaded VLC Installer to Disk
        installer_path = r'C:\temp\vlc_installer.exe'  # Specify the path where you want to save the installer
        with open(installer_path, 'wb') as file:
            file.write(file_content)
        
        # Step 5: Silently Run the VLC Installer
        subprocess.run([installer_path, '/S'], check=True)
        
        # Step 6: Delete the VLC Installer from Disk
        os.remove(installer_path)
        
        print("VLC installation completed and installer deleted.")
    else:
        print("Hash verification failed. Download might be corrupted.")
else:
    print("Failed to download the installer.")
