from collections import Iterable

import psutil

from common.model.info import Info
from common.model.service import Service
from common.utils.general import get_processes, parse_process, write_data, get_cpu_usage, get_memory, get_disks_usage, \
    _get_win_services
from common.utils.utils import object_to_json


def run():
    # Get Services
    win_services: Iterable = _get_win_services()
    services = []
    for win_service in win_services:
        services.append(_parse_service(_get_service_detail(win_service._name).as_dict()))

    # Get Processes
    win_processes = get_processes()
    processes = []
    for win_process in win_processes:
        if win_process is not None:
            processes.append(parse_process(win_process))

    # Process to json tree
    processes_json = []
    for process in processes:
        processes_json.append(object_to_json(process.__dict__))
    write_data("processes", object_to_json(processes_json))

    # Services to json tree
    services_json = []
    for service in services:
        services_json.append(object_to_json(service.__dict__))
    write_data("services", object_to_json(services_json))

    # Build de info object
    info = Info()
    info.set_cpu_usage(get_cpu_usage())
    info.set_memory(object_to_json(get_memory().__dict__))

    sys_disks = get_disks_usage()
    disks = []
    for sys_disk in sys_disks:
        disks.append(object_to_json(sys_disk.__dict__))
    info.set_disk(object_to_json(disks))

    write_data("general", object_to_json(info.__dict__))


# Parse Windows Service to own service Object
def _parse_service(service_to_parse) -> Service:
    service = Service()
    service.set_id(service_to_parse['pid'])
    service.set_name(service_to_parse['name'])
    service.set_display_name(service_to_parse['display_name'])
    service.set_status(service_to_parse['status'])
    service.set_start_type(service_to_parse['start_type'])
    service.set_description(service_to_parse['description'])
    return service


# Get detailed information of windows service
def _get_service_detail(service_name) -> object:
    return psutil.win_service_get(service_name)
