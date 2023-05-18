from typing import List
import time
from tclrpc import TclException
from tclrpc import OpenOcdTclRpc

# --------------------------
# PM register offset
# --------------------------
PM_BASE_ADDRESS = 0x000050000

PM_Clk_AHB_Set_OFFSET = 0x0C
PM_Clk_APB_M_Set_OFFSET = 0x14
PM_Clk_APB_P_Set_OFFSET = 0x1C

# --------------------------
# PM register fields
# --------------------------
# AHB BUS
PM_CLOCK_CPU_S = 0
PM_CLOCK_CPU_M = (1 << PM_CLOCK_CPU_S)
PM_CLOCK_EEPROM_S = 1
PM_CLOCK_EEPROM_M = (1 << PM_CLOCK_EEPROM_S)
PM_CLOCK_RAM_S = 2
PM_CLOCK_RAM_M = (1 << PM_CLOCK_RAM_S)
PM_CLOCK_SPIFI_S = 3
PM_CLOCK_SPIFI_M = (1 << PM_CLOCK_SPIFI_S)
PM_CLOCK_TCB_S = 4
PM_CLOCK_TCB_M = (1 << PM_CLOCK_TCB_S)
PM_CLOCK_DMA_S = 5
PM_CLOCK_DMA_M = (1 << PM_CLOCK_DMA_S)
PM_CLOCK_CRYPTO_S = 6
PM_CLOCK_CRYPTO_M = (1 << PM_CLOCK_CRYPTO_S)
PM_CLOCK_CRC32_S = 7
PM_CLOCK_CRC32_M = (1 << PM_CLOCK_CRC32_S)

# APB M
PM_CLOCK_PM_S = 0
PM_CLOCK_PM_M = (1 << PM_CLOCK_PM_S)

# --------------------------
# WU register offset
# --------------------------
WU_BASE_ADDRESS = 0x00060000

WU_Clocks_OFFSET = 0x10

# --------------------------
# SPIFI register offset
# --------------------------
SPIFI_REGS_BASE_ADDRESS = 0x00070000

SPIFI_CONFIG_CTRL = SPIFI_REGS_BASE_ADDRESS + 0x000
SPIFI_CONFIG_CMD = SPIFI_REGS_BASE_ADDRESS + 0x004
SPIFI_CONFIG_ADDR = SPIFI_REGS_BASE_ADDRESS + 0x008
SPIFI_CONFIG_IDATA = SPIFI_REGS_BASE_ADDRESS + 0x00C
SPIFI_CONFIG_CLIMIT = SPIFI_REGS_BASE_ADDRESS + 0x010
SPIFI_CONFIG_DATA32 = SPIFI_REGS_BASE_ADDRESS + 0x014
SPIFI_CONFIG_MCMD = SPIFI_REGS_BASE_ADDRESS + 0x018
SPIFI_CONFIG_STAT = SPIFI_REGS_BASE_ADDRESS + 0x01C

# --------------------------
# SPIFI register fields
# --------------------------
# CTRL
SPIFI_CONFIG_CTRL_TIMEOUT_S = 0
SPIFI_CONFIG_CTRL_TIMEOUT_M = (0xFFFF << SPIFI_CONFIG_CTRL_TIMEOUT_S)


def SPIFI_CONFIG_CTRL_TIMEOUT(v):
    return (((v) << SPIFI_CONFIG_CTRL_TIMEOUT_S) & SPIFI_CONFIG_CTRL_TIMEOUT_M)


SPIFI_CONFIG_CTRL_CSHIGH_S = 16
SPIFI_CONFIG_CTRL_CSHIGH_M = (0xF << SPIFI_CONFIG_CTRL_CSHIGH_S)


def SPIFI_CONFIG_CTRL_CSHIGH(v):
    return (((v) << SPIFI_CONFIG_CTRL_CSHIGH_S) & SPIFI_CONFIG_CTRL_CSHIGH_M)


