from md.mn_f import mn_control_open, mn_control_close, control_ac_onoff
import uasyncio as asyncio  # Import asyncio at the top

# arko house ko lagi change garda
# arko house ko lagi change garda
# DC ko lagi
# _1,
# _1',
# _1_flg
# _1)


# LEFT 
async def sd_control_left_1f(var, gpio):
    while True:
        # If you want these operations to be sequential:
        await mn_control_open(gpio, var, var.chuk_ch_1f_o_1, 'chuk_ch_1f_o_1', var.motor_1f_chuk_1, var.chuk_ch_1f_o_1_flg, var.chuk_1f_ato_man_1)
        await mn_control_close(gpio, var, var.chuk_ch_1f_c_1, 'chuk_ch_1f_c_1', var.motor_1f_chuk_1, var.chuk_ch_1f_c_1_flg, var.chuk_1f_ato_man_1)
        await asyncio.sleep(1)  # Small delay to prevent tight looping


async def sd_control_left_2f(var, gpio):
    while True:
        # If you want these operations to be sequential:
        await mn_control_open(gpio, var, var.chuk_ch_2f_o_1, 'chuk_ch_2f_o_1', var.motor_2f_chuk_1, var.chuk_ch_2f_o_1_flg, var.chuk_2f_ato_man_1)
        await mn_control_close(gpio, var, var.chuk_ch_2f_c_1, 'chuk_ch_2f_c_1', var.motor_2f_chuk_1, var.chuk_ch_2f_c_1_flg ,var.chuk_2f_ato_man_1)
        await asyncio.sleep(1)  # Small delay to prevent tight looping


async def sd_control_left_3f(var, gpio):
    while True:
        # If you want these operations to be sequential:
        await mn_control_open(gpio, var, var.chuk_ch_3f_o_1, 'chuk_ch_3f_o_1', var.motor_3f_chuk_1, var.chuk_ch_3f_o_1_flg, var.chuk_3f_ato_man_1)
        await mn_control_close(gpio, var, var.chuk_ch_3f_c_1, 'chuk_ch_3f_c_1', var.motor_3f_chuk_1, var.chuk_ch_3f_c_1_flg, var.chuk_3f_ato_man_1)
        await asyncio.sleep(1)  # Small delay to prevent tight looping
        #

# RIGHT
async def sd_control_right_1f(var, gpio):
    while True:
        # If you want these operations to be sequential:
        await mn_control_open(gpio, var, var.chuk_uu_1f_o_1, 'chuk_uu_1f_o_1', var.motor_1f_chuk_1, var.chuk_uu_1f_o_1_flg, var.chuk_1f_ato_man_1)
        await mn_control_close(gpio, var, var.chuk_uu_1f_c_1, 'chuk_uu_1f_c_1', var.motor_1f_chuk_1, var.chuk_uu_1f_c_1_flg, var.chuk_1f_ato_man_1)
        await asyncio.sleep(1)  # Small delay to prevent tight looping


async def sd_control_right_2f(var, gpio):
    while True:
        # If you want these operations to be sequential:
        await mn_control_open(gpio, var, var.chuk_uu_2f_o_1, 'chuk_uu_2f_o_1', var.motor_2f_chuk_1, var.chuk_uu_2f_o_1_flg, var.chuk_2f_ato_man_1)
        await mn_control_close(gpio, var, var.chuk_uu_2f_c_1, 'chuk_uu_2f_c_1', var.motor_2f_chuk_1, var.chuk_uu_2f_c_1_flg, var.chuk_2f_ato_man_1)
        await asyncio.sleep(1)  # Small delay to prevent tight looping


async def sd_control_right_3f(var, gpio):
    while True:

        # If you want these operations to be sequential:
        await mn_control_open(gpio, var, var.chuk_uu_3f_o_1, 'chuk_uu_3f_o_1', var.motor_3f_chuk_1, var.chuk_uu_3f_o_1_flg, var.chuk_3f_ato_man_1)
        await mn_control_close(gpio, var, var.chuk_uu_3f_c_1, 'chuk_uu_3f_c_1', var.motor_3f_chuk_1, var.chuk_uu_3f_c_1_flg, var.chuk_3f_ato_man_1)
        await asyncio.sleep(1)  # Small delay to prevent tight looping

