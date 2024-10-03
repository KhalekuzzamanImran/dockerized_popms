import datetime
import calendar


def get_date_range_this_week():
    today = datetime.date.today()
    start_of_week = today - datetime.timedelta(days=today.weekday()+1)
    end_of_week = start_of_week + datetime.timedelta(days=6)
    return start_of_week, end_of_week


def get_date_range_this_month():
    today = datetime.date.today()
    _, last_day_of_month = calendar.monthrange(today.year, today.month)
    start_of_month = today.replace(day=1)
    end_of_month = today.replace(day=last_day_of_month)
    return start_of_month, end_of_month


def get_date_range_last_month():
    today = datetime.date.today()
    first_day_of_this_month = today.replace(day=1)
    last_day_of_last_month = first_day_of_this_month - datetime.timedelta(days=1)
    first_day_of_last_month = last_day_of_last_month.replace(day=1)
    return first_day_of_last_month, last_day_of_last_month


def get_date_range_this_year():
    today = datetime.date.today()
    start_of_year = today.replace(month=1, day=1)
    end_of_year = today.replace(month=12, day=31)
    return start_of_year, end_of_year


def get_date_range_last_year():
    today = datetime.date.today()
    last_year = today.year - 1
    start_of_last_year = datetime.date(last_year, 1, 1)
    end_of_last_year = datetime.date(last_year, 12, 31)
    return start_of_last_year, end_of_last_year


def filter_fields(self, *extra):
    # print('======', extra)
    fields = self.request.GET.copy()

    today = datetime.date.today()

    if 'created_date__lte' in fields and 'created_date__gte' in fields:
        from_date = datetime.datetime.strptime(fields['created_date__gte'], '%d-%m-%Y')
        to_date = datetime.datetime.strptime(fields['created_date__lte'], '%d-%m-%Y')
        
        if from_date == to_date:
            fields['created_date__lte'] = datetime.datetime.strptime(fields['created_date__lte'], '%d-%m-%Y') + datetime.timedelta(days=1)
        else:
            fields['created_date__lte'] = to_date

        fields['created_date__gte'] = from_date

    if 'date' in fields and fields['date'] == 'today':
        fields['created_date__gte'] = today

    if 'date' in fields and fields['date'] == 'this_week':
        fields['created_date__gte'], fields['created_date__lte'] = get_date_range_this_week()

    if 'date' in fields and fields['date'] == 'this_month':
        fields['created_date__gte'], fields['created_date__lte'] = get_date_range_this_month()

    if 'date' in fields and fields['date'] == 'last_month':
        fields['created_date__gte'], fields['created_date__lte'] = get_date_range_last_month()

    if 'date' in fields and fields['date'] == 'this_year':
        fields['created_date__gte'], fields['created_date__lte'] = get_date_range_this_year()

    if 'date' in fields and fields['date'] == 'last_year':
       fields['created_date__gte'], fields['created_date__lte'] = get_date_range_last_year()

    if 'date' in fields and fields['date'] == 'last_seven_days':
        fields['created_date__lte'] = today + datetime.timedelta(days=1)
        fields['created_date__gte'] = today - datetime.timedelta(days=7)

    if 'date' in fields and fields['date'] == 'last_fourteen_days':
        fields['created_date__lte'] = today + datetime.timedelta(days=1)
        fields['created_date__gte'] = today - datetime.timedelta(days=14)

    if 'date' in fields and fields['date'] == 'last_thirty_days':
        fields['created_date__lte'] = today + datetime.timedelta(days=1)
        fields['created_date__gte'] = today - datetime.timedelta(days=30)

    if 'date' in fields and fields['date'] == 'last_sixty_days':
        fields['created_date__lte'] = today + datetime.timedelta(days=1)
        fields['created_date__gte'] = today - datetime.timedelta(days=60)

    if 'date' in fields:
        del fields['date']

    if 'search' in fields:
        del fields['search']

    if 'page_size' in fields:
        del fields['page_size']

    if 'page' in fields:
        del fields['page']

    final_fields = {}

    for key, value in fields.items():
        if fields[key]:
            final_fields[key] = value

    return final_fields
