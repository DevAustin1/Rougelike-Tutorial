from typing import Optional # part of pythons type hinting. Optional denotes somthing that could be set to None

import tcod.event # imports tcods event system

from actions import Action, EscapeAction, MovementAction

class EventHandler(tcod.event.EventDispatch[Action]): # create new class that is a subclass of tcods eventDispatch class. useful because they already define all events/key presses
    
    def ev_quit(self, event: tcod.event.Quit) -> Optional[Action]: # override og ev_quit so the screen exits instead of printing a messaage
        raise SystemExit()
    
    def ev_keydown(self, event: tcod.event.KeyDown) -> Optional[Action]: # receive key presses and return an action or none (optional[Action])
        action: Optional[Action] = None # action is the variable that holds a specific subclass of Action. If no valid key is pressed it will stay as none.
        
        key = event.sym # key records the actual key that is pressed
        
        # check list of possible keys to be pressed
        if key == tcod.event.K_UP:
            action = MovementAction(dx=0, dy=-1)
        elif key == tcod.event.K_DOWN:
            action = MovementAction(dx=0, dy=1)
        elif key == tcod.event.K_LEFT:
            action = MovementAction(dx=-1, dy=0)
        elif key == tcod.event.K_RIGHT:
            action = MovementAction(dx=1, dy=0)
            
        elif key == tcod.event.K_ESCAPE:
            action = EscapeAction()
            
        return action