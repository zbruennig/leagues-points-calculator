from typing import List

from classes import Regions


def get_region_combos() -> List[Regions]:
    combinations = []
    regions = ['v', 'z', 't', 'k', 'a', 'f', 'w', 'd', 'm']
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
