import tcod

from engine import Engine
from entity import Entity
from procgen import generate_dungeon
from input_handlers import EventHandler


def main() -> None:
    # Define varaibles for screen size
    screen_width = 80
    screen_height = 50

    map_width = 80
    map_height = 45

    # Load image and break up using a tile format. This allows
    # you to grab individual sections of the image.
    tileset = tcod.tileset.load_tilesheet(
        "gameImages.png", 32, 8, tcod.tileset.CHARMAP_TCOD
    )

    event_handler = EventHandler()  # create an instance of the event handler class

    player = Entity(int(screen_width / 2), int(screen_height / 2), "@", (255, 255, 255))
    npc = Entity(int(screen_width / 2 - 5), int(screen_height / 2), "@", (255, 255, 0))
    entities = {npc, player}

    game_map = generate_dungeon(map_width, map_height)

    engine = Engine(
        entities=entities, event_handler=event_handler, game_map=game_map, player=player
    )

    # Create the screen
    with tcod.context.new_terminal(
        screen_width,
        screen_height,
        tileset=tileset,
        title="Rougelike Tutorial",
        vsync=True,
    ) as context:
        # Create a console to fill the screen
        root_console = tcod.Console(screen_width, screen_height, order="F")

        # create a "game loop" that continuously updates until we
        # exit the screen
        while True:

            # Tell the console to display an "@" sympol at position x,y
            engine.render(console=root_console, context=context)

            # Update the console
            events = tcod.event.wait()

            engine.handle_events(events)


if __name__ == "__main__":
    main()
