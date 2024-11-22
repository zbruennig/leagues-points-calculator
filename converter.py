from classes import Task
from helper import update_with_known_tasks
from wiki_dumps.trailblazer_2020_data import leagues_2 as leagues_2
from wiki_dumps.tbr_latest import leagues_4
from wiki_dumps.tbr_earliest import leagues_4_initial
from wiki_dumps.echoes_earliest import echoes_initial

"""
rows = document.querySelectorAll('table.wikitable.lighttable > tbody > tr')
rows = Array.from(rows)
data = rows.map(row => [row.cells[0].childNodes[0].childNodes[0].childNodes[0].currentSrc, row.cells[1].innerText, row.cells[2].innerText, row.cells[3].innerText, row.cells[4].innerText])
Wayback Machine:
data = rows.map(row => [row.cells[0].childNodes[0].currentSrc ?? row.cells[0].childNodes[0].children[0].currentSrc, row.cells[1].innerText, row.cells[2].innerText, row.cells[3].innerText, row.cells[4].innerText])
"""

def parse_region(text: str, base: bool):
    if 'Globe' in text:
        return ''
    if 'Misthalin' in text:
        return 's'
    if 'Karamja' in text:
        return 's'
    if 'Varlamore' in text:
        return 'v'
    if 'Kourend' in text:
        return 'z'
    if 'Tirannwn' in text:
        return 't'
    if 'Kandarin' in text:
        return 'k'
    if 'Asgarnia' in text:
        return 'a'
    if 'Fremennik' in text:
        return 'f'
    if 'Wilderness' in text:
        return 'w'
    if 'Morytania' in text:
        return 'm'
    if 'Desert' in text:
        return 'd'

    if base:
        raise Exception('Could not find a url')
    else:
        return ''


def generate():
    # UPDATE THESE LINES
    task_source = echoes_initial
    # Set True if creating a list of possible tasks,
    # False if creating the actual/final Leagues 5 list
    only_create_missing_tasks = False
    tasks = []
    for task_data in task_source:
        region = parse_region(task_data[0], base=True)
        points = int(task_data[4].strip())
        other_regions = parse_region(task_data[3], base=False)
        tasks.append(Task(
            name=task_data[1].replace("'", "").replace(" ", ""),
            area=region,
            description=task_data[2].replace("'", "").replace(" ", ""),
            points=points,
            regions=region if region or not other_regions else '**fixme**'
        ))

    missing_tasks, is_new = update_with_known_tasks(tasks, return_unknown_only=only_create_missing_tasks)

    # used if we want to update the master list with new tasks we learn about, without duplicating
    if only_create_missing_tasks:
        for task in missing_tasks:
            print(f'{task},')
    else:
        for task, is_new_status in zip(tasks, is_new):
            print(f'{task},{"  # New!" if is_new_status else ""}')


if __name__ == '__main__':
    generate()