SPIFI_CONFIG_CTRL_CACHE_EN_S = 20
SPIFI_CONFIG_CTRL_CACHE_EN_M = (0x1 << SPIFI_CONFIG_CTRL_CACHE_EN_S)
SPIFI_CONFIG_CTRL_D_CACHE_DIS_S = 21
SPIFI_CONFIG_CTRL_D_CACHE_DIS_M = (0x1 << SPIFI_CONFIG_CTRL_D_CACHE_DIS_S)
SPIFI_CONFIG_CTRL_INTEN_S = 22
SPIFI_CONFIG_CTRL_INTEN_M = (0x1 << SPIFI_CONFIG_CTRL_INTEN_S)
SPIFI_CONFIG_CTRL_MODE3_S = 23
SPIFI_CONFIG_CTRL_MODE3_M = (0x1 << SPIFI_CONFIG_CTRL_MODE3_S)
SPIFI_CONFIG_CTRL_SCK_DIV_S = 24
SPIFI_CONFIG_CTRL_SCK_DIV_M = (0x7 << SPIFI_CONFIG_CTRL_SCK_DIV_S)


def SPIFI_CONFIG_CTRL_SCK_DIV(v):
    return (((v) << SPIFI_CONFIG_CTRL_SCK_DIV_S) & SPIFI_CONFIG_CTRL_SCK_DIV_M)


SPIFI_CONFIG_CTRL_PREFETCH_DIS_S = 27
SPIFI_CONFIG_CTRL_PREFETCH_DIS_M = (0x1 << SPIFI_CONFIG_CTRL_PREFETCH_DIS_S)
SPIFI_CONFIG_CTRL_DUAL_S = 28
SPIFI_CONFIG_CTRL_DUAL_M = (0x1 << SPIFI_CONFIG_CTRL_DUAL_S)
SPIFI_CONFIG_CTRL_RFCLK_S = 29
SPIFI_CONFIG_CTRL_RFCLK_M = (0x1 << SPIFI_CONFIG_CTRL_RFCLK_S)
SPIFI_CONFIG_CTRL_FBCLK_S = 30
SPIFI_CONFIG_CTRL_FBCLK_M = (0x1 << SPIFI_CONFIG_CTRL_FBCLK_S)
SPIFI_CONFIG_CTRL_DMAEN_S = 31
SPIFI_CONFIG_CTRL_DMAEN_M = (0x1 << SPIFI_CONFIG_CTRL_DMAEN_S)

# CMD
SPIFI_CONFIG_CMD_DATALEN_S = 0
SPIFI_CONFIG_CMD_DATALEN_M = (0x3FFF << SPIFI_CONFIG_CMD_DATALEN_S)


def SPIFI_CONFIG_CMD_DATALEN(v):
    return (((v) << SPIFI_CONFIG_CMD_DATALEN_S) & SPIFI_CONFIG_CMD_DATALEN_M)


SPIFI_CONFIG_CMD_POLL_S = 14
SPIFI_CONFIG_CMD_POLL_M = (0x1 << SPIFI_CONFIG_CMD_POLL_S)
SPIFI_CONFIG_CMD_DOUT_S = 15
SPIFI_CONFIG_CMD_DOUT_M = (0x1 << SPIFI_CONFIG_CMD_DOUT_S)
SPIFI_CONFIG_CMD_INTLEN_S = 16
SPIFI_CONFIG_CMD_INTLEN_M = (0x7 << SPIFI_CONFIG_CMD_INTLEN_S)
SPIFI_CONFIG_CMD_FIELDFORM_S = 19
SPIFI_CONFIG_CMD_FIELDFORM_M = (0x3 << SPIFI_CONFIG_CMD_FIELDFORM_S)
SPIFI_CONFIG_CMD_FRAMEFORM_S = 21
SPIFI_CONFIG_CMD_FRAMEFORM_M = (0x7 << SPIFI_CONFIG_CMD_FRAMEFORM_S)
SPIFI_CONFIG_CMD_OPCODE_S = 24
SPIFI_CONFIG_CMD_OPCODE_M = (0xFF << SPIFI_CONFIG_CMD_OPCODE_S)

SPIFI_CONFIG_CMD_DATALEN_BUSY_INDEX_S = 0
SPIFI_CONFIG_CMD_DATALEN_BUSY_DONE_VALUE_S = 3

SPIFI_CONFIG_CMD_FRAMEFORM_RESERVED = 0
SPIFI_CONFIG_CMD_FRAMEFORM_OPCODE_NOADDR = 1
SPIFI_CONFIG_CMD_FRAMEFORM_OPCODE_1ADDR = 2
SPIFI_CONFIG_CMD_FRAMEFORM_OPCODE_2ADDR = 3
SPIFI_CONFIG_CMD_FRAMEFORM_OPCODE_3ADDR = 4
SPIFI_CONFIG_CMD_FRAMEFORM_OPCODE_4ADDR = 5
SPIFI_CONFIG_CMD_FRAMEFORM_NOOPCODE_3ADDR = 6
SPIFI_CONFIG_CMD_FRAMEFORM_NOOPCODE_4ADDR = 7

