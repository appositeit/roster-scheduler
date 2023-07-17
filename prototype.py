#!/usr/bin/env python
'''
Want to solve for an oncall schedule.

Inputs:
* Existing schedule
* List of people to schedule
* Constrained list of who can work on what days.

Variables:

'''

import collections
import numpy as np
from cpmpy import *
import protos.oncall_pb2

'''
Consider a single oncall schedule with a single oncaller per
oncall shift, which can be represented by an array:
    schedule = []
    
The people are in a list
    people = ['personA', 'personB', ...]
    
People are constrained whether they can work or not:
    availability = [
        [1,1,1,1,1,1,0,1,1,1,1,0,1,1,1,0,1,1,0],
        [1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
        ...
    ]

People also have a history of hours already worked:

    hours_history = [8, 16, 16, 8, 24]

Historical hours worked should be based on a configurable sliding window (e.g. 3 months)
    
We want to optimize for balanced oncall hours such that:

   minimize f = sum for each person(sum(weighting(scheduled hours for a person))^2)

The final schedule will look something like:

schedule = [1,3,0,2,4,0,1,2,3,3]

...where each number represents a person in the oncall schedule.
schedule is an intvar, with integers in the range of people ids.

The solution is found in two phases:

* We use a constraint based solver to generate alternatives.
* We then rank the different solutions using a ranking metric.

Note that this may not find the optimal solution since the solver does not use the metric,
but it should come up with a good solution. The solver is arbitrarily time bounded.


ToDo:
* Generalizing to shifts with secondary rotations, we need to add constraints
such that the primary, secondary cannot be the same person, and we should add
weights such that secondary oncallers cost less in the ranking function. For convenience
we should also allow the tertiary oncaller to be statically assigned (typically a team escalation).
  * Secondary oncallers do not require a different availability matrix.

* Write pre-processor code which can ingest YAML formatted oncall files and query calendars to make
this a working solution.

* Separately write code to handle rotating between rosters.

* Identify if there is common nomenclature for oncall.
'''

rotations_count = 5

people = ['a', 'b', 'c', 'd', 'e', '-']

schedule = intvar(0, len(people)-1, shape=rotations_count, name="schedule")

availability = np.array([
    [False, True,  False, True,  True],    # a
    [True,  True,  False, True,  True],     # b
    [True,  False, True,  True,  True],     # c
    [False, True,  True,  False, True],     # d
    [False, True,  True,  True,  True],     # e
    [False] * 5
])

availability_t = availability.T

SHIFT_DURATION = 8

people_historical_hours = [
    3, 8, 15, 12, 5
]


def rank_solution(solution):
    try:
        unique, counts = np.unique(solution, return_counts=True)
    except Exception as e:
        print(solution)
        print(e)
    shifts = dict(zip(unique, counts))
    hours = np.array([])
    for i, h in enumerate(people_historical_hours):
        hours = np.append(hours, h + SHIFT_DURATION * shifts.get(i, 0))
    
    value = np.sum(np.square(hours)) 
    print(hours, " ", value)
    return value, hours


def solve():
    m = Model()

    # for shift, p_a in enumerate(availability.T):
    #     print(f'p_a: {p_a}')
    #     available = [person for person, v in enumerate(p_a) if v]
    #     if available:
    #         m += schedule[shift] == available
        
    # Add availability constraints.
    # for shift_i, shift_a in enumerate(availability_t):
    #     print(shift_i, shift_a)
    #     ps = [p_i for p_i, p_a in enumerate(shift_a) if p_a]
    #     m += schedule[shift_i] == ps
            
    for person, p_a in enumerate(availability):
        for shift, s_a in enumerate(p_a):
            if s_a:
                # m += schedule[shift] == person
                continue
            else:
                # This person can't do this shift
                print(f'{people[person]} can\'t do shift {shift}')
                m += schedule[shift] != person

    # counts = np.bincount(schedule)
    # m.minimize = np.dot(counts,weights)
    # frequency = np.array([0] * (len(people)+1))
    # print(frequency)
    # m += GlobalCardinalityCount(schedule, frequency)
    # m.minimize(sum(frequency)**2)
    print(m)

    # # Create constraints to count the frequency of each integer value
    # constraints = []
    # for value in set(range(len(people))):
    #     m += sum(schedule == value)
    #     # constraints.append(count == frequency)

    # m.minimize(frequency ** 2)

    # m += constraints
    # m += objective

    # m.minimize(sum(schedule == person) for person, _ in enumerate(people))

    solutions = []

    def accumulate():
        # s = [f'{shift}: {who.value()}' for shift, who in enumerate(schedule)]
        s = [f'{who.value()}' for shift, who in enumerate(schedule)]
        s = [who.value() for who in schedule]
        solutions.append(s)

    count = m.solveAll(time_limit=5, display=accumulate)
    if not count:
        print("No solution found")
        return
    
    print(count)
    sorted_solutions = [] 
    for solution in solutions:
        value, hours = rank_solution(solution)
        sorted_solutions.append((value, solution, hours))
    sorted_solutions = sorted(sorted_solutions)
    for s in reversed(sorted_solutions):
        print(s)
    
    print()
    print(sorted_solutions[0])

def main():
    solve()


if __name__ == '__main__':
    main()