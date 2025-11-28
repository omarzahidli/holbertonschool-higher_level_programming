#!/usr/bin/python3
import csv
import json
def convert_csv_to_json(file_csv):
    try:
        with open (file_csv, "r") as csvfile:
            csv_read =csv.DictReader(csvfile)
            info = [row for row in csv_read]

        with open('data.json', 'w') as jsonfile:
            json.dump(info, jsonfile)

        return True
    except FileNotFoundError:
        print("File not found")
        return False
