import uasyncio as asyncio  # Import asyncio at the top
from md.at_f import sw_cw_rn_control, sw_cw_of_control
# change for the other house
# _1"
# _1,
# _1)
# _1_flg

# IF MIXED HOUSES
# SENSOR CHECK,
# temperature
# MAY BE , rain, max_temp, env_in_rain




        # ## pin auto man flag
        # self.chuk_ch_1f_am_flg_1 = False
        # self.chuk_ch_2f_am_flg_1 = False
        # self.chuk_ch_3f_am_flg_1 = False

        # self.chuk_uu_1f_am_flg_1 = False
        # self.chuk_uu_2f_am_flg_1 = False
        # self.chuk_uu_3f_am_flg_1 = False
# async def sw_cw_rn_control(var,     gpio,  o_pin,    cl_pin,  mtr_time,    temp_thresh, env_in_temp_r, env_in_temp, rain_max, rain, c_hour, c_min, o_hour, o_min, cl_hour, cl_min, at_btn, pin_btn, cl_flag, o_flag, cl_flg_n, o_flg_n, slt_swtch):

# ==============================================================SIDE WINDOWSN (sw) CHUKJANG --first floor
# 1F
# LEFT
async def sw_1f_left_atc_s1(var, gpio):
    while True:
        # print("---------sw-------left s1")
        await sw_cw_rn_control(var, gpio, "chuk_ch_1f_o_1", "chuk_ch_1f_c_1", int(var.motor_1f_chuk_1), int(var.s1_1f_chuk_temp_1), var.env_in_temp_r_1, var.envin_temp_1, int(var.rain_max_temp_1),var.rain_1, int(var.c_hour_1), int(var.c_min_1),  int(var.s1_1f_chuk_o_h_1), int(var.s1_1f_chuk_o_m_1), int(var.s1_1f_chuk_c_h_1), int(var.s1_1f_chuk_c_m_1), var.chuk_1f_ato_man_1, var.chuk_1f_ch_btn_1, var.chuk_ch_1f_c_1_flg, var.chuk_ch_1f_o_1_flg, "chuk_ch_1f_c_1_flg", "chuk_ch_1f_o_1_flg", "chuk_ch_1f_oc_1",var.chuk_ch_1f_am_flg_1,"chuk_ch_1f_am_flg_1",var.auto_manual_1)
        await asyncio.sleep(2)


async def sw_1f_left_atc_s2(var, gpio):
    while True:
        # print("---------sw---------left s2")
        await sw_cw_rn_control(var, gpio, "chuk_ch_1f_o_1", "chuk_ch_1f_c_1", int(var.motor_1f_chuk_1), int(var.s2_1f_chuk_temp_1), var.env_in_temp_r_1, var.envin_temp_1, int(var.rain_max_temp_1),var.rain_1, int(var.c_hour_1), int(var.c_min_1),  int(var.s2_1f_chuk_o_h_1), int(var.s2_1f_chuk_o_m_1), int(var.s2_1f_chuk_c_h_1), int(var.s2_1f_chuk_c_m_1), var.chuk_1f_ato_man_1, var.chuk_1f_ch_btn_1, var.chuk_ch_1f_c_1_flg, var.chuk_ch_1f_o_1_flg, "chuk_ch_1f_c_1_flg", "chuk_ch_1f_o_1_flg", "chuk_ch_1f_oc_1",var.chuk_ch_1f_am_flg_1,"chuk_ch_1f_am_flg_1",var.auto_manual_1)
        await asyncio.sleep(2)


async def sw_1f_left_atc_s3(var, gpio):
    while True:
        # print("---------sw---------left s3")
        await sw_cw_rn_control(var, gpio, "chuk_ch_1f_o_1", "chuk_ch_1f_c_1", int(var.motor_1f_chuk_1), int(var.s3_1f_chuk_temp_1), var.env_in_temp_r_1, var.envin_temp_1, int(var.rain_max_temp_1),var.rain_1, int(var.c_hour_1), int(var.c_min_1),  int(var.s3_1f_chuk_o_h_1), int(var.s3_1f_chuk_o_m_1), int(var.s3_1f_chuk_c_h_1), int(var.s3_1f_chuk_c_m_1), var.chuk_1f_ato_man_1, var.chuk_1f_ch_btn_1, var.chuk_ch_1f_c_1_flg, var.chuk_ch_1f_o_1_flg, "chuk_ch_1f_c_1_flg", "chuk_ch_1f_o_1_flg", "chuk_ch_1f_oc_1",var.chuk_ch_1f_am_flg_1,"chuk_ch_1f_am_flg_1",var.auto_manual_1)
        await asyncio.sleep(2)


