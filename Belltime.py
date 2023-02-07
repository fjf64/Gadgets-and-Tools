import time as t
advisory = {
    1:"8:30-9:18",
    2:"9:22-10:09",
    3:"10:13-11:00",
    4:"11:04-11:51",
    5:"12:25-13:12",
    "adv":"13:16-13:47",
    6:"13:51-14:38",
    7:"14:42-15:30",
}
normal = {
    1:"8:30-9:23",
    2:"9:27-10:19",
    3:"10:23-11:15",
    4:"11:19-12:11",
    5:"12:45-13:37",
    6:"13:41-14:33",
    7:"14:37-15:30",
}
two_delay = {
    1:"10:30-11:05",
    2:"11:09-11:44",
    3:"12:18-12:53",
    4:"12:57-13:32",
    5:"13:36-14:11",
    6:"14:15-14:50",
    7:"14:54-15:30",
}
csr = {
    "a":advisory,
    "n":normal,
    "2":two_delay
}
pp = t.asctime()
current_time = pp[11:19]
sect = current_time.split(":")
sect[0] = str(int(sect[0]) - 5)
day = input("[a] Advisory || [n] Normal || [2] Two Hour Delay")
for x in csr[day]:
    halfsies = csr[day][x].split("-")
    fhalf = halfsies[0].split(":")
    shalf = halfsies[1].split(":")
    period = x
    if int(fhalf[0]) <= int(sect[0]) <= int(shalf[0]) and int(fhalf[1]) <= int(sect[1]) <= int(shalf[1]) or int(fhalf[0]) <= int(sect[0]) <= int(shalf[0]) and int(sect[1]) <= int(shalf[1]):
        break
distbase = int(shalf[0])*60 + int(shalf[1])
distsub = int(sect[0])*60 + int(sect[1])
dist = distbase - distsub
print(f"Period {period}")
print(f"{dist} Minutes and {60 - int(sect[2])} Seconds until Next Period at {halfsies[1]}")
