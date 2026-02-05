import os
import time
import json

class SovereignNexus:
    def __init__(self):
        self.data_file = "nexus_data.json"
        self.architect_name = "Austin"
        
        # Default starting values
        self.default_data = {
            "guardian_active": False,
            "stats": {
                "INT": 10,
                "DEX": 10,
                "WIS": 10
            }
        }
        
        # Load data from memory (the JSON file)
        self.load_system_data()

    def load_system_data(self):
        """Loads data from the Crimson Repository file."""
        if os.path.exists(self.data_file):
            with open(self.data_file, "r") as f:
                self.system_data = json.load(f)
        else:
            self.system_data = self.default_data
            self.save_system_data()

    def save_system_data(self):
        """Saves current data to the Crimson Repository file."""
        with open(self.data_file, "w") as f:
            json.dump(self.system_data, f, indent=4)

    def clear_screen(self):
        os.system('clear')

    def toggle_guard(self):
        """Switches Bevi's state and saves it."""
        self.clear_screen()
        if self.system_data["guardian_active"]:
            print("--- INITIATING PROTOCOL: HOLD THE GUARD ---")
            time.sleep(1)
            print(">> Guardian Bevi is now entering Code-Sleep.")
            self.system_data["guardian_active"] = False
        else:
            print("--- INITIATING PROTOCOL: SUMMON GUARDIAN ---")
            time.sleep(1)
            print(">> Guardian Bevi is ONLINE and ready for orders.")
            self.system_data["guardian_active"] = True
        
        self.save_system_data()
        input("\n[Press Enter to return]")

    def training_protocol(self):
        """Increases a stat and saves the progress."""
        self.clear_screen()
        print("=== INITIATING TRAINING PROTOCOL ===")
        print("1. [INT] Editing Task")
        print("2. [DEX] Coding/Manual Task")
        print("3. [WIS] Planning/Meditation")
        print("4. Cancel")
        
        choice = input("\nSelect sector to optimize >> ")
        mapping = {"1": "INT", "2": "DEX", "3": "WIS"}
        
        if choice in mapping:
            stat = mapping[choice]
            self.system_data["stats"][stat] += 1
            print(f"\n>> Success! {stat} is now {self.system_data['stats'][stat]}.")
            self.save_system_data()
        else:
            print("\nProtocol Aborted.")
        
        time.sleep(1.5)

    def view_status(self):
        """Displays all current data."""
        self.clear_screen()
        print(f"=== SOVEREIGN NEXUS: STATUS REPORT ===")
        print(f"ARCHITECT: {self.architect_name}")
        
        active = self.system_data["guardian_active"]
        state_text = "ONLINE (Active)" if active else "OFFLINE (Code-Sleep)"
        
        print(f"GUARDIAN STATUS: {state_text}")
        print("--------------------------------------")
        print(" [ ATTRIBUTES ]")
        for stat, value in self.system_data["stats"].items():
            print(f" > {stat}: {value}")
        print("--------------------------------------")
        input("\n[Press Enter to return]")

    def main_menu(self):
        """The main interface hub."""
        while True:
            self.clear_screen()
            print("=== AMALGAM INTERFACE v1.2 ===")
            print("1. View System Status")
            print("2. Toggle Guardian State (Hold/Summon)")
            print("3. Execute Training Protocol")
            print("4. Exit Nexus")
            
            choice = input("\nCommand >> ")

            if choice == "1":
                self.view_status()
            elif choice == "2":
                self.toggle_guard()
            elif choice == "3":
                self.training_protocol()
            elif choice == "4":
                print("Disconnecting...")
                break

if __name__ == "__main__":
    system = SovereignNexus()
    system.main_menu()