async def sw_1f_left_atc_s4(var, gpio):
    while True:
        # print("---------sw---------left s4")
        await sw_cw_rn_control(var, gpio, "chuk_ch_1f_o_1", "chuk_ch_1f_c_1", int(var.motor_1f_chuk_1), int(var.s4_1f_chuk_temp_1), var.env_in_temp_r_1, var.envin_temp_1, int(var.rain_max_temp_1),var.rain_1, int(var.c_hour_1), int(var.c_min_1),  int(var.s4_1f_chuk_o_h_1), int(var.s4_1f_chuk_o_m_1), int(var.s4_1f_chuk_c_h_1), int(var.s4_1f_chuk_c_m_1), var.chuk_1f_ato_man_1, var.chuk_1f_ch_btn_1, var.chuk_ch_1f_c_1_flg, var.chuk_ch_1f_o_1_flg, "chuk_ch_1f_c_1_flg", "chuk_ch_1f_o_1_flg", "chuk_ch_1f_oc_1",var.chuk_ch_1f_am_flg_1,"chuk_ch_1f_am_flg_1",var.auto_manual_1)
        await asyncio.sleep(2)


async def sw_1f_left_atc_s5(var, gpio):
    while True:
        # print("---------sw---------left s5")
        await sw_cw_rn_control(var, gpio, "chuk_ch_1f_o_1", "chuk_ch_1f_c_1", int(var.motor_1f_chuk_1), int(var.s5_1f_chuk_temp_1), var.env_in_temp_r_1, var.envin_temp_1, int(var.rain_max_temp_1),var.rain_1, int(var.c_hour_1), int(var.c_min_1),  int(var.s5_1f_chuk_o_h_1), int(var.s5_1f_chuk_o_m_1), int(var.s5_1f_chuk_c_h_1), int(var.s5_1f_chuk_c_m_1), var.chuk_1f_ato_man_1, var.chuk_1f_ch_btn_1, var.chuk_ch_1f_c_1_flg, var.chuk_ch_1f_o_1_flg, "chuk_ch_1f_c_1_flg", "chuk_ch_1f_o_1_flg", "chuk_ch_1f_oc_1",var.chuk_ch_1f_am_flg_1,"chuk_ch_1f_am_flg_1",var.auto_manual_1)
        await asyncio.sleep(2)


async def sw_1f_left_atc_s6(var, gpio):
    while True:
        # print("---------sw---------left s6")
        await sw_cw_rn_control(var, gpio, "chuk_ch_1f_o_1", "chuk_ch_1f_c_1", int(var.motor_1f_chuk_1), int(var.s6_1f_chuk_temp_1), var.env_in_temp_r_1, var.envin_temp_1, int(var.rain_max_temp_1),var.rain_1, int(var.c_hour_1), int(var.c_min_1),  int(var.s6_1f_chuk_o_h_1), int(var.s6_1f_chuk_o_m_1), int(var.s6_1f_chuk_c_h_1), int(var.s6_1f_chuk_c_m_1), var.chuk_1f_ato_man_1, var.chuk_1f_ch_btn_1, var.chuk_ch_1f_c_1_flg, var.chuk_ch_1f_o_1_flg, "chuk_ch_1f_c_1_flg", "chuk_ch_1f_o_1_flg", "chuk_ch_1f_oc_1",var.chuk_ch_1f_am_flg_1,"chuk_ch_1f_am_flg_1",var.auto_manual_1)
        await asyncio.sleep(2)

















