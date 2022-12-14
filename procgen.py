from typing import Iterator, Tuple
import random

import tcod


from game_map import GameMap
import tile_types


class RectangluarRoom:
    def __init__(self, x: int, y: int, width: int, height: int):
        """take the provided x and y coordinates from top left corner, computes the bottom right corner based on the w and h parameters"""
        self.x1 = x
        self.y1 = y
        self.x2 = x + width
        self.y2 = y + height

    @property
    def center(self) -> Tuple[int, int]:
        """find center coordinates of room center"""
        center_x = int((self.x1 + self.x2) / 2)
        center_y = int((self.y1 + self.y2) / 2)

        return center_x, center_y

    @property
    def inner(self) -> Tuple[int, int]:
        """Return the inner area of this room as a 2D array index."""
        return slice(self.x1 + 1, self.x2), slice(self.y1 + 1, self.y2)



def tunnel_between(
    start: Tuple [int, int], end: Tuple[int, int]) -> Iterator[Tuple[int, int]]:
    """ Return an L-shaped tunnel between these two points."""
    x1, y1 = start
    x2, y2 = end
    if random.random() < 0.5: # 50% chance
        # move horzontally, then vertically.add()
        corner_x, corner_y = x2, y1
    else:
        # Move vertically, then horizontally.
        corner_x, corner_y = x1, y2

    # Generate the coordinates for this tunnel.
    for x, y in tcod.los.bresenham((x1, y1), (corner_x, corner_y)).tolist():
        yield x, y
    for x, y in tcod.los.bresenham((corner_x, corner_y), (x2, y2)).tolist():
        yield x, y

def generate_dungeon(map_width, map_height) -> GameMap:
    dungeon = GameMap(map_width, map_height)

    room_1 = RectangluarRoom(x=20, y=15, width=10, height=15)
    room_2 = RectangluarRoom(x=35, y=15, width=10, height=15)

    dungeon.tiles[room_1.inner] = tile_types.floor
    dungeon.tiles[room_2.inner] = tile_types.floor
    
    for x, y in tunnel_between(room_2.center, room_1.center):
       dungeon.tiles[x, y] = tile_types.floor

    return dungeon
