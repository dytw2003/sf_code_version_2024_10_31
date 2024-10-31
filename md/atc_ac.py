import uasyncio as asyncio  # Import asyncio at the top


# change for the other house
# _1"
# _1,
# _1)


##===============================================fegi and hong fan control ============================================================ BOTHE TEMPERATURE AND TIME BASED OR ONLY TEMPERATURE BASED
# async def fan_ctrl_func(var, gpio, pin,flag, temp_thresh,  o_hour, o_min, cl_hour, cl_min, at_btn, pin_btn):

from md.at_fac import fan_ctrl_func ,sb_ctrl_func   #,fog_ctrl_func,co2_ctrl_func
#Fegi fan 
# CHANGE THE VALUES 
async def fegi_fan_control(var, gpio):
    while True:
       await fan_ctrl_func(var, gpio, "fegi_fan_1",var.fegi_o_1, "fegi_o_1", int(var.fegi_fan_temp_1),  int(var.fegi_fan_o_h_1), int(var.fegi_fan_o_m_1), int(var.fegi_fan_c_h_1), int(var.fegi_fan_c_m_1), var.fegi_hongi_ato_man_1, var.fegi_hongi_u_ch_btn_1)
       await asyncio.sleep(2.5)
async def hongi_fan_control(var, gpio):
    while True:
       await fan_ctrl_func(var, gpio, "hongi_fan_1",var.hongi_o_1, "hongi_o_1",int( var.hongi_fan_temp_1),  int(var.hongi_fan_o_h_1), int(var.hongi_fan_o_m_1), int(var.hongi_fan_c_h_1), int(var.hongi_fan_c_m_1), var.fegi_hongi_ato_man_1, var.fegi_hongi_u_ch_btn_1)
       await asyncio.sleep(2.5)


async def fegi_fan_control2(var, gpio):
    while True:
       await fan_ctrl_func(var, gpio,  "fog_valve_1",var.fog_o_1,"fog_o_1", int(var.fegi_fan_temp_1),  int(var.fegi_fan_o_h_1), int(var.fegi_fan_o_m_1), int(var.fegi_fan_c_h_1), int(var.fegi_fan_c_m_1), var.fegi_hongi_ato_man_1, var.fegi_hongi_u_ch_btn_1)
       await asyncio.sleep(2.5)
async def hongi_fan_control(var, gpio):
    while True:
       await fan_ctrl_func(var, gpio, "nangbangi_1",var.hongi_o_1, "hongi_o_1",int( var.hongi_fan_temp_1),  int(var.hongi_fan_o_h_1), int(var.hongi_fan_o_m_1), int(var.hongi_fan_c_h_1), int(var.hongi_fan_c_m_1), var.fegi_hongi_ato_man_1, var.fegi_hongi_u_ch_btn_1)
       await asyncio.sleep(2.5)

async def fegi_fan_control2(var, gpio):
    while True:
       await fan_ctrl_func(var, gpio,  "co2_1",var.co2_o_1, "co2_o_1", int(var.fegi_fan_temp_1),  int(var.fegi_fan_o_h_1), int(var.fegi_fan_o_m_1), int(var.fegi_fan_c_h_1), int(var.fegi_fan_c_m_1), var.fegi_hongi_ato_man_1, var.fegi_hongi_u_ch_btn_1)
       await asyncio.sleep(2.5)
async def hongi_fan_control(var, gpio):
    while True:
       await fan_ctrl_func(var, gpio, "sp01_1",var.hongi_o_1, "hongi_o_1",int( var.hongi_fan_temp_1),  int(var.hongi_fan_o_h_1), int(var.hongi_fan_o_m_1), int(var.hongi_fan_c_h_1), int(var.hongi_fan_c_m_1), var.fegi_hongi_ato_man_1, var.fegi_hongi_u_ch_btn_1)
       await asyncio.sleep(2.5)

# #=========================  sumag, bogwangdong  control only  TIME BASED ON AND OFF 
async def bog_control(var, gpio):
    while True:
       await sb_ctrl_func(var, gpio, "bogwangdong_1",var.bog_o_1, "bog_o_1",  int(var.bog_yallim_h_1), int(var.bog_yallim_m_1), int(var.bog_thathim_h_1), int(var.bog_thathim_m_1), var.bog_ato_man_1, var.bog_u_ch_btn_1)
       await asyncio.sleep(2.5)
