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