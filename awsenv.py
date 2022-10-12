#!/usr/bin/env python3

import fileinput
import json
# import dateutil.parser

def getInput():
    arg = ""
    for line in fileinput.input():
        arg = arg + line
    return arg

def getCreds(creds):
    return {
        "AWS_ACCESS_KEY_ID": creds['AccessKeyId'],
        "AWS_SECRET_ACCESS_KEY": creds["SecretAccessKey"],
        "AWS_SESSION_TOKEN": creds['SessionToken'],
        "AWS_REGION":'us-west-2'
    }

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    arg = getInput()

    creds = getCreds(json.loads(arg)['Credentials'])
    str = ""
    for key, value in creds.items():
        str = str + "{}={};".format(key,value)
        print("export {}={}".format(key,value))

    print(str)
    # expire = dateutil.parser.isoparse(json.loads(arg)['Credentials']['Expiration'])
    # local = expire.astimezone(dateutil.tz.gettz())
    # print('echo "Credentials expire {}"'.format(local))
