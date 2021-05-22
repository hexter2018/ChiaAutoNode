from datetime import datetime
import os, time, subprocess, requests

def titleCredit():
    print("-----------------------------------")
    print("iDisk Thailand - Auto Add Full Node")
    print("-----------------------------------")

def mainFunction():
    # Credit Title Program
    titleCredit()
            
    chia_exec_path = "/usr/lib/chia-blockchain/resources/app.asar.unpacked/daemon/chia"
        
    while True:
        timeNow = datetime.now().strftime("%H:%M:%S")
        print("[" + str(timeNow) + "][System] Fetch new node from iDisk")
        chia_api_node = requests.get('https://chia-thailand.com/nodes/api.php?t' + str(time.time()))
        chia_node_json = chia_api_node.json()
        for node_chia in chia_node_json:
            argument_chia = " show -a " + str(node_chia["IP"])
            subprocess.Popen(chia_exec_path + argument_chia, shell=True)
            time.sleep(30)

if __name__ == "__main__":
    mainFunction()
