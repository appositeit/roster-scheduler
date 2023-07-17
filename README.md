# roster-scheduler
*This repo is in early development stage and the only code that does anything is protoype.py.*

An API drive automatic scheduler for oncall rosters driven by calendar availability with plugin support. In short, the roster scheduler can be used to automatically extend team oncall rosters while accounting for their calendar commitments, and try to keep scheduling fair.

The scheduler is designed to be modular and API driven to it can be used with various oncall systems. It uses a plugin system and proto3 to abstract the reprepresentation of oncall schedules, oncall rosters, and calendars.


Primary documentation is currently in Google Docs:
  * [About Oncall](https://docs.google.com/document/d/1SUsvL6WDW4biHvgOXOQ2mAizNZH3fHxX-fPDVGVqPzA/edit): Defines common terminology and understanding about oncall.
  * [Roster Scheduler: Design](https://docs.google.com/document/d/1AMKQMk0FwxEhip2SAQ6koP641tM7PdnRlvyfDwEhS64/edit#heading=h.1xxcmzzihtwz): Talks to the (aspirational!) design of Roster Scheduler.

## Installation

- **Step 1**. Clone the repo
   ```sh
   git clone https://github.com/appositeit/roster-scheduler && cd roster-scheduler
    ```
- **Step 2**. Setup python venv
  ```sh
  python3 -m venv .
  . bin/activate
  ```
- **Step 3**. Install requirements
    ```sh
    pip install -r requirements.txt
    ```
## Running the code

At this stage the only code that does anything is prototype.py so, umm, run it I guess?
```sh
python3 prototype.py
```

Be amazed at it's obtuse output! Woo! \o/
