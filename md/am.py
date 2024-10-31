# am.py
from machine import Pin
import uasyncio as asyncio
pin_A1 = Pin('A1', Pin.IN)
# NEED TO CHANGE
     #_1
async def am_status(var):    
    while True:
    # selector switch status on variable
        slt_switch = pin_A1.value()
        if slt_switch == 0:           
            setattr(var,"auto_manual_1","at")
            setattr(var,"mnsig_flag_1", False)
            print(f"SELECTOR SWITCH Auto-----: {getattr(var,"auto_manual_1")}")            
        else:            
            setattr(var,"auto_manual_1","mn")            
            print(f"_SELECTOR SWITCH Manual----: {getattr(var,"auto_manual_1")}")
        await asyncio.sleep(1)

