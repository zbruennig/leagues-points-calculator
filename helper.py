from copy import deepcopy
from typing import List

from classes import Regions
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

def update_tasks():
    remaining_existing_tasks = deepcopy(tasks)
    updated_tasks = []
    fresh_list = fresh_tasks_tbr
    for task in fresh_list:
        for idx, e in enumerate(remaining_existing_tasks):
            if task.is_equivalent_to(e):
                task.regions = e.regions
                task.needed_regions = e.needed_regions
                task.ca_tasks = e.ca_tasks
                task.ca_points = e.ca_points
                task.speed_tasks = e.speed_tasks

                del remaining_existing_tasks[idx]
                break

        updated_tasks.append(task)

    for task in updated_tasks:
        print(f"{task},")


if __name__ == '__main__':
    update_tasks()
