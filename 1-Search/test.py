
"""
class GeoLocation:
    A latitude/longitude of a physical location on Earth.
    latitude: float
    longitude: float

    def __repr__(self):
        return f"{self.latitude},{self.longitude}"

Library = GeoLocation(1,2)
print(Library)
"""
"""
import heapq
from dataclasses import dataclass
from typing import Dict, Hashable, List, Optional, Tuple

class State:
    
    A State consists of a string `location` and (possibly null) `memory`.
    Note that `memory` must be a "Hashable" data type -- for example:
        - any non-mutable primitive (str, int, float, etc.)
        - tuples
        - nested combinations of the above

    As you implement different types of search problems throughout the assignment,
    think of what `memory` should contain to enable efficient search!
    
    location: str
    memory: Optional[Hashable] = None

class SearchProblem:
    # Return the start state.
    def startState(self) -> State:
        raise NotImplementedError("Override me")

    # Return whether `state` is an end state or not.
    def isEnd(self, state: State) -> bool:
        raise NotImplementedError("Override me")

    # Return a list of (action: str, state: State, cost: float) tuples corresponding to
    # the various edges coming out of `state`
    def successorsAndCosts(self, state: State) -> List[Tuple[str, State, float]]:
        raise NotImplementedError("Override me")

class ShortestPathProblem(SearchProblem):
    
    Defines a search problem that corresponds to finding the shortest path
    from `startLocation` to any location with the specified `endTag`.
    
#cityMap:CityMap
    def __init__(self, startLocation: str, endTag: str, cityMap: str):
        self.startLocation = startLocation
        self.endTag = endTag
        self.cityMap = cityMap

    def startState(self) -> State:
        # BEGIN_YOUR_CODE (our solution is 1 line of code, but don't worry if you deviate from this)
        Start_state = State()
        Start_state.location = self.startLocation
        return Start_state
        # END_YOUR_CODE
        raise Exception("Not implemented yet")
        # END_YOUR_CODE

x = ShortestPathProblem('abc', 'cde', 'fgh')
y = x.startState()
print(y.location)
print(type(x.startState()))
"""

"""
# x = tuple(0 for i in range(10))
# print(x)

x = (1,0,0)
print(any(x))

# 如果元组全0，则any返回False
"""

from util import State

location = "abc"
state = State(location)

aDict = {state:"xxx"}

for key, value in aDict.items():
    print(key)