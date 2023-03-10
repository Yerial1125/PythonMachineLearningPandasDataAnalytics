import pandas as pd

dates = ['2019-01-01', '2020-03-01', '2021-06-01']

ts_dates = pd.to_datetime(dates)
print(ts_dates)
print()

pr_day = ts_dates.to_period(freq='D')
print(pr_day)
print()

pr_month = ts_dates.to_period(freq='M')
print(pr_month)
print()

pr_year = ts_dates.to_period(freq='Y')
print(pr_year)
print()