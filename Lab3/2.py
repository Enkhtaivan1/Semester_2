ehniiTsag = int(input())
ehniiMinute = int(input())
ehniiSecond = int(input())

hoyrdohTsag = int(input())
hoyrdohMinute = int(input())
hoyrdohSecond = int(input())

time1 = ehniiTsag*3600 + ehniiMinute * 60 + ehniiSecond
time2 = hoyrdohTsag*3600 + hoyrdohMinute * 60 + hoyrdohSecond

print(time2 - time1)