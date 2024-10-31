import uasyncio as asyncio  # Import asyncio at the top
from md.at_f import sw_cw_rn_control, sw_cw_of_control



# change for the other house
# _1"
# _1,
# _1)
# _1_flg

# SIDE WINDOWS
# 1F


# ====================================================FRONT WINDOWS rain
# ==== FRONT BACK
# 1F 
async def fw_1f_atc_s1(var, gpio):
    while True:
        #print("----------fw------ s1")
        await sw_cw_rn_control(var, gpio, "fw_o_1", "fw_c_1", int(var.mfwbw_1), int(var.s1fwbwt_1),var.env_in_temp_r_1, var.envin_temp_1, int(var.rain_max_temp_1),var.rain_1, int(var.c_hour_1), int(var.c_min_1), int(var.s1fwbw_oh_1), int(var.s1fwbw_om_1), int(var.s1fwbw_ch_1), int(var.s1fwbw_cm_1), var.fwbw_am_1, var.fwb_1, var.fw_c_1_flg, var.fw_o_1_flg,"fw_c_1_flg", "fw_o_1_flg","fw_oc_1",var.auto_manual_1)
        await asyncio.sleep(2)


async def fw_1f_atc_s2(var, gpio):
    while True:
        #print("---------fw------- s2")
        await sw_cw_rn_control(var, gpio, "fw_o_1", "fw_c_1", int(var.mfwbw_1), int(var.s2fwbwt_1),var.env_in_temp_r_1, var.envin_temp_1, int(var.rain_max_temp_1),var.rain_1, int(var.c_hour_1), int(var.c_min_1), int(var.s2fwbw_oh_1), int(var.s2fwbw_om_1), int(var.s2fwbw_ch_1), int(var.s2fwbw_cm_1), var.fwbw_am_1, var.fwb_1, var.fw_c_1_flg, var.fw_o_1_flg,"fw_c_1_flg", "fw_o_1_flg","fw_oc_1",var.auto_manual_1)
        await asyncio.sleep(2)


async def fw_1f_atc_s3(var, gpio):
    while True:
        #print("----------fw------ s3")
        await sw_cw_rn_control(var, gpio, "fw_o_1", "fw_c_1", int(var.mfwbw_1), int(var.s3fwbwt_1),var.env_in_temp_r_1, var.envin_temp_1, int(var.rain_max_temp_1),var.rain_1, int(var.c_hour_1), int(var.c_min_1), int(var.s3fwbw_oh_1), int(var.s3fwbw_om_1), int(var.s3fwbw_ch_1), int(var.s3fwbw_cm_1), var.fwbw_am_1, var.fwb_1, var.fw_c_1_flg, var.fw_o_1_flg,"fw_c_1_flg", "fw_o_1_flg","fw_oc_1",var.auto_manual_1)
        await asyncio.sleep(2)


async def fw_1f_atc_s4(var, gpio):
    while True:
        #print("---------fw------- s4")
        await sw_cw_rn_control(var, gpio, "fw_o_1", "fw_c_1", int(var.mfwbw_1), int(var.s4fwbwt_1),var.env_in_temp_r_1, var.envin_temp_1, int(var.rain_max_temp_1),var.rain_1, int(var.c_hour_1), int(var.c_min_1), int(var.s4fwbw_oh_1), int(var.s4fwbw_om_1), int(var.s4fwbw_ch_1), int(var.s4fwbw_cm_1), var.fwbw_am_1, var.fwb_1, var.fw_c_1_flg, var.fw_o_1_flg,"fw_c_1_flg", "fw_o_1_flg","fw_oc_1",var.auto_manual_1)
        await asyncio.sleep(2)