SPIFI_CONFIG_CMD_FIELDFORM_ALL_SERIAL = 0
SPIFI_CONFIG_CMD_FIELDFORM_DATA_PARALLEL = 1
SPIFI_CONFIG_CMD_FIELDFORM_OPCODE_SERIAL = 2
SPIFI_CONFIG_CMD_FIELDFORM_ALL_PARALLEL = 3

# MCMD
SPIFI_CONFIG_MCMD_POLL_S = 14
SPIFI_CONFIG_MCMD_POLL_M = (0x1 << SPIFI_CONFIG_MCMD_POLL_S)
SPIFI_CONFIG_MCMD_DOUT_S = 15
SPIFI_CONFIG_MCMD_DOUT_M = (0x1 << SPIFI_CONFIG_MCMD_DOUT_S)
SPIFI_CONFIG_MCMD_INTLEN_S = 16
SPIFI_CONFIG_MCMD_INTLEN_M = (0x7 << SPIFI_CONFIG_MCMD_INTLEN_S)
SPIFI_CONFIG_MCMD_FIELDFORM_S = 19
SPIFI_CONFIG_MCMD_FIELDFORM_M = (0x3 << SPIFI_CONFIG_MCMD_FIELDFORM_S)
SPIFI_CONFIG_MCMD_FRAMEFORM_S = 21
SPIFI_CONFIG_MCMD_FRAMEFORM_M = (0x7 << SPIFI_CONFIG_MCMD_FRAMEFORM_S)
SPIFI_CONFIG_MCMD_OPCODE_S = 24
SPIFI_CONFIG_MCMD_OPCODE_M = (0xFF << SPIFI_CONFIG_MCMD_OPCODE_S)

# STATUS
SPIFI_CONFIG_STAT_MCINIT_S = 0
SPIFI_CONFIG_STAT_MCINIT_M = (0x1 << SPIFI_CONFIG_STAT_MCINIT_S)
SPIFI_CONFIG_STAT_CMD_S = 1
SPIFI_CONFIG_STAT_CMD_M = (0x1 << SPIFI_CONFIG_STAT_CMD_S)
SPIFI_CONFIG_STAT_RESET_S = 4
SPIFI_CONFIG_STAT_RESET_M = (0x1 << SPIFI_CONFIG_STAT_RESET_S)
SPIFI_CONFIG_STAT_INTRQ_S = 5
SPIFI_CONFIG_STAT_INTRQ_M = (0x1 << SPIFI_CONFIG_STAT_INTRQ_S)
SPIFI_CONFIG_STAT_VERSION_S = 24
SPIFI_CONFIG_STAT_VERSION_M = (0xFF << SPIFI_CONFIG_STAT_VERSION_S)

# --------------------------
# Commands
# --------------------------
SREG1_BUSY = 1

READ_SREG = 1
READ_LEN = 256
TIMEOUT = 100000

CHIP_ERASE_COMMAND = 0xC7

WRITE_ENABLE_COMMAND = 0x06
WRITE_DISABLE_COMMAND = 0x04

MEM_CONFIG_COMMAND = 0x61
MEM_CONFIG_VALUE = 0x7F

READ_DATA_COMMAND = 0x03
READ_SREG_COMMAND = 0x05

PAGE_PROGRAM_COMMAND = 0x02


def spifi_intrq_clear(openocd: OpenOcdTclRpc):
    openocd.write_word(SPIFI_CONFIG_STAT, openocd.read_word(SPIFI_CONFIG_STAT) |
                       SPIFI_CONFIG_STAT_INTRQ_M)


