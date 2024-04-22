import tkinter as tk
from tkinter import ttk
import subprocess
import os
import webbrowser
import sys
import ctypes
import requests
import tempfile
import zipfile

# Function to perform installation or checking of the application
def perform_action(application, action, architecture, executable_path):
    try:
        if action == "Install":
            # Check if the file has a .ps1 extension and execute it with PowerShell if so
            if executable_path.endswith(".ps1"):
                subprocess.Popen(["powershell.exe", "-ExecutionPolicy", "Bypass", "-File", executable_path])
            else:
                # Otherwise, perform installation by executing the specified installation file
                subprocess.Popen([executable_path])
        elif action == "Run":
            if executable_path.startswith("https://"):
                # If the file is a URL, open it in the default web browser
                webbrowser.open(executable_path)
            else:
                # Open executable file with the default associated program
                subprocess.Popen(["start", "", executable_path], shell=True)
    except Exception as e:
        print(f"Error performing {action} for {application}: {str(e)}")

def get_latest_release_info():
    repo_url = "https://api.github.com/repos/Aditya-fmh/plngrt-toolkit/releases/latest"
    try:
        response = requests.get(repo_url)
        latest_release = response.json()
        return latest_release
    except Exception as e:
        print(f"Failed to get latest release info: {e}")
        return None

def check_for_updates(current_version):
    latest_release = get_latest_release_info()
    if latest_release:
        latest_version = latest_release["tag_name"]
        if latest_version > current_version:
            return True, latest_version, latest_release["assets"][0]["browser_download_url"]
    return False, current_version, None

def download_and_apply_update(download_url):
    with tempfile.TemporaryDirectory() as temp_dir:
        update_file_path = os.path.join(temp_dir, "update.zip")  # Path to save the update within the temp directory
        
        try:
            # Download the update
            response = requests.get(download_url)
            with open(update_file_path, "wb") as file:
                file.write(response.content)
            
            # Extract the ZIP file directly into the installation directory
            install_directory = os.path.dirname(__file__)  # Assuming the current directory is the installation directory
            with zipfile.ZipFile(update_file_path, 'r') as zip_ref:
                zip_ref.extractall(install_directory)
            
            print("Update downloaded and applied successfully.")
        except Exception as e:
            print(f"Failed to download or apply update: {e}")

def main_update_check():
    current_version = "1.3"  # This should be dynamically determined based on your application's current version
    update_available, latest_version, download_url = check_for_updates(current_version)
    if update_available:
        print(f"Update available: Version {latest_version}")
        download_and_apply_update(download_url)
    else:
        print("Your application is up to date.")

script_dir = os.path.dirname(__file__)
data_path = os.path.join(script_dir, "data", "script", "activator.cmd")
of_path = os.path.join(script_dir, "data", "script", "office-aio.bat")
w10_path = os.path.join(script_dir, "data", "script", "win10.bat")
w11_path = os.path.join(script_dir, "data", "script", "win11.bat")
wsh_path = os.path.join(script_dir, "data", "script", "enable-wsh.bat")

if getattr(sys, 'frozen', False):
    # If the script is compiled, set the icon for the executable
    if sys.platform == 'win32':
        ctypes.windll.kernel32.SetConsoleTitleW("PLNGRT Toolkit Buikd1.3")
        icon_file = "icon.ico"  # Replace with your icon file name
        ctypes.windll.kernel32.SetConsoleIcon(0)
        ctypes.windll.kernel32.SetConsoleIcon(icon_file)

# Define data for the "Standard" tab
standard_data = [
    ("AIO Runtime", "x32/x64", "Install", "data/app/aio.exe"),
    ("AIMP", "x64", "Install", "data/app/aimp_installer.exe"),
    ("Canva", "x32/x64", "Install", "data/app/canva_installer.exe"),
    ("CapCut", "x32/x64", "Install", "data/app/capcut_installer.exe"),
    ("Foobar2000", "x64", "Install", "data/app/foobar_installer.exe"),
    ("FoxitPDF", "x64", "Install", "data/app/foxit_installer.exe"),
    ("Google Chrome", "x64", "Install", "data/app/chrome_installer.exe"),
    ("Mendeley", "x64", "Install", "data/app/mendeley_installer.exe"),
    ("Mozilla Firefox", "x64", "Install", "data/app/firefox_installer.exe"),
    ("OperaGX", "x64", "Install", "data/app/operagx_installer.exe"),
    ("Telegram", "x64", "Install", "data/app/telegram_installer.exe"),
    ("VLC", "x64", "Install", "data/app/vlc_installer.exe"),
    ("WinCDEmu", "x64", "Install", "data/app/wincdemu_installer.exe"),
    ("WinRAR", "x64", "Install", "data/app/winrar_installer.exe"),
    ("Zoom", "x64", "Install", "data/app/zoom_installer.exe"),
]

