from classes import Task
from wiki_data import leagues_4

"""
rows = document.querySelectorAll('table.wikitable.lighttable > tbody > tr')
rows = Array.from(rows)
data = rows.map(row => [row.cells[0].childNodes[0].childNodes[0].childNodes[0].currentSrc, row.cells[2].innerText, row.cells[3].innerText, row.cells[4].innerText])
"""

def parse_region(text: str, base: bool):
    if 'Globe' in text:
        return ''
    if 'Misthalin' in text:
        return ''
    if 'Karamja' in text:
        return ''
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
    tasks = []
    for task_data in leagues_4:
        region = parse_region(task_data[0], base=True)
        points = int(task_data[3].strip())
        other_regions = parse_region(task_data[2], base=False)
        tasks.append(Task(
            description=task_data[1].replace("'", "").replace(" ", ""),
            points=points,
            regions='**FIXME**' if (other_regions and other_regions != region) else region
        ))

    for task in tasks:
        print(f'{task},')


if __name__ == '__main__':
    generate()