# 1F
# right
async def sw_1f_right_atc_s1(var, gpio):
    while True:
        # print("---------sw-------right s1")
        await sw_cw_rn_control(var, gpio, "chuk_uu_1f_o_1", "chuk_uu_1f_c_1", int(var.motor_1f_chuk_1), int(var.s1_1f_chuk_temp_1), var.env_in_temp_r_1, var.envin_temp_1, int(var.rain_max_temp_1),var.rain_1, int(var.c_hour_1), int(var.c_min_1),  int(var.s1_1f_chuk_o_h_1), int(var.s1_1f_chuk_o_m_1), int(var.s1_1f_chuk_c_h_1), int(var.s1_1f_chuk_c_m_1), var.chuk_1f_ato_man_1, var.chuk_1f_uu_btn_1, var.chuk_uu_1f_c_1_flg, var.chuk_uu_1f_o_1_flg, "chuk_uu_1f_c_1_flg", "chuk_uu_1f_o_1_flg", "chuk_uu_1f_oc_1",var.chuk_uu_1f_am_flg_1, "chuk_uu_1f_am_flg_1",var.auto_manual_1)
        await asyncio.sleep(2)


async def sw_1f_right_atc_s2(var, gpio):
    while True:
        # print("---------sw---------right s2")
        await sw_cw_rn_control(var, gpio, "chuk_uu_1f_o_1", "chuk_uu_1f_c_1", int(var.motor_1f_chuk_1), int(var.s2_1f_chuk_temp_1), var.env_in_temp_r_1, var.envin_temp_1, int(var.rain_max_temp_1),var.rain_1, int(var.c_hour_1), int(var.c_min_1),  int(var.s2_1f_chuk_o_h_1), int(var.s2_1f_chuk_o_m_1), int(var.s2_1f_chuk_c_h_1), int(var.s2_1f_chuk_c_m_1), var.chuk_1f_ato_man_1, var.chuk_1f_uu_btn_1, var.chuk_uu_1f_c_1_flg, var.chuk_uu_1f_o_1_flg, "chuk_uu_1f_c_1_flg", "chuk_uu_1f_o_1_flg", "chuk_uu_1f_oc_1",var.chuk_uu_1f_am_flg_1, "chuk_uu_1f_am_flg_1",var.auto_manual_1)
        await asyncio.sleep(2)


async def sw_1f_right_atc_s3(var, gpio):
    while True:
        # print("---------sw---------right s3")
        await sw_cw_rn_control(var, gpio, "chuk_uu_1f_o_1", "chuk_uu_1f_c_1", int(var.motor_1f_chuk_1), int(var.s3_1f_chuk_temp_1), var.env_in_temp_r_1, var.envin_temp_1, int(var.rain_max_temp_1),var.rain_1, int(var.c_hour_1), int(var.c_min_1),  int(var.s3_1f_chuk_o_h_1), int(var.s3_1f_chuk_o_m_1), int(var.s3_1f_chuk_c_h_1), int(var.s3_1f_chuk_c_m_1), var.chuk_1f_ato_man_1, var.chuk_1f_uu_btn_1, var.chuk_uu_1f_c_1_flg, var.chuk_uu_1f_o_1_flg, "chuk_uu_1f_c_1_flg", "chuk_uu_1f_o_1_flg", "chuk_uu_1f_oc_1",var.chuk_uu_1f_am_flg_1, "chuk_uu_1f_am_flg_1",var.auto_manual_1)
        await asyncio.sleep(2)


async def sw_1f_right_atc_s4(var, gpio):
    while True:
        # print("---------sw---------right s4")
        await sw_cw_rn_control(var, gpio, "chuk_uu_1f_o_1", "chuk_uu_1f_c_1", int(var.motor_1f_chuk_1), int(var.s4_1f_chuk_temp_1), var.env_in_temp_r_1, var.envin_temp_1, int(var.rain_max_temp_1),var.rain_1, int(var.c_hour_1), int(var.c_min_1),  int(var.s4_1f_chuk_o_h_1), int(var.s4_1f_chuk_o_m_1), int(var.s4_1f_chuk_c_h_1), int(var.s4_1f_chuk_c_m_1), var.chuk_1f_ato_man_1, var.chuk_1f_uu_btn_1, var.chuk_uu_1f_c_1_flg, var.chuk_uu_1f_o_1_flg, "chuk_uu_1f_c_1_flg", "chuk_uu_1f_o_1_flg", "chuk_uu_1f_oc_1",var.chuk_uu_1f_am_flg_1, "chuk_uu_1f_am_flg_1",var.auto_manual_1)
        await asyncio.sleep(2)


