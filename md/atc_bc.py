import uasyncio as asyncio  # Import asyncio at the top
from md.at_f import  bc_of_control

# change for the other house
# _1"
# _1,
# _1)
# _1_flg

# BOHU CURTAIN

        # self.bc_1f_am_flg_1=False
        # self.bc_2f_am_flg_1=False
        # self.bc_3f_am_flg_1=False

        # self.bc_4f_am_flg_1=False
        # self.bc_5f_am_flg_1=False
        # self.bc_6f_am_flg_1=False

        # self.bc_7f_am_flg_1=False
        # self.bc_8f_am_flg_1=False
        # self.bc_9f_am_flg_1=False

        # self.bc_10f_am_flg_1=False
        # self.bc_11f_am_flg_1=False
        # self.bc_12f_am_flg_1=False



async def bc_1f_atc(var, gpio):
    while True:
        #print("---------bc--------f1")
        await bc_of_control(var, gpio, "bhc_1_o_1", "bhc_1_c_1", int(var.motor_1f_bohu_1), int(var.s_1_bhc_temp_1),var.envin_temp_1,int(var.c_hour_1), int(var.c_min_1), int(var.s_1_bhc_o_h_1), int(var.s_1_bhc_o_m_1), int(var.s_1_bhc_c_h_1), int(var.s_1_bhc_c_m_1), var.bhc_1_ato_man_1, var.bhc_1_u_ch_btn_1, var.bhc_1_c_1_flg, var.bhc_1_o_1_flg, "bhc_1_c_1_flg", "bhc_1_o_1_flg","bohu_1f_oc_1",var.bc_1f_am_flg_1, "bc_1f_am_flg_1",var.auto_manual_1)
        await asyncio.sleep(2)


async def bc_2f_atc(var, gpio):
    while True:
        #print("--------bc--------f2")
        await bc_of_control(var, gpio, "bhc_2_o_1", "bhc_2_c_1", int(var.motor_2f_bohu_1), int(var.s_2_bhc_temp_1),var.envin_temp_1,int(var.c_hour_1), int(var.c_min_1), int(var.s_2_bhc_o_h_1), int(var.s_2_bhc_o_m_1), int(var.s_2_bhc_c_h_1), int(var.s_2_bhc_c_m_1), var.bhc_2_ato_man_1, var.bhc_2_u_ch_btn_1, var.bhc_2_c_1_flg, var.bhc_2_o_1_flg, "bhc_2_c_1_flg", "bhc_2_o_1_flg","bohu_2f_oc_1",var.bc_2f_am_flg_1, "bc_2f_am_flg_1",var.auto_manual_1)
        await asyncio.sleep(2)



async def bc_3f_atc(var, gpio):
    while True:
        #print("---------bc--------f1")
        await bc_of_control(var, gpio, "bhc_3_o_1", "bhc_3_c_1", int(var.motor_3f_bohu_1), int(var.s_3_bhc_temp_1),var.envin_temp_1,int(var.c_hour_1), int(var.c_min_1), int(var.s_3_bhc_o_h_1), int(var.s_3_bhc_o_m_1), int(var.s_3_bhc_c_h_1), int(var.s_3_bhc_c_m_1), var.bhc_3_ato_man_1, var.bhc_3_u_ch_btn_1, var.bhc_3_c_1_flg, var.bhc_3_o_1_flg, "bhc_3_c_1_flg", "bhc_3_o_1_flg","bohu_3f_oc_1",var.bc_3f_am_flg_1, "bc_3f_am_flg_1",var.auto_manual_1)
        await asyncio.sleep(2)


