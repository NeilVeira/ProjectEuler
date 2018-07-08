MONTHS = [31,28,31,30,31,30,31,31,30,31,30,31]

def do_year(year,weekday):
    months = list(MONTHS)
    if year%4 == 0 and (year%100 != 0 or year%400 == 0):
        #leapyear
        months[1] = 29
        
    cnt = 0
    for m in months:
        if weekday== 0:
            cnt += 1
        weekday = (weekday+m)%7
    return cnt,weekday
    
ans = 0
weekday = 1
for year in xrange(1900,2001):
    #print year,weekday
    cnt,weekday = do_year(year,weekday)
    if year > 1900:
        ans += cnt
print ans