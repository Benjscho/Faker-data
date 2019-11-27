# VM Fake data gen file
# coding=utf-8

from faker import Faker
import pandas as pd
import numpy as np
from datetime import datetime
import os

cwd = os.getcwd()

# Initialise our faker
fake = Faker()

# Set number of entries in data set
n = 5

# create random fake user

def new_fake_row():
    tmp_first = fake.first_name()
    tmp_last = fake.last_name()
    tmp_email = tmp_first + "." + tmp_last + "@" + fake.domain_name()
    tmp_number = "+" + fake.msisdn()
    return [tmp_email,tmp_last,tmp_first,tmp_email,tmp_number]


# create data variable
data = []
for i in range(n):
    data.append(new_fake_row())

# print(data)
# Set up a df wtih the desired columnds
df = pd.DataFrame(data,columns=['Reference','Last','First','Email','Number'])

path = cwd+'Testdata'+ datetime.now().strftime('%Y-%m-%d %H:%M:%S').replace(" ","")
# Save df to tab delimited file
df.to_csv('Testdata-'+ datetime.now().strftime('%Y-%m-%d-T%H-%M-%S')+'.txt', index=False, sep='\t')
