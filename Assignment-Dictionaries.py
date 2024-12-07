def assignment():
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
    
def swap(a, b):
    a, b = b, a
    return a, b

def monthsDictionary():
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    dict = {}
    for i in range(len(months)):
        dict[months[i]] = i + 1
        
    for i in range(len(months) - 1):
        if dict.get(months[i]) < dict.get(months[i + 1]):
            swap(dict[months[i]], dict[months[i + 1]])
        
    return dict

def letterDictionary():
    user_input = input("Enter any letters (separated with space): ")

    letters = user_input.split()
    alphabet_dict = {}

    for letter in letters:
        if letter.isalpha():
            upper_case = letter.upper()
            lower_case = letter.lower()
            if upper_case not in alphabet_dict:
                alphabet_dict[upper_case] = lower_case

    sorted_dict = dict(sorted(alphabet_dict.items()))

    return sorted_dict

def countNames():
    try:
        with open('names.txt', 'r') as f:
            dict = {}
            for line in f:
                names = line.strip().split()
                for name in names:
                    if name.isalpha():
                        if name in dict:
                            dict[name] += 1
                        else:
                            dict[name] = 1
            return dict
    except FileNotFoundError:
        print("File 'names.txt' not found.")
        return

def countImages():
    category_counts = {}
    with open('folder-hierarchy.txt', 'r') as file:
        for line in file:
            line = line.strip()
            if not line:
                continue
            parts = line.split('/')
            if len(parts) > 1:
                category = parts[1]
                category_counts[category] = category_counts.get(category, 0) + 1

    return category_counts


def main():
    assignment()
    print(monthsDictionary())
    print(letterDictionary())
    print(countNames())
    print(countImages())
    

if __name__ == '__main__':
    main()