async def bc_4f_atc(var, gpio):
    while True:
        #print("--------bc--------f2")
        await bc_of_control(var, gpio, "bhc_4_o_1", "bhc_4_c_1", int(var.motor_4f_bohu_1), int(var.s_4_bhc_temp_1),var.envin_temp_1,int(var.c_hour_1), int(var.c_min_1), int(var.s_4_bhc_o_h_1), int(var.s_4_bhc_o_m_1), int(var.s_4_bhc_c_h_1), int(var.s_4_bhc_c_m_1), var.bhc_4_ato_man_1, var.bhc_4_u_ch_btn_1, var.bhc_4_c_1_flg, var.bhc_4_o_1_flg, "bhc_4_c_1_flg", "bhc_4_o_1_flg","bohu_4f_oc_1",var.bc_4f_am_flg_1, "bc_4f_am_flg_1",var.auto_manual_1)
        await asyncio.sleep(2)






async def bc_5f_atc(var, gpio):
    while True:
        #print("---------bc--------f1")
        await bc_of_control(var, gpio, "bhc_5_o_1", "bhc_5_c_1", int(var.motor_5f_bohu_1), int(var.s_5_bhc_temp_1),var.envin_temp_1,int(var.c_hour_1), int(var.c_min_1), int(var.s_5_bhc_o_h_1), int(var.s_5_bhc_o_m_1), int(var.s_5_bhc_c_h_1), int(var.s_5_bhc_c_m_1), var.bhc_5_ato_man_1, var.bhc_5_u_ch_btn_1, var.bhc_5_c_1_flg, var.bhc_5_o_1_flg, "bhc_5_c_1_flg", "bhc_5_o_1_flg","bohu_5f_oc_1",var.bc_5f_am_flg_1, "bc_5f_am_flg_1",var.auto_manual_1)
        await asyncio.sleep(2)


async def bc_6f_atc(var, gpio):
    while True:
        #print("--------bc--------f2")
        await bc_of_control(var, gpio, "bhc_6_o_1", "bhc_6_c_1", int(var.motor_6f_bohu_1), int(var.s_6_bhc_temp_1),var.envin_temp_1,int(var.c_hour_1), int(var.c_min_1), int(var.s_6_bhc_o_h_1), int(var.s_6_bhc_o_m_1), int(var.s_6_bhc_c_h_1), int(var.s_6_bhc_c_m_1), var.bhc_6_ato_man_1, var.bhc_6_u_ch_btn_1, var.bhc_6_c_1_flg, var.bhc_6_o_1_flg, "bhc_6_c_1_flg", "bhc_6_o_1_flg","bohu_6f_oc_1",var.bc_6f_am_flg_1, "bc_6f_am_flg_1",var.auto_manual_1)
        await asyncio.sleep(2)



async def bc_7f_atc(var, gpio):
    while True:
        #print("---------bc--------f1")
        await bc_of_control(var, gpio, "bhc_7_o_1", "bhc_7_c_1", int(var.motor_7f_bohu_1), int(var.s_7_bhc_temp_1),var.envin_temp_1,int(var.c_hour_1), int(var.c_min_1), int(var.s_7_bhc_o_h_1), int(var.s_7_bhc_o_m_1), int(var.s_7_bhc_c_h_1), int(var.s_7_bhc_c_m_1), var.bhc_7_ato_man_1, var.bhc_7_u_ch_btn_1, var.bhc_7_c_1_flg, var.bhc_7_o_1_flg, "bhc_7_c_1_flg", "bhc_7_o_1_flg","bohu_7f_oc_1",var.bc_7f_am_flg_1, "bc_7f_am_flg_1",var.auto_manual_1)
        await asyncio.sleep(2)


async def bc_8f_atc(var, gpio):
    while True:
        #print("--------bc--------f2")
        await bc_of_control(var, gpio, "bhc_8_o_1", "bhc_8_c_1", int(var.motor_8f_bohu_1), int(var.s_8_bhc_temp_1),var.envin_temp_1,int(var.c_hour_1), int(var.c_min_1), int(var.s_8_bhc_o_h_1), int(var.s_8_bhc_o_m_1), int(var.s_8_bhc_c_h_1), int(var.s_8_bhc_c_m_1), var.bhc_8_ato_man_1, var.bhc_8_u_ch_btn_1, var.bhc_8_c_1_flg, var.bhc_8_o_1_flg, "bhc_8_c_1_flg", "bhc_8_o_1_flg","bohu_8f_oc_1",var.bc_8f_am_flg_1, "bc_8f_am_flg_1",var.auto_manual_1)
        await asyncio.sleep(2)