# CHANJANG (CEILING WINDOWS{cw})
# chan_1f_ato_man_1
# chan_2f_ato_man_1
# chan_3f_ato_man_1

# LEFT 
async def cw_control_left_1f(var, gpio):
    while True:
        # If you want these operations to be sequential:
        await mn_control_open(gpio, var, var.chan_ch_1f_o_1, 'chan_ch_1f_o_1', var.motor_1f_chan_1, var.chan_ch_1f_o_1_flg, var.chan_1f_ato_man_1)
        await mn_control_close(gpio, var, var.chan_ch_1f_c_1, 'chan_ch_1f_c_1', var.motor_1f_chan_1, var.chan_ch_1f_c_1_flg, var.chan_1f_ato_man_1)
        await asyncio.sleep(1)  # Small delay to prevent tight looping


async def cw_control_left_2f(var, gpio):
    while True:
        # If you want these operations to be sequential:
        await mn_control_open(gpio, var, var.chan_ch_2f_o_1, 'chan_ch_2f_o_1', var.motor_2f_chan_1, var.chan_ch_2f_o_1_flg, var.chan_2f_ato_man_1)
        await mn_control_close(gpio, var, var.chan_ch_2f_c_1, 'chan_ch_2f_c_1', var.motor_2f_chan_1, var.chan_ch_2f_c_1_flg, var.chan_2f_ato_man_1)
        await asyncio.sleep(1)  # Small delay to prevent tight looping


async def cw_control_left_3f(var, gpio):
    while True:
        # If you want these operations to be sequential:
        await mn_control_open(gpio, var, var.chan_ch_3f_o_1, 'chan_ch_3f_o_1', var.motor_3f_chan_1, var.chan_ch_3f_o_1_flg, var.chan_3f_ato_man_1)
        await mn_control_close(gpio, var, var.chan_ch_3f_c_1, 'chan_ch_3f_c_1', var.motor_3f_chan_1, var.chan_ch_3f_c_1_flg, var.chan_3f_ato_man_1)
        await asyncio.sleep(1)  # Small delay to prevent tight looping
        #

# RIGHT 
async def cw_control_right_1f(var, gpio):
    while True:
        # If you want these operations to be sequential:
        await mn_control_open(gpio, var, var.chan_uu_1f_o_1, 'chan_uu_1f_o_1', var.motor_1f_chan_1, var.chan_uu_1f_o_1_flg, var.chan_1f_ato_man_1)
        await mn_control_close(gpio, var, var.chan_uu_1f_c_1, 'chan_uu_1f_c_1', var.motor_1f_chan_1, var.chan_uu_1f_c_1_flg, var.chan_1f_ato_man_1)
        await asyncio.sleep(1)  # Small delay to prevent tight looping


async def cw_control_right_2f(var, gpio):
    while True:
        # If you want these operations to be sequential:
        await mn_control_open(gpio, var, var.chan_uu_2f_o_1, 'chan_uu_2f_o_1', var.motor_2f_chan_1, var.chan_uu_2f_o_1_flg, var.chan_2f_ato_man_1)
        await mn_control_close(gpio, var, var.chan_uu_2f_c_1, 'chan_uu_2f_c_1', var.motor_2f_chan_1, var.chan_uu_2f_c_1_flg, var.chan_2f_ato_man_1)
        await asyncio.sleep(1)  # Small delay to prevent tight looping


async def cw_control_right_3f(var, gpio):
    while True:
        # If you want these operations to be sequential:
        await mn_control_open(gpio, var, var.chan_uu_3f_o_1, 'chan_uu_3f_o_1', var.motor_3f_chan_1, var.chan_uu_3f_o_1_flg, var.chan_3f_ato_man_1)
        await mn_control_close(gpio, var, var.chan_uu_3f_c_1, 'chan_uu_3f_c_1', var.motor_3f_chan_1, var.chan_uu_3f_c_1_flg, var.chan_3f_ato_man_1)
        await asyncio.sleep(1)  # Small delay to prevent tight looping

# FRONT WINDOWS
# fwbw_am_1
# FRONT

# # 1F
# async def fw_control_1f(var, gpio):
#     while True:

