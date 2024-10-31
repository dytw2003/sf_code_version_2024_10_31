import asyncio
from md.mnsf import mn_signal


async def ctrl_open_full(var, gpio, o_pin, cl_pin, mtr_time, o_flag, o_flg_n, cl_flg_n, indi):

    if not o_flag:
        # First OFF the OPPOSITE pin(CLOSE)
        gpio.turn_off_pins(cl_pin)  # OFF the close pin
        # setattr(var, cl_pin, "OFF")
        setattr(var, cl_flg_n, False)  # CLOSE o_flag False
        # ON the OPEN
        gpio.turn_on_pins(o_pin)
        setattr(var, indi, "OPEN")
        # setattr(var, o_pin, "ON")
        await asyncio.sleep(mtr_time)
        gpio.turn_off_pins(o_pin)
        # setattr(var, o_flg_n, True)  # OPEN o_flag True
    else:
        print(f"OPEN o_FLAG IS TRUE:{o_flag}")


async def ctrl_close_full(var, gpio, o_pin, cl_pin, mtr_time, cl_flag, o_flg_n, cl_flg_n, indi):
    if not cl_flag:
        # First OFF the OPPOSITE pin(open)
        gpio.turn_off_pins(o_pin)  # OFF the open pin
        # setattr(var, o_pin, "OFF")
        setattr(var, o_flg_n, False)  # OPEN cl_flag False
        # ON the OPEN
        gpio.turn_on_pins(cl_pin)
        setattr(var, indi, "CLOSED")
        # setattr(var, cl_pin, "ON")
        await asyncio.sleep(mtr_time)
        gpio.turn_off_pins(cl_pin)
        # setattr(var, cl_flg_n, True)  # CLOSE cl_flag True

    else:
        print(f"OPEN cl_FLAG IS TRUE:{cl_flag}")


async def handle_time_based_control_full(var, gpio, o_pin, cl_pin, mtr_time, o_time, cl_time, c_time, cl_flag, o_flag, o_flg_n, cl_flg_n, indi):

    if o_time < cl_time:
        if o_time <= c_time < cl_time:
            print(f"[DEBUG] Current time is within open interval. Opening motor.")
            await ctrl_open_full(var, gpio, o_pin, cl_pin, mtr_time, o_flag, o_flg_n, cl_flg_n, indi)
        elif c_time >= cl_time:
            print(f"[DEBUG] Current time has passed close interval. Closing motor.")
            await ctrl_close_full(var, gpio, o_pin, cl_pin, mtr_time, cl_flag, o_flg_n, cl_flg_n, indi)
    else:
        if cl_time <= c_time < o_time:
            print(
                f"[DEBUG] Current time is within close-first interval. Closing motor.")
            await ctrl_close_full(var, gpio, o_pin, cl_pin, mtr_time, cl_flag, o_flg_n, cl_flg_n, indi)
        elif c_time >= o_time:
            print(f"[DEBUG] Current time has passed open interval. Opening motor.")
            await ctrl_open_full(var, gpio, o_pin, cl_pin, mtr_time, o_flag, o_flg_n, cl_flg_n, indi)


# ==========================================================================  STEP BY STEP FUNCTION CLOSE AND OPEN
async def ctrl_open_stp(var, gpio, o_pin, cl_pin, mtr_time, o_flag, o_flg_n, cl_flg_n, run_fst, mtr_wait_time, indi):

    if not o_flag:
        gpio.turn_off_pins(cl_pin)
        setattr(var, cl_flg_n, False)  # Set close flag to False
        # setattr(var, cl_pin, "OFF")  # Set open flag to True
        gpio.turn_on_pins(o_pin)
        # setattr(var, o_pin, "ON")
        setattr(var, indi, "OPEN")  # Set open flag to True
        await asyncio.sleep(run_fst)
        gpio.turn_off_pins(o_pin)
        # setattr(var, o_pin, "OFF")
        await asyncio.sleep(mtr_wait_time)

    else:
        print(f"[DEBUG] OPEN FLAG IS TRUE: Motor {
              o_pin} is prevented from opening due to flag")


# Function to control the "close" operation of the motor in a step-by-step manner
async def ctrl_close_stp(var, gpio, o_pin, cl_pin, mtr_time, cl_flag, o_flg_n, cl_flg_n, run_fst, mtr_wait_time, indi):

    if not cl_flag:
        gpio.turn_off_pins(o_pin)
        setattr(var, o_flg_n, False)  # Set open flag to False
        # setattr(var, o_pin, "OFF")
        gpio.turn_on_pins(cl_pin)
        # setattr(var, cl_pin, "ON")
        setattr(var, indi, "CLOSED")
        await asyncio.sleep(run_fst)
        gpio.turn_off_pins(cl_pin)

        await asyncio.sleep(mtr_wait_time)
    else:
        print(f"[DEBUG] CLOSE FLAG IS TRUE: Motor {
              cl_pin} is prevented from closing due to flag")


