from pathlib import Path
from gui import MainWindow
from SwitchManager import SwitchManager

OUTPUT_PATH = Path(__file__).parent.parent.parent
ASSETS_PATH = OUTPUT_PATH / Path("assets/summary")


if __name__ == "__main__":
    switch_manager = SwitchManager(OUTPUT_PATH/Path("component"))
    main_window = MainWindow(switch_manager, ASSETS_PATH)
    main_window.run()
