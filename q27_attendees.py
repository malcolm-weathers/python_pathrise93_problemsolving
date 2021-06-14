# Given an array of objects of attendees for an event, return the date that
# most attendees of one country could attend the event.

def best(att):
    days = {}
    for attendee in att:
        for date in attendee:
            if not date in days:
                days[date] = 1
            else:
                days[date] += 1
    return max(days, key=days.get)

def main():
    att = [
        ('6/15','6/16'),
        ('6/15','6/17','6/18','6/19',),
        ('6/17',),
        ('6/17','6/18'),
        ('6/19','6/20')
    ]
    print(best(att))

if __name__ == '__main__':
    main()
