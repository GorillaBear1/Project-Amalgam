import google.generativeai as genai

# Using the Key you provided
API_KEY = "AIzaSyAfo9dlUvIeyaRd98LBENsB_iVjfivg5vM"

print("--- DIAGNOSTIC SCAN INITIATED ---")
try:
    genai.configure(api_key=API_KEY)
    
    # Fetch all available models
    available_models = []
    for m in genai.list_models():
        if 'generateContent' in m.supported_generation_methods:
            print(f"FOUND: {m.name}")
            available_models.append(m.name)
            
    if not available_models:
        print("CRITICAL: Authentication worked, but no models were found.")
    else:
        print(f"\nScan Complete. {len(available_models)} engines available.")

except Exception as e:
    print(f"SCAN FAILED. Error details:\n{e}")