#         # If you want these operations to be sequential:
#         await mn_control_open(gpio, var, var.fw_o_1, 'fw_o_1', var.mfwbw_1, var.fw_o_1_flg, var.fwbw_am_1)
#         await mn_control_close(gpio, var, var.fw_c_1, 'fw_c_1', var.mfwbw_1, var.fw_c_1_flg, var.fwbw_am_1)
#         await asyncio.sleep(1)  # Small delay to prevent tight looping
# # BACK WINDOWS
# # fwbw_am_1
# async def bw_control_1f(var, gpio):
#     while True:

#         # If you want these operations to be sequential:
#         await mn_control_open(gpio, var, var.bw_o_1, 'bw_o_1', var.mfwbw_1, var.bw_o_1_flg, var.fwbw_am_1)
#         await mn_control_close(gpio, var, var.bw_c_1, 'bw_c_1', var.mfwbw_1, var.bw_c_1_flg, var.fwbw_am_1)
#         await asyncio.sleep(1)  # Small delay to prevent tight looping


# # 2F
# async def fw_control_2f(var, gpio):
#     while True:

#         # If you want these operations to be sequential:
#         await mn_control_open(gpio, var, var.fw_2f_o_1, 'fw_2f_o_1', var.mfwbw_1, var.fw_2f_o_1_flg, var.fwbw_2f_ato_man_2 )
#         await mn_control_close(gpio, var, var.fw_2f_c_1, 'fw_2f_c_1', var.mfwbw_1, var.fw_2f_c_1_flg, var.fwbw_2f_ato_man_2 )
#         await asyncio.sleep(1)  # Small delay to prevent tight looping
# # BACK WINDOWS
# # fwbw_am_1
# async def bw_control_2f(var, gpio):
#     while True:

#         # If you want these operations to be sequential:
#         await mn_control_open(gpio, var, var.bw_2f_o_1, 'bw_2f_o_1', var.mfwbw_1, var.bw_2f_o_1_flg, var.fwbw_2f_ato_man_2 )
#         await mn_control_close(gpio, var, var.bw_2f_c_1, 'bw_2f_c_1', var.mfwbw_1, var.bw_2f_c_1_flg, var.fwbw_2f_ato_man_2 )
#         await asyncio.sleep(1)  # Small delay to prevent tight looping

#  ============================================================================================================================

# bhc_1_ato_man_1
# bhc_2_ato_man_1
# bhc_3_ato_man_1
# bhc_4_ato_man_1
# bhc_5_ato_man_1
# bhc_6_ato_man_1
# bhc_7_ato_man_1
# bhc_8_ato_man_1
# bhc_9_ato_man_1
# bhc_10_ato_man_1
# bhc_11_ato_man_1
# bhc_12_ato_man_1


# BOHU CURTAIN 1
async def bc_control_1(var, gpio):
    while True:
        # if var.bhc_1_ato_man_1 != "ON":
        # If you want these operations to be sequential:
        await mn_control_open(gpio, var, var.bhc_1_o_1, 'bhc_1_o_1', var.motor_1f_bohu_1, var.bhc_1_o_1_flg,var.bhc_1_ato_man_1)
        await mn_control_close(gpio, var, var.bhc_1_c_1, 'bhc_1_c_1', var.motor_1f_bohu_1, var.bhc_1_c_1_flg,var.bhc_1_ato_man_1)
        await asyncio.sleep(1)  # Small delay to prevent tight looping
        # else:
     #   print(f"auto mode is ON-------{var.bhc_1_ato_man_1}")
# BOHU CURTAIN 2


async def bc_control_2(var, gpio):
    while True:
        # if var.bhc_2_ato_man_1 != "ON":
        # If you want these operations to be sequential:
        await mn_control_open(gpio, var, var.bhc_2_o_1, 'bhc_2_o_1', var.motor_2f_bohu_1, var.bhc_2_o_1_flg, var.bhc_2_ato_man_1)
        await mn_control_close(gpio, var, var.bhc_2_c_1, 'bhc_2_c_1', var.motor_2f_bohu_1, var.bhc_2_c_1_flg, var.bhc_2_ato_man_1)
        await asyncio.sleep(1)  # Small delay to prevent tight looping
        # else:
     #   print(f"auto mode is ON-------{var.bhc_2_ato_man_1}")
# BOHU CURTAIN 3