async def fw_1f_atc_s5(var, gpio):
    while True:
        #print("---------fw------- s5")
        await sw_cw_rn_control(var, gpio, "fw_o_1", "fw_c_1", int(var.mfwbw_1), int(var.s5fwbwt_1),var.env_in_temp_r_1, var.envin_temp_1, int(var.rain_max_temp_1),var.rain_1, int(var.c_hour_1), int(var.c_min_1), int(var.s5fwbw_oh_1), int(var.s5fwbw_om_1), int(var.s5fwbw_ch_1), int(var.s5fwbw_cm_1), var.fwbw_am_1, var.fwb_1, var.fw_c_1_flg, var.fw_o_1_flg,"fw_c_1_flg", "fw_o_1_flg","fw_oc_1",var.auto_manual_1)
        await asyncio.sleep(2)


async def fw_1f_atc_s6(var, gpio):
    while True:
        #print("---------------- s6")
        await sw_cw_rn_control(var, gpio, "fw_o_1", "fw_c_1", int(var.mfwbw_1), int(var.s6fwbwt_1),var.env_in_temp_r_1, var.envin_temp_1, int(var.rain_max_temp_1),var.rain_1, int(var.c_hour_1), int(var.c_min_1), int(var.s6fwbw_oh_1), int(var.s6fwbw_om_1), int(var.s6fwbw_ch_1), int(var.s6fwbw_cm_1), var.fwbw_am_1, var.fwb_1, var.fw_c_1_flg, var.fw_o_1_flg,"fw_c_1_flg", "fw_o_1_flg","fw_oc_1",var.auto_manual_1)
        await asyncio.sleep(2)
# ================================BACK WINDOWS
async def bw_1f_atc_s1(var, gpio):
    while True:
        #print("---------------- s1")
        await sw_cw_rn_control(var, gpio, "bw_o_1", "bw_c_1", int(var.mfwbw_1), int(var.s1fwbwt_1),var.env_in_temp_r_1, var.envin_temp_1, int(var.rain_max_temp_1),var.rain_1, int(var.c_hour_1), int(var.c_min_1), int(var.s1fwbw_oh_1), int(var.s1fwbw_om_1), int(var.s1fwbw_ch_1), int(var.s1fwbw_cm_1), var.fwbw_am_1, var.bwb_1, var.bw_c_1_flg, var.bw_o_1_flg,"bw_c_1_flg", "bw_o_1_flg","bw_oc_1",var.auto_manual_1)
        await asyncio.sleep(2)


async def bw_1f_atc_s2(var, gpio):
    while True:
        #print("------bw--------- s2")
        await sw_cw_rn_control(var, gpio, "bw_o_1", "bw_c_1", int(var.mfwbw_1), int(var.s2fwbwt_1),var.env_in_temp_r_1, var.envin_temp_1, int(var.rain_max_temp_1),var.rain_1, int(var.c_hour_1), int(var.c_min_1), int(var.s2fwbw_oh_1), int(var.s2fwbw_om_1), int(var.s2fwbw_ch_1), int(var.s2fwbw_cm_1), var.fwbw_am_1, var.bwb_1, var.bw_c_1_flg, var.bw_o_1_flg,"bw_c_1_flg", "bw_o_1_flg","bw_oc_1",var.auto_manual_1)
        await asyncio.sleep(2)


async def bw_1f_atc_s3(var, gpio):
    while True:
        #print("------bw---------- s3")
        await sw_cw_rn_control(var, gpio, "bw_o_1", "bw_c_1", int(var.mfwbw_1), int(var.s3fwbwt_1),var.env_in_temp_r_1, var.envin_temp_1, int(var.rain_max_temp_1),var.rain_1, int(var.c_hour_1), int(var.c_min_1), int(var.s3fwbw_oh_1), int(var.s3fwbw_om_1), int(var.s3fwbw_ch_1), int(var.s3fwbw_cm_1), var.fwbw_am_1, var.bwb_1, var.bw_c_1_flg, var.bw_o_1_flg,"bw_c_1_flg", "bw_o_1_flg","bw_oc_1",var.auto_manual_1)
        await asyncio.sleep(2)


