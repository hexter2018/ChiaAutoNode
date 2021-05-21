from datetime import datetime
import os, time, subprocess, requests

def titleCredit():
    print("------------------------------------------------------------------------------")
    print("iDisk Thailand - Auto Add Full Node")
    print("Fanpage - https://www.facebook.com/IDISKThailand")
    print("------------------------------------------------------------------------------")

def mainFunction():
    # Credit Title Program
    titleCredit()
    
    # Search Version Chia
    chia_app_path = os.listdir(os.environ['USERPROFILE'] + "\\AppData\\Local\\chia-blockchain\\")
    chia_app_version = ""
    for chia_data in chia_app_path:
        if "app-" in chia_data:
            chia_app_version = chia_data
            
    # Check Condition
    if len(chia_app_version) == 0:
        timeNow = datetime.now().strftime("%H:%M:%S")
        print("[" + str(timeNow) + "][System] Please install Chia-Blockchian on you computer")
    else:
        # Set Chia Execute Folders
        chia_exec_path = os.environ['USERPROFILE'] + "\\AppData\\Local\\chia-blockchain\\" + chia_app_version + "\\resources\\app.asar.unpacked\\daemon\\chia.exe"
        
        # Start Get and Add Node
        while True:
            timeNow = datetime.now().strftime("%H:%M:%S")
            print("[" + str(timeNow) + "][System] Fetch new node from iDisk")
            chia_api_node = requests.get('https://chia-thailand.com/nodes/api.php?t' + str(time.time()))
            chia_node_json = chia_api_node.json()
            for node_chia in chia_node_json:
                argument_chia = " show -a " + str(node_chia["IP"])
                subprocess.Popen(chia_exec_path + argument_chia, shell=True)
                time.sleep(1) # CPU fixed
                
            time.sleep(30)

if __name__ == "__main__":
    mainFunction()