async def sw_1f_right_atc_s5(var, gpio):
    while True:
        # print("---------sw---------right s5")
        await sw_cw_rn_control(var, gpio, "chuk_uu_1f_o_1", "chuk_uu_1f_c_1", int(var.motor_1f_chuk_1), int(var.s5_1f_chuk_temp_1), var.env_in_temp_r_1, var.envin_temp_1, int(var.rain_max_temp_1),var.rain_1, int(var.c_hour_1), int(var.c_min_1),  int(var.s5_1f_chuk_o_h_1), int(var.s5_1f_chuk_o_m_1), int(var.s5_1f_chuk_c_h_1), int(var.s5_1f_chuk_c_m_1), var.chuk_1f_ato_man_1, var.chuk_1f_uu_btn_1, var.chuk_uu_1f_c_1_flg, var.chuk_uu_1f_o_1_flg, "chuk_uu_1f_c_1_flg", "chuk_uu_1f_o_1_flg", "chuk_uu_1f_oc_1",var.chuk_uu_1f_am_flg_1, "chuk_uu_1f_am_flg_1",var.auto_manual_1)
        await asyncio.sleep(2)


async def sw_1f_right_atc_s6(var, gpio):
    while True:
        # print("---------sw---------right s6")
        await sw_cw_rn_control(var, gpio, "chuk_uu_1f_o_1", "chuk_uu_1f_c_1", int(var.motor_1f_chuk_1), int(var.s6_1f_chuk_temp_1), var.env_in_temp_r_1, var.envin_temp_1, int(var.rain_max_temp_1),var.rain_1, int(var.c_hour_1), int(var.c_min_1),  int(var.s6_1f_chuk_o_h_1), int(var.s6_1f_chuk_o_m_1), int(var.s6_1f_chuk_c_h_1), int(var.s6_1f_chuk_c_m_1), var.chuk_1f_ato_man_1, var.chuk_1f_uu_btn_1, var.chuk_uu_1f_c_1_flg, var.chuk_uu_1f_o_1_flg, "chuk_uu_1f_c_1_flg", "chuk_uu_1f_o_1_flg", "chuk_uu_1f_oc_1",var.chuk_uu_1f_am_flg_1, "chuk_uu_1f_am_flg_1",var.auto_manual_1)
        await asyncio.sleep(2)




















# ================================================================= SECOND FLOOR

# 2F
# LEFT
async def sw_2f_left_atc_s1(var, gpio):
    while True:
        # print("---------sw-------left s1")
        await sw_cw_rn_control(var, gpio, "chuk_ch_2f_o_1", "chuk_ch_2f_c_1", int(var.motor_2f_chuk_1), int(var.s1_2f_chuk_temp_1), var.env_in_temp_r_1, var.envin_temp_1, int(var.rain_max_temp_1),var.rain_1, int(var.c_hour_1), int(var.c_min_1),  int(var.s1_2f_chuk_o_h_1), int(var.s1_2f_chuk_o_m_1), int(var.s1_2f_chuk_c_h_1), int(var.s1_2f_chuk_c_m_1), var.chuk_2f_ato_man_1, var.chuk_2f_ch_btn_1, var.chuk_ch_2f_c_1_flg, var.chuk_ch_2f_o_1_flg, "chuk_ch_2f_c_1_flg", "chuk_ch_2f_o_1_flg", "chuk_ch_2f_oc_1",var.chuk_ch_2f_am_flg_1, "chuk_ch_2f_am_flg_1",var.auto_manual_1)
        await asyncio.sleep(2)