async def bc_control_3(var, gpio):
    while True:
        # if var.bhc_3_ato_man_1 != "ON":
        # If you want these operations to be sequential:
        await mn_control_open(gpio, var, var.bhc_3_o_1, 'bhc_3_o_1', var.motor_3f_bohu_1, var.bhc_3_o_1_flg,var.bhc_3_ato_man_1)
        await mn_control_close(gpio, var, var.bhc_3_c_1, 'bhc_3_c_1', var.motor_3f_bohu_1, var.bhc_3_c_1_flg,var.bhc_3_ato_man_1)
        await asyncio.sleep(1)  # Small delay to prevent tight looping
        # else:
     #   print(f"auto mode is ON-------{var.bhc_3_ato_man_1}")
# BOHU CURTAIN 4


async def bc_control_4(var, gpio):
    while True:
        # if var.bhc_4_ato_man_1 != "ON":
        # If you want these operations to be sequential:
        await mn_control_open(gpio, var, var.bhc_4_o_1, 'bhc_4_o_1', var.motor_4f_bohu_1, var.bhc_4_o_1_flg, var.bhc_4_ato_man_1)
        await mn_control_close(gpio, var, var.bhc_4_c_1, 'bhc_4_c_1', var.motor_4f_bohu_1, var.bhc_4_c_1_flg, var.bhc_4_ato_man_1)
        await asyncio.sleep(1)  # Small delay to prevent tight looping
        # else:
     #   print(f"auto mode is ON-------{var.bhc_4_ato_man_1}")
# BOHU CURTAIN 5


async def bc_control_5(var, gpio):
    while True:
        # if var.bhc_5_ato_man_1 != "ON":
        # If you want these operations to be sequential:
        await mn_control_open(gpio, var, var.bhc_5_o_1, 'bhc_5_o_1', var.motor_5f_bohu_1, var.bhc_5_o_1_flg, var.bhc_5_ato_man_1)
        await mn_control_close(gpio, var, var.bhc_5_c_1, 'bhc_5_c_1', var.motor_5f_bohu_1, var.bhc_5_c_1_flg, var.bhc_5_ato_man_1)
        await asyncio.sleep(1)  # Small delay to prevent tight looping
        # else:
     #   print(f"auto mode is ON-------{var.bhc_5_ato_man_1}")
# BOHU CURTAIN 6


async def bc_control_6(var, gpio):
    while True:
        # if var.bhc_6_ato_man_1 != "ON":
        # If you want these operations to be sequential:
        await mn_control_open(gpio, var, var.bhc_6_o_1, 'bhc_6_o_1', var.motor_6f_bohu_1, var.bhc_6_o_1_flg, var.bhc_6_ato_man_1)
        await mn_control_close(gpio, var, var.bhc_6_c_1, 'bhc_6_c_1', var.motor_6f_bohu_1, var.bhc_6_c_1_flg, var.bhc_6_ato_man_1)
        await asyncio.sleep(1)  # Small delay to prevent tight looping
        # else:
     #   print(f"auto mode is ON-------{var.bhc_6_ato_man_1}")
# BOHU CURTAIN 7


async def bc_control_7(var, gpio):
    while True:
        # if var.bhc_7_ato_man_1 != "ON":
        # If you want these operations to be sequential:
        await mn_control_open(gpio, var, var.bhc_7_o_1, 'bhc_7_o_1', var.motor_7f_bohu_1, var.bhc_7_o_1_flg, var.bhc_7_ato_man_1)
        await mn_control_close(gpio, var, var.bhc_7_c_1, 'bhc_7_c_1', var.motor_7f_bohu_1, var.bhc_7_c_1_flg, var.bhc_7_ato_man_1)
        await asyncio.sleep(1)  # Small delay to prevent tight looping
        # else:
     #   print(f"auto mode is ON-------{var.bhc_7_ato_man_1}")
# BOHU CURTAIN 8


async def bc_control_8(var, gpio):
    while True:
        # if var.bhc_8_ato_man_1 != "ON":
        # If you want these operations to be sequential:
        await mn_control_open(gpio, var, var.bhc_8_o_1, 'bhc_8_o_1', var.motor_8f_bohu_1, var.bhc_8_o_1_flg, var.bhc_8_ato_man_1)
        await mn_control_close(gpio, var, var.bhc_8_c_1, 'bhc_8_c_1', var.motor_8f_bohu_1, var.bhc_8_c_1_flg, var.bhc_8_ato_man_1)
        await asyncio.sleep(1)  # Small delay to prevent tight looping
        # else:
     #   print(f"auto mode is ON-------{var.bhc_8_ato_man_1}")

