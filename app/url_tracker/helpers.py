from app.url_tracker.models import Target, Click
from collections import OrderedDict
import datetime, io, csv

DATETIME_FORMAT = '%m-%d-%Y'

# GenerateTrend()
# This method will take an ordered list or click data and combine it into an
# OrderedDict that has the number of clicks per day.
def generate_trend(click_data, days=35):

    if click_data:

        # Call make_empty_series with the start and end date. So we get a well
        # formatted time series.
        data = make_empty_series(
            start_date=click_data[0].date_created,
            end_date=click_data[-1].date_created
        )

        # If there is no data then return
        if not data:
            return None

        # Iterate over the actual click data and update the counts based on the
        # formatted_date.
        for click in click_data:
            formatted_date = click.date_created.strftime(DATETIME_FORMAT)
            data[formatted_date] = data[formatted_date] + 1

        # If we have more than 30 days then we can trim it down to 30 days of
        # click data. Converting OrderedDict to array and slicing it. Then
        # overwriting the existing variable for data.
        if len(data) > days:

            data = OrderedDict(
                list( data.items() )[-days:]
            )

        # Return data to calling function
        return data

    # No data for Target.
    else:

        return None

# make_empty_series()
# This method will take two dates as parameters and build an empty OrderedDict
# of days between the parameters. Will return the empty dictionary for later
# population.
def make_empty_series(start_date=None, end_date=None):

    # We want to strip the times so converting to date
    start_date = start_date.date()
    end_date = end_date.date()

    data_dict = OrderedDict()

    if start_date and end_date:

        # Initialize with the start date
        data_dict[start_date.strftime(DATETIME_FORMAT)] = 0

        # We will append delta number of days starting with current_date
        delta = abs((start_date - end_date).days)
        current_date = start_date + datetime.timedelta(days=1)

        # Looping over for each day between start and end
        for i in range(delta):
            data_dict[current_date.strftime(DATETIME_FORMAT)] = 0
            current_date += datetime.timedelta(days=1)

    else:
        return None

    return data_dict

# generate_csvdata()
# This method will generate a csv file using the click data that is provided as
# a parameter. We will escape any values that may contain a comma etc.
def generate_csvdata(click_results):

    if click_results:

        output = io.StringIO()
        writer = csv.writer(output, quoting=csv.QUOTE_MINIMAL)

        # Attach the header first.
        writer.writerow(click_results[0].to_array()[0])

        for click in click_results:
            writer.writerow( click.to_array()[1])

        return output.getvalue()

    else:
        return None

# datetime_filter()
# This function will be our jinja2 filter that will consistently format our
# different datetime objects.
def datetime_filter(input_datetime, format="%c"):

    datetime_str = input_datetime.strftime(format)

    return datetime_str
