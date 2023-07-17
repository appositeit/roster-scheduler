#!/usr/bin/env python3

import importlib
import pkgutil
import plugins.calendar
import plugins.roster
import pprint



pp = pprint.PrettyPrinter(indent=4, width=80, compact=True)

def iter_namespace(ns_pkg):
    # Specifying the second argument (prefix) to iter_modules makes the
    # returned name an absolute name instead of a relative one. This allows
    # import_module to work without having to do additional modification to
    # the name.
    return pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + ".")

def list_plugins():
    calendars = {
        name: importlib.import_module(name)
        for finder, name, ispkg
        in iter_namespace(plugins.calendar)
    }
    rosters = {
        name: importlib.import_module(name)
        for finder, name, ispkg
        in iter_namespace(plugins.roster)
    }

    return {
        'calendars': calendars,
        'rosters': rosters,
    }


class Scheduler:

    def __init__(self, roster_name):
        self.roster_name = roster_name
        self.plugins = list_plugins()

    @property
    def _roster_plugin(self):
        if len(self.plugins['rosters']) == 1:
            print('Found plugin')
            return list(self.plugins['rosters'].values())[0]


    def _get_roster(self):
        self.roster_plugin = self._roster_plugin.Roster(self.roster_name)
        print(self.roster_plugin)
        self.roster = self.roster_plugin.retrieve()
        pp.pprint(self.roster)


if __name__ == '__main__':
    main()