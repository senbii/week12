dict = {}
email_count = 0

with open("mbox.txt", "r") as file:
    for line in file:
        line = line.strip()
        if line.startswith('From '):
            words = line.split()
            if len(words) > 1:
                email_address = words[1]
                dict[email_address] = dict.get(email_address, 0) + 1

max_sender = None
max_count = 0
for email, count in dict.items():
    if count > max_count:
        max_sender = email
        max_count = count
        
print(f'the most prolific comitter is {max_sender} with {max_count} emails.')