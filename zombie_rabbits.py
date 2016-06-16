import random
def answer(meetings):
    num_meetings_requested = len(meetings)
    if num_meetings_requested == 1:
        return 1

    zombie_to_bunny_rabbits_meetings = []

    # first sort the meeting using end time,
    # since number of meetings will be no larger than 100, this should be  sorting operation
    meetings.sort(key=lambda x: x[1])

    # take the first meeting, since number of meetings will be at least 1 and it's already sorted by meeting_end_time
    zombie_to_bunny_rabbits_meetings.append(meetings[0])
    last_accepted_meeting_end_time = meetings[0][1]

    for index in range(1, num_meetings_requested):
        # only accept new meetings that start close to end time of last accepted meeting
        if meetings[index][0] >= last_accepted_meeting_end_time:
            zombie_to_bunny_rabbits_meetings.append(meetings[index])
            last_accepted_meeting_end_time = meetings[index][1]

    return len(zombie_to_bunny_rabbits_meetings)

#Test cases

meetings1 = [[0, 1], [1, 2], [2, 3], [3, 5], [4, 5]]
print answer(meetings1)
#4

meetings2 = [[0, 1000000], [42, 43], [0, 1000000], [42, 43]]
print answer(meetings2)
#1

meetings3 = [[0, 1000000], [42, 43], [0, 1000000], [43, 44], [0, 5], [0, 1], [42, 43]]
print answer(meetings3)
#1

meetings4 = []
for i in range(100):
    start = random.sample(range(0, 1000000), 1)
    end = random.sample(range(start[0], 1000000), 1)
    meetings4.append([start[0], end[0]])
print meetings4
print answer(meetings4)