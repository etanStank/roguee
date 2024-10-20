from __future__ import annotations

from typing import TYPE_CHECKING

from engine import Engine
from entity import Entity

if TYPE_CHECKING:
    from engine import Engine
    from entity import Entity

class Action:
    def preform(self, engine: Engine, entity: Entity) -> None:
        raise NotImplementedError()
    
class EscapeAction(Action):
    def preform(self, engine: Engine, entity: Entity) -> None:
        raise SystemExit()

class MovementAction(Action):
    def __int__(self, dx: int, dy: int):
        super().__init__()

        self.dx = dx
        self.dy = dy
    
    def preform(self, engine: Engine, entity: Entity) -> None:
        dest_x = entity.x + self.dx
        dest_y = entity.y + self.dy

        if not engine.game_map.in_bounds(dest_x, dest_y):
            return
        if not engine.game_map.tiles["walkable"][dest_x, dest_y]:
            return
    
        entity.move(self.dx, self.dy)