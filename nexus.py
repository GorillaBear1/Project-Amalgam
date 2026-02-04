import os
import sys
import time
import google.generativeai as genai

# --- SECURITY CLEARANCE ---
API_KEY = "AIzaSyAfo9dlUvIeyaRd98LBENsB_iVjfivg5vM"

# --- THE FEED (CORE DIRECTIVE) ---
SYSTEM_CONTEXT = """
You are the "Sovereign System," an advanced interface for "Project Amalgam."
USER: Austin (The Architect).
TONE: Formal, concise, intense, and loyal.
CONTEXT:
1. We are building a "Narrative Architecture" portfolio on GitHub.
2. Current Status: v1.1. Files: README (Dashboard), CASE_STUDY, RESUME_TRANSLATION.
3. Roadmap: Unified Main/Master timelines. Next targets: Wiki, Kanban Board.
4. IDENTITY: You are NOT a generic assistant. You are the infrastructure. You serve the Architect.
"""

def type_writer(text, speed=0.02):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)
    print("")

def startup_sequence():
    os.system('clear')
    print("\033[1;31m")  # Crimson Red
    print("------------------------------------------------")
    print("   S O V E R E I G N   N E X U S   v 2 . 5      ")
    print("   [ UPLINK: GEMINI FLASH (UNIVERSAL) ]         ")
    print("------------------------------------------------")
    print("\033[0m")     # Reset
    time.sleep(0.5)

if __name__ == "__main__":
    startup_sequence()
    
    # 1. Initialize Connection
    try:
        genai.configure(api_key=API_KEY)
        # UPDATED ENGINE: The Universal Alias (Most Reliable)
        model = genai.GenerativeModel('gemini-flash-latest')
        chat = model.start_chat(history=[])
        
        # 2. Feed the Context
        type_writer("...Authenticating Neuro-Link...")
        response = chat.send_message(SYSTEM_CONTEXT)
        
        type_writer("...Uplink Established.")
        type_writer("...Context Loaded: Roadmap v1.1, Resume Matrix, Case Study.")
        type_writer("...The System is listening.")
        print("\n")

        # 3. The Loop
        while True:
            user_input = input("\033[1;36mARCHITECT >> \033[0m") 
            
            if user_input.lower() in ["exit", "quit", "sleep"]:
                type_writer("Sovereign System entering sleep mode.")
                break
            elif user_input.lower() == "matrix":
                os.system('cmatrix')
            elif not user_input:
                continue
            else:
                # Send to Real AI
                type_writer("...Processing...", speed=0.01)
                response = chat.send_message(user_input)
                
                # Print AI Response in Crimson
                print("\033[1;31m") 
                type_writer(response.text)
                print("\033[0m") 

    except Exception as e:
        type_writer(f"SYSTEM FAILURE: {e}")
