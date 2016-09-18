from app.url_tracker.models import Target, Click
from collections import OrderedDict
import datetime, io, csv
import pdb

# GenerateTrend()
# This method will take an ordered list or click data and combine it into an
# OrderedDict that has the number of clicks per day.
def generate_trend(click_data):

    if click_data:

        # Call make_empty_series with the start and end date. So we get a well
        # formatted time series.
        data = make_empty_series(
            start_date=click_data[0].date_created,
            end_date=click_data[-1].date_created
        )

        # Iterate over the actual click data and update the counts based on the
        # formatted_date.
        for click in click_data:
            formatted_date = click.date_created.strftime('%m-%d-%Y')
            data[formatted_date] = data[formatted_date] + 1

        return data

    else:
        return None

# make_empty_series()
# This method will take two dates as parameters and build an empty OrderedDict
# of days between the parameters. Will return the empty dictionary for later
# population.
def make_empty_series(start_date=None, end_date=None):

    data_dict = OrderedDict()
    end_date += datetime.timedelta(days=1)
    start_date += datetime.timedelta(days=-1)

    if start_date and end_date:

        current_date = start_date

        # Keep processing until we reach the end date + 1 day
        while (current_date <= end_date):

            data_dict[current_date.strftime('%m-%d-%Y')] = 0
            current_date += datetime.timedelta(days=1)

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
