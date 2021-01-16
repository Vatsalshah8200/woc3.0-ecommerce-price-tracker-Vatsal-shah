import csv
import sys


def script(link, price, email):
    rows = [[',',link, price, email, price]]
    filename = "D:\woc python\djangoprac\DjangoPracAkki\demo.csv"
    with open(filename, 'a') as csvfile:
        csvwriter = csv.writer(csvfile)
        # csvwriter.writerow(fields)
        csvwriter.writerows(rows)