async def bw_1f_atc_s4(var, gpio):
    while True:
        #print("--------bw-------- s4")
        await sw_cw_rn_control(var, gpio, "bw_o_1", "bw_c_1", int(var.mfwbw_1), int(var.s4fwbwt_1),var.env_in_temp_r_1, var.envin_temp_1, int(var.rain_max_temp_1),var.rain_1, int(var.c_hour_1), int(var.c_min_1), int(var.s4fwbw_oh_1), int(var.s4fwbw_om_1), int(var.s4fwbw_ch_1), int(var.s4fwbw_cm_1), var.fwbw_am_1, var.bwb_1, var.bw_c_1_flg, var.bw_o_1_flg,"bw_c_1_flg", "bw_o_1_flg","bw_oc_1",var.auto_manual_1)
        await asyncio.sleep(2)


async def bw_1f_atc_s5(var, gpio):
    while True:
        #print("---------bw------- s5")
        await sw_cw_rn_control(var, gpio, "bw_o_1", "bw_c_1", int(var.mfwbw_1), int(var.s5fwbwt_1),var.env_in_temp_r_1, var.envin_temp_1, int(var.rain_max_temp_1),var.rain_1, int(var.c_hour_1), int(var.c_min_1), int(var.s5fwbw_oh_1), int(var.s5fwbw_om_1), int(var.s5fwbw_ch_1), int(var.s5fwbw_cm_1), var.fwbw_am_1, var.bwb_1, var.bw_c_1_flg, var.bw_o_1_flg,"bw_c_1_flg", "bw_o_1_flg","bw_oc_1",var.auto_manual_1)
        await asyncio.sleep(2)


async def bw_1f_atc_s6(var, gpio):
    while True:
        #print("-------bw--------- s6")
        await sw_cw_rn_control(var, gpio, "bw_o_1", "bw_c_1", int(var.mfwbw_1), int(var.s6fwbwt_1),var.env_in_temp_r_1, var.envin_temp_1, int(var.rain_max_temp_1),var.rain_1, int(var.c_hour_1), int(var.c_min_1), int(var.s6fwbw_oh_1), int(var.s6fwbw_om_1), int(var.s6fwbw_ch_1), int(var.s6fwbw_cm_1), var.fwbw_am_1, var.bwb_1, var.bw_c_1_flg, var.bw_o_1_flg,"bw_c_1_flg", "bw_o_1_flg","bw_oc_1",var.auto_manual_1)
        await asyncio.sleep(2)





# ==== FRONT BACK
# 2F  -------- no rain
# left

async def fw_2f_atc_s1(var, gpio):
    while True:
        #print("----------fw------ s1")
        await sw_cw_of_control(var, gpio, "fw_2f_o_1", "fw_2f_c_1", int(var.m_f2fwbw_1), int(var.s1_f2_fwbwt_1),var.env_in_temp_r_1, var.envin_temp_1, int(var.rain_max_temp_1),var.rain_1, int(var.c_hour_1), int(var.c_min_1),int(var.s1_f2_fwbw_oh_1), int(var.s1_f2_fwbw_om_1), int(var.s1_f2_fwbw_ch_1), int(var.s1_fwbw_cm_1), var.fwbw_f2_am_1, var.fwb_f2_1, var.fw_2f_c_1_flg, var.fw_2f_o_1_flg, "fw_2f_c_1_flg", "fw_2f_o_1_flg","fw_2f_oc_1",var.auto_manual_1)
        await asyncio.sleep(2)

async def fw_2f_atc_s2(var, gpio):
    while True:
        #print("----------fw------ s2")
        await sw_cw_of_control(var, gpio, "fw_2f_o_1", "fw_2f_c_1", int(var.m_f2fwbw_1), int(var.s2_f2_fwbwt_1),var.env_in_temp_r_1, var.envin_temp_1, int(var.rain_max_temp_1),var.rain_1, int(var.c_hour_1), int(var.c_min_1),int(var.s2_f2_fwbw_oh_1), int(var.s2_f2_fwbw_om_1), int(var.s2_f2_fwbw_ch_1), int(var.s2_fwbw_cm_1), var.fwbw_f2_am_1, var.fwb_f2_1, var.fw_2f_c_1_flg, var.fw_2f_o_1_flg, "fw_2f_c_1_flg", "fw_2f_o_1_flg","fw_2f_oc_1",var.auto_manual_1)
        await asyncio.sleep(2)
    
