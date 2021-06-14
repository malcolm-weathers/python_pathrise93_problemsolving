# You have a number of meetings (with their start and end times). You need to
# schedule them using the minimum number of rooms. Return the list of meetings
# in every room.

# Return True if there is overlap between two meetings.
def overlap(m1, m2):
    m1_start = int(m1[0].replace(':',''))
    m1_end = int(m1[1].replace(':',''))
    m2_start = int(m2[0].replace(':',''))
    m2_end = int(m2[1].replace(':',''))
    return (m1_start > m2_start and m1_start < m2_end) or \
           (m1_end > m2_start and m1_end < m2_end)

# Check existing rooms if a meeting can be scheduled and if not, create a new
# one.
def schedule(meetings):
    rooms = [[meetings[0]]]
    del meetings[0]
    while len(meetings) > 0:
        m = meetings[0]
        del meetings[0]
        for room in rooms:
            if not any(overlap(m, meeting) for meeting in room):
                room.append(m)
                break
            else:
                rooms.append([m])
                break
    return rooms

def main():
    meetings = [
        ('7:15', '8:15'),
        ('8:00', '8:30'),
        ('1:00', '2:00'),
        ('10:30', '11:15'),
        ('10:45', '11:30'),
        ('11:15', '12:00'),
        ('8:00', '11:00')
    ]
    print(schedule(meetings))

if __name__ == '__main__':
    main()
