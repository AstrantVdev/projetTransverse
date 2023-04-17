import Buttons
import Main
import Scenes
import UserInterfaces


def loadMap(mapname):
    scene = None
    match mapname:
        case "map1":
            scene = (
                Scenes.Scene(mapname)
                .addEntity(
                    Main.Player()
                    .setX(700)
                    .setY(0)

                )
                .addUserInterface(
                    UserInterfaces.UserInterface("menu")
                    .addButton(
                        Buttons.Quit
                    )
                )
            )
        case "map2":
            scene = (
                Scenes.Scene(mapname)
                .addEntity(
                    Main.Player()
                    .setX(700)
                    .setY(0)

                )
                .addUserInterface(
                    UserInterfaces.UserInterface("menu")
                    .addButton(
                        Buttons.Quit
                    )
                )
            )
    return scene