async def sw_cw_rn_control(var, gpio, o_pin, cl_pin, mtr_time, temp_thresh, env_in_temp_r, env_in_temp, rain_max, rain, c_hour, c_min, o_hour, o_min, cl_hour, cl_min, at_btn, pin_btn, cl_flag, o_flag, cl_flg_n, o_flg_n, indi, pin_am_flg, pin_am_flg_n, slt_swtch):

    c_time = (c_hour, c_min)
    o_time = (o_hour, o_min)
    cl_time = (cl_hour, cl_min)
    run_fst = 10
    mtr_wait_time = 60

    if slt_swtch == "at":
        if at_btn == "ON":
            setattr(var, pin_am_flg_n, False)
            if pin_btn == "ON":
                if int(rain) == 1 and int(env_in_temp) > (int(rain_max)):
                    print("Raining but -- Max Temperature is reached")
                    # OPEN THE DOOR
                    await ctrl_open_stp(var, gpio, o_pin, cl_pin, mtr_time, o_flag, o_flg_n, cl_flg_n, run_fst, mtr_wait_time, indi)
                elif int(rain) == 1 and int(env_in_temp_r) < (int(rain_max)-1):
                    print("Min Temperature is reached---- Rain deteced")
                    # CLOSE THE DOOR
                    # ----------------------RAINING CLOSE THE DOOR FULL
                    await ctrl_close_full(var, gpio, o_pin, cl_pin, mtr_time, cl_flag, o_flg_n, cl_flg_n,indi)
                else:
                    if temp_thresh == 0:
                        if o_time != (0, 0) and cl_time != (0, 0):
                            print(f"[DEBUG] -------------Time-only control")
                            await handle_time_based_control_full(var, gpio, o_pin, cl_pin, mtr_time, o_time, cl_time, c_time, cl_flag, o_flag, o_flg_n, cl_flg_n, indi)
                        else:
                            print(
                                f"[DEBUG] ------------NONE OF THE VALUES ARE SETED")
                    if temp_thresh > 0:
                        if env_in_temp is not None:
                            if o_time != (0, 0) and cl_time != (0, 0):
                                # IF THE OPEN TIME IS LESS THEN CLOSE TIME
                                if o_time <= c_time <= cl_time:
                                    print(
                                        "IN between the time ------------interval")
                                    if env_in_temp > (int(temp_thresh)):      # OPEN
                                        print("-OPENING THE DOOR")
                                        await ctrl_open_stp(var, gpio, o_pin, cl_pin, mtr_time, o_flag, o_flg_n, cl_flg_n, run_fst, mtr_wait_time, indi)
                                    # CLOSE
                                    elif env_in_temp < (int(temp_thresh)):
                                        print("--CLOSING THE DOOR")
                                        await ctrl_close_stp(var, gpio, o_pin, cl_pin, mtr_time, cl_flag, o_flg_n, cl_flg_n, run_fst, mtr_wait_time, indi)
                                    # Track close time if not equal to 23
                                # elif cl_s1_h != 23 and cl_s2_h != 23 and cl_s3_h != 23 and cl_s4_h != 23 and cl_s5_h != 23 and cl_s6_h != 23:
                                #     print("All settings are not set to 23, closing the door")
                                else:
                                    print("Not in the time Interval")

                            elif temp_thresh > 0 and o_time == (0, 0) and cl_time == (0, 0):
                                print(f"[DEBUG] ----------------------Temperature-only control: env_temp={
                                    env_in_temp}, threshold={temp_thresh}")
                                if env_in_temp > temp_thresh:
                                    await ctrl_open_stp(var, gpio, o_pin, cl_pin, mtr_time, o_flag, o_flg_n, cl_flg_n, run_fst, mtr_wait_time, indi)
                                elif env_in_temp < temp_thresh:
                                    await ctrl_close_stp(var, gpio, o_pin, cl_pin, mtr_time, cl_flag, o_flg_n, cl_flg_n, run_fst, mtr_wait_time, indi)
                            else:
                                print(
                                    "---None of the task perform------no conditon matched ")
                        else:
                            print(f"sensor not working for the {
                                env_in_temp}")
                    else:
                        print(
                            "[DEBUG] Set values are missing; please configure settings.")

            elif pin_btn == "OFF":
                print(f"[DEBUG]--CURRENT ACTUATOR PIN OFF: {pin_btn}")
                gpio.turn_off_pins(o_pin)
                gpio.turn_off_pins(cl_pin)
                setattr(var, o_flg_n, False)  # Set open flag to False
                setattr(var, cl_flg_n, False)  # Set open flag to False

        elif at_btn == "OFF" and not pin_am_flg:
            print(f"[DEBUG] Web Auto mode OFF: {at_btn}")
            gpio.turn_off_pins(o_pin)
            gpio.turn_off_pins(cl_pin)
            setattr(var, pin_am_flg_n, True)  # Set open flag to False
            setattr(var, o_flg_n, False)  # Set open flag to False
            setattr(var, cl_flg_n, False)  # Set open flag to False

    elif slt_swtch == "mn":
        print(f"[DEBUG] Manual mode active: {slt_swtch}")
        await mn_signal(gpio, var)


