times = '1h 45m,360s,25m,30m 120s,2h 60s'

total_minutes =  0

time_list = times.split(',')
for time in time_list:
    for part in time.split(' '):
        if 'h' in part:
            part = part.replace('h', '')
            h = int(part) * 60
            total_minutes += h
        elif 'm' in part:
            part = part.replace('m', '')   
            total_minutes += int(part)
        else:
            part = part.replace('s', '')
            s = int(part) // 60
            total_minutes += s
        

print(total_minutes)