def spifi_init(openocd: OpenOcdTclRpc):
    print("MCU clock init...")

    openocd.write_word(WU_BASE_ADDRESS + WU_Clocks_OFFSET, 0x202)
    openocd.write_word(PM_BASE_ADDRESS + PM_Clk_APB_P_Set_OFFSET, 0xffffffff)
    openocd.write_word(PM_BASE_ADDRESS + PM_Clk_APB_M_Set_OFFSET, 0xffffffff)
    openocd.write_word(PM_BASE_ADDRESS + PM_Clk_AHB_Set_OFFSET, 0xffffffff)

    """
    *
    * STAT - регистр статуса
    * INTRQ - Запись «1» в бит сбрасывает запрос на прерывание от контроллера SPIFI
    * RESET - Бит предназначен для того, чтобы прервать текущую команду периферийного режима или режима памяти
    *
    * ADDR - Исполнительный адрес команды
    *
    * IDATA - регистр промежуточных данных
    *
    * CLIMIT - Верхний предел кэшируемой памяти
    *
    * CTRL - регистр управления
    * INTEN - Бит разрешения прерывания при завершении выполнения команды (если этот бит равен «1», то прерывание разрешено)
    *
    """
    openocd.write_word(SPIFI_CONFIG_STAT, openocd.read_word(SPIFI_CONFIG_STAT) |
                       SPIFI_CONFIG_STAT_INTRQ_M |
                       SPIFI_CONFIG_STAT_RESET_M)
    openocd.write_word(SPIFI_CONFIG_ADDR, 0x00)
    openocd.write_word(SPIFI_CONFIG_IDATA, 0x00)
    openocd.write_word(SPIFI_CONFIG_CLIMIT, 0x00)

    time.sleep(1)
    print("Finish init SPIFI")


def SPIFI_WaitIntrqTimeout(openocd: OpenOcdTclRpc, timeout: int) -> int:
    timeout_inner = timeout
    while timeout_inner:
        timeout_inner -= 1
        if (openocd.read_word(SPIFI_CONFIG_STAT) & SPIFI_CONFIG_STAT_INTRQ_M) != 0:
            return 1
    return 0


def spifi_wait_intrq_timeout(openocd: OpenOcdTclRpc, error_message: str):
    if SPIFI_WaitIntrqTimeout(openocd, TIMEOUT) == 0:
        raise Exception(error_message)
        return


def spifi_write_enable(openocd: OpenOcdTclRpc):
    """
    *
    * CMD  код операции
    * OPCODE - код операции
    * FRAMEFORM - Бит управления полями кода операции и адреса команды:
    * «0» – резерв;
    * «1» – выдается только код операции, адреса нет; (SPIFI_CONFIG_CMD_FRAMEFORM_OPCODE_NOADDR)
    * «2» – код операции и младший байт адреса;
    * «3» – код операции и два младших байта адреса;
    * «4» – код операции и три младших байта адреса;
    * «5» – код операции и 4 байта адреса;
    * «6» – нет кода операции, три младших байта адре-са;
    * «7» – нет кода операции, 4 байта адреса
    *
    * FIELDFORM - Формат вывода полей команды:
    * «0» – все поля выводятся в последовательном режиме; (SPIFI_CONFIG_CMD_FIELDFORM_ALL_SERIAL)
    * «1» – данные выводятся в четырех или двух битовом режиме, а остальные поля в последовательном режиме;
    * «2» – код операции выводится в последовательном режиме, а остальные в четырех или двух битовом;
    * «3» – все поля в четырех или двух битовом режиме
    *
    """
    print("Start write en")
    # spifi_intrq_clear(openocd)
    openocd.write_word(SPIFI_CONFIG_STAT, openocd.read_word(
        SPIFI_CONFIG_STAT) | SPIFI_CONFIG_STAT_INTRQ_M)
    openocd.write_word(SPIFI_CONFIG_CMD, (WRITE_ENABLE_COMMAND << SPIFI_CONFIG_CMD_OPCODE_S) |
                       (SPIFI_CONFIG_CMD_FRAMEFORM_OPCODE_NOADDR << SPIFI_CONFIG_CMD_FRAMEFORM_S) |
                       (SPIFI_CONFIG_CMD_FIELDFORM_ALL_SERIAL << SPIFI_CONFIG_CMD_FIELDFORM_S))
    spifi_wait_intrq_timeout(openocd, "Timeout executing write enable command")


