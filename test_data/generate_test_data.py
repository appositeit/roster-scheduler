#!/user/bin/env python
'''
Generate, save, load and print test data in YAML format.
Test data and the test data format should NOT be used in production
systems. The format is, at best, suggestive of the data structures
needed for oncall scheduler to work.
'''
import protos.oncall_pb2

import yaml
import pprint

SCHEDULE_FILE = 'test_data/scheduleA.yaml'
CALENDAR_FILE = 'test_data/calendars.yaml'

people = {
    "personA": "personA@calendar",
    "personB": "personB@calendar",
    "personC": "personC@calendar",
    "personD": "personD@calendar",
    "personE": "personE@calendar",
    "personF": "personF@calendar",
    "personG": "personG@calendar",
    "personH": "personH@calendar",
}

scheduleA = {
    "service_name": "Big Web Service",
    "rosters": [
        {
            "name": "teamA",
            "rotation_time": "08:00",
        },
        {
            "name": "teamB",
            "rotation_time": "20:00",
        },
    ]
}

teamA = {
    "configuration": {
        "name": "teamA",
        "timezone": "Australia/Sydney",
        "shiftchange": "02:00"
    },
    "shifts": [
        ["2023-07-01", ["personA", "personC"]],
        ["2023-07-02", ["personB", "personD"]],
        ["2023-07-03", ["personC", "personA"]],
        ["2023-07-04", ["personD", "personB"]],
    ]
    
}

teamB = {
    "configuration": {
        "name": "teamB",
        "timezone": "Europe/Zurich",
        "shiftchange": "02:00"
    },
    "shifts": [
        ["2023-07-01", ["personE", "personG"]],
        ["2023-07-02", ["personF", "personH"]],
        ["2023-07-03", ["personG", "personE"]],
        ["2023-07-04", ["personH", "personF"]],
    ]
    
}

schedule = {
    'schedule': scheduleA,
    'people': people,
    'rosters': {
        'teamA': teamA,
        'teamB': teamB,
    }
}


with open(SCHEDULE_FILE, 'w') as f:
    yaml.dump_all([schedule], f)


with open(SCHEDULE_FILE, 'r') as f:
    doc = yaml.safe_load(f)
    pp = pprint.PrettyPrinter(indent=2)
    pp.pprint(doc)
    
    
calendar = {
   'personA': [
       ['2023-07-10 10:00', '2023-07-10 11:00', 'DNS'],
       ['2023-07-11 10:00', '2023-07-11 11:00', 'Normal Meeting'],
       ['2023-07-12 02:00', '2023-07-12 03:00', 'DNS'],
   ]
}

with open(CALENDAR_FILE, 'w') as f:
    yaml.dump_all([calendar], f)


with open(CALENDAR_FILE, 'r') as f:
    doc = yaml.safe_load(f)
    pp = pprint.PrettyPrinter(indent=2)
    pp.pprint(doc)