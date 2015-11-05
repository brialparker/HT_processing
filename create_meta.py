#!/usr/bin/env python3

import json, yaml, sys, datetime
import dateutil.parser as parser

data = json.load(sys.stdin)

#split the date apart to replace the non-ISO ':' with a '-' then put it back together again

def datesplit(CreateDate):
        splitdate = CreateDate.split(" ")
        splitdate[0]
        splitdate[1]
        splitdate[0]=splitdate[0].replace(":","-")
        capture_date="T".join(splitdate)
        return capture_date

#rename the keys according to HT specs, while also providing some of the constant values

for item in data:
        item.pop("SourceFile")
#       item["capture_date"] = datesplit(item.pop("CreateDate")) CreateDate does not consistently appear in metadata - can't use
        item["capture_date"] = datesplit(item.pop("FileModifyDate"))
        item["scanner_make"] = "NIKON CORPORATION"
        item["scanner_model"] = "NIKON D810"
        item["scanner_user"] = "Creekside Digital"
        item["contone_resolution_dpi"] = item.pop("XResolution")
        item["scanning_order"] = "right-to-left"
        item["reading_order"] = "right-to-left"

#print data into yaml format

yml = yaml.safe_dump(data[0],default_flow_style=False, stream=None)

print(yml)