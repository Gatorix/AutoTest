import datetime


def get_today():
    return datetime.date.today()


def format_seconds(secs):
    h = int(secs / 3600)
    secs -= h * 3600
    m = int(secs / 60)
    secs -= m * 60
    return f"{h:d}:{m:02d}:{secs:05.2f}"