async def sw_2f_left_atc_s2(var, gpio):
    while True:
        # print("---------sw---------left s2")
        await sw_cw_rn_control(var, gpio, "chuk_ch_2f_o_1", "chuk_ch_2f_c_1", int(var.motor_2f_chuk_1), int(var.s2_2f_chuk_temp_1), var.env_in_temp_r_1, var.envin_temp_1, int(var.rain_max_temp_1),var.rain_1, int(var.c_hour_1), int(var.c_min_1),  int(var.s2_2f_chuk_o_h_1), int(var.s2_2f_chuk_o_m_1), int(var.s2_2f_chuk_c_h_1), int(var.s2_2f_chuk_c_m_1), var.chuk_2f_ato_man_1, var.chuk_2f_ch_btn_1, var.chuk_ch_2f_c_1_flg, var.chuk_ch_2f_o_1_flg, "chuk_ch_2f_c_1_flg", "chuk_ch_2f_o_1_flg", "chuk_ch_2f_oc_1",var.chuk_ch_2f_am_flg_1, "chuk_ch_2f_am_flg_1",var.auto_manual_1)
        await asyncio.sleep(2)


async def sw_2f_left_atc_s3(var, gpio):
    while True:
        # print("---------sw---------left s3")
        await sw_cw_rn_control(var, gpio, "chuk_ch_2f_o_1", "chuk_ch_2f_c_1", int(var.motor_2f_chuk_1), int(var.s3_2f_chuk_temp_1), var.env_in_temp_r_1, var.envin_temp_1, int(var.rain_max_temp_1),var.rain_1, int(var.c_hour_1), int(var.c_min_1),  int(var.s3_2f_chuk_o_h_1), int(var.s3_2f_chuk_o_m_1), int(var.s3_2f_chuk_c_h_1), int(var.s3_2f_chuk_c_m_1), var.chuk_2f_ato_man_1, var.chuk_2f_ch_btn_1, var.chuk_ch_2f_c_1_flg, var.chuk_ch_2f_o_1_flg, "chuk_ch_2f_c_1_flg", "chuk_ch_2f_o_1_flg", "chuk_ch_2f_oc_1",var.chuk_ch_2f_am_flg_1, "chuk_ch_2f_am_flg_1",var.auto_manual_1)
        await asyncio.sleep(2)









# 2F
# right
async def sw_2f_right_atc_s1(var, gpio):
    while True:
        # print("---------sw-------right s1")
        await sw_cw_rn_control(var, gpio, "chuk_uu_2f_o_1", "chuk_uu_2f_c_1", int(var.motor_2f_chuk_1), int(var.s1_2f_chuk_temp_1), var.env_in_temp_r_1, var.envin_temp_1, int(var.rain_max_temp_1),var.rain_1, int(var.c_hour_1), int(var.c_min_1),  int(var.s1_2f_chuk_o_h_1), int(var.s1_2f_chuk_o_m_1), int(var.s1_2f_chuk_c_h_1), int(var.s1_2f_chuk_c_m_1), var.chuk_2f_ato_man_1, var.chuk_2f_uu_btn_1, var.chuk_uu_2f_c_1_flg, var.chuk_uu_2f_o_1_flg, "chuk_uu_2f_c_1_flg", "chuk_uu_2f_o_1_flg", "chuk_uu_2f_oc_1",var.chuk_uu_2f_am_flg_1,"chuk_uu_2f_am_flg_1",var.auto_manual_1)
        await asyncio.sleep(2)


async def sw_2f_right_atc_s2(var, gpio):
    while True:
        # print("---------sw---------right s2")
        await sw_cw_rn_control(var, gpio, "chuk_uu_2f_o_1", "chuk_uu_2f_c_1", int(var.motor_2f_chuk_1), int(var.s2_2f_chuk_temp_1), var.env_in_temp_r_1, var.envin_temp_1, int(var.rain_max_temp_1),var.rain_1, int(var.c_hour_1), int(var.c_min_1),  int(var.s2_2f_chuk_o_h_1), int(var.s2_2f_chuk_o_m_1), int(var.s2_2f_chuk_c_h_1), int(var.s2_2f_chuk_c_m_1), var.chuk_2f_ato_man_1, var.chuk_2f_uu_btn_1, var.chuk_uu_2f_c_1_flg, var.chuk_uu_2f_o_1_flg, "chuk_uu_2f_c_1_flg", "chuk_uu_2f_o_1_flg", "chuk_uu_2f_oc_1",var.chuk_uu_2f_am_flg_1,"chuk_uu_2f_am_flg_1",var.auto_manual_1)
        await asyncio.sleep(2)