# BOHU CURTAIN 9


async def bc_control_9(var, gpio):
    while True:
        # if var.bhc_9_ato_man_1 != "ON":
        # If you want these operations to be sequential:
        await mn_control_open(gpio, var, var.bhc_9_o_1, 'bhc_9_o_1', var.motor_9f_bohu_1, var.bhc_9_o_1_flg, var.bhc_9_ato_man_1)
        await mn_control_close(gpio, var, var.bhc_9_c_1, 'bhc_9_c_1', var.motor_9f_bohu_1, var.bhc_9_c_1_flg, var.bhc_9_ato_man_1)
        await asyncio.sleep(1)  # Small delay to prevent tight looping
        # else:
     #   print(f"auto mode is ON-------{var.bhc_9_ato_man_1}")

# BOHU CURTAIN 10


async def bc_control_10(var, gpio):
    while True:
        # if var.bhc_10_ato_man_1 != "ON":
        # If you want these operations to be sequential:
        await mn_control_open(gpio, var, var.bhc_10_o_1, 'bhc_10_o_1', var.motor_10f_bohu_1, var.bhc_10_o_1_flg, var.bhc_10_ato_man_1)
        await mn_control_close(gpio, var, var.bhc_10_c_1, 'bhc_10_c_1', var.motor_10f_bohu_1, var.bhc_10_c_1_flg, var.bhc_10_ato_man_1)
        await asyncio.sleep(1)  # Small delay to prevent tight looping
        # else:
     #   print(f"auto mode is ON-------{var.bhc_10_ato_man_1}")
# BOHU CURTAIN 11


async def bc_control_11(var, gpio):
    while True:
        # if var.bhc_11_ato_man_1 != "ON":
        # If you want these operations to be sequential:
        await mn_control_open(gpio, var, var.bhc_11_o_1, 'bhc_11_o_1', var.motor_11f_bohu_1, var.bhc_11_o_1_flg, var.bhc_11_ato_man_1)
        await mn_control_close(gpio, var, var.bhc_11_c_1, 'bhc_11_c_1', var.motor_11f_bohu_1, var.bhc_11_c_1_flg, var.bhc_11_ato_man_1)
        await asyncio.sleep(1)  # Small delay to prevent tight looping
        # else:
     #   print(f"auto mode is ON-------{var.bhc_11_ato_man_1}")

# BOHU CURTAIN 12


async def bc_control_12(var, gpio):
    while True:
        # if var.bhc_12_ato_man_1 != "ON":
        # If you want these operations to be sequential:
        await mn_control_open(gpio, var, var.bhc_12_o_1, 'bhc_12_o_1', var.motor_12f_bohu_1, var.bhc_12_o_1_flg, var.bhc_12_ato_man_1)
        await mn_control_close(gpio, var, var.bhc_12_c_1, 'bhc_12_c_1', var.motor_12f_bohu_1, var.bhc_12_c_1_flg, var.bhc_12_ato_man_1)
        await asyncio.sleep(1)  # Small delay to prevent tight looping
        # else:
     #   print(f"Auto mode is ON-------{var.bhc_12_ato_man_1}")

# ==============================================================================================================================
# AC CONTROL OTHERS
# co2_ato_man_1
# fog_valve_ato_man_1
# sumag_ato_man_1
# bog_ato_man_1
# fegi_hongi_ato_man_1
# sp1_ato_man_1
# sp2_ato_man_1


async def ac_control_1(var, gpio):
    while True:
       # if var.sumag_ato_man_1 != "ON":
        await control_ac_onoff(gpio,var, var.sumag_1, 'sumag_1', var.sumag_ato_man_1)
        await asyncio.sleep(1)
        # else:
        #    print(f"Auto mode is ON-------{var.sumag_ato_man_1}")


async def ac_control_2(var, gpio):
    while True:
       # if var.bog_ato_man_1 != "ON":
        await control_ac_onoff(gpio,var, var.bogwangdong_1, 'bogwangdong_1', var.bog_ato_man_1)
        await asyncio.sleep(1)
        # else:
        #    print(f"Auto mode is ON-------{var.bog_ato_man_1}")