# Define data for the "Checking" tab
checking_data = [
    ("BatteryInfoView", "x32/x64", "Run", "data/checking/batteryinfoview/batteryinfoview.exe"),
    ("CPU-Z", "x32/x64", "Run", "data/checking/cpu-z/cpuz_x32.exe"),
    ("CrystalDiskInfo", "x32/x64", "Run", "data/checking/CrystalDiskInfo/DiskInfo32.exe"),
    ("GPU-Z", "x64", "Run", "data/checking/gpu-z/GPU-Z.2.55.0.exe"),
    ("HDSentinel", "x32/x64", "Run", "data/checking/HDSentinel/HDSentinelProPortable.exe"),
    ("HWMonitor", "x32/x64", "Run", "data/checking/hwmonitor/HWMonitor_x32.exe"),
    ("Key Test", "All", "Run", "https://en.key-test.ru"),
    ("LCD Test", "All", "Run", "https://lcdtech.info/en/tests/dead.pixel.htm"),
    ("Mic Test", "All", "Run", "https://webcammictest.com/check-mic.html"),
    ("Speaker Test", "All", "Run", "https://www.youtube.com/watch?v=6TWJaFD6R2s"),
    ("Speccy", "x32/x64", "Run", "data/checking/speccy/Speccy.exe"),
]

# Define data for the "Activator" tab
activator_data = [
    ("Windows + Office AIO", "All", "Run", data_path),  # Replace 'data_path' with the path to your activator
    ("Microsoft Office AIO", "All", "Run", of_path),
    ("Windows 10", "All", "Run", w10_path),
    ("Windows 11", "All", "Run", w11_path)
    # Add more data here...
]

# Define data for the "MS Store" tab
msstore_data = [
    ("Install All App", "All", "Install", "data/script/all-install.ps1"),
    ("Install This First", "All", "Install", "data/script/requirement.ps1"),
    ("Microsoft Photos", "All", "Install", "data/script/install-photos.ps1"),
    ("Paint", "All", "Install", "data/script/install-paint.ps1"),
    ("Paint 3D", "All", "Install", "data/script/install-paint3d.ps1"),
    ("Whatsapp", "All", "Install", "data/script/install-whatsapp.ps1"),
    ("Windows Calculator", "All", "Install", "data/script/install-calculator.ps1"),
    ("Windows Camera", "All", "Install", "data/script/install-camera.ps1"),
    ("Microsoft Store", "All", "Install", "data/script/Add-Store.cmd")
]

# Define data for the "Win Updater" tab
winupdate_data = [
    ("WUMGR", "All", "Run", "data/checking/wumgr/wumgr.exe"),
    ("WUMT", "32-bit", "Run", "data/checking/wumt/wumt_x86.exe"),
    ("WUMT", "64-bit", "Run", "data/checking/wumt/wumt_x64.exe"),
]

# Define data for the "Extra Driver" tab
extdrv_data = [
    ("Camera T440p", "All", "Run", "data/driver/t440p_camera.exe"),
    ("HP Fn Key", "All", "Run", "data/driver/hp_fn_key.exe"),
]

# Create a new instance of the main window
window = tk.Tk()
window.title("PLNGRT Toolkit")

# Set the icon for the main window
window.iconbitmap(default='icon.ico')

# Create a Notebook widget for tab-like organization
notebook = ttk.Notebook(window)
notebook.pack(fill=tk.BOTH, expand=True)  # Make the notebook fill the window

# Create tabs for "Activator," "Checking," and "Standard" in this order
activator_tab = ttk.Frame(notebook)
checking_tab = ttk.Frame(notebook)
standard_tab = ttk.Frame(notebook)
msstore_tab = ttk.Frame(notebook)
winupdate_tab = ttk.Frame(notebook)
extdrv_tab = ttk.Frame(notebook)

notebook.add(activator_tab, text="Activator")
notebook.add(checking_tab, text="Checking")
notebook.add(standard_tab, text="Standard")
notebook.add(msstore_tab, text="MS Store")
notebook.add(winupdate_tab, text="Win Updater")
notebook.add(extdrv_tab, text="Extra Driver")

# Create a Frame within each tab to center the content
center_frame_standard = ttk.Frame(standard_tab)
center_frame_standard.pack(fill=tk.BOTH, expand=True)

center_frame_checking = ttk.Frame(checking_tab)
center_frame_checking.pack(fill=tk.BOTH, expand=True)

center_frame_activator = ttk.Frame(activator_tab)
center_frame_activator.pack(fill=tk.BOTH, expand=True)

center_frame_msstore = ttk.Frame(msstore_tab)
center_frame_msstore.pack(fill=tk.BOTH, expand=True)

center_frame_winupdate = ttk.Frame(winupdate_tab)
center_frame_winupdate.pack(fill=tk.BOTH, expand=True)

center_frame_extdrv = ttk.Frame(extdrv_tab)
center_frame_extdrv.pack(fill=tk.BOTH, expand=True)

# Create a header row for each tab
header_font = ("Helvetica", 12, "bold")

