import configparser
import platform
import threading
import time

from common.utils.general import process_instructions
from common.utils.utils import win_map_net_drive, win_delete_net_drive
from core import windows, linux


def monitor(config: configparser):
    while True:
        refresh_rate = config.get("global", "refreshRate")
        # TODO CREAR LOG
        # print(datetime.now())
        if platform.system() == "Windows":
            windows.run()
        elif platform.system() == "Linux":
            linux.run()

        time.sleep(int(refresh_rate))


def manage(config: configparser):
    while True:
        # TODO CREAR LOG
        # print("Read Instruction" + str(datetime.now()))

        process_instructions()

        time.sleep(int(config.get("global", "instructionsRate")))


if __name__ == '__main__':
    main_config = configparser.ConfigParser()
    main_config.read("config/main.cfg")
    try:
        win_map_net_drive()
        threading.Thread(target=monitor, args=(main_config,)).start()
        threading.Thread(target=manage, args=(main_config,)).start()
    finally:
        win_delete_net_drive()
