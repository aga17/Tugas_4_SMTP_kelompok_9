log_file_path = "smtp_debug.log"
    
def parsingText(text):
        text = ":".join(text.split(':')[1:])
        return text
    
    # Define the condition and action in a directory
condition = {
        #1
        "ehlo": lambda line: print(parsingText(line)),
        #2
        "250-starttls": lambda line: print(parsingText(line)),
        #3
        "msg: b'2.0.0 smtp server ready": lambda line: print(parsingText(line)),
        #4
        "send: 'auth login": lambda line: print(parsingText(line)),
        #5
        "reply: b'250-si": lambda line: print(parsingText(line)),
        #6
        "reply: b'221 2.0.0": lambda line: print(parsingText(line)),
        #7
        "send: rcpt to:": lambda line: print(parsingText(line))
        
    }
    
# set to keep track of matched conditions
matched_conditions = set()

# membuka file log dalam mode baca
with open(log_file_path, 'r') as log_file:
    
    # Membaca setiap baris dalam file log
    for line in log_file.readlines():
        
        # Loop through the conditions dictionary and check if any condition matches
        for condition, action in condition.items():
            if condition in line.lower() and condition not in matched_conditions:
                action(line)
                matched_conditions.add(condition)
                break # Break out of the loop after the first matching condition