def spifi_read_sreg_1(openocd: OpenOcdTclRpc) -> int:
    read_sreg: int = 0

    """
    *
    * CMD  код операции
    * OPCODE - код операции
    * FRAMEFORM - Бит управления полями кода операции и адреса команды:
    * «0» – резерв;
    * «1» – выдается только код операции, адреса нет; (SPIFI_CONFIG_CMD_FRAMEFORM_OPCODE_NOADDR)
    * «2» – код операции и младший байт адреса;
    * «3» – код операции и два младших байта адреса;
    * «4» – код операции и три младших байта адреса;
    * «5» – код операции и 4 байта адреса;
    * «6» – нет кода операции, три младших байта адре-са;
    * «7» – нет кода операции, 4 байта адреса
    *
    * FIELDFORM - Формат вывода полей команды:
    * «0» – все поля выводятся в последовательном режиме; (SPIFI_CONFIG_CMD_FIELDFORM_ALL_SERIAL)
    * «1» – данные выводятся в четырех или двух битовом режиме, а остальные поля в последовательном режиме;
    * «2» – код операции выводится в последовательном режиме, а остальные в четырех или двух битовом;
    * «3» – все поля в четырех или двух битовом режиме
    *
    """
    # spifi_intrq_clear(openocd)
    openocd.write_word(SPIFI_CONFIG_STAT, openocd.read_word(
        SPIFI_CONFIG_STAT) | SPIFI_CONFIG_STAT_INTRQ_M)
    openocd.write_word(SPIFI_CONFIG_CMD, (READ_SREG_COMMAND << SPIFI_CONFIG_CMD_OPCODE_S) |
                       (SPIFI_CONFIG_CMD_FRAMEFORM_OPCODE_NOADDR << SPIFI_CONFIG_CMD_FRAMEFORM_S) |
                       (SPIFI_CONFIG_CMD_FIELDFORM_ALL_SERIAL << SPIFI_CONFIG_CMD_FIELDFORM_S) |
                       (READ_SREG << SPIFI_CONFIG_CMD_DATALEN_S))
    spifi_wait_intrq_timeout(openocd, "Timeout executing read sreg1 command")
    return openocd.read_memory(SPIFI_CONFIG_DATA32, 8, 1)[0]


def spifi_wait_busy(openocd: OpenOcdTclRpc):
    print("Wait busy")
    while 1:
        sreg = spifi_read_sreg_1(openocd)
        if not (sreg & SREG1_BUSY):
            break


def spifi_chip_erase(openocd: OpenOcdTclRpc):
    print("Start erase")
    # spifi_intrq_clear(openocd)
    openocd.write_word(SPIFI_CONFIG_STAT, openocd.read_word(
        SPIFI_CONFIG_STAT) | SPIFI_CONFIG_STAT_INTRQ_M)
    openocd.write_word(SPIFI_CONFIG_CMD, (CHIP_ERASE_COMMAND << SPIFI_CONFIG_CMD_OPCODE_S) |
                       (SPIFI_CONFIG_CMD_FRAMEFORM_OPCODE_NOADDR << SPIFI_CONFIG_CMD_FRAMEFORM_S) |
                       (SPIFI_CONFIG_CMD_FIELDFORM_ALL_SERIAL << SPIFI_CONFIG_CMD_FIELDFORM_S))
    spifi_wait_intrq_timeout(openocd, "Timeout executing chip erase command")


def spifi_read_data(openocd: OpenOcdTclRpc, address: int, byte_count: int, bin_data: List[int]) -> int:
    print("read data")
    read_data: List[int] = []
    openocd.write_word(SPIFI_CONFIG_ADDR, address)

    """
    *
    * CMD  код операции
    * OPCODE - код операции
    * FRAMEFORM - Бит управления полями кода операции и адреса команды:
    * «0» – резерв;
    * «1» – выдается только код операции, адреса нет; (SPIFI_CONFIG_CMD_FRAMEFORM_OPCODE_NOADDR)
    * «2» – код операции и младший байт адреса;
    * «3» – код операции и два младших байта адреса;
    * «4» – код операции и три младших байта адреса;
    * «5» – код операции и 4 байта адреса;
    * «6» – нет кода операции, три младших байта адре-са;
    * «7» – нет кода операции, 4 байта адреса
    *
    * FIELDFORM - Формат вывода полей команды:
    * «0» – все поля выводятся в последовательном режиме; (SPIFI_CONFIG_CMD_FIELDFORM_ALL_SERIAL)
    * «1» – данные выводятся в четырех или двух битовом режиме, а остальные поля в последовательном режиме;
    * «2» – код операции выводится в последовательном режиме, а остальные в четырех или двух битовом;
    * «3» – все поля в четырех или двух битовом режиме
    *
    """
    spifi_intrq_clear(openocd)
    openocd.write_word(SPIFI_CONFIG_CMD, (READ_DATA_COMMAND << SPIFI_CONFIG_CMD_OPCODE_S) |
                       (SPIFI_CONFIG_CMD_FRAMEFORM_OPCODE_3ADDR << SPIFI_CONFIG_CMD_FRAMEFORM_S) |
                       (SPIFI_CONFIG_CMD_FIELDFORM_ALL_SERIAL << SPIFI_CONFIG_CMD_FIELDFORM_S) |
                       (byte_count << SPIFI_CONFIG_CMD_DATALEN_S))
    # spifi_wait_intrq_timeout(openocd, "Timeout executing read data command")
    for i in range(byte_count):
        data8 = openocd.read_memory(SPIFI_CONFIG_DATA32, 8, 1)[0]
        read_data.append(data8)
        # print(f"DATA[{i+address}] = {read_data[i]:#0x}")

    for i in range(byte_count):
        if read_data[i] != bin_data[address + i]:
            print(f"DATA[{i+address}] = {read_data[i]:#0x} - ошибка")
            return 1
    
    return 0


