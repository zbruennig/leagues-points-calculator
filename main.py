from typing import List

from boss_list import bosses
from classes import BossCollection, Regions, Task
from task_list import tasks
import helper


def compute():
    combos = helper.get_region_combos()

    combo_max_points = {}
    for combo in combos:
        points_available = 0
        available_bosses = BossCollection()
        for boss in bosses:
            if boss.is_possible_with(combo):
                available_bosses.add(boss)
        for task in tasks:
            if task.is_possible_with(combo, available_bosses):
                points_available += task.points
        if points_available > 0:
            combo_max_points[combo] = points_available

    # Will assume all the collection log ones are possible with any region choice

    point_list = [(r, p) for r, p in combo_max_points.items()]
    point_list = sorted(point_list, key=lambda p: p[1], reverse=True)

    width = 6
    line = ""
    for idx, item in enumerate(point_list):
        line = f"{line} {item[0]} {item[1]} |"
        if idx % width == width - 1:
            print(line)
            line = ""




if __name__ == '__main__':
    compute()
