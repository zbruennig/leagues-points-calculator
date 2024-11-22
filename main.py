from collections import defaultdict

from boss_list import bosses
from classes import BossCollection
from task_lists.task_list_tbr import tasks
from task_lists.master_task_list import all_known_tasks
import helper


def compute():
    print_combinations = True
    print_impossible = False
    print_completable = False

    task_list = all_known_tasks  # TODO Change this

    combos = helper.get_region_combos()

    combo_max_points = {}
    combo_bosses = {}
    combo_tasks = defaultdict(list)
    not_completable_tasks = defaultdict(list)
    completable_tasks = defaultdict(list)
    for combo in combos:
        points_available = 0
        available_bosses = BossCollection()
        for boss in bosses:
            if boss.is_possible_with(combo):
                available_bosses.add(boss)
        for task in task_list:
            if task.area not in combo.__repr__():
                continue
            if task.is_possible_with(combo, available_bosses):
                points_available += task.points
                completable_tasks[combo].append(task)
                if task.is_complicated:
                    combo_tasks[combo].append(task)
            else:
                not_completable_tasks[combo].append(task)

        combo_max_points[combo] = points_available
        combo_bosses[combo] = available_bosses

    # Will assume all the collection log ones are possible with any region choice

    region_list = [(r, p) for r, p in combo_max_points.items()]
    region_list = sorted(region_list, key=lambda p: p[1], reverse=True)


    for idx, item in enumerate(region_list):
        region = item[0]
        points = item[1]
        # output = f"{region.__repr__().upper()[1:]} {points} {combo_bosses[region]}"
        output = f"{region.__repr__().upper()[1:]} {combo_bosses[region]}"
        print(output)

        if print_combinations:
            print("\nCombinations:")
            for task in combo_tasks[region]:
                print(task.to_str())

        if print_impossible:
            print("\nImpossible Region Tasks:")
            for task in not_completable_tasks[region]:
                print(task.to_str())

        if print_completable:
            print("\nAll Possible Tasks:")
            for task in completable_tasks[region]:
                print(task.to_str())

        if print_completable or print_impossible or print_combinations:
            print("\n==================================================\n")





if __name__ == '__main__':
    compute()