async def sw_2f_right_atc_s3(var, gpio):
    while True:
        # print("---------sw---------right s3")
        await sw_cw_rn_control(var, gpio, "chuk_uu_2f_o_1", "chuk_uu_2f_c_1", int(var.motor_2f_chuk_1), int(var.s3_2f_chuk_temp_1), var.env_in_temp_r_1, var.envin_temp_1, int(var.rain_max_temp_1),var.rain_1, int(var.c_hour_1), int(var.c_min_1),  int(var.s3_2f_chuk_o_h_1), int(var.s3_2f_chuk_o_m_1), int(var.s3_2f_chuk_c_h_1), int(var.s3_2f_chuk_c_m_1), var.chuk_2f_ato_man_1, var.chuk_2f_uu_btn_1, var.chuk_uu_2f_c_1_flg, var.chuk_uu_2f_o_1_flg, "chuk_uu_2f_c_1_flg", "chuk_uu_2f_o_1_flg", "chuk_uu_2f_oc_1",var.chuk_uu_2f_am_flg_1,"chuk_uu_2f_am_flg_1",var.auto_manual_1)
        await asyncio.sleep(2)


# ================================================================= THIRD FLOOR

# 3F
# LEFT
async def sw_3f_left_atc_s1(var, gpio):
    while True:
        # print("---------sw-------left s1")
        await sw_cw_of_control(var, gpio, "chuk_ch_3f_o_1", "chuk_ch_3f_c_1", int(var.motor_3f_chuk_1), int(var.s1_3f_chuk_temp_1), var.env_in_temp_r_1, var.envin_temp_1, int(var.rain_max_temp_1),var.rain_1, int(var.c_hour_1), int(var.c_min_1),  int(var.s1_3f_chuk_o_h_1), int(var.s1_3f_chuk_o_m_1), int(var.s1_3f_chuk_c_h_1), int(var.s1_3f_chuk_c_m_1), var.chuk_3f_ato_man_1, var.chuk_3f_ch_btn_1, var.chuk_ch_3f_c_1_flg, var.chuk_ch_3f_o_1_flg, "chuk_ch_3f_c_1_flg", "chuk_ch_3f_o_1_flg", "chuk_ch_3f_oc_1",var.chuk_ch_3f_am_flg_1,"chuk_ch_3f_am_flg_1",var.auto_manual_1)
        await asyncio.sleep(2)


async def sw_3f_left_atc_s2(var, gpio):
    while True:
        # print("---------sw---------left s2")
        await sw_cw_of_control(var, gpio, "chuk_ch_3f_o_1", "chuk_ch_3f_c_1", int(var.motor_3f_chuk_1), int(var.s2_3f_chuk_temp_1), var.env_in_temp_r_1, var.envin_temp_1, int(var.rain_max_temp_1),var.rain_1, int(var.c_hour_1), int(var.c_min_1),  int(var.s2_3f_chuk_o_h_1), int(var.s2_3f_chuk_o_m_1), int(var.s2_3f_chuk_c_h_1), int(var.s2_3f_chuk_c_m_1), var.chuk_3f_ato_man_1, var.chuk_3f_ch_btn_1, var.chuk_ch_3f_c_1_flg, var.chuk_ch_3f_o_1_flg, "chuk_ch_3f_c_1_flg", "chuk_ch_3f_o_1_flg", "chuk_ch_3f_oc_1",var.chuk_ch_3f_am_flg_1,"chuk_ch_3f_am_flg_1",var.auto_manual_1)
        await asyncio.sleep(2)


