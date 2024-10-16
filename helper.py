from copy import deepcopy
from typing import List

from classes import Regions, Task
from task_lists.master_task_list import all_known_tasks
from task_lists.task_list_tbr import tasks as tasks
from task_lists.task_list_tbr_raw import tasks as fresh_tasks_tbr
from task_lists.task_list_2020 import tasks as tasks_2020

def get_region_combos() -> List[Regions]:
    combinations = []
    regions = [
        # 'v',
        'z', 't', 'k', 'a', 'f', 'w', 'd', 'm']
        # 'z', 'd', 'm']
    length = len(regions)
    for i in range(0, length):
        for j in range(i+1, length):
            for k in range(j+1, length):
                combinations.append(Regions(**{
                    regions[i]: True,
                    regions[j]: True,
                    regions[k]: True
                }))
    return combinations

def update_with_known_tasks(task_list: List[Task], return_unknown_only: bool = False) -> List[Task]:
    remaining_existing_tasks = deepcopy(all_known_tasks)
    updated_tasks = []
    for task in task_list:
        matches = False
        for idx, e in enumerate(remaining_existing_tasks):
            if task.is_equivalent_to(e):
                matches = True
                task.regions = e.regions
                task.needed_regions = e.needed_regions
                task.ca_tasks = e.ca_tasks
                task.ca_points = e.ca_points
                task.speed_tasks = e.speed_tasks

                del remaining_existing_tasks[idx]
                break

        if matches and return_unknown_only:
            continue

        updated_tasks.append(task)

    return updated_tasks