async def fw_2f_atc_s3(var, gpio):
    while True:
        #print("----------fw------ s3")
        await sw_cw_of_control(var, gpio, "fw_2f_o_1", "fw_2f_c_1", int(var.m_f2fwbw_1), int(var.s3_f2_fwbwt_1),var.env_in_temp_r_1, var.envin_temp_1, int(var.rain_max_temp_1),var.rain_1, int(var.c_hour_1), int(var.c_min_1),int(var.s3_f2_fwbw_oh_1), int(var.s3_f2_fwbw_om_1), int(var.s3_f2_fwbw_ch_1), int(var.s3_fwbw_cm_1), var.fwbw_f2_am_1, var.fwb_f2_1, var.fw_2f_c_1_flg, var.fw_2f_o_1_flg, "fw_2f_c_1_flg", "fw_2f_o_1_flg","fw_2f_oc_1",var.auto_manual_1)
        await asyncio.sleep(2)

#right
async def bw_2f_atc_s1(var, gpio):
    while True:
        #print("----------bw------ s1")
        await sw_cw_of_control(var, gpio, "bw_2f_o_1", "bw_2f_c_1", int(var.m_f2fwbw_1), int(var.s1_f2_fwbwt_1),var.env_in_temp_r_1, var.envin_temp_1, int(var.rain_max_temp_1),var.rain_1, int(var.c_hour_1), int(var.c_min_1),int(var.s1_f2_fwbw_oh_1), int(var.s1_f2_fwbw_om_1), int(var.s1_f2_fwbw_ch_1), int(var.s1_fwbw_cm_1), var.fwbw_f2_am_1, var.bwb_f2_1, var.bw_2f_c_1_flg, var.bw_2f_o_1_flg, "bw_2f_c_1_flg", "bw_2f_o_1_flg","bw_2f_oc_1",var.auto_manual_1)
        await asyncio.sleep(2)
async def bw_2f_atc_s2(var, gpio):
    while True:
        #print("----------bw------ s2")
        await sw_cw_of_control(var, gpio, "bw_2f_o_1", "bw_2f_c_1", int(var.m_f2fwbw_1), int(var.s2_f2_fwbwt_1),var.env_in_temp_r_1, var.envin_temp_1, int(var.rain_max_temp_1),var.rain_1, int(var.c_hour_1), int(var.c_min_1),int(var.s2_f2_fwbw_oh_1), int(var.s2_f2_fwbw_om_1), int(var.s2_f2_fwbw_ch_1), int(var.s2_fwbw_cm_1), var.fwbw_f2_am_1, var.bwb_f2_1, var.bw_2f_c_1_flg, var.bw_2f_o_1_flg, "bw_2f_c_1_flg", "bw_2f_o_1_flg","bw_2f_oc_1",var.auto_manual_1)
        await asyncio.sleep(2)

async def bw_2f_atc_s3(var, gpio):
    while True:
        #print("----------bw------ s3")
        await sw_cw_of_control(var, gpio, "bw_2f_o_1", "bw_2f_c_1", int(var.m_f2fwbw_1), int(var.s3_f2_fwbwt_1),var.env_in_temp_r_1, var.envin_temp_1, int(var.rain_max_temp_1),var.rain_1, int(var.c_hour_1), int(var.c_min_1),int(var.s3_f2_fwbw_oh_1), int(var.s3_f2_fwbw_om_1), int(var.s3_f2_fwbw_ch_1), int(var.s3_fwbw_cm_1), var.fwbw_f2_am_1, var.bwb_f2_1, var.bw_2f_c_1_flg, var.bw_2f_o_1_flg, "bw_2f_c_1_flg", "bw_2f_o_1_flg","bw_2f_oc_1",var.auto_manual_1)
        await asyncio.sleep(2)


# ==========================================================================================================================================================================================================================

