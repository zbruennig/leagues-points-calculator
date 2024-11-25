import re

class Regions:
    def __init__(
        self,
        z: bool = None,  # zeah
        v: bool = None,  # varlamore
        t: bool = None,  # tirannwn
        k: bool = None,  # kandarin
        a: bool = None,  # asgarnia
        f: bool = None,  # fremmy
        d: bool = None,  # desert
        m: bool = None,  # morytania
        w: bool = None,  # wilderness
        s: bool = True,  # starter, misthalin and karamja
    ):
        self.map = {}
        if s:
            self.map['s'] = True
        if z:
            self.map['z'] = True
        if v:
            self.map['v'] = True
        if t:
            self.map['t'] = True
        if k:
            self.map['k'] = True
        if a:
            self.map['a'] = True
        if f:
            self.map['f'] = True
        if d:
            self.map['d'] = True
        if m:
            self.map['m'] = True
        if w:
            self.map['w'] = True

    def __repr__(self) -> str:
        return ''.join(list(self.map.keys()))


class RegionTree:
    def __init__(self, expr: str):
        expr = expr.lower()
        self.is_or = False
        self.is_singleton = True

        self.left = None
        self.right = None
        self.regions = None


        or_loc = expr.find('|')
        if or_loc != -1:
            self.is_or = True
            # can't use split cause might be many ORs
            self.left = RegionTree(expr[0:or_loc].strip())
            self.right = RegionTree(expr[or_loc+1:].strip())
        else:
            self.is_singleton = True
            self.regions = expr

    def is_satisfied_by(self, regions: Regions):
        if self.is_or:
            return (
                self.left.is_satisfied_by(regions) or
                self.right.is_satisfied_by(regions)
            )
        else:
            needed_regions = {r: True for r in self.regions}
            for chosen_region in regions.map.keys():
                if chosen_region in needed_regions:
                    del needed_regions[chosen_region]
            return not needed_regions

    @property
    def complexity(self) -> int:
        if self.is_or:
            return max(self.left.complexity, self.right.complexity)
        else:
            return len(self.regions.strip())

class Boss:
    def __init__(
        self,
        name: str,
        regions: str,
        tasks: int,
        points: int,
        speed_tasks: int = 0
    ):
        self.name = name
        self.regions = regions
        self.needed_regions = RegionTree(regions)
        self.tasks = tasks
        self.points = points
        self.speed_tasks = speed_tasks or 0

    def is_possible_with(self, chosen_regions: Regions):
        return self.needed_regions.is_satisfied_by(chosen_regions)


class BossCollection:
    def __init__(self):
        self.bosses = []
        self.total_tasks = 0
        self.total_points = 0
        self.total_speed_tasks = 0

    def add(self, boss: Boss):
        self.bosses.append(boss)
        self.total_tasks += boss.tasks
        self.total_points += boss.points
        self.total_speed_tasks += boss.speed_tasks

    def __repr__(self):
        return str({
            "ca_tasks": self.total_tasks,
            "ca_points": self.total_points,
            "speed": self.total_speed_tasks
        })


class Displayable:
    def __init__(self, name: str):
        self.name = name

    @property
    def display(self) -> str:
        return self.name


class Task(Displayable):
    def __init__(
        self,
        name: str,
        area: str,  # Listed region that needs to be unlocked for any points
        description: str,
        points: int,
        regions: str = '',
        ca_tasks: int = 0,
        ca_points: int = 0,
        speed_tasks: int = 0
    ):
        self.name = name
        self.area = area
        self.description = description
        self.points = points
        self.regions = regions.lower()
        self.needed_regions = RegionTree(regions.lower())
        self.ca_tasks = ca_tasks or None
        self.ca_points = ca_points or None
        self.speed_tasks = speed_tasks or None

    def is_possible_with(self, chosen_regions: Regions, bosses: BossCollection):
        if self.ca_tasks:
            return bosses.total_tasks >= self.ca_tasks
        elif self.ca_points:
            return bosses.total_points >= self.ca_points
        elif self.speed_tasks:
            return bosses.total_speed_tasks >= self.speed_tasks
        return self.needed_regions.is_satisfied_by(chosen_regions)

    def is_equivalent_to(self, other):
        # Equivalent for the purposes of requirements, not points or region locks
        # We'll use this to try to automatically populate as many tasks as possible

        this_name = self._prepare_for_comparison(self.name.lower())
        other_name = self._prepare_for_comparison(other.name.lower())
        this_desc = self._prepare_for_comparison(self.description.lower())
        other_desc = self._prepare_for_comparison(other.description.lower())
        return (
            isinstance(other, Task)
            # and self.area == other.area
            and (
                this_desc == other_desc
                or this_name == other_name
            )
        )

    def _prepare_for_comparison(self, phrase: str):
        return (
            re.sub('\d+', '#', phrase)
            .replace(" a ", " ")
            .replace(" an ", " ")
            .replace(" some ", " ")
            .replace(" the ", " ")
            .replace("craft", "create")
            .replace(".", "")
            .replace("'", "")
            .replace('"', '')
        )

    def __repr__(self):
        base = f"Task('{self.name}', {chr(39)}{self.area}{chr(39)}, '{self.description}', {self.points}" \
               f"{f', {chr(39)}{self.regions}{chr(39)}' if self.regions else ''}"
        if self.ca_points:
            representation = f"{base}, ca_points={self.ca_points})"
        elif self.ca_tasks:
            representation = f"{base}, ca_tasks={self.ca_tasks})"
        elif self.speed_tasks:
            representation = f"{base}, speed_tasks={self.speed_tasks})"
        else:
            representation = f"{base})"
        return representation

    def to_str(self) -> str:
        output = f"{self.area.upper() if self.area else 'All'}-{self.points}: {self.name}"
        if self.regions != self.area:
            output += f". Requires {self.regions.upper()}."

        return output

    def needs_many_regions(self) -> bool:
        return self.needed_regions.complexity > 1

    @property
    def is_complicated(self) -> bool:
        return self.needs_many_regions() or self.needed_regions.is_or or self.area != self.regions

    @property
    def is_starter(self) -> bool:
        return self.points <= 40 and self.area in ['', 's']

    @property
    def display(self) -> str:
        return f'{self.points}: {self.name}'


class Notice(Displayable):
    def __init__(self, note: str):
        self.name = note

    @property
    def display(self) -> str:
        return f'**{self.name}**'


class Header(Displayable):
    def __init__(self, header: str):
        self.name = header
    @property
    def display(self) -> str:
        return f'\n-{self.name.upper()}-'


class Banking(Displayable):
    def __init__(self, note: str):
        self.name = note

    @property
    def display(self) -> str:
        return f'$BANK {self.name}'
