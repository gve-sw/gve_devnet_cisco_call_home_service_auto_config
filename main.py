""" Copyright (c) 2022 Cisco and/or its affiliates.
This software is licensed to you under the terms of the Cisco Sample
Code License, Version 1.1 (the "License"). You may obtain a copy of the
License at
           https://developer.cisco.com/docs/licenses
All use of the material herein must be in accordance with the terms of
the License. All rights not expressly granted by the License are
reserved. Unless required by applicable law or agreed to separately in
writing, software distributed under the License is distributed on an "AS
IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
or implied.
"""

from tabnanny import verbose
from tkinter import wantobjects
from netmiko import ConnectHandler
import xlrd
import logging
import sys
import json

logging.basicConfig(filename='output.log', encoding='utf-8', level=logging.INFO)
log_str = '*'*15 + ' New Script Run ' + '*'*15
logging.info('')
logging.info('*' * len(log_str))
logging.info(log_str)
logging.info('*' * len(log_str))
logging.info('')

# get the file name
excel_file = "file.xlsx"
email = "x@domain.com"

# read the workbook, we'll just use the first sheet only
wb = xlrd.open_workbook(excel_file)
sheet = wb.sheet_by_index(0)

# find the column numbers for the serial, network, and tags

for i in range(sheet.ncols):
    if sheet.cell_value(0, i).lower() == "ip":
        ip_col = i
    elif sheet.cell_value(0, i).lower() == "username":
        username_col = i
    elif sheet.cell_value(0, i).lower() == "password":
        password_col = i

# add all the entries to a list of dictionaries to reference later
device_list = []

for i in range(1, sheet.nrows):
    device = {}

    device["ip"] = sheet.cell_value(i, ip_col)
    device["username"] = sheet.cell_value(i, username_col)
    device["password"] = sheet.cell_value(i, password_col)


    device_list.append(device)

for row in device_list:
    # update the device's tags
    print(row)
    contact_email = "contact-email-addr " + email
    try:
        net_connect = ConnectHandler(
        verbose=False,
        device_type="cisco_xe",
        host=row["ip"],
        username=row["username"],
        password=row["password"],
    )

        cfg_list = [
        "service call-home",
        "call-home",
        contact_email,
    ]
        cfg_output1 = net_connect.send_config_set(cfg_list)

        print(cfg_output1)

        verify = "show run | in contact-email-addr"

        cfg_output2 = net_connect.send_command(verify)
        cfg_output2= cfg_output2.strip()
        
        expected_result = "contact-email-addr " + email
        if cfg_output2 == expected_result: 
            log_entry = "Email " +  email + " changed succcesfully for host " + str(row["ip"])

            logging.info(log_entry)
        else:
            log_entry = "Change failed for host " + str(row["ip"])
            logging.error(log_entry)

    except Exception as e:
        print(e)
