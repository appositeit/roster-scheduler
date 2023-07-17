#!/usr/bin/env python3

'''
This wrapper script calls scheduler as if it were invoked by RPC. It is primarily
used for testing and development. (Although I guess it'll evolve into a general tool?)
'''

import scheduler



def main():
    sch = scheduler.Scheduler('teama')
    sch._get_roster()


if __name__ == '__main__':
    main()