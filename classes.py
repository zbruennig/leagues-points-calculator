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
        self.is_or = False
        self.is_singleton = True

        self.left = None
        self.right = None
        self.regions = None


        or_loc = expr.find('OR')
        if or_loc != -1:
            self.is_or = True
            # can't use split cause might be many ORs
            self.left = RegionTree(expr[0:or_loc].strip())
            self.right = RegionTree(expr[or_loc+2:].strip())
            return

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


class Task:
    def __init__(self, description: str, points: int, regions: str = ''):
        self.description = description
        self.points = points
        self.regions = regions
        self.needed_regions = RegionTree(regions)

    def is_possible_with(self, chosen_regions: Regions):
        return self.needed_regions.is_satisfied_by(chosen_regions)

    def __repr__(self):
        return f"Task('{self.description}', {self.points}{f', {chr(39)}{self.regions}{chr(39)}' if self.regions else ''})"

