from datetime import datetime

def get_date(request):
    return {'date': datetime.today()}
