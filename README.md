# roster-scheduler
*This repo is in early development stage and the only code that does anything is protoype.py.*

An API drive automatic scheduler for oncall rosters driven by calendar availability with plugin support. In short, the roster scheduler can be used to automatically extend team oncall rosters while accounting for their calendar commitments, and try to keep scheduling fair.

The scheduler is designed to be modular and API driven to it can be used with various oncall systems. It uses a plugin system and proto3 to abstract the reprepresentation of oncall schedules, oncall rosters, and calendars.


Primary documentation is currently in Google Docs:
  * [About Ocall](https://docs.google.com/document/d/1SUsvL6WDW4biHvgOXOQ2mAizNZH3fHxX-fPDVGVqPzA/edit): Defines common terminology and understanding about oncall.
  * [Roster Scheduler: Design](https://docs.google.com/document/d/1AMKQMk0FwxEhip2SAQ6koP641tM7PdnRlvyfDwEhS64/edit#heading=h.1xxcmzzihtwz): Talks to the (aspirational!) design of Roster Scheduler.
