# mn_f.py
import uasyncio as asyncio  # Import asyncio at the top

# IMPORT FROM THE MANUAL
from md.mnsf import mn_signal
# changes for the other house
# _1"
## auto_manual_1

# DC CONTROL


async def mn_control_open(gpio, var, check, pin, motor_time, full_flag, auto_mode):
    e_pin = pin.split("_o_")[0]
    if var.auto_manual_1 == "at" and auto_mode != "ON":
        if check == "ON" and not full_flag:
            gpio.turn_off_pins(f"{e_pin}_c_1")
            setattr(var, f"{e_pin}_c_1", "OFF")            
            gpio.turn_on_pins(pin)
            print(f"GPIO {pin} turned ON")
        elif check == "OFF":
            gpio.turn_off_pins(pin)
            setattr(var, pin, "OFF")
            print(f"GPIO {pin} turned OFF")
    elif var.auto_manual_1 == "mn":
        print(f"Auto mode BTN{var.auto_manual_1} ")
        await mn_signal(gpio,var)

    else:
        print(f"Auto mode is -------{auto_mode}")


async def mn_control_close(gpio, var, check, pin, motor_time, full_flag, auto_mode):
    e_pin = pin.split("_c_")[0]
    if var.auto_manual_1 == "at" and auto_mode != "ON":
        if check == "ON" and not full_flag:
            gpio.turn_off_pins(f"{e_pin}_o_1")
            setattr(var, f"{e_pin}_o_1", "OFF")
            gpio.turn_on_pins(pin)
            print(f"GPIO {pin} turned ON")
        elif check == "OFF":
            gpio.turn_off_pins(pin)
            setattr(var, pin, "OFF")
            print(f"GPIO {pin} turned OFF")
    elif var.auto_manual_1 == "mn":
        print(f"Auto mode BTN{var.auto_manual_1} ")
        await mn_signal(gpio,var)

    else:
        print(f"Auto mode is -------{auto_mode}")

# AC CONTROL


async def control_ac_onoff(gpio, var, check, pin, auto_mode):
    if var.auto_manual_1 == "at" and auto_mode != "ON":
        if check == "ON":
            gpio.turn_on_pins(pin)
        elif check == "OFF":
            gpio.turn_off_pins(pin)
    elif var.auto_manual_1 == "mn":
        print(f"Auto mode BTN{var.auto_manual_1} ")
        await mn_signal(gpio,var)

    else:
        print(f"Auto mode is -------{auto_mode}")
