import random
subjects = ['Virat Kohli', 'Sachin Tendulkar', 'PM Naredra Modi', 'SRK', 
            'Zerodha founder Nikhil Kamath', 'Nirmala Sitaraman', 'Salman Khan', "Akshay kumar(akky)"]
actions = ['appears', 'was enjoying', 'lose all money', 'scored a century', 
           'released his movie poster', 'launches trailer',
           'free all taxes', 'laughed loud']
objects = ['at the park', 'at the beach', 'in a club', 'in treding', 'in pvr cinema'
            'in IPL match', 'in test match', 'at pubic event', 'after seeing middle man life']

while True:
    subject = random.choice(subjects)
    action = random.choice(actions)
    object = random.choice(objects)

    headline = f"BREKING News: {subject} {action} {object}"
    print(headline)

    userinput =  input("do youn want more headlines? (yes/no) : ").strip().lower()
    if userinput == "no":
        break

print ("thanks for using fake headline generator")