async def sw_3f_left_atc_s3(var, gpio):
    while True:
        # print("---------sw---------left s3")
        await sw_cw_of_control(var, gpio, "chuk_ch_3f_o_1", "chuk_ch_3f_c_1", int(var.motor_3f_chuk_1), int(var.s3_3f_chuk_temp_1), var.env_in_temp_r_1, var.envin_temp_1, int(var.rain_max_temp_1),var.rain_1, int(var.c_hour_1), int(var.c_min_1),  int(var.s3_3f_chuk_o_h_1), int(var.s3_3f_chuk_o_m_1), int(var.s3_3f_chuk_c_h_1), int(var.s3_3f_chuk_c_m_1), var.chuk_3f_ato_man_1, var.chuk_3f_ch_btn_1, var.chuk_ch_3f_c_1_flg, var.chuk_ch_3f_o_1_flg, "chuk_ch_3f_c_1_flg", "chuk_ch_3f_o_1_flg", "chuk_ch_3f_oc_1",var.chuk_ch_3f_am_flg_1,"chuk_ch_3f_am_flg_1",var.auto_manual_1)
        await asyncio.sleep(2)






# 3F
# right
async def sw_3f_right_atc_s1(var, gpio):
    while True:
        # print("---------sw-------right s1")
        await sw_cw_of_control(var, gpio, "chuk_uu_3f_o_1", "chuk_uu_3f_c_1", int(var.motor_3f_chuk_1), int(var.s1_3f_chuk_temp_1), var.env_in_temp_r_1, var.envin_temp_1, int(var.rain_max_temp_1),var.rain_1, int(var.c_hour_1), int(var.c_min_1),  int(var.s1_3f_chuk_o_h_1), int(var.s1_3f_chuk_o_m_1), int(var.s1_3f_chuk_c_h_1), int(var.s1_3f_chuk_c_m_1), var.chuk_3f_ato_man_1, var.chuk_3f_uu_btn_1, var.chuk_uu_3f_c_1_flg, var.chuk_uu_3f_o_1_flg, "chuk_uu_3f_c_1_flg", "chuk_uu_3f_o_1_flg", "chuk_uu_3f_oc_1",var.chuk_uu_3f_am_flg_1, "chuk_uu_3f_am_flg_1",var.auto_manual_1)
        await asyncio.sleep(2)


async def sw_3f_right_atc_s2(var, gpio):
    while True:
        # print("---------sw---------right s2")
        await sw_cw_of_control(var, gpio, "chuk_uu_3f_o_1", "chuk_uu_3f_c_1", int(var.motor_3f_chuk_1), int(var.s2_3f_chuk_temp_1), var.env_in_temp_r_1, var.envin_temp_1, int(var.rain_max_temp_1),var.rain_1, int(var.c_hour_1), int(var.c_min_1),  int(var.s2_3f_chuk_o_h_1), int(var.s2_3f_chuk_o_m_1), int(var.s2_3f_chuk_c_h_1), int(var.s2_3f_chuk_c_m_1), var.chuk_3f_ato_man_1, var.chuk_3f_uu_btn_1, var.chuk_uu_3f_c_1_flg, var.chuk_uu_3f_o_1_flg, "chuk_uu_3f_c_1_flg", "chuk_uu_3f_o_1_flg", "chuk_uu_3f_oc_1",var.chuk_uu_3f_am_flg_1, "chuk_uu_3f_am_flg_1",var.auto_manual_1)
        await asyncio.sleep(2)


async def sw_3f_right_atc_s3(var, gpio):
    while True:
        # print("---------sw---------right s3")
        await sw_cw_of_control(var, gpio, "chuk_uu_3f_o_1", "chuk_uu_3f_c_1", int(var.motor_3f_chuk_1), int(var.s3_3f_chuk_temp_1), var.env_in_temp_r_1, var.envin_temp_1, int(var.rain_max_temp_1),var.rain_1, int(var.c_hour_1), int(var.c_min_1),  int(var.s3_3f_chuk_o_h_1), int(var.s3_3f_chuk_o_m_1), int(var.s3_3f_chuk_c_h_1), int(var.s3_3f_chuk_c_m_1), var.chuk_3f_ato_man_1, var.chuk_3f_uu_btn_1, var.chuk_uu_3f_c_1_flg, var.chuk_uu_3f_o_1_flg, "chuk_uu_3f_c_1_flg", "chuk_uu_3f_o_1_flg", "chuk_uu_3f_oc_1",var.chuk_uu_3f_am_flg_1, "chuk_uu_3f_am_flg_1",var.auto_manual_1)
        await asyncio.sleep(2)
