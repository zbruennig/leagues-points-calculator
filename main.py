from collections import defaultdict

from boss_list import bosses
from classes import BossCollection
from task_list import tasks
import helper


def compute():
    combos = helper.get_region_combos()

    combo_max_points = {}
    combo_bosses = {}
    combo_tasks = defaultdict(list)
    uncompletable_tasks = defaultdict(list)
    for combo in combos:
        points_available = 0
        available_bosses = BossCollection()
        for boss in bosses:
            if boss.is_possible_with(combo):
                available_bosses.add(boss)
        for task in tasks:
            if task.is_possible_with(combo, available_bosses):
                points_available += task.points
                if task.needs_many_regions():
                    combo_tasks[combo].append(task)
            elif task.area in combo.__repr__():
                uncompletable_tasks[combo].append(task)
            else:
                pass

        combo_max_points[combo] = points_available
        combo_bosses[combo] = available_bosses

    # Will assume all the collection log ones are possible with any region choice

    region_list = [(r, p) for r, p in combo_max_points.items()]
    region_list = sorted(region_list, key=lambda p: p[1], reverse=True)


    for idx, item in enumerate(region_list):
        region = item[0]
        points = item[1]
        output = f"{region.__repr__().upper()} {points} {combo_bosses[region]}"
        print(output)

        print("\nCombinations:")
        for task in combo_tasks[region]:
            print(task.to_str())

        print("\nImpossible Region Tasks:")
        for task in uncompletable_tasks[region]:
            print(task.to_str())

        print("\n==================================================\n")





if __name__ == '__main__':
    compute()
