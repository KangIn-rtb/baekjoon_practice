# 유연근무제

def solution(schedules, timelogs, startday):
    daylist = []
    count = 0
    for i in range(len(schedules)):
        gift = [False]*(7)
        schedules[i] += 10
        if schedules[i]%100 >= 60:
            schedules[i] += 40
        for j in range(7):
            if timelogs[i][j] <= schedules[i]:
                gift[j] = True
            elif startday == 6 or startday == 7:
                gift[j] = True
            else:
                pass
            startday += 1
            if startday > 7:
                startday -= 7
        if False in gift:
            pass
        else:
            count += 1
    return count