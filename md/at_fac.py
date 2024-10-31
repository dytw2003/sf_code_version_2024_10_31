import uasyncio as asyncio  # Import asyncio at the top
from md.mnsf import mn_signal
# Change For the Other House
# _1

from md.mnsf import mn_signal


# Helper function to turn a device on


async def turn_on_device(var, gpio, pin, indi, flag, flag_n):

    gpio.turn_on_pins(pin)
    setattr(var, indi, "RUN")
    # setattr(var, flag_n, True)
    print(f"Device ON: {pin}")

# Helper function to turn a device off


async def turn_off_device(var, gpio, pin, indi, flag, flag_n):

    gpio.turn_off_pins(pin)
    setattr(var, indi, "STOP")
    # setattr(var, flag_n, False)
    print(f"Device OFF: {pin}")


# -========================================================== FOG ON/OFF FUNCTION
async def turn_on_off_fog(var, gpio, pin, indi, run_time, stop_time):
    gpio.turn_on_pins(pin)
    setattr(var, indi, "RUN")
    await asyncio.sleep(run_time)
    gpio.turn_off_pins(pin)
    setattr(var, indi, "STOP")
    await asyncio.sleep(stop_time)


async def turn_off_fog(var, gpio, pin, indi):
    gpio.turn_off_pins(pin)
    setattr(var, indi, "STOP")


# Helper function to assign indicator based on pin name
def assign_indi(pin):
    pin_mapping = {
        "fegi_fan_1": "fegi_oc_1",
        "hongi_fan_1": "hongi_oc_1",
        "fog_valve_1": "fog_oc_1",
        "bogwangdong_1": "bog_oc_1",
        "co2_1": "co2_oc_1",
        "sumag_1": "sumag_oc_1",
        "nangbangi_1": "ngh_oc_1",
        "sp01_1": "sp01_oc_1"
    }
    return pin_mapping.get(pin, None)


# General function for threshold, time-based, or combined control
async def control_device(var, gpio, pin, indi, flag, flag_n, threshold, threshold_var, o_time, cl_time, c_time):

    # Only time-based operation
    if threshold == 0:
        if o_time <= c_time < cl_time:
            print("----------------TIME BASED ,,")
            await turn_on_device(var, gpio, pin, indi, flag, flag_n)
        else:
            await turn_off_device(var, gpio, pin, indi, flag, flag_n)
    elif threshold > 0:
        if threshold_var is not None:
            # Only threshold-based operation
            if o_time == cl_time == (0, 0):  # No specific time given
                if threshold_var > threshold:
                    print(f"-------------temperature greater {threshold_var}")
                    await turn_on_device(var, gpio, pin, indi, flag, flag_n)
                else:
                    print(f"-------------temperature less {threshold_var} ")
                    await turn_off_device(var, gpio, pin, indi, flag, flag_n)
            elif o_time <= c_time < cl_time and threshold_var > threshold:
                await turn_on_device(var, gpio, pin, indi, flag, flag_n)
            else:
                await turn_off_device(var, gpio, pin, indi, flag, flag_n)

        else:
            print(f"--------------sensor is not workin ::{threshold_var}")
    else:
        print(f"--------------ac ----- device contrl nont")


# Fan control function: supports temperature-only, time-only, or combined control
async def fan_ctrl_func(var, gpio, pin, flag, flag_n, temp_thresh, o_hour, o_min, cl_hour, cl_min, at_btn, pin_btn):
    indi = assign_indi(pin)
    c_time = (var.c_hour_1, var.c_min_1)
    o_time = (o_hour, o_min)
    cl_time = (cl_hour, cl_min)
    bog_temp_thresh=0

    if var.auto_manual_1 == "at":
        print("----------------AUTO MOD FAN CONTROL FUNCTION  mode active")
        if at_btn == "ON":
            setattr(var,flag_n, False)
            print("---------------WEB-AUTO --FAN CONTROL FUNCTION  mode active")
            if pin_btn == "ON":
                print("--------------PIN--- FAN CONTROL FUNCTION  mode active")
                await control_device(var, gpio, pin, indi, flag, flag_n, bog_temp_thresh, var.envin_temp_1, o_time, cl_time, c_time)
            elif at_btn == "OFF":
                await turn_off_device(var, gpio, pin, indi, flag, flag_n)
        elif at_btn == "OFF"  and not flag :            
            await turn_off_device(var, gpio, pin, indi, flag, flag_n)
            setattr(var,flag_n, True)
    elif var.auto_manual_1 == "mn":
        print("--------FAC------Manual mode active")
        await mn_signal(gpio, var)
















