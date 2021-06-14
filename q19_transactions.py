# Given a list of transactions between a group of friends (can be one person
# paying multiple people, multiple people paying one person and vice versa),
# calculate and print out how much money individuals owe one another.

def bill(transactions):
    users = set()
    for t in transactions:
        for p in t[0]:
            users.add(p)
        for r in t[1]:
            users.add(r)

    owes = {}
    for user in users:
        owes[user] = {}
        for other in users:
            if other != user:
                owes[user][other] = 0

    for t in transactions:
        for p in t[0]:
            for r in t[1]:
                owes[p][r] += round(t[2]/len(t[1])/len(t[0]), 2)
    return owes

def main():
    # paying, receiving, amount
    # Assumes transactions w/ multiple people are split evenly, that is
    # each pays the same amount and each receives the same amount.
    transactions = [
        (('Jeff','Todd'), ('Tina','Kaylee','Ross'), 35),
        (('Ross','Kaylee'), ('Tina',), 12),
        (('Tina','Kaylee','Todd'), ('Jeff',), 90),
        (('Jeff',), ('Michael',), 5)
    ]
    print(bill(transactions))

if __name__ == '__main__':
    main()