async def bc_9f_atc(var, gpio):
    while True:
        #print("---------bc--------f1")
        await bc_of_control(var, gpio, "bhc_9_o_1", "bhc_9_c_1", int(var.motor_9f_bohu_1), int(var.s_9_bhc_temp_1),var.envin_temp_1,int(var.c_hour_1), int(var.c_min_1), int(var.s_9_bhc_o_h_1), int(var.s_9_bhc_o_m_1), int(var.s_9_bhc_c_h_1), int(var.s_9_bhc_c_m_1), var.bhc_9_ato_man_1, var.bhc_9_u_ch_btn_1, var.bhc_9_c_1_flg, var.bhc_9_o_1_flg, "bhc_9_c_1_flg", "bhc_9_o_1_flg","bohu_1f_oc_1",var.bc_9f_am_flg_1, "bc_9f_am_flg_1",var.auto_manual_1)
        await asyncio.sleep(2)


async def bc_10f_atc(var, gpio):
    while True:
        #print("---------bc--------f1")
        await bc_of_control(var, gpio, "bhc_10_o_1", "bhc_10_c_1", int(var.motor_10f_bohu_1), int(var.s_10_bhc_temp_1),var.envin_temp_1,int(var.c_hour_1), int(var.c_min_1), int(var.s_10_bhc_o_h_1), int(var.s_10_bhc_o_m_1), int(var.s_10_bhc_c_h_1), int(var.s_10_bhc_c_m_1), var.bhc_10_ato_man_1, var.bhc_10_u_ch_btn_1, var.bhc_10_c_1_flg, var.bhc_10_o_1_flg, "bhc_10_c_1_flg", "bhc_10_o_1_flg","bohu_10f_oc_1",var.bc_10f_am_flg_1, "bc_10f_am_flg_1",var.auto_manual_1)
        await asyncio.sleep(2)

async def bc_11f_atc(var, gpio):
    while True:
        #print("---------bc--------f1")
        await bc_of_control(var, gpio, "bhc_11_o_1", "bhc_11_c_1", int(var.motor_11f_bohu_1), int(var.s_11_bhc_temp_1),var.envin_temp_1,int(var.c_hour_1), int(var.c_min_1), int(var.s_11_bhc_o_h_1), int(var.s_11_bhc_o_m_1), int(var.s_11_bhc_c_h_1), int(var.s_11_bhc_c_m_1), var.bhc_11_ato_man_1, var.bhc_11_u_ch_btn_1, var.bhc_11_c_1_flg, var.bhc_11_o_1_flg, "bhc_11_c_1_flg", "bhc_11_o_1_flg","bohu_10f_oc_1",var.bc_11f_am_flg_1, "bc_11f_am_flg_1",var.auto_manual_1)
        await asyncio.sleep(2)



async def bc_12f_atc(var, gpio):
    while True:
        #print("---------bc--------f1")
        await bc_of_control(var, gpio, "bhc_12_o_1", "bhc_12_c_1", int(var.motor_12f_bohu_1), int(var.s_12_bhc_temp_1),var.envin_temp_1,int(var.c_hour_1), int(var.c_min_1), int(var.s_12_bhc_o_h_1), int(var.s_12_bhc_o_m_1), int(var.s_12_bhc_c_h_1), int(var.s_12_bhc_c_m_1), var.bhc_12_ato_man_1, var.bhc_12_u_ch_btn_1, var.bhc_12_c_1_flg, var.bhc_12_o_1_flg, "bhc_12_c_1_flg", "bhc_12_o_1_flg","bohu_12f_oc_1",var.bc_12f_am_flg_1, "bc_12f_am_flg_1",var.auto_manual_1)
        await asyncio.sleep(2)