# =============================== ===============================================================================================  NO--RAIN -- 2nd and 3rd floor
# Main control function for the motor based on conditions
async def sw_cw_of_control(var, gpio, o_pin, cl_pin, mtr_time, temp_thresh, env_in_temp_r, env_in_temp, rain_max, rain, c_hour, c_min, o_hour, o_min, cl_hour, cl_min, at_btn, pin_btn, cl_flag, o_flag, cl_flg_n, o_flg_n, indi, pin_am_flg, pin_am_flg_n, slt_swtch):

    c_time = (c_hour, c_min)
    o_time = (o_hour, o_min)
    cl_time = (cl_hour, cl_min)
    run_fst = 10
    mtr_wait_time = 60
    if slt_swtch == "at":
        if at_btn == "ON":
            setattr(var, pin_am_flg_n, False)
            if pin_btn == "ON":
                # Condition 1: Temperature threshold only
                if temp_thresh == 0:
                    if o_time != (0, 0) and cl_time != (0, 0):
                        print(f"[DEBUG] -------------Time-only control")
                        await handle_time_based_control_full(var, gpio, o_pin, cl_pin, mtr_time, o_time, cl_time, c_time, cl_flag, o_flag, o_flg_n, cl_flg_n, indi)
                    else:
                        print(
                            f"[DEBUG] ------------NONE OF THE VALUES ARE SETED")
                if temp_thresh > 0:
                    if env_in_temp is not None:
                        if o_time != (0, 0) and cl_time != (0, 0):
                            # IF THE OPEN TIME IS LESS THEN CLOSE TIME
                            if o_time <= c_time <= cl_time:
                                print(
                                    "IN between the time ------------interval")
                                if env_in_temp > (int(temp_thresh)):      # OPEN
                                    print("-OPENING THE DOOR")
                                    await ctrl_open_stp(var, gpio, o_pin, cl_pin, mtr_time, o_flag, o_flg_n, cl_flg_n, run_fst, mtr_wait_time, indi)
                                # CLOSE
                                elif env_in_temp < (int(temp_thresh)):
                                    print("--CLOSING THE DOOR")
                                    await ctrl_close_stp(var, gpio, o_pin, cl_pin, mtr_time, cl_flag, o_flg_n, cl_flg_n, run_fst, mtr_wait_time, indi)
                            else:
                                print("not with in the - time interval ")

                        elif temp_thresh > 0 and o_time == (0, 0) and cl_time == (0, 0):
                            print(f"[DEBUG] ----------------------Temperature-only control: env_temp={
                                env_in_temp}, threshold={temp_thresh}")
                            if env_in_temp > temp_thresh:
                                await ctrl_open_stp(var, gpio, o_pin, cl_pin, mtr_time, o_flag, o_flg_n, cl_flg_n, run_fst, mtr_wait_time, indi)
                            elif env_in_temp < temp_thresh:
                                await ctrl_close_stp(var, gpio, o_pin, cl_pin, mtr_time, cl_flag, o_flg_n, cl_flg_n, run_fst, mtr_wait_time, indi)
                        else:
                            print(
                                "---None of the task perform------no conditon matched ")
                    else:
                        print(f"sensor not working for the {
                            env_in_temp}")
                else:
                    print(
                        "[DEBUG] Set values are missing; please configure settings.")

            elif pin_btn == "OFF":

                print(f"[DEBUG]--CURRENT ACTUATOR PIN OFF: {pin_btn}")
                gpio.turn_off_pins(o_pin)
                gpio.turn_off_pins(cl_pin)

                setattr(var, o_flg_n, False)  # Set open flag to False
                setattr(var, cl_flg_n, False)  # Set open flag to False

        elif at_btn == "OFF" and not pin_am_flg:
            print(f"[DEBUG] Web Auto mode OFF: {at_btn}")
            gpio.turn_off_pins(o_pin)
            gpio.turn_off_pins(cl_pin)
            setattr(var, pin_am_flg_n, True)  # Set open flag to False
            setattr(var, o_flg_n, False)  # Set open flag to False
            setattr(var, cl_flg_n, False)  # Set open flag to False

    elif slt_swtch == "mn":
        print(f"[DEBUG] Manual mode active: {slt_swtch}")
        await mn_signal(gpio, var)