async def ac_control_3(var, gpio):
    while True:
       # if var.fog_valve_ato_man_1 != "ON":
        await control_ac_onoff(gpio,var, var.fog_valve_1, 'fog_valve_1', var.fog_valve_ato_man_1)
        await asyncio.sleep(1)
        # else:
        #    print(f"Auto mode is ON-------{var.fog_valve_ato_man_1}")


async def ac_control_4(var, gpio):
    while True:
       # if var.fegi_hongi_ato_man_1 != "ON":
        await control_ac_onoff(gpio,var, var.hongi_fan_1, 'hongi_fan_1', var.fegi_hongi_ato_man_1)
        await asyncio.sleep(1)
        # else:
        #    print(f"Auto mode is ON-------{var.fegi_hongi_ato_man}")


async def ac_control_5(var, gpio):
    while True:
       # if var.fegi_hongi_ato_man_1 != "ON":
        await control_ac_onoff(gpio,var, var.fegi_fan_1, 'fegi_fan_1', var.fegi_hongi_ato_man_1)
        await asyncio.sleep(1)
        # else:
        #    print(f"Auto mode is ON-------{var.fegi_hongi_ato_man}")


async def ac_control_6(var, gpio):
    while True:
       # if var.co2_ato_man_1 != "ON":
        await control_ac_onoff(gpio,var, var.co2_1, 'co2_1', var.fegi_hongi_ato_man_1)
        await asyncio.sleep(1)
        # else:
        #    print(f"Auto mode is ON-------{var.co2_ato_man_1}")


async def ac_control_7(var, gpio):
    while True:
       # if var.sp2_ato_man_1 != "ON":
        await control_ac_onoff(gpio,var, var.nangbangi_1, 'nangbangi_1',var.fegi_hongi_ato_man_1)
        await asyncio.sleep(1)
        # else:
        #    print(f"Auto mode is ON-------{var.sp2_ato_man_1}")


async def ac_control_8(var, gpio):
    while True:
       # if var.sp1_ato_man_1 != "ON":
        await control_ac_onoff(gpio,var, var.sp01_1, 'sp01_1',var.fegi_hongi_ato_man_1)
        await asyncio.sleep(1)
        # else:
        #    print(f"Auto mode is ON-------{var.sp1_ato_man_1}")


# YOUDONG FAN CONTROL
# yudong_fan1_ato_man_1
# yudong_fan2_ato_man_1

async def yf_control_1(var, gpio):
    while True:
       # if var.yudong_fan1_ato_man_1 != "ON":

        await control_ac_onoff(gpio,var, var.yudong_fan_1_cy_1, 'yudong_fan_1_cy_1', var.yudong_fan1_ato_man_1)
        #    await asyncio.sleep(1)
        # else:
        print(f"Auto mode is ON-------{var.yudong_fan1_ato_man}")


async def yf_control_2(var, gpio):
    while True:
       # if var.yudong_fan1_ato_man_1 != "ON":
        await control_ac_onoff(gpio,var, var.yudong_fan_1_uc_1, 'yudong_fan_1_uc_1',var.yudong_fan1_ato_man_1)
        await asyncio.sleep(1)
        # else:
        #    print(f"Auto mode is ON-------{var.yudong_fan1_ato_man}")


async def yf_control_3(var, gpio):
    while True:
       # if var.yudong_fan2_ato_man_1 != "ON":
        await control_ac_onoff(gpio,var, var.yudong_fan_2_cy_1, 'yudong_fan_2_cy_1', var.yudong_fan2_ato_man_1)
        await asyncio.sleep(1)
        # else:
        #    print(f"Auto mode is ON-------{var.yudong_fan2_ato_man}")


async def yf_control_4(var, gpio):
    while True:
       # if var.yudong_fan2_ato_man_1 != "ON":
        await control_ac_onoff(gpio,var, var.yudong_fan_2_uc_1, 'yudong_fan_2_uc_1',var.yudong_fan2_ato_man_1)
        await asyncio.sleep(1)
        # else:
        #    print(f"Auto mode is ON-------{var.yudong_fan2_ato_man}")