standard_header = ttk.Label(center_frame_standard, text="Name", font=header_font)
standard_header.grid(row=0, column=0, padx=10, pady=5)
architecture_header = ttk.Label(center_frame_standard, text="Architecture", font=header_font)
architecture_header.grid(row=0, column=1, padx=10, pady=5)
action_header = ttk.Label(center_frame_standard, text="Action", font=header_font)
action_header.grid(row=0, column=2, padx=10, pady=5)

separator_standard = ttk.Separator(center_frame_standard, orient="horizontal")
separator_standard.grid(row=1, column=0, columnspan=3, sticky="ew", pady=5)

checking_header = ttk.Label(center_frame_checking, text="Name", font=header_font)
checking_header.grid(row=0, column=0, padx=10, pady=5)
architecture_header = ttk.Label(center_frame_checking, text="Architecture", font=header_font)
architecture_header.grid(row=0, column=1, padx=10, pady=5)
action_header = ttk.Label(center_frame_checking, text="Action", font=header_font)
action_header.grid(row=0, column=2, padx=10, pady=5)

separator_checking = ttk.Separator(center_frame_checking, orient="horizontal")
separator_checking.grid(row=1, column=0, columnspan=3, sticky="ew", pady=5)

activator_name_header = ttk.Label(center_frame_activator, text="Name", font=header_font)
activator_name_header.grid(row=0, column=0, padx=10, pady=5)
activator_architecture_header = ttk.Label(center_frame_activator, text="Architecture", font=header_font)
activator_architecture_header.grid(row=0, column=1, padx=10, pady=5)
activator_action_header = ttk.Label(center_frame_activator, text="Action", font=header_font)
activator_action_header.grid(row=0, column=2, padx=10, pady=5)

separator_activator = ttk.Separator(center_frame_activator, orient="horizontal")
separator_activator.grid(row=1, column=0, columnspan=3, sticky="ew", pady=5)

msstore_name_header = ttk.Label(center_frame_msstore, text="Name", font=header_font)
msstore_name_header.grid(row=0, column=0, padx=10, pady=5)
msstore_architecture_header = ttk.Label(center_frame_msstore, text="Architecture", font=header_font)
msstore_architecture_header.grid(row=0, column=1, padx=10, pady=5)
msstore_action_header = ttk.Label(center_frame_msstore, text="Action", font=header_font)
msstore_action_header.grid(row=0, column=2, padx=10, pady=5)

separator_msstore = ttk.Separator(center_frame_msstore, orient="horizontal")
separator_msstore.grid(row=1, column=0, columnspan=3, sticky="ew", pady=5)

winupdate_name_header = ttk.Label(center_frame_winupdate, text="Name", font=header_font)
winupdate_name_header.grid(row=0, column=0, padx=10, pady=5)
winupdate_architecture_header = ttk.Label(center_frame_winupdate, text="Architecture", font=header_font)
winupdate_architecture_header.grid(row=0, column=1, padx=10, pady=5)
winupdate_action_header = ttk.Label(center_frame_winupdate, text="Action", font=header_font)
winupdate_action_header.grid(row=0, column=2, padx=10, pady=5)

separator_winupdate = ttk.Separator(center_frame_winupdate, orient="horizontal")
separator_winupdate.grid(row=1, column=0, columnspan=3, sticky="ew", pady=5)

extdrv_name_header = ttk.Label(center_frame_extdrv, text="Name", font=header_font)
extdrv_name_header.grid(row=0, column=0, padx=10, pady=5)
extdrv_architecture_header = ttk.Label(center_frame_extdrv, text="Architecture", font=header_font)
extdrv_architecture_header.grid(row=0, column=1, padx=10, pady=5)
extdrv_action_header = ttk.Label(center_frame_extdrv, text="Action", font=header_font)
extdrv_action_header.grid(row=0, column=2, padx=10, pady=5)

separator_extdrv = ttk.Separator(center_frame_extdrv, orient="horizontal")
separator_extdrv.grid(row=1, column=0, columnspan=3, sticky="ew", pady=5)

# Function to display data for the specified tab
def display_data(tab_frame, data):
    tab_buttons = []  # List to keep references to buttons

    for i, (name, architecture, action, executable_path) in enumerate(data, start=2):
        name_label = ttk.Label(tab_frame, text=name)
        architecture_label = ttk.Label(tab_frame, text=architecture)

        # Create and configure the button for either installation or checking
        action_button = ttk.Button(tab_frame, text=action, command=lambda app=name, act=action, arch=architecture, path=executable_path: perform_action(app, act, arch, path))
        tab_buttons.append(action_button)

        name_label.grid(row=i, column=0, padx=10, pady=5)
        architecture_label.grid(row=i, column=1, padx=10, pady=5)
        action_button.grid(row=i, column=2, padx=10, pady=5)

# Display data in the tabs
display_data(center_frame_standard, standard_data)
display_data(center_frame_checking, checking_data)
display_data(center_frame_activator, activator_data)
display_data(center_frame_msstore, msstore_data)
display_data(center_frame_winupdate, winupdate_data)
display_data(center_frame_extdrv, extdrv_data)

# Start the GUI main loop
window.mainloop()

# Check for updates on application start
main_update_check()