# =======================================================================================================    curtain.


async def bc_of_control(var, gpio, o_pin, cl_pin, mtr_time, temp_thresh, env_in_temp, c_hour, c_min, o_hour, o_min, cl_hour, cl_min, at_btn, pin_btn, cl_flag, o_flag, cl_flg_n, o_flg_n, indi, pin_am_flg, pin_am_flg_n, slt_swtch):

    c_time = (c_hour, c_min)
    o_time = (o_hour, o_min)
    cl_time = (cl_hour, cl_min)
    if slt_swtch == "at":
        if at_btn == "ON":
            setattr(var, pin_am_flg_n, False)
            if pin_btn == "ON":
                if temp_thresh == 0:
                    if o_time != (0, 0) and cl_time != (0, 0):
                        print(f"[DEBUG] -------------Time-only control")
                        await handle_time_based_control_full(var, gpio, o_pin, cl_pin, mtr_time, o_time, cl_time, c_time, cl_flag, o_flag, o_flg_n, cl_flg_n, indi)
                    else:
                        print(
                            f"[DEBUG] ------------NONE OF THE VALUES ARE SETED")
                if temp_thresh > 0:
                    if env_in_temp is not None:
                        if o_time != (0, 0) and cl_time != (0, 0):
                            # IF THE OPEN TIME IS LESS THEN CLOSE TIME
                            if o_time <= c_time <= cl_time:
                                print(
                                    "IN between the time ------------interval")
                                if env_in_temp > (int(temp_thresh)):      # OPEN
                                    print("-OPENING THE DOOR")
                                    await ctrl_open_full(var, gpio, o_pin, cl_pin, mtr_time, o_flag, o_flg_n, cl_flg_n, indi)
                                # CLOSE
                                elif env_in_temp < (int(temp_thresh)):
                                    print("--CLOSING THE DOOR")
                                    await ctrl_close_full(var, gpio, o_pin, cl_pin, mtr_time, cl_flag, o_flg_n, cl_flg_n, indi)
                            else:
                                print("not with in the - time interval ")

                        elif temp_thresh > 0 and o_time == (0, 0) and cl_time == (0, 0):
                            print(f"[DEBUG] ----------------------Temperature-only control: env_temp={
                                env_in_temp}, threshold={temp_thresh}")
                            if env_in_temp > temp_thresh:
                                await ctrl_open_full(var, gpio, o_pin, cl_pin, mtr_time, o_flag, o_flg_n, cl_flg_n, indi)
                            elif env_in_temp < temp_thresh:
                                await ctrl_close_full(var, gpio, o_pin, cl_pin, mtr_time, cl_flag, o_flg_n, cl_flg_n, indi)
                        else:
                            print(
                                "---None of the task perform------no conditon matched ")
                    else:
                        print(f"sensor not working for the {
                            env_in_temp}")
                else:
                    print(
                        "[DEBUG] Set values are missing; please configure settings.")

            elif pin_btn == "OFF":
                print(f"[DEBUG]--CURRENT ACTUATOR PIN OFF: {pin_btn}")
                gpio.turn_off_pins(o_pin)
                gpio.turn_off_pins(cl_pin)
                setattr(var, o_flg_n, False)  # Set open flag to False
                setattr(var, cl_flg_n, False)  # Set open flag to False

        elif at_btn == "OFF" and not pin_am_flg:
            print(f"[DEBUG] Web Auto mode OFF: {at_btn}")
            gpio.turn_off_pins(o_pin)
            gpio.turn_off_pins(cl_pin)
            setattr(var, pin_am_flg_n, True)  # Set open flag to False
            setattr(var, o_flg_n, False)  # Set open flag to False
            setattr(var, cl_flg_n, False)  # Set open flag to False

    elif slt_swtch == "mn":
        print(f"[DEBUG] Manual mode active: {slt_swtch}")
        await mn_signal(gpio, var)