def spifi_page_program(openocd: OpenOcdTclRpc, ByteAddress: int, data: List[int], byte_count: int):
    if byte_count > 256:
        raise Exception("Byte count more than 256")

    print("Start page program")

    # spifi_intrq_clear(openocd)
    openocd.write_word(SPIFI_CONFIG_STAT, openocd.read_word(
        SPIFI_CONFIG_STAT) | SPIFI_CONFIG_STAT_INTRQ_M)
    openocd.write_word(SPIFI_CONFIG_ADDR, ByteAddress)
    openocd.write_word(SPIFI_CONFIG_IDATA, 0x00)
    openocd.write_word(SPIFI_CONFIG_CLIMIT, 0x00000000)
    openocd.write_word(SPIFI_CONFIG_CMD, (PAGE_PROGRAM_COMMAND << SPIFI_CONFIG_CMD_OPCODE_S) |
                       (SPIFI_CONFIG_CMD_FRAMEFORM_OPCODE_3ADDR << SPIFI_CONFIG_CMD_FRAMEFORM_S) |
                       (SPIFI_CONFIG_CMD_FIELDFORM_ALL_SERIAL << SPIFI_CONFIG_CMD_FIELDFORM_S) |
                       (0 << SPIFI_CONFIG_CMD_INTLEN_S) |
                       (1 << SPIFI_CONFIG_CMD_DOUT_S) |
                       (0 << SPIFI_CONFIG_CMD_POLL_S) |
                       (byte_count << SPIFI_CONFIG_CMD_DATALEN_S))
    for i in range(ByteAddress, ByteAddress + byte_count, 1):
        # openocd.write_word(SPIFI_CONFIG_DATA32, data[i+ByteAddress])
        # print(data[i])
        openocd.write_memory(SPIFI_CONFIG_DATA32, 8, [data[i]])
    # spifi_intrq_clear(openocd)
    openocd.write_word(SPIFI_CONFIG_STAT, openocd.read_word(
        SPIFI_CONFIG_STAT) | SPIFI_CONFIG_STAT_INTRQ_M)


def spifi_erase(openocd):
    spifi_write_enable(openocd)
    spifi_chip_erase(openocd)
    spifi_wait_busy(openocd)


def spifi_write(openocd: OpenOcdTclRpc, address: int, data: List[int], data_len: int):
    if data_len > 256:
        raise Exception("Byte count more than 256")

    spifi_write_enable(openocd)
    spifi_page_program(openocd, address, data, data_len)
    spifi_wait_busy(openocd)

    print("written")


def spifi_write_file(bytes: List[int], openocd: OpenOcdTclRpc, is_resume=True):
    """
    Write bytes in MIK32 External SPIFI Flash memory

    @bytes: list of bytes to write at offset 0x0

    TODO: implement setting byte array offset, add error handling, 
    improve progress visualisation
    """
    # print(bytes)
    print(f"Write {len(bytes)} bytes")
    
    openocd.halt()
    spifi_init(openocd)
    spifi_erase(openocd)
    print("bin_data_len = ", len(bytes))
    address = 0

    for address in range(0, len(bytes), 256):
        if ((address + 256) > len(bytes)):
            break
        print("address = ", address)
        spifi_write(openocd, address, bytes, 256)
        if spifi_read_data(openocd, address, 256, bytes) == 1:
            return 1

    if (len(bytes) % 256) != 0:
        print(
            f"address = {address}, +{len(bytes) - address-1}[{address + len(bytes) - address-1}]")
        spifi_write(openocd, address, bytes, len(bytes) - address)
        if spifi_read_data(openocd, address, len(bytes) - address, bytes) == 1:
            return 1
    print("end")
    if is_resume:
        openocd.resume(0)
    
    return 0