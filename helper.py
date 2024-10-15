from copy import deepcopy
from typing import List

from classes import Regions, Task
from task_list_raw import tasks as fresh_tasks
from task_list import tasks

def get_region_combos() -> List[Regions]:
    combinations = []
    regions = [
        # 'v',
        'z', 't', 'k', 'a', 'f', 'w', 'd', 'm']
        # 'z', 'd', 'k']
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
    for task in fresh_tasks:
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
