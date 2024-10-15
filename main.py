from boss_list import bosses
from classes import BossCollection
from task_list import tasks
import helper


def compute():
    combos = helper.get_region_combos()

    combo_max_points = {}
    combo_bosses = {}
    for combo in combos:
        points_available = 0
        available_bosses = BossCollection()
        for boss in bosses:
            if boss.is_possible_with(combo):
                available_bosses.add(boss)
        for task in tasks:
            if task.is_possible_with(combo, available_bosses):
                points_available += task.points
        combo_max_points[combo] = points_available
        combo_bosses[combo] = available_bosses

    # Will assume all the collection log ones are possible with any region choice

    region_list = [(r, p, combo_bosses[r]) for r, p in combo_max_points.items()]
    region_list = sorted(region_list, key=lambda p: p[1], reverse=True)

    width = 1
    line = ""
    for idx, item in enumerate(region_list):
        line = f"{line} {item[0]} {item[1]} {item[2]} |"
        if idx % width == width - 1:
            print(line)
            line = ""




if __name__ == '__main__':
    compute()
