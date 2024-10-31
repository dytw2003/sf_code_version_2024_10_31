# mnsf.py

import uasyncio as asyncio


## CHANGE FOR THE OTHER HOUSE


##  _1"
##  _1_flg"
## mnsig_flag_1



async def mn_signal_gpio_fun(gpio, pin):   
    gpio.turn_off_pins(pin)
    print(f"GPIO {pin} turned OFF----:::::----")


async def mn_signal_flg_func(var, fname):
    setattr(var, fname, False)
    print(f"FLAG {fname} turned OFF::::: {getattr(var, fname)}")


async def mn_signal(gpio, var):
    # set the all the gpio pins OFF

    pins = {
        "chuk_ch_1f_o_1",
        "chuk_ch_1f_c_1",
        "chuk_uu_1f_o_1",  # uu chuk
        "chuk_uu_1f_c_1",
        ##2 floor
        "chuk_ch_2f_o_1",
        "chuk_ch_2f_c_1",
        "chuk_uu_2f_o_1",  # uu chuk
        "chuk_uu_2f_c_1",
        # 3 floor
        "chuk_ch_3f_o_1",
        "chuk_ch_3f_c_1",
        "chuk_uu_3f_o_1",  # uu chuk
        "chuk_uu_3f_c_1",
        # gpio "D21~D32"
        # chhan jang  ------
        # 1 floor
        "chan_ch_1f_o_1",
        "chan_ch_1f_c_1",
        "chan_uu_1f_o_1",  # uu chuk
        "chan_uu_1f_c_1",
        # 2 floor

        "chan_ch_2f_o_1",
        "chan_ch_2f_c_1",
        "chan_uu_2f_o_1",  # uu chuk
        "chan_uu_2f_c_1",
        # 3 flo
        "chan_ch_3f_o_1",
        "chan_ch_3f_c_1",
        "chan_uu_3f_o_1",  # uu chuk
        "chan_uu_3f_c_1",
        "fw_o_1",
        "fw_c_1",
        "bw_o_1",  # uu chuk
        "bw_c_1",
        "fw_o_1",
        "fw_c_1",
        "bw_o_1",  # uu chuk
        "bw_c_1",
        # gpio ("D41~D54")
        # bohu curtain---
        "bhc_1_o_1",  # chhan myang bohu
        "bhc_1_c_1",
        "bhc_2_o_1",  # chhwa chuk myon bohu
        "bhc_2_c_1",
        "bhc_3_o_1",  # uu chuk myon bohu
        "bhc_3_c_1",
        "bhc_4_o_1",  # hu myon bohu
        "bhc_4_c_1",
        "bhc_5_o_1",  # chhanjang bohu
        "bhc_5_c_1",
        "bhc_6_o_1",  # chhanjang chhagong mak
        "bhc_6_c_1",
        "bhc_7_o_1",  # chhanjang finil
        "bhc_7_c_1",
        "bhc_8_o_1",  # vc-06
        "bhc_8_c_1",

        "bhc_9_o_1",  # vc-07
        "bhc_9_c_1",
        "bhc_10_o_1",  # vc-08
        "bhc_10_c_1",
        "bhc_11_o_1",  # vc-09
        "bhc_11_c_1",
        "bhc_12_o_1",  # vc-010
        "bhc_12_c_1",
        # Gpio ("D55~D63")

        "bogwangdong_1",  # -fegi fan
        "sumag_1",  # -Hongi fan
        "fog_valve_1",  # -fog valve
        "co2_1",  # flash_light
        "fegi_fan_1",
        "hongi_fan_1",  # "sumag_1",  # -sumag
        "nangbangi_1",
        "sp01_1",

        #
        "yudong_fan_1_cy_1",  # -yudong fan 1 # chhak/ yak
        "yudong_fan_1_uc_1",  # unjan / chhangji(ON/OFF)
        "yudong_fan_2_cy_1",  # yudong fan2     # chhak/ yak
        "yudong_fan_2_uc_1",  # unjan / chhangji(ON/OFF)

    }

    flags = {
        # self.chuk_ch_3f_o_1_flg = False
        # self.chuk_ch_3f_c_1_flg = False
        "chuk_ch_1f_o_1_flg",
        "chuk_ch_1f_c_1_flg",
        "chuk_uu_1f_o_1_flg",  # uu chuk
        "chuk_uu_1f_c_1_flg",
        ###2 floor
        "chuk_ch_2f_o_1_flg",
        "chuk_ch_2f_c_1_flg",
        "chuk_uu_2f_o_1_flg",  # uu chuk
        "chuk_uu_2f_c_1_flg",
        # 3 floor
        "chuk_ch_3f_o_1_flg",
        "chuk_ch_3f_c_1_flg",
        "chuk_uu_3f_o_1_flg",  # uu chuk
        "chuk_uu_3f_c_1_flg",
        # gpio "D21~D32"
        # chhan jang  ------
        # 1 floor
        "chan_ch_1f_o_1_flg",
        "chan_ch_1f_c_1_flg",
        "chan_uu_1f_o_1_flg",  # uu chuk
        "chan_uu_1f_c_1_flg",
        # 2 floor

        "chan_ch_2f_o_1_flg",
        "chan_ch_2f_c_1_flg",
        "chan_uu_2f_o_1_flg",  # uu chuk
        "chan_uu_2f_c_1_flg",
        # 3 flo
        "chan_ch_3f_o_1_flg",
        "chan_ch_3f_c_1_flg",
        "chan_uu_3f_o_1_flg",  # uu chuk
        "chan_uu_3f_c_1_flg",
        
        "fw_o_1_flg",
        "fw_c_1_flg",
        "bw_o_1_flg",  # uu chuk
        "bw_c_1_flg",
        # gpio ("D41~D54")
        # bohu curtain---
        "bhc_1_o_1_flg ",  # chhan myang bohu
        "bhc_1_c_1_flg ",
        "bhc_2_o_1_flg ",  # chhwa chuk myon bohu
        "bhc_2_c_1_flg ",
        "bhc_3_o_1_flg ",  # uu chuk myon bohu
        "bhc_3_c_1_flg ",
        "bhc_4_o_1_flg ",  # hu myon bohu
        "bhc_4_c_1_flg ",
        "bhc_5_o_1_flg ",  # chhanjang bohu
        "bhc_5_c_1_flg ",
        "bhc_6_o_1_flg ",  # chhanjang chhagong mak
        "bhc_6_c_1_flg ",
        "bhc_7_o_1_flg ",  # chhanjang finil
        "bhc_7_c_1_flg ",
        "bhc_8_o_1_flg ",  # uu chuk myon bohu
        "bhc_8_c_1_flg ",
        "bhc_9_o_1_flg ",  # hu myon bohu
        "bhc_9_c_1_flg ",
        "bhc_10_o_1_flg ",  # chhanjang bohu
        "bhc_10_c_1_flg ",
        "bhc_11_o_1_flg ",  # chhanjang chhagong mak
        "bhc_11_c_1_flg ",
        "bhc_12_o_1_flg ",  # chhanjang finil
        "bhc_12_c_1_flg ",
        # Gpio ("D55~D63")
        # sudong-2-- page 3

        #

        "fegi_fan_1_flg",  # -fegi fan
        "hongi_fan_1_flg",  # -Hongi fan
        "fog_valve_1_flg",  # -fog valve
        "bogwangdong_1_flg",  # flash_light
        "co2_1_flg",
        "nangbangi_1_flg",  # "sumag_1_flg",  # -sumag
        "sumag_1 _flg",
        "sp01_1_flg",

        #
        "yudong_fan_1_cy_1_flg",  # -yudong fan 1 # chhak/ yak
        "yudong_fan_1_uc_1_flg",  # unjan / chhangji(ON/OFF)
        "yudong_fan_2_cy_1_flg",  # yudong fan2     # chhak/ yak
        "yudong_fan_2_uc_1_flg",  # unjan / chhangji(ON/OFF)
    }

    if not var.mnsig_flag_1:

        for pin in pins:
            await mn_signal_gpio_fun(gpio, pin)
        # set the all the flag to False
        for flag in flags:
            await mn_signal_flg_func(var, flag)
        setattr(var,"mnsig_flag_1", True)
        print(f"ATMN FLAG  is ----I{getattr(var,"mnsig_flag_1")}--- AND -- MANUAL --MODE ")
    else:
        print("ATMN FLAG 1 is ----------True-------")

    await asyncio.sleep(2)
