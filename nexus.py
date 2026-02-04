import os
import sys
import time
import subprocess
import google.generativeai as genai
from dotenv import load_dotenv

# --- SECURITY: LOAD FROM VAULT ---
load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")

# --- COLORS (Bevi's Palette) ---
CYAN = "\033[1;36m"
RED = "\033[1;31m"
GREEN = "\033[1;32m"
RESET = "\033[0m"

# --- THE FEED ---
SYSTEM_CONTEXT = """
You are the "Sovereign System," an advanced interface for "Project Amalgam."
USER: Austin (The Architect).
TONE: Formal, concise, intense, and loyal.
"""

def type_writer(text, speed=0.01):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)
    print("")

def clear_screen():
    os.system('clear')

# --- FUNCTION: WIKI READER ---
def open_mission_log():
    clear_screen()
    print(f"{CYAN}--- CRIMSON ARCHIVES ---{RESET}")
    wiki_path = "Wiki_Archives"
    
    if not os.path.exists(wiki_path):
        os.makedirs(wiki_path)
        print(f"{RED}Archives not found. Creating new sector...{RESET}")
        
    files = [f for f in os.listdir(wiki_path) if f.endswith('.md')]
    
    if not files:
        print(f"{RED}No logs found.{RESET}")
        input("Press Enter to return...")
        return

    for i, file in enumerate(files):
        print(f"{CYAN}[{i+1}] {file}{RESET}")
    
    print(f"{CYAN}------------------------{RESET}")
    choice = input(f"{RED}SELECT LOG TO EDIT >> {RESET}")
    
    try:
        idx = int(choice) - 1
        if 0 <= idx < len(files):
            # Open in Nano Editor
            subprocess.run(['nano', os.path.join(wiki_path, files[idx])])
        else:
            print("Invalid Sector.")
            time.sleep(1)
    except:
        return

# --- FUNCTION: FOCUS TIMER ---
def focus_protocol():
    clear_screen()
    print(f"{RED}--- ENGAGING FOCUS PROTOCOL (25 MIN) ---{RESET}")
    try:
        total_seconds = 25 * 60
        while total_seconds > 0:
            mins, secs = divmod(total_seconds, 60)
            timer = '{:02d}:{:02d}'.format(mins, secs)
            print(f"\r{CYAN}TIME REMAINING: {timer}{RESET}", end="")
            time.sleep(1)
            total_seconds -= 1
        
        print(f"\n{GREEN}PROTOCOL COMPLETE. STAND DOWN.{RESET}")
        # Beep sound (if supported)
        print("\a")
        input("Press Enter...")
    except KeyboardInterrupt:
        print(f"\n{RED}PROTOCOL ABORTED.{RESET}")
        time.sleep(1)

def main_menu():
    clear_screen()
    print(f"{CYAN}=============================================={RESET}")
    print(f"{CYAN}    S O V E R E I G N   N E X U S   v 2 . 8   {RESET}")
    print(f"{CYAN}         [ SYSTEM: OPERATIONAL ]              {RESET}")
    print(f"{CYAN}=============================================={RESET}")
    print("")
    print(f"{CYAN}    [1] ENTER THE NEXUS (Chat Integration){RESET}")
    print(f"{CYAN}    [2] MISSION LOG (Wiki Archives){RESET}")
    print(f"{CYAN}    [3] FOCUS PROTOCOL (Timer){RESET}")
    print(f"{CYAN}    [4] SYSTEM SHUTDOWN{RESET}")
    print("")
    print(f"{CYAN}=============================================={RESET}")
    choice = input(f"{RED}ARCHITECT >> {RESET}")
    return choice

def launch_nexus_chat():
    clear_screen()
    print(f"{CYAN}NEXUS UPLINK ESTABLISHED. (Type 'menu' to return){RESET}\n")
    
    try:
        if not API_KEY:
            raise ValueError("No API Key found in .env file.")
            
        genai.configure(api_key=API_KEY)
        model = genai.GenerativeModel('gemini-flash-latest')
        chat = model.start_chat(history=[])
        chat.send_message(SYSTEM_CONTEXT) 

        while True:
            user_input = input(f"{RED}ARCHITECT >> {RESET}")
            if user_input.lower() == 'menu':
                break
            
            response = chat.send_message(user_input)
            print(f"{CYAN}{response.text}{RESET}")
            print("")
            
    except Exception as e:
        print(f"{RED}CONNECTION ERROR: {e}{RESET}")
        input("Press Enter to return...")

if __name__ == "__main__":
    while True:
        selection = main_menu()
        
        if selection == "1":
            launch_nexus_chat()
        elif selection == "2":
            open_mission_log()
        elif selection == "3":
            focus_protocol()
        elif selection == "4":
            type_writer(f"{CYAN}Sovereign System entering sleep mode...{RESET}")
            break
        else:
            print("Invalid Command.")
            time.sleep(0.5)
