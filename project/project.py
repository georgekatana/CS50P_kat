import json
import sys
import os
import requests
import urllib
import urllib.error
import shutil
import tqdm
import csv
from datetime import datetime, timedelta
import time
import winsound
import sounddevice as sd

download_url = ""  # Global variable to store the download URL
authenticated_user = None  # Global variable to store the authenticated user details

def main():
    global authenticated_user
    authenticated_user = authenticate_user()

    check_file()
    delete_old_files()

def authenticate_user():
    global authenticated_user

    if authenticated_user:
        # If the user is already authenticated, return the authenticated user details
        print(f"{authenticated_user} Logged IN")
        return authenticated_user

    with open("users.json") as file:
        users_data = json.load(file)

    login_trials = 3
    while login_trials > 0:
        username = input("Username: ")
        password = input("Password: ")
        for user_data in users_data:
            if user_data['username'] == username and user_data['password'] == password:
                session_user = user_data['username']
                authenticated_user = session_user  # Store the authenticated user details
                print(f"{session_user} Logged IN")
                return session_user

        login_trials -= 1
        if login_trials > 0:
            print(f"Authentication failed. {login_trials} Attempts left. Please try again.")
        else:
           sys.exit(f"Authentication failed. {login_trials} Attempts left. Please contact admin.")
    return False

def check_file():
    global download_url
    while True:
        try:
            download_url = input("Enter download URL below:\n")
            download_file = urllib.request.urlopen(download_url,timeout=15)
            download_file_name = download_url.split("/")[-1]
            download_file_mbs = download_file.length / 1048576
            if download_file_mbs > 10:
                print(f"The file size is {download_file_mbs:.2f} MB:\n \n Checking local files.....")
            folder_path = 'backed_up_files'
            for root, dirs, files in os.walk(folder_path):
                if download_file_name in files:
                    print("File found in local network \n")
                    copy_file()
                    return True  # Return after copying the file

            # If the file is not found in the local network, back it up in the backed_up_files directory
            back_up_file(download_url)
            copy_file()
            break
        except urllib.error.HTTPError as error1:
            print(error1.status, error1.reason)
        except urllib.error.URLError as error2:
            print(error2.reason, "Enter a valid url and try again")
        except TimeoutError:
            print( "Request Timed Out")
        except ValueError:
            print("Invalid url string try again or Press CTRL C to exit")
        except KeyboardInterrupt:
            exit_animation = "\n \nE \n  x\n   i\n    t\n     i\n      n\n       g\n.............. \n"
            for letter in  exit_animation:
                print(" "+letter, end='', flush=True)
                if letter in"Exiting":
                    time.sleep(1)
                    winsound.PlaySound("/sounds/06.wav",winsound.SND_FILENAME)
            sys.exit()

        # Move the return statement here
    return True  # If no error occurred or file didn't meet size condition

def back_up_file(download_url):
    dest_folder = "backed_up_files"
    filename = download_url.split("/")[-1]
    dest_path = os.path.join(dest_folder, filename)

    response = requests.get(download_url, stream=True)
    response.raise_for_status()

    total_size = int(response.headers.get("content-length", 0))
    block_size = 8192
    progress_bar = tqdm.tqdm(total=total_size, unit="B", unit_scale=True, desc="Downloading", dynamic_ncols=True)
    with open(dest_path, 'wb') as file:
        for chunk in response.iter_content(chunk_size=block_size):
            file.write(chunk)
            progress_bar.update(len(chunk))

    progress_bar.close()
    print(f"File downloaded and saved to: {dest_folder}")
    winsound.PlaySound("/sounds/06.wav",winsound.SND_FILENAME)
    return dest_path

def copy_file():
    file = download_url.split("/")[-1]
    src_dir = "backed_up_files"
    dest_dir = input("Enter the destination folder to copy to:\n")
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)
    files = os.listdir(src_dir)
    session_user = authenticate_user()
    src_file = os.path.join(src_dir, file)
    dest_file = os.path.join(dest_dir, file)
    # Log the file access using the authenticated session_user
    log_file_access(src_file, session_user)

    with tqdm.tqdm(total=len(files), unit="file") as pbar:
        for file in files:
            shutil.copy2(src_file, dest_file)
            pbar.update()
    winsound.PlaySound("/sounds/06.wav",winsound.SND_FILENAME)
    print(f"Copied file: {file}")

    return src_file

def log_file_access(file_path, session_user):
    access_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    with open('access_log.csv', 'a', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow([file_path, access_time, session_user])
        print("\n File Access logged\n...........................")
    return True

def delete_old_files():
    current_date = datetime.now()
    six_months_ago = current_date - timedelta(days=180)

    with open('access_log.csv', newline='') as csvfile:
        csv_reader = csv.reader(csvfile)
        next(csv_reader)  # Skip the header row
        for row in csv_reader:
            file_path, access_time_str, _ = row
            access_time = datetime.strptime(access_time_str, '%Y-%m-%d %H:%M:%S')
            if access_time < six_months_ago:
                try:
                    os.remove(file_path)
                    print(f"Deleted old file: {file_path}")
                    winsound.PlaySound("/sounds/06.wav",winsound.SND_FILENAME)
                except OSError as e:
                    print(f"Error deleting file: {file_path} - {e}")
    return True

if __name__ == "__main__":
    main()
