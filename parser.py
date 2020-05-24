# TODO:
# 1. parse json conf file
# 2. Read origin data
# 3. Convert to binary string
# 4. byte swap
# 5. parse table based on conf
# 6. print result based on choice
# 7. A good input interface

import json

tbl_type = 'oam_session_1st'
net_type = 'l2vpn'
ip_proto = 'ipv4'

def read_data(tbl_type, file_name):
    """Read raw data and do basic preprocess"""


def read_conf():
    """Read json-based conf file"""
    print("hi!")

with open('./tbl.json') as fp:
    tbl_conf = json.load(fp);
