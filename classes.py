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
        w: bool = None   # wilderness
    ):
        self.map = {}
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


class Task:
    def __init__(
        self,
        name: str,
        area: str,  # Listed region that needs to be unlocked for any points
        description: str,
        points: int,
        regions: str = '',
        ca_count: int = 0,
        ca_points: int = 0,
        speed_tasks: int = 0
    ):
        self.name = name
        self.area = area
        self.description = description
        self.points = points
        self.regions = regions.lower()
        self.needed_regions = RegionTree(regions.lower())
        self.ca_tasks = ca_count or None
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

    def is_equivalent(self, other):
        # Equivalent for the purposes of requirements, not points or region locks
        # We'll use this to try to automatically populate as many tasks as possible
        return (
            isinstance(other, Task)
            and self.area == other.area
            and (
                self.description == other.description
                or self.name == other.name
            )
        )

    def __repr__(self):
        return f"Task('{self.name}', {chr(39)}{self.area}{chr(39)}, '{self.description}', {self.points}" \
               f"{f', {chr(39)}{self.regions}{chr(39)}' if self.regions else ''})"
