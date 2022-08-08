from datetime import datetime

DATETIME_FORMAT = '%Y-%m-%d:%H-%M'


def validate_time_continuum(end_date, start_date):
    if end_date and start_date > end_date:
        raise ValueError('End date is before start date.')


def get_start_date(request):
    start_date = request.GET.get('start_date')

    if not start_date:
        return datetime.now()

    try:
        start_date = datetime.strptime(start_date, DATETIME_FORMAT)
        return start_date
    except ValueError:
        raise ValueError('Invalid start date format.')


def get_end_date(request):
    end_date = request.GET.get('end_date')
    try:
        if end_date:
            return datetime.strptime(end_date, DATETIME_FORMAT)

    except ValueError:
        raise ValueError('Invalid end date format.')
