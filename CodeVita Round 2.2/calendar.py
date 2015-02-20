day = {0 : 'Sunday', 1 : 'Monday', 2 : 'Tuesday', 3 : 'Wednesday', 4 : 'Thursday', 5 : 'Friday', 6 : 'Saturday'}
inv_days = {'Sunday' : 0, 'Monday' : 1, 'Tuesday' : 2, 'Wednesday' : 3, 'Thursday' : 4, 'Friday' : 5, 'Saturday' : 6}
day_list = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
def main():
    months = int(raw_input().split(':')[1].strip())
    days = raw_input().split(':')[1].strip()
    days = map(int, days.split())
    ref = raw_input().split()
    start_day = ref[1]
    start_dd, start_mm, start_yy = map(int, ref[0].strip().split('-'))
##    print months
##    print days
##    print start_day
##    print start_dd, start_mm, start_yy
    epoch = days_since0(start_dd, start_mm, start_yy, months, days)
    tests = int(raw_input())
    for i in xrange(tests):
        given = map(int, raw_input().split('-'))
        print work(epoch, months, days, given[0], given[1], given[2], start_day)


def work(epoch, months, days, now_dd, now_mm, now_yy, ref):
    diff = days_since0(now_dd, now_mm, now_yy, months, days) - epoch
    count = diff % 7
    key = (count + inv_days[ref]) % 7
    return day[key]


def days_since0(dd, mm, yy, months, days):
    total = sum(days)
    leaps = yy // 25 + 1
    tot = yy * total + leaps * (25 - days[2])
    idx = 1
    t = 0
    while idx < mm:
        t += days[idx - 1]
        idx += 1
    if mm < 4 and yy % 25 == 0:
        tot -= (25 - days[2])
    tot += t + dd
    return tot

main()
##print days_since0(1, 1, 0, 4, [10, 12, 12, 14])
##print days_since0(1, 1, 25, 4, [10, 12, 12, 14])
##print days_since0(1, 3, 25, 4, [10, 12, 12, 14])
##print days_since0(1, 4, 25, 4, [10, 12, 12, 14])
##print days_since0(1, 1, 26, 4, [10, 12, 12, 14])