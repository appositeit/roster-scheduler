'''
Pythonic representation of a roster.
'''

import os
import glob
import pprint
import yaml

from get_project_root import root_path


pp = pprint.PrettyPrinter(indent=4, width=80, compact=True)

ROSTER_STORE = os.path.join(root_path(ignore_cwd=True), "test_data")


class Roster:
    
    def __init__(self, roster_name):
        self.roster_name = roster_name
        self._list_rosters()

    def _list_rosters(self):
        rosters = glob.glob(f'{ROSTER_STORE}/*.roster')
        self.rosters = {}
        for r in rosters:
            _, name = os.path.split(r)
            name, _ = os.path.splitext(name)
            self.rosters[name] = r
        print(self.rosters)
    

    def retrieve(self):
        print(self.roster_name)
        if self.roster_name not in self.rosters:
            print('Not found')
            return None

        filepath = self.rosters[self.roster_name]
        print(filepath)
        with open(filepath, 'r') as f:
            roster = yaml.safe_load(f)
            pp.pprint(roster)
            return roster