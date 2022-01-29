

def convert_time(duration: int) -> str:
    if duration <= 59:
        print(duration, "сек")
    if 60 < duration < 3600:
        minute = duration // 60
        sec = duration % 60
        print(minute, "мин", sec, "сек")
    if 3600 < duration < 86400:
        hour = duration // 3600
        minute = (duration % 3600) // 60
        sec = (duration % 3600) % 60
        print(hour, "час", minute, "мин", sec, "сек" )
    if 86400 < duration < 604800:
        week = duration // 86400
        hour = (duration % 86400) // 3600
        minute = (duration % 3600) // 60
        sec = (duration % 3600) % 60
        print(week, "дн", hour, "час", minute, "мин", sec, "сек")
    return 0


duration = 400153
result = convert_time(duration)
print(result)
