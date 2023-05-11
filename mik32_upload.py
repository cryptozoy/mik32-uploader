import shlex
import argparse
import sys
import subprocess
import os
from enum import Enum
from typing import List, Tuple
from drivers.tclrpc import OpenOcdTclRpc
from drivers.mik32_eeprom import *
from drivers.mik32_spifi import *
from drivers.mik32_ram import *
from mik32_parsers import *


# class bcolors(Enum):
#     OK = '\033[92m'
#     WARNING = '\033[93m'
#     FAIL = '\033[91m'
#     ENDC = '\033[0m'
#     BOLD = '\033[1m'
#     UNDERLINE = '\033[4m'


DEFAULT_OPENOCD_EXEC_FILE_PATH = os.path.join("openocd", "bin", "openocd.exe")
DEFAULT_OPENOCD_SCRIPTS_PATH = os.path.join(
    "openocd", "share", "openocd", "scripts")

supported_formats = [".hex"]


def test_connection():
    output = ""
    with OpenOcdTclRpc() as openocd:
        output = openocd.run(f"capture \"reg\"")

    if output == "":
        raise Exception("ERROR: no regs found, check MCU connection")


@dataclass
class Segment:
    offset: int
    data: List[int]

def read_file(filename: str) -> List[Segment]:
    segments: List[Segment] = []
    lines: List[str] = []

    file_name, file_extension = os.path.splitext(filename)
    if file_extension in supported_formats:
        with open(filename) as f:
            lines = f.readlines()
    elif file_extension == ".bin":
        with open(filename, "rb") as f:
            contents = list(f.read())
            segments[0] = (0, contents)
    else:
        raise Exception("Unsupported file format: %s" % (file_extension))

    lba: int = 0        # Linear Base Address
    expect_address = 0  # Address of the next byte

    for line in lines:
        record: Record = parse_line(line, file_extension)
        if record.type == RecordType.DATA:
            drlo: int = record.address # Data Record Load Offset
            if segments.__len__() == 0:
                expect_address = lba+drlo
                segments.append(Segment(offset=expect_address, data=[]))
            if expect_address != lba+drlo:
                expect_address = lba+drlo
                segments.append(Segment(offset=expect_address, data=[]))
            
            for byte in record.data:
                segments[-1].data.append(byte)
                expect_address += 1
        elif record.type == RecordType.EXTADDR:
            lba = record.address
        elif record.type == RecordType.LINEARSTARTADDR:
            print("Start Linear Address:", record.address)


    return segments


def upload_file(filename: str, is_resume=True) -> int:
    """
    Write ihex or binary file into MIK32 EEPROM or external flash memory

    @filename: full path to the file with hex or bin file format
    @boot_source: boot source, eeprom, ram or spifi, define memory block mapped to boot memory area (0x0 offset)

    @return: return 0 if successful, 1 if failed

    TODO: Implement error handling
    """

    # print("Running OpenOCD...")

    # print(DEFAULT_OPENOCD_EXEC_FILE_PATH)
    # print(DEFAULT_OPENOCD_SCRIPTS_PATH)

    if not os.path.exists(filename):
        print("ERROR: File %s does not exist" % filename)
        exit(1)
    
    print(read_file(filename))

    # cmd = shlex.split("%s -s %s -f interface/ftdi/m-link.cfg -f target/mcu32.cfg" % (DEFAULT_OPENOCD_EXEC_FILE_PATH, DEFAULT_OPENOCD_SCRIPTS_PATH), posix=False)
    # with subprocess.Popen(cmd, shell=True, stdout=subprocess.DEVNULL) as proc:
    #     if boot_source == "eeprom":
    #         result = write_words(bytes2words(get_content(filename)))
    #     elif boot_source == "spifi":
    #         spifi_write_file(get_content(filename))
    #         result = 0 # TODO
    #     elif boot_source == "ram":
    #         write_file(filename)
    #         result = 0 # TODO
    #     else:
    #         raise Exception("Unsupported boot source, use eeprom or spifi")
    #         result = 1
    #     proc.kill()

    # if boot_source == "eeprom":
    #     result = write_words(bytes2words(get_content(filename)), is_resume)
    # elif boot_source == "spifi":
    #     result = spifi_write_file(get_content(filename), is_resume)
    # elif boot_source == "ram":
    #     write_file(filename, is_resume)
    #     result = 0  # TODO
    # else:
    #     raise Exception("Unsupported boot source, use eeprom or spifi")
    #     result = 1

    return 1


def createParser():
    parser = argparse.ArgumentParser()
    parser.add_argument('filepath', nargs='?')
    # parser.add_argument('-b', '--boot-mode', default='undefined')

    return parser


if __name__ == '__main__':
    parser = createParser()
    namespace = parser.parse_args()

    if namespace.filepath:
        upload_file(namespace.filepath)
    else:
        print("Nothing to upload")
