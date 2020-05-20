import random
suites = ['♡', '♢', '♤', '♧']
values = list(range(1,14))

def get_random_card():
    # your code here
    return random.randint(0, 13)
    
    
print(suites[get_random_card()] + str(values[get_random_card()]))
