#
# This file is part of the python-linux project
#
# Copyright (c) 2023 Tiago Coutinho
# Distributed under the GPLv3 license. See LICENSE for more info.

import pathlib

from .base import CEnum, run


HEADERS = [
    "/usr/include/linux/input.h",
    "/usr/include/linux/uinput.h",
    "/usr/include/linux/input-event-codes.h",
]


TEMPLATE = """\
#
# This file is part of the python-linux project
#
# Copyright (c) 2023 Tiago Coutinho
# Distributed under the GPLv3 license. See LICENSE for more info.

# This file has been generated by {name}
# Date: {date}
# System: {system}
# Release: {release}
# Version: {version}

import enum

from linuxpy.ioctl import IO as _IO, IOR as _IOR, IOW as _IOW, IOWR as _IOWR
from linuxpy.ctypes import u8, u16, i16, i64, cuint, cint, cchar, ccharp
from linuxpy.ctypes import Struct, Union, POINTER, timeval


{enums_body}


{structs_body}


{iocs_body}"""


this_dir = pathlib.Path(__file__).parent


class IOCEnum(CEnum):
    def add_item(self, name, value):
        value = value.replace("UINPUT_IOCTL_BASE", '"U"')
        super().add_item(name, value)


# macros from #define statements
MACRO_ENUMS = [
    IOCEnum("UIOC", "UI_", filter=lambda _, value: "_IO" not in value),
    CEnum("Property", "INPUT_PROP_"),
    CEnum(
        "EventType",
        "EV_",
        filter=lambda name, _: name not in {"EV_VERSION", "EV_UINPUT"},
    ),
    CEnum("Key", ["KEY_", "BTN_"], with_prefix=True),
    CEnum("Relative", "REL_"),
    CEnum("Absolute", "ABS_"),
    CEnum("Miscelaneous", "MSC_"),
    CEnum("Synchronization", "SYN_"),
    CEnum("Led", "LED_"),
    CEnum("ID", "ID_"),
    CEnum("Bus", "BUS_"),
    CEnum("MultiTouch", "MT_TOOL_"),
    CEnum("ForceFeedbackStatus", "FF_STATUS_"),
    CEnum("ForceFeedback", "FF_"),
    CEnum("UIForceFeedback", "UI_FF_"),
    CEnum("Sound", "SND_"),
    CEnum("Switch", "SW_"),
    CEnum("AutoRepeat", "REP_"),
    # IOC values are too complex to generate for now
    # CEnum("IOC", "EVIOC")
]


def main(output=this_dir.parent / "input" / "raw.py"):
    run(__name__, HEADERS, TEMPLATE, MACRO_ENUMS, output=output)


if __name__ == "__main__":
    main()