# Flashlight control function: supports light intensity-only, time-only, or combined control
async def sb_ctrl_func(var, gpio, pin, flag, flag_n, o_hour, o_min, cl_hour, cl_min, at_btn, pin_btn):
    indi = assign_indi(pin)
    c_time = (var.c_hour_1, var.c_min_1)
    o_time = (o_hour, o_min)
    cl_time = (cl_hour, cl_min)
    light_thresh = 0

    if var.auto_manual_1 == "at":
        if at_btn == "ON":
            setattr(var,flag_n, False)
            if pin_btn == "ON":
                await control_device(var, gpio, pin, indi, flag, flag_n, light_thresh, var.envin_solar_light_1, o_time, cl_time, c_time)
            elif pin_btn == "OFF":
                await turn_off_device(var, gpio, pin, indi, flag, flag_n)
        elif at_btn == "OFF"and not flag:
            await turn_off_device(var, gpio, pin, indi, flag, flag_n)
            setattr(var,flag_n, True)
    elif var.auto_manual_1 == "mn":
        print("Manual mode active")
        await mn_signal(gpio, var)


# # =========================================================================== FOG CONTROL FUNCTION

# # Fog control function: supports humidity-only, RUN TIME , STOP TIME

# # -----------------------NEED TO CORRECT
# async def fog_ctrl_func(var, gpio, pin, flag, flag_n, hum_thresh, run_time, stop_time, at_btn, pin_btn):
#     indi = assign_indi(pin)

#     if var.auto_manual_1 == "at" and at_btn == "ON" and pin_btn == "ON":
#         if hum_thresh > var.envin_humi_1:
#             await turn_on_off_fog(var, gpio, pin, indi, run_time, stop_time)
#         else:
#             await turn_off_fog(var, gpio, pin, indi)
#         # await control_device(var, gpio, pin, indi, flag, flag_n, hum_thresh, var.envin_humi_1, o_time, cl_time, c_time)
#     elif pin_btn == "OFF":
#         await turn_off_fog(var, gpio, pin, indi)
#     elif var.auto_manual_1 == "mn":
#         print("Manual mode active")
#         await mn_signal(gpio, var)

# # CO2 control function: supports CO2-only, time-only, or combined control


# async def co2_ctrl_func(var, gpio, pin, flag, flag_n, co2_thresh, min_temp, max_temp, at_btn, pin_btn):
#     indi = assign_indi(pin)
#     c_temp = var.envin_temp_1
#     if var.auto_manual_1 == "at" and at_btn == "ON" and pin_btn == "ON":
#         if min_temp < c_temp < max_temp:
#             if var.envin_co2_1 < co2_thresh:  # if not sufficent co2 ON the co2 Generator device
#                 await turn_on_device(var, gpio, pin, indi, flag, flag_n)
#             else:
#                 await turn_off_device(var, gpio, pin, indi, flag, flag_n)
#         else:
#             await turn_off_device(var, gpio, pin, indi, flag, flag_n)
#             print(f" Temperature is Either Low or High")
#     elif pin_btn == "OFF":
#         await turn_off_device(var, gpio, pin, indi, flag, flag_n)
#     elif var.auto_manual_1 == "mn":
#         print("Manual mode active")
#         await mn_signal(gpio, var)
