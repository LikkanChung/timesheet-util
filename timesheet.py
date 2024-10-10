from datetime import datetime
from datetime import timedelta
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("start_time", help="Start time in the day (hhmm)")
parser.add_argument("break_mins", help="Total time of breaks in mins")
parser.add_argument("end_time", help="End time in day (hhmm)")
args = parser.parse_args()
start_time = args.start_time
break_mins = args.break_mins
end_time = args.end_time


dt_format = "%H%M"
tdelta = datetime.strptime(end_time, dt_format) - datetime.strptime(start_time, dt_format)
mins_in_office = tdelta.total_seconds() / 60
mins_working = mins_in_office - int(break_mins)
hours_working = mins_working / 60
formatted_hours = "%02d:%02d" % (divmod(mins_working, 60))
print(f"Total hours: {hours_working} ({formatted_hours})")

if hours_working > 7.5:
    overtime_hours = hours_working - 7.5
    print(f"Overtime: {overtime_hours}")
