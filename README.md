# Timesheet Utility
This is a quick Python script to help work out how much time to enter into a timesheet.

```
python timehsheet.py <start_time> <break_mins> <end_time>
```

Example usage:
If I start working at 09:00 and leave at 17:30 with a 30 minute lunch, then I have worked 7.5 hours
```
python timesheet.py 0900 30 1700
```
Output:
```
Total hours: 7.5 (07:30)
```

It will also calculate how much overtime hours, if worked for more than 7.5 hours:

```
python timesheet.py 0900 30 1900
```
Output:
```
Total hours: 9.5 (09:30)
Overtime: 2.0
```
