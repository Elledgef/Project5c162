#Author: Faith Elledge
#Githubuser: elledgf
#Data: 10/26/22
#Description: Imports a Json file with SAT test results and writes the data to a text file in CSV format

import json


class SatData:
    "Private class"
    def __init__(self):
        """Imports data from json file"""
        with open('sat.json', 'r') as infile:
            self._sat_data = json.load(infile)['data']


    def save_as_csv(self,dbns):
        "Sorts the DBN in the CSV file in desending order"
        column_headers = ['DBN', 'School Name', 'Number of Test Takers', 'CRM', 'Math', 'Writing Mean']
        with open('output.csv','w') as outfile:
            for column in column_headers:
                outfile.write(str(column_headers) + '\n')

