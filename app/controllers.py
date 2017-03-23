import medioex
from medioex import do_write, di_read, ao_write, ai_read, temp_read


DO_DI_INIT = False
AI_INIT = False
AO_INIT = False
TEMP_INIT = False


def do_di_init():
    global DO_DI_INIT
    if not DO_DI_INIT:
        medioex.do_di_init()
        DO_DI_INIT = True


def ai_init():
    global AI_INIT
    if not AI_INIT:
        medioex.ai_init()
        AI_INIT = True


def ao_init():
    global AO_INIT
    if not AO_INIT:
        medioex.ao_init()
        AO_INIT = True


def temp_init():
    global TEMP_INIT
    if not TEMP_INIT:
        medioex.temp_init()
        TEMP_INIT = True