# async def sumag_control(var, gpio):
#     while True:
#        await sb_ctrl_func(var, gpio, "sumag_1",var.sumag_o_1,"sumag_o_1", int(var.sumag_yallim_h_1), int(var.sumag_yallim_m_1), int(var.sumag_thathim_h_1), int(var.sumag_thathim_m_1), var.sumag_ato_man_1, var.sumag_u_ch_btn_1)
#        await asyncio.sleep(2.5)

# #========================== fog valve control 

# async def fog_control_s1(var, gpio):
#     while True:
#        await fog_ctrl_func(var, gpio, "fog_valve_1",var.fog_o_1,"fog_o_1", int( var.s1_fog_valve_humi_1),  int(var.s1_fog_valve_run_time_1), int(var.s1_fog_valve_stop_time_1), var.fog_valve_ato_man_1, var.fog_valve_u_ch_btn_1)
#        await asyncio.sleep(2.5)
# async def fog_control_s2(var, gpio):
#     while True:
#        await fog_ctrl_func(var, gpio, "fog_valve_1",var.fog_o_1,"fog_o_1", int( var.s2_fog_valve_humi_1),  int(var.s2_fog_valve_run_time_1), int(var.s2_fog_valve_stop_time_1), var.fog_valve_ato_man_1, var.fog_valve_u_ch_btn_1)
#        await asyncio.sleep(2.5)
# async def fog_control_s3(var, gpio):
#     while True:
#        await fog_ctrl_func(var, gpio, "fog_valve_1",var.fog_o_1,"fog_o_1", int( var.s3_fog_valve_humi_1),  int(var.s3_fog_valve_run_time_1), int(var.s3_fog_valve_stop_time_1), var.fog_valve_ato_man_1, var.fog_valve_u_ch_btn_1)
#        await asyncio.sleep(2.5)


# #========================= co2 control

# async def co2_control(var, gpio):
#     while True:
#        await co2_ctrl_func(var, gpio, "co2_1",var.co2_o_1, "co2_o_1",int( var.co2_nongdo_1),  int(var.co2_chhaun_1), int(var.co2_khoun_1),  var.co2_ato_man_1, var.co2_u_ch_btn_1)
#        await asyncio.sleep(2.5)




# #=========================== yudong fan control 
# async def yudong_fan_control(var, gpio):
#     while True:
#        await fan_ctrl_func(var, gpio, "sumag_1",var.sumag_o_1,"sumag_o_1", int( var.fegi_fan_temp_1),  int(var.fegi_fan_o_h_1), int(var.fegi_fan_o_m_1), int(var.fegi_fan_c_h_1), int(var.fegi_fan_c_m_1), var.fegi_hongi_ato_man_1, var.fegi_hongi_u_ch_btn_1)
#        await asyncio.sleep(2.5)

# async def yudong_fan_control(var, gpio):
#     while True:
#        await fan_ctrl_func(var, gpio, "co2_1",var.co2_o_1, "co2_o_1",int( var.co2_nongdo_1),  int(var.co2_chhaun_1), int(var.co2_khoun_1),  var.co2_ato_man_1, var.co2_u_ch_btn_1)
#        await asyncio.sleep(2.5)

# async def yudong_fan_control_3(var, gpio):
#     while True:
#        await fan_ctrl_func(var, gpio, "fegi_fan_1", int( var.fegi_fan_temp_1),  int(var.fegi_fan_o_h_1), int(var.fegi_fan_o_m_1), int(var.fegi_fan_c_h_1), int(var.fegi_fan_c_m_1), var.fegi_hongi_ato_man_1, var.fegi_hongi_u_ch_btn_1)
#        await asyncio.sleep(2.5)

# async def yudong_fan_control_4(var, gpio):
#     while True:
#        await fan_ctrl_func(var, gpio, "fegi_fan_1", int( var.fegi_fan_temp_1),  int(var.fegi_fan_o_h_1), int(var.fegi_fan_o_m_1), int(var.fegi_fan_c_h_1), int(var.fegi_fan_c_m_1), var.fegi_hongi_ato_man_1, var.fegi_hongi_u_ch_btn_1)
#        await asyncio.sleep(2.5)




##=========================================================================================================== ONLY THE TIME BASED 









