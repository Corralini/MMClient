import psutil

from common.utils.general import get_processes


def run():
    print("I am Linux")
    get_processes()


# Not tested
# TODO: TEST this!!!
def get_processes():
    for p in psutil.pids():
        print(p)
