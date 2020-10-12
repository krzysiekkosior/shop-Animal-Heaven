from datetime import datetime, timedelta

from django.utils import timezone


def get_date(request):
    date = datetime.today() + timedelta(hours=2)
    return {'date': date}
