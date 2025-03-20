# Blind-Data-Exfil-Server-Side-javascript-injection

A Python script that automates blind NoSQL injection to extract usernames from vulnerable web applications. The script exploits Server-Side JavaScript Injection (SSJI) via the $where clause in MongoDB queries.

🚀 Features
Automated username extraction using character-by-character brute force.
Uses NoSQL injection (this.username.match()) to determine valid username characters.
Supports a-z, A-Z, 0-9 (modifiable charset).
Mimics real browser headers for stealth.
Response-based detection (checks for successful login indicators).
Includes debugging output (payload, response length, status code).

## Usage
`python3 extract_username.py`

## Configuration
Modify these values before running the script:

URL → Set to the vulnerable website.
HEADERS → Update headers if needed for better stealth.
CHARSET → Modify character set if usernames contain special characters.
username → Change the starting prefix (HTB{) if applicable.


## How It Works
Sends a NoSQL injection payload:
```
" || (this.username.match("^HTB{X.*")) || ""=="  
```

If "X" is correct, the server responds with "Logged in as" or "Nothing to see here".
If "X" is incorrect, it moves to the next character.
Loops through a-z, A-Z, 0-9 until it reconstructs the full username.

Stops when the complete username is found.
