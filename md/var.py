# control_gpio.py
# NEED TO CHANGE FOR OTHER HOUSE
# 1_flg =
# _1 =
# am_flg_1 =
class VariableData:
    def __init__(self):
        # ld flag
        self.ld_flg = False
        self.auto_manual_1 = None
        self.rst_1 = None
        # flag to publish to the cloud
        self.rst_atmn_flg = False

        self.mnsig_flag_1 = False
        # chhuk jang --------------
        # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++  CONTROL AND SETTING VALUES VARIABLE DECLEAR

        # pin auto man flag
        self.chuk_ch_1f_am_flg_1 = False
        self.chuk_ch_2f_am_flg_1 = False
        self.chuk_ch_3f_am_flg_1 = False

        self.chuk_uu_1f_am_flg_1 = False
        self.chuk_uu_2f_am_flg_1 = False
        self.chuk_uu_3f_am_flg_1 = False

        self.chan_ch_1f_am_flg_1 = False
        self.chan_ch_2f_am_flg_1 = False
        self.chan_ch_3f_am_flg_1 = False

        self.chan_uu_1f_am_flg_1 = False
        self.chan_uu_2f_am_flg_1 = False
        self.chan_uu_3f_am_flg_1 = False

        self.bc_1f_am_flg_1 = False
        self.bc_2f_am_flg_1 = False
        self.bc_3f_am_flg_1 = False

        self.bc_4f_am_flg_1 = False
        self.bc_5f_am_flg_1 = False
        self.bc_6f_am_flg_1 = False

        self.bc_7f_am_flg_1 = False
        self.bc_8f_am_flg_1 = False
        self.bc_9f_am_flg_1 = False

        self.bc_10f_am_flg_1 = False
        self.bc_11f_am_flg_1 = False
        self.bc_12f_am_flg_1 = False

        # chhuk jang ---------------------------MANUAL BUTTON
        # for the motor Flag
        self.chuk_ch_1f_o_1_flg = False
        self.chuk_ch_1f_c_1_flg = False

        self.chuk_ch_2f_o_1_flg = False
        self.chuk_ch_2f_c_1_flg = False

        self.chuk_ch_3f_o_1_flg = False
        self.chuk_ch_3f_c_1_flg = False

        self.chuk_uu_1f_o_1_flg = False  # uu chuk
        self.chuk_uu_1f_c_1_flg = False

        self.chuk_uu_2f_o_1_flg = False
        self.chuk_uu_2f_c_1_flg = False

        self.chuk_uu_3f_o_1_flg = False
        self.chuk_uu_3f_c_1_flg = False
        # OPEN CLOSE  flag ---------------- send this to the server
        self.chuk_ch_1f_oc_1 = None
        self.chuk_ch_2f_oc_1 = None
        self.chuk_ch_3f_oc_1 = None
        self.chuk_uu_1f_oc_1 = None
        self.chuk_uu_2f_oc_1 = None
        self.chuk_uu_3f_oc_1 = None

        # For Mother runnig length  chhuk jang
        self.motor_1f_chuk_1 = 0
        self.motor_2f_chuk_1 = 0
        self.motor_3f_chuk_1 = 0
        # For Button
        self.chuk_ch_1f_o_1 = None
        self.chuk_ch_1f_c_1 = None
        self.chuk_ch_2f_o_1 = None
        self.chuk_ch_2f_c_1 = None
        self.chuk_ch_3f_o_1 = None
        self.chuk_ch_3f_c_1 = None
        self.chuk_uu_1f_o_1 = None  # uu chuk
        self.chuk_uu_1f_c_1 = None
        self.chuk_uu_2f_o_1 = None
        self.chuk_uu_2f_c_1 = None
        self.chuk_uu_3f_o_1 = None
        self.chuk_uu_3f_c_1 = None
        # chhan jang  ------
        # for the motor Flag
        # For Button
        self.chan_ch_1f_o_1_flg = False
        self.chan_ch_1f_c_1_flg = False
        self.chan_ch_2f_o_1_flg = False
        self.chan_ch_2f_c_1_flg = False
        self.chan_ch_3f_o_1_flg = False
        self.chan_ch_3f_c_1_flg = False

        self.chan_uu_1f_o_1_flg = False  # uu chuk
        self.chan_uu_1f_c_1_flg = False
        self.chan_uu_2f_o_1_flg = False
        self.chan_uu_2f_c_1_flg = False
        self.chan_uu_3f_o_1_flg = False
        self.chan_uu_3f_c_1_flg = False
        # OPEN CLOSE ---------------- send this to the server
        self.chan_ch_1f_oc_1 = None
        self.chan_ch_2f_oc_1 = None
        self.chan_ch_3f_oc_1 = None
        self.chan_uu_1f_oc_1 = None
        self.chan_uu_2f_oc_1 = None
        self.chan_uu_3f_oc_1 = None

        # For Mother runnig length  chhan jang
        self.motor_1f_chan_1 = 0
        self.motor_2f_chan_1 = 0
        self.motor_3f_chan_1 = 0
        # For Button
        self.chan_ch_1f_o_1 = None
        self.chan_ch_1f_c_1 = None
        self.chan_ch_2f_o_1 = None
        self.chan_ch_2f_c_1 = None
        self.chan_ch_3f_o_1 = None
        self.chan_ch_3f_c_1 = None

        self.chan_uu_1f_o_1 = None  # uu chuk
        self.chan_uu_1f_c_1 = None
        self.chan_uu_2f_o_1 = None
        self.chan_uu_2f_c_1 = None
        self.chan_uu_3f_o_1 = None
        self.chan_uu_3f_c_1 = None
        # front and back windows

        # 1F
        # open_close_flag
        self.fw_oc_1 = None
        self.bw_oc_1 = None
        # motor time
        self.mfwbw_1 = 0
        # button flag
        self.fw_o_1_flg = False
        self.fw_c_1_flg = False
        self.bw_o_1_flg = False
        self.bw_c_1_flg = False
        # button front window(fw) back window(bw)
        self.fw_o_1 = None
        self.fw_c_1 = None

        self.bw_o_1 = None
        self.bw_c_1 = None

        # 2F
        self.fw_2f_oc_1 = None
        self.bw_2f_oc_1 = None
        # motor time
        self.m_f2fwbw_1 = 0
        # button flag
        self.fw_2f_o_1_flg = False
        self.fw_2f_c_1_flg = False
        self.bw_2f_o_1_flg = False
        self.bw_2f_c_1_flg = False
        # button front window(fw_2f) back window(bw_2f)
        self.fw_2f_o_1 = None
        self.fw_2f_c_1 = None

        self.bw_2f_o_1 = None
        self.bw_2f_c_1 = None

        # bohu curtain---
        # For Mother runnig length
        self.motor_1f_bohu_1 = 0  # chhan myang bohu
        self.motor_2f_bohu_1 = 0  # chhwa chuk myon bohu
        self.motor_3f_bohu_1 = 0  # uu chuk myon bohu
        self.motor_4f_bohu_1 = 0  # hu myon bohu
        self.motor_5f_bohu_1 = 0  # chhanjang bohu
        self.motor_6f_bohu_1 = 0  # chhanjang chhagong mak
        self.motor_7f_bohu_1 = 0  # chhanjang finil
        self.motor_8f_bohu_1 = 0  # uu chuk myon bohu
        self.motor_9f_bohu_1 = 0  # hu myon bohu
        self.motor_10f_bohu_1 = 0  # chhanjang bohu
        self.motor_11f_bohu_1 = 0  # chhanjang chhagong mak
        self.motor_12f_bohu_1 = 0  # chhanjang finil
        # For Button
        # for the motor Flag # full  open/close Flag
        self.bhc_1_o_1_flg = False  # chhan myang bohu
        self.bhc_1_c_1_flg = False
        self.bhc_2_o_1_flg = False  # chhwa chuk myon bohu
        self.bhc_2_c_1_flg = False
        self.bhc_3_o_1_flg = False  # uu chuk myon bohu
        self.bhc_3_c_1_flg = False
        self.bhc_4_o_1_flg = False  # hu myon bohu
        self.bhc_4_c_1_flg = False
        self.bhc_5_o_1_flg = False  # chhanjang bohu
        self.bhc_5_c_1_flg = False
        self.bhc_6_o_1_flg = False  # chhanjang chhagong mak
        self.bhc_6_c_1_flg = False
        self.bhc_7_o_1_flg = False  # chhanjang finil
        self.bhc_7_c_1_flg = False
        self.bhc_8_o_1_flg = False  # uu chuk myon bohu
        self.bhc_8_c_1_flg = False
        self.bhc_9_o_1_flg = False  # hu myon bohu
        self.bhc_9_c_1_flg = False
        self.bhc_10_o_1_flg = False  # chhanjang bohu
        self.bhc_10_c_1_flg = False
        self.bhc_11_o_1_flg = False  # chhanjang chhagong mak
        self.bhc_11_c_1_flg = False
        self.bhc_12_o_1_flg = False  # chhanjang finil
        self.bhc_12_c_1_flg = False

        # OPEN CLOSE ---------------- send this to the server
        self.bohu_1f_oc_1 = None
        self.bohu_2f_oc_1 = None
        self.bohu_3f_oc_1 = None
        self.bohu_4f_oc_1 = None
        self.bohu_5f_oc_1 = None
        self.bohu_6f_oc_1 = None
        self.bohu_7f_oc_1 = None
        self.bohu_8f_oc_1 = None
        self.bohu_9f_oc_1 = None
        self.bohu_10f_oc_1 = None
        self.bohu_11f_oc_1 = None
        self.bohu_12f_oc_1 = None

        # button

        self.bhc_1_o_1 = None  # chhan myang bohu
        self.bhc_1_c_1 = None
        self.bhc_2_o_1 = None  # chhwa chuk myon bohu
        self.bhc_2_c_1 = None
        self.bhc_3_o_1 = None  # uu chuk myon bohu
        self.bhc_3_c_1 = None
        self.bhc_4_o_1 = None  # hu myon bohu
        self.bhc_4_c_1 = None
        self.bhc_5_o_1 = None  # chhanjang bohu
        self.bhc_5_c_1 = None
        self.bhc_6_o_1 = None  # chhanjang chhagong mak
        self.bhc_6_c_1 = None
        self.bhc_7_o_1 = None  # chhanjang finil
        self.bhc_7_c_1 = None
        self.bhc_8_o_1 = None   # bhou 08
        self.bhc_8_c_1 = None
        self.bhc_9_o_1 = None   # bhou 09
        self.bhc_9_c_1 = None
        self.bhc_10_o_1 = None   # bhou 10
        self.bhc_10_c_1 = None
        self.bhc_11_o_1 = None   # bhou 11
        self.bhc_11_c_1 = None
        self.bhc_12_o_1 = None   # bhou 12
        self.bhc_12_c_1 = None

        # sudong-2-- page 3
        #
        # # for the flag status of the other control systems--------------- flags-- AUTO FLAGS

        self.fegi_o_1 = False
        self.hongi_o_1 = False
        self.co2_o_1 = False
        self.fog_o_1 = False
        self.sumag_o_1 = False
        self.bog_o_1 = False
        self.ngh_o_1 = False
        self.sp01_o_1 = False
        self.yudong_fan1_o_1 = False
        self.yudong_fan2_o_1 = False

        # OPEN CLOSE VALUE STORE
        self.fegi_oc_1 = None
        self.hongi_oc_1 = None
        self.co2_oc_1 = None
        self.fog_oc_1 = None
        self.sumag_oc_1 = None
        self.bog_oc_1 = None
        self.ngh_oc_1 = None
        self.sp01_oc_1 = None
        self.yudong_fan1_oc_1 = None
        self.yudong_fan2_oc_1 = None
        # ---------wait flags
        self.fg_wt_1_flg = False
        # button  #sudong-2-- page 3
        self.yudong_fan_1_cy_1 = None  # -yudong fan 1 # chhak/ yak
        self.yudong_fan_1_uc_1 = None  # unjan / chhangji
        self.yudong_fan_2_cy_1 = None  # yudong fan2     # chhak/ yak
        self.yudong_fan_2_uc_1 = None  # unjan / chhangji
        self.sumag_1 = None  # -sumag
        self.bogwangdong_1 = None  # flash_light
        self.fog_valve_1 = None  # -fog valve
        self.hongi_fan_1 = None  # -Hongi fan
        self.fegi_fan_1 = None  # -fegi fan
        self.co2_1 = None  # -co2
        self.nangbangi_1 = None
        self.sp01_1 = None

        self.psv_sen_flg = False
        self.psv_man_flg = False
        self.psv_ato_flg = False
        self.psv_sen_slave_flg = False
        # auto
        # --------------------------------------   chanjang salchang-  page -05--------------------SETTING
        self.rain_max_temp_1 = 0
        # ----------------------first--floor 1-chung -------chhuk-jang-
        # sel#f.motor_1f_chuk_1=None #chhanje(second)// Time For Motor Full  length ++ +++++ ALREADY DECLEARED ??+++++
        # -salchang-1--

        self.s1_1f_chuk_temp_1 = 0  # temperature
        self.s1_1f_chuk_o_h_1 = 0  # open Hour
        self.s1_1f_chuk_o_m_1 = 0  # open minute
        self.s1_1f_chuk_c_h_1 = 0  # close hour
        self.s1_1f_chuk_c_m_1 = 0  # close minute
        self.s1_1f_chuk_stp_1 = 0  # sutep(second)// Time for moving Motor Step
        # -salchang-2-- -
        self.s2_1f_chuk_temp_1 = 0  # temperature
        self.s2_1f_chuk_o_h_1 = 0  # open Hour
        self.s2_1f_chuk_o_m_1 = 0  # open minute
        self.s2_1f_chuk_c_h_1 = 0  # close hour
        self.s2_1f_chuk_c_m_1 = 0  # close minute
        self.s2_1f_chuk_stp_1 = 0  # sutep(second)
        # -salchang-3--
        self.s3_1f_chuk_temp_1 = 0  # temperature
        self.s3_1f_chuk_o_h_1 = 0  # open Hour
        self.s3_1f_chuk_o_m_1 = 0  # open minute
        self.s3_1f_chuk_c_h_1 = 0  # close hour
        self.s3_1f_chuk_c_m_1 = 0  # close minute
        self.s3_1f_chuk_stp_1 = 0  # sutep(second)
        # -salchang-4--
        self.s4_1f_chuk_temp_1 = 0  # temperature
        self.s4_1f_chuk_o_h_1 = 0  # open Hour
        self.s4_1f_chuk_o_m_1 = 0  # open minute
        self.s4_1f_chuk_c_h_1 = 0  # close hour
        self.s4_1f_chuk_c_m_1 = 0  # close minute
        self.s4_1f_chuk_stp_1 = 0  # sutep(second)
        # -salchang-5--
        self.s5_1f_chuk_temp_1 = 0  # temperature
        self.s5_1f_chuk_o_h_1 = 0  # open Hour
        self.s5_1f_chuk_o_m_1 = 0  # open minute
        self.s5_1f_chuk_c_h_1 = 0  # close hour
        self.s5_1f_chuk_c_m_1 = 0  # close minute
        self.s5_1f_chuk_stp_1 = 0  # sutep(second)
        # -salchang-6--
        self.s6_1f_chuk_temp_1 = 0  # temperature
        self.s6_1f_chuk_o_h_1 = 0  # open Hour
        self.s6_1f_chuk_o_m_1 = 0  # open minute
        self.s6_1f_chuk_c_h_1 = 0  # close hour
        self.s6_1f_chuk_c_m_1 = 0  # close minute
        self.s6_1f_chuk_stp_1 = 0  # sutep(second)
        # ------ -------BUTTON- FOR MANUAL
        # -chhwa--chuk-chhangi--dongchak-
        self.chuk_1f_ch_btn_1 = None
        # -uu--chuk-chhangi--dongchak-
        self.chuk_1f_uu_btn_1 = None
        # --chhuk-jang-chhangi--dongchak- rain
        self.chuk_1f_rain_ud_btn_1 = None
        # -chhadong--sudong-
        self.chuk_1f_ato_man_1 = None

        # ----------second---floor-----2-chung -chhuk-jang-
        # -salchang-
        # -salchang-1--
        self.s1_2f_chuk_temp_1 = 0  # temperature
        self.s1_2f_chuk_o_h_1 = 0  # open Hour
        self.s1_2f_chuk_o_m_1 = 0  # open minute
        self.s1_2f_chuk_c_h_1 = 0  # close hour
        self.s1_2f_chuk_c_m_1 = 0  # close minute
        self.s1_2f_chuk_stp_1 = 0  # sutep(second)// Time for moving Motor Step
        # -salchang-2-- -
        self.s2_2f_chuk_temp_1 = 0  # temperature
        self.s2_2f_chuk_o_h_1 = 0  # open Hour
        self.s2_2f_chuk_o_m_1 = 0  # open minute
        self.s2_2f_chuk_c_h_1 = 0  # close hour
        self.s2_2f_chuk_c_m_1 = 0  # close minute
        self.s2_2f_chuk_stp_1 = 0  # sutep(second)
        # -salchang-3--
        self.s3_2f_chuk_temp_1 = 0  # temperature
        self.s3_2f_chuk_o_h_1 = 0  # open Hour
        self.s3_2f_chuk_o_m_1 = 0  # open minute
        self.s3_2f_chuk_c_h_1 = 0  # close hour
        self.s3_2f_chuk_c_m_1 = 0  # close minute
        self.s3_2f_chuk_stp_1 = 0  # sutep(second)

        # ------ -------BUTTON- FOR MANUAL
        # -chhwa--chuk-chhangi--dongchak-
        self.chuk_2f_ch_btn_1 = None
        # -uu--chuk-chhangi--dongchak-
        self.chuk_2f_uu_btn_1 = None
        # -chhadong--sudong-
        self.chuk_2f_ato_man_1 = None

        # ----------third---floor----3-chung -chhuk-jang-
        # -salchang-
        # -salchang-1--
        self.s1_3f_chuk_temp_1 = 0  # temperature
        self.s1_3f_chuk_o_h_1 = 0  # open Hour
        self.s1_3f_chuk_o_m_1 = 0  # open minute
        self.s1_3f_chuk_c_h_1 = 0  # close hour
        self.s1_3f_chuk_c_m_1 = 0  # close minute
        self.s1_3f_chuk_stp_1 = 0  # sutep(second)// Time for moving Motor Step
        # -salchang-2-- -
        self.s2_3f_chuk_temp_1 = 0  # temperature
        self.s2_3f_chuk_o_h_1 = 0  # open Hour
        self.s2_3f_chuk_o_m_1 = 0  # open minute
        self.s2_3f_chuk_c_h_1 = 0  # close hour
        self.s2_3f_chuk_c_m_1 = 0  # close minute
        self.s2_3f_chuk_stp_1 = 0  # sutep(second)
        # -salchang-3--
        self.s3_3f_chuk_temp_1 = 0  # temperature
        self.s3_3f_chuk_o_h_1 = 0  # open Hour
        self.s3_3f_chuk_o_m_1 = 0  # open minute
        self.s3_3f_chuk_c_h_1 = 0  # close hour
        self.s3_3f_chuk_c_m_1 = 0  # close minute
        self.s3_3f_chuk_stp_1 = 0  # sutep(second)

        # -chhwa--chuk-chhangi--dongchak-
        self.chuk_3f_ch_btn_1 = None
        # -uu--chuk-chhangi--dongchak-
        self.chuk_3f_uu_btn_1 = None
        # -chhadong--sudong-
        self.chuk_3f_ato_man_1 = None

        # -------------chhan-jang-salchang-(setting)-------Dwin--------------------------------------------page 6
        # -----first--flooer----1- ----chhan-jang-
        # -salchang-1--
        self.s1_1f_chan_temp_1 = 0  # temperature
        self.s1_1f_chan_o_h_1 = 0  # open Hour
        self.s1_1f_chan_o_m_1 = 0  # open minute
        self.s1_1f_chan_c_h_1 = 0  # close hour
        self.s1_1f_chan_c_m_1 = 0  # close minute
        self.s1_1f_chan_stp_1 = 0  # sutep(second)
        # -salchang-2-- -
        self.s2_1f_chan_temp_1 = 0  # temperature
        self.s2_1f_chan_o_h_1 = 0  # open Hour
        self.s2_1f_chan_o_m_1 = 0  # open minute
        self.s2_1f_chan_c_h_1 = 0  # close hour
        self.s2_1f_chan_c_m_1 = 0  # close minute
        self.s2_1f_chan_stp_1 = 0  # sutep(second)
        # -salchang-3--
        self.s3_1f_chan_temp_1 = 0  # temperature
        self.s3_1f_chan_o_h_1 = 0  # open Hour
        self.s3_1f_chan_o_m_1 = 0  # open minute
        self.s3_1f_chan_c_h_1 = 0  # close hour
        self.s3_1f_chan_c_m_1 = 0  # close minute
        self.s3_1f_chan_stp_1 = 0  # sutep(second)
        # -salchang-4--
        self.s4_1f_chan_temp_1 = 0  # temperature
        self.s4_1f_chan_o_h_1 = 0  # open Hour
        self.s4_1f_chan_o_m_1 = 0  # open minute
        self.s4_1f_chan_c_h_1 = 0  # close hour
        self.s4_1f_chan_c_m_1 = 0  # close minute
        self.s4_1f_chan_stp_1 = 0  # sutep(second)
        # -salchang-5--
        self.s5_1f_chan_temp_1 = 0  # temperature
        self.s5_1f_chan_o_h_1 = 0  # open Hour
        self.s5_1f_chan_o_m_1 = 0  # open minute
        self.s5_1f_chan_c_h_1 = 0  # close hour
        self.s5_1f_chan_c_m_1 = 0  # close minute
        self.s5_1f_chan_stp_1 = 0  # sutep(second)
        # -salchang-6--
        self.s6_1f_chan_temp_1 = 0  # temperature
        self.s6_1f_chan_o_h_1 = 0  # open Hour
        self.s6_1f_chan_o_m_1 = 0  # open minute
        self.s6_1f_chan_c_h_1 = 0  # close hour
        self.s6_1f_chan_c_m_1 = 0  # close minute
        self.s6_1f_chan_stp_1 = 0  # sutep(second)
        # ----chanjang--1-floor--
        # -chhwa--chuk-chhangi--dongchak-
        self.chan_1f_ch_btn_1 = None
        # -uu--chuk-chhangi--dongchak-
        self.chan_1f_uu_btn_1 = None
        # --chhan-jang-chhangi--dongchak- Rain
        self.chan_1f_rain_ud_btn_1 = None
        # -chhadong--sudong-
        self.chan_1f_ato_man_1 = None
        # ----------second---floor-------------------------2- -chhan-jang-
        # -salchang-
       # -salchang-1--
        self.s1_2f_chan_temp_1 = 0  # temperature
        self.s1_2f_chan_o_h_1 = 0  # open Hour
        self.s1_2f_chan_o_m_1 = 0  # open minute
        self.s1_2f_chan_c_h_1 = 0  # close hour
        self.s1_2f_chan_c_m_1 = 0  # close minute
        self.s1_2f_chan_stp_1 = 0  # sutep(second)
        # -salchang-2-- -
        self.s2_2f_chan_temp_1 = 0  # temperature
        self.s2_2f_chan_o_h_1 = 0  # open Hour
        self.s2_2f_chan_o_m_1 = 0  # open minute
        self.s2_2f_chan_c_h_1 = 0  # close hour
        self.s2_2f_chan_c_m_1 = 0  # close minute
        self.s2_2f_chan_stp_1 = 0  # sutep(second)
        # -salchang-3--
        self.s3_2f_chan_temp_1 = 0  # temperature
        self.s3_2f_chan_o_h_1 = 0  # open Hour
        self.s3_2f_chan_o_m_1 = 0  # open minute
        self.s3_2f_chan_c_h_1 = 0  # close hour
        self.s3_2f_chan_c_m_1 = 0  # close minute
        self.s3_2f_chan_stp_1 = 0  # sutep(second)

        # ---chukjang--2-floor--
        # -chhwa--chuk-chhangi--dongchak-
        self.chan_2f_ch_btn_1 = None
        # -uu--chuk-chhangi--dongchak-
        self.chan_2f_uu_btn_1 = None
        # -chhadong--sudong-
        self.chan_2f_ato_man_1 = None
        # ----------third----------floor----------------------3- -chhan-jang-
        # -salchang-
       # -salchang-1--
        self.s1_3f_chan_temp_1 = 0  # temperature
        self.s1_3f_chan_o_h_1 = 0  # open Hour
        self.s1_3f_chan_o_m_1 = 0  # open minute
        self.s1_3f_chan_c_h_1 = 0  # close hour
        self.s1_3f_chan_c_m_1 = 0  # close minute
        self.s1_3f_chan_stp_1 = 0  # sutep(second)
        # -salchang-2-- -
        self.s2_3f_chan_temp_1 = 0  # temperature
        self.s2_3f_chan_o_h_1 = 0  # open Hour
        self.s2_3f_chan_o_m_1 = 0  # open minute
        self.s2_3f_chan_c_h_1 = 0  # close hour
        self.s2_3f_chan_c_m_1 = 0  # close minute
        self.s2_3f_chan_stp_1 = 0  # sutep(second)
        # -salchang-3--
        self.s3_3f_chan_temp_1 = 0  # temperature
        self.s3_3f_chan_o_h_1 = 0  # open Hour
        self.s3_3f_chan_o_m_1 = 0  # open minute
        self.s3_3f_chan_c_h_1 = 0  # close hour
        self.s3_3f_chan_c_m_1 = 0  # close minute
        self.s3_3f_chan_stp_1 = 0  # sutep(second)

        self.chan_3f_ch_btn_1 = None
        # -uu--chuk-chhangi--dongchak-
        self.chan_3f_uu_btn_1 = None
        # -chhadong--sudong-
        self.chan_3f_ato_man_1 = None

        # -------------back -- front -salchang-(setting)-------Dwin-------------------------------------------back front

        # -----first--flooer----1- ----chanmyang humyan
        # -salchang-1--
        self.s1fwbwt_1 = 0  # temperature
        self.s1fwbw_oh_1 = 0  # open Hour
        self.s1fwbw_om_1 = 0  # open minute
        self.s1fwbw_ch_1 = 0  # close hour
        self.s1fwbw_cm_1 = 0  # close minute
        self.s1fwbw_st_1 = 0  # sutep(second)

        # -salchang-2-- -
        self.s2fwbwt_1 = 0  # temperature
        self.s2fwbw_oh_1 = 0  # open Hour
        self.s2fwbw_om_1 = 0  # open minute
        self.s2fwbw_ch_1 = 0  # close hour
        self.s2fwbw_cm_1 = 0  # close minute
        self.s2fwbw_st_1 = 0  # sutep(second)
        # -salchang-3--
        self.s3fwbwt_1 = 0  # temperature
        self.s3fwbw_oh_1 = 0  # open Hour
        self.s3fwbw_om_1 = 0  # open minute
        self.s3fwbw_ch_1 = 0  # close hour
        self.s3fwbw_cm_1 = 0  # close minute
        self.s3fwbw_st_1 = 0  # sutep(second)
        # -salchang-4--
        self.s4fwbwt_1 = 0  # temperature
        self.s4fwbw_oh_1 = 0  # open Hour
        self.s4fwbw_om_1 = 0  # open minute
        self.s4fwbw_ch_1 = 0  # close hour
        self.s4fwbw_cm_1 = 0  # close minute
        self.s4fwbw_st_1 = 0  # sutep(second)
        # -salchang-5--
        self.s5fwbwt_1 = 0  # temperature
        self.s5fwbw_oh_1 = 0  # open Hour
        self.s5fwbw_om_1 = 0  # open minute
        self.s5fwbw_ch_1 = 0  # close hour
        self.s5fwbw_cm_1 = 0  # close minute
        self.s5fwbw_st_1 = 0  # sutep(second)
        # -salchang-6--
        self.s6fwbwt_1 = 0  # temperature
        self.s6fwbw_oh_1 = 0  # open Hour
        self.s6fwbw_om_1 = 0  # open minute
        self.s6fwbw_ch_1 = 0  # close hour
        self.s6fwbw_cm_1 = 0  # close minute
        self.s6fwbw_st_1 = 0  # sutep(second)
        # ----back-- front --1-floor--
        # -chhwa--chuk-chhangi--dongchak-
        # -chhwa--chuk-chhangi--dongchak-
        self.fwb_1 = None
        # -uu--chuk-chhangi--dongchak-
        self.bwb_1 = None
        # --chhan-jang-chhangi--dongchak- Rain
        self.fwbw_rb_1 = None
        # -chhadong--sudong-
        self.fwbw_am_1 = None

        # 2f---------------- front back control

        # -salchang-1--
        self.s1_f2_fwbwt_1 = 0  # temperature
        self.s1_f2_fwbw_oh_1 = 0  # open Hour
        self.s1_f2_fwbw_om_1 = 0  # open minute
        self.s1_f2_fwbw_ch_1 = 0  # close hour
        self.s1_f2_fwbw_cm_1 = 0  # close minute
        self.s1_f2_fwbw_st_1 = 0  # sutep(second)
        # -salchang-2-- -
        self.s2_f2_fwbwt_1 = 0  # temperature
        self.s2_f2_fwbw_oh_1 = 0  # open Hour
        self.s2_f2_fwbw_om_1 = 0  # open minute
        self.s2_f2_fwbw_ch_1 = 0  # close hour
        self.s2_f2_fwbw_cm_1 = 0  # close minute
        self.s2_f2_fwbw_st_1 = 0  # sutep(second)
        # -salchang-3--
        self.s3_f2_fwbwt_1 = 0  # temperature
        self.s3_f2_fwbw_oh_1 = 0  # open Hour
        self.s3_f2_fwbw_om_1 = 0  # open minute
        self.s3_f2_fwbw_ch_1 = 0  # close hour
        self.s3_f2_fwbw_cm_1 = 0  # close minute
        self.s3_f2_fwbw_st_1 = 0  # sutep(second)
        # ----back-- front --1-floor--

        self.fwb_f2_1 = None
        # -uu--chuk-chhangi--dongchak-
        self.bwb_f2_1 = None
        # --chhan-jang-chhangi--dongchak- Rain
        self.fwbw_rb_f2_1 = None

        # -chhadong--sudong-
        self.fwbw_f2_am_1 = None

        # -------------bohu-curtian-salchang-(setting)--------------------------------------page 7
        # --------전면보온커튼----1--
        self.s_1_bhc_temp_1 = 0  # temperature
        self.s_1_bhc_o_h_1 = 0  # open Hour
        self.s_1_bhc_o_m_1 = 0  # open minute
        self.s_1_bhc_c_h_1 = 0  # close hour
        self.s_1_bhc_c_m_1 = 0  # close minute
        self.s_1_bhc_stp_1 = 0  # sutep(second)
        # ---1--BUTTON--
        # -unjan-chhangi
        self.bhc_1_u_ch_btn_1 = None
        # -chhadong--sudong-
        self. bhc_1_ato_man_1 = None
        # ------좌측면보온커튼---------2--
        self.s_2_bhc_temp_1 = 0  # temperature
        self.s_2_bhc_o_h_1 = 0  # open Hour
        self.s_2_bhc_o_m_1 = 0  # open minute
        self.s_2_bhc_c_h_1 = 0  # close hour
        self.s_2_bhc_c_m_1 = 0  # close minute
        self.s_2_bhc_stp_1 = 0  # sutep(second)
        # ---2-BUTTON--
        # -unjan-chhangi
        self.bhc_2_u_ch_btn_1 = None
        # -chhadong--sudong-
        self.bhc_2_ato_man_1 = None
        # --------우측면보온커튼--------------3--
        self.s_3_bhc_temp_1 = 0  # temperature
        self.s_3_bhc_o_h_1 = 0  # open Hour
        self.s_3_bhc_o_m_1 = 0  # open minute
        self.s_3_bhc_c_h_1 = 0  # close hour
        self.s_3_bhc_c_m_1 = 0  # close minute
        self.s_3_bhc_stp_1 = 0  # sutep(second)

        # ---3--BUTTON--
        # -unjan-chhangi
        self.bhc_3_u_ch_btn_1 = None
        # -chhadong--sudong-
        self.bhc_3_ato_man_1 = None
        # -----------후면보온커튼 -----------4--
        self.s_4_bhc_temp_1 = 0  # temperature
        self.s_4_bhc_o_h_1 = 0  # open Hour
        self.s_4_bhc_o_m_1 = 0  # open minute
        self.s_4_bhc_c_h_1 = 0  # close hour
        self.s_4_bhc_c_m_1 = 0  # close minute
        self.s_4_bhc_stp_1 = 0  # sutep(second)
        # ---4--BUTTON--
        # -unjan-chhangi
        self.bhc_4_u_ch_btn_1 = None
        # -chhadong--sudong-
        self.bhc_4_ato_man_1 = None
        # -----------------천창보온커튼 ------5--

        self.s_5_bhc_temp_1 = 0  # temperature
        self.s_5_bhc_o_h_1 = 0  # open Hour
        self.s_5_bhc_o_m_1 = 0  # open minute
        self.s_5_bhc_c_h_1 = 0  # close hour
        self.s_5_bhc_c_m_1 = 0  # close minute
        self.s_5_bhc_stp_1 = 0  # sutep(second)
        # ---5--BUTTON--
        # -unjan-chhangi
        self.bhc_5_u_ch_btn_1 = None
        # -chhadong--sudong-
        self.bhc_5_ato_man_1 = None
        # -------------천창 차광막 보온커튼-----------6--
        self.s_6_bhc_light_lux_1 = 0  # light intensity (khwangrang)
        self.s_6_bhc_temp_1 = 0  # temperature
        self.s_6_bhc_o_h_1 = 0  # open Hour
        self.s_6_bhc_o_m_1 = 0  # open minute
        self.s_6_bhc_c_h_1 = 0  # close hour
        self.s_6_bhc_c_m_1 = 0  # close minute
        self.s_6_bhc_stp_1 = 0  # sutep(second)
        # ---6--BUTTON--
        # -unjan-chhangi
        self.bhc_6_u_ch_btn_1 = None
        # -chhadong--sudong-
        self.bhc_6_ato_man_1 = None
        # ------------천창보온비닐------------------------------7--
        self.s_7_bhc_temp_1 = 0  # temperature
        self.s_7_bhc_o_h_1 = 0  # open Hour
        self.s_7_bhc_o_m_1 = 0  # open minute
        self.s_7_bhc_c_h_1 = 0  # close hour
        self.s_7_bhc_c_m_1 = 0  # close minute
        self.s_7_bhc_stp_1 = 0  # sutep(second)
        # ---7--------BUTTON--
        # -unjan-chhangi
        self.bhc_7_u_ch_btn_1 = None
        # -chhadong--sudong-
        self.bhc_7_ato_man_1 = None
        # --------우측면보온커튼--------------8--
        self.s_8_bhc_temp_1 = 0  # temperature
        self.s_8_bhc_o_h_1 = 0  # open Hour
        self.s_8_bhc_o_m_1 = 0  # open minute
        self.s_8_bhc_c_h_1 = 0  # close hour
        self.s_8_bhc_c_m_1 = 0  # close minute
        self.s_8_bhc_stp_1 = 0  # sutep(second)

        # ---8--BUTTON--
        # -unjan-chhangi
        self.bhc_8_u_ch_btn_1 = None
        # -chhadong--sudong-
        self.bhc_8_ato_man_1 = None
        # -----------후면보온커튼 -----------9--
        self.s_9_bhc_temp_1 = 0  # temperature
        self.s_9_bhc_o_h_1 = 0  # open Hour
        self.s_9_bhc_o_m_1 = 0  # open minute
        self.s_9_bhc_c_h_1 = 0  # close hour
        self.s_9_bhc_c_m_1 = 0  # close minute
        self.s_9_bhc_stp_1 = 0  # sutep(second)
        # ---9--BUTTON--
        # -unjan-chhangi
        self.bhc_9_u_ch_btn_1 = None
        # -chhadong--sudong-
        self.bhc_9_ato_man_1 = None
        # -----------------천창보온커튼 ------10--

        self.s_10_bhc_temp_1 = 0  # temperature
        self.s_10_bhc_o_h_1 = 0  # open Hour
        self.s_10_bhc_o_m_1 = 0  # open minute
        self.s_10_bhc_c_h_1 = 0  # close hour
        self.s_10_bhc_c_m_1 = 0  # close minute
        self.s_10_bhc_stp_1 = 0  # sutep(second)
        # ---10--BUTTON--
        # -unjan-chhangi
        self.bhc_10_u_ch_btn_1 = None
        # -chhadong--sudong-
        self.bhc_10_ato_man_1 = None
        # -------------천창 차광막 보온커튼-----------11--
        self.s_11_bhc_light_lux_1 = 0  # light intensity (khwangrang)
        self.s_11_bhc_temp_1 = 0  # temperature
        self.s_11_bhc_o_h_1 = 0  # open Hour
        self.s_11_bhc_o_m_1 = 0  # open minute
        self.s_11_bhc_c_h_1 = 0  # close hour
        self.s_11_bhc_c_m_1 = 0  # close minute
        self.s_11_bhc_stp_1 = 0  # sutep(second)
        # ---11--BUTTON--
        # -unjan-chhangi
        self.bhc_11_u_ch_btn_1 = None
        # -chhadong--sudong-
        self.bhc_11_ato_man_1 = None
        # ------------천창보온비닐------------------------------12--
        self.s_12_bhc_temp_1 = 0  # temperature
        self.s_12_bhc_o_h_1 = 0  # open Hour
        self.s_12_bhc_o_m_1 = 0  # open minute
        self.s_12_bhc_c_h_1 = 0  # close hour
        self.s_12_bhc_c_m_1 = 0  # close minute
        self.s_12_bhc_stp_1 = 0  # sutep(second)
        # ---12--------BUTTON--
        # -unjan-chhangi
        self.bhc_12_u_ch_btn_1 = None
        # -chhadong--sudong-
        self.bhc_12_ato_man_1 = None

        # ---------------khitha-salchang-(setting)-------------------Dwin-----page 8
        # --------------------------fegi-fan &---Hongi-fan---fan
        # -------fegi-fan
        self.fegi_fan_temp_1 = 0  # temperature
        self.fegi_fan_o_h_1 = 0  # khadong sijang hour, On
        self.fegi_fan_o_m_1 = 0  # khadong sijang minute, on
        self.fegi_fan_c_h_1 = 0  # khadong chhongro hour, close / off
        self.fegi_fan_c_m_1 = 0  # khadong chhongro minute, close / off
        # -------Hongi-fan
        self.hongi_fan_temp_1 = 0  # temperature
        self.hongi_fan_o_h_1 = 0  # khadong sijang hour, on
        self.hongi_fan_o_m_1 = 0  # khadong sijang minute, on
        self.hongi_fan_c_h_1 = 0  # khadong chhongro hour close / off
        self.hongi_fan_c_m_1 = 0  # khadong chhongro minute close / off
        # fegi-fan & Hongi-fan--BUTTON--
        # -unjan-chhangi
        self.fegi_hongi_u_ch_btn_1 = None
        # -chhadong--sudong-
        self.fegi_hongi_ato_man_1 = None

        # -------------------------------------co2
        # -chhan-myang-bohu-cutton
        self.co2_khoun_1 = 0  # khoun----- Hot  high temperature
        self.co2_chhaun_1 = 0  # chhaun--Low temperature
        self.co2_nongdo_1 = 0  # nongdo--co2  concentration
        # ---co2--BUTTON--
        # -unjan-chhangi
        self.co2_u_ch_btn_1 = None
        # -chhadong--sudong-
        self.co2_ato_man_1 = None
        # ---------------------------fog--valve-
        # --salchang--1
        self.s1_fog_valve_humi_1 = 0  # humidity
        self.s1_fog_valve_run_time_1 = 0  # sigan(run time Time) second
        self.s1_fog_valve_stop_time_1 = 0  # sigan(stop time Time) minute
        # --salchang--2
        self.s2_fog_valve_humi_1 = 0  # humidity
        self.s2_fog_valve_run_time_1 = 0  # sigan(run time Time) second
        self.s2_fog_valve_stop_time_1 = 0  # sigan(stop time Time) minute
        # --salchang--3
        self.s3_fog_valve_humi_1 = 0  # humidity
        self.s3_fog_valve_run_time_1 = 0  # sigan(run time Time) second
        self.s3_fog_valve_stop_time_1 = 0  # sigan(stop time Time) minute
        # ---fog-valve-BUTTON--
        # -unjan-chhangi
        self.fog_valve_u_ch_btn_1 = None
        # -chhadong--sudong-
        self.fog_valve_ato_man_1 = None
        # --------------------------------   sumag-
        # ------yallim
        self.sumag_yallim_h_1 = 0  # hour
        self.sumag_yallim_m_1 = 0  # minute
        # ------thathim
        self.sumag_thathim_h_1 = 0  # hour
        self.sumag_thathim_m_1 = 0  # minute
        # ---sumag-BUTTON--
        # -unjan-chhangi
        self.sumag_u_ch_btn_1 = None
        # -chhadong--sudong-
        self.sumag_ato_man_1 = None

        # --------------------------------  ---sp1_ato_man_1--------------------- sp01

        self.sp1_ato_man_1 = None

     # --------------------------------   ---sp2_ato_man_1------------------ sp02

        self.sp2_ato_man_1 = None

        # --------------------------------   bog---wang dong-----------------------bogwangodng
        # ------yallim
        self.bog_yallim_h_1 = 0  # hour
        self.bog_yallim_m_1 = 0  # minute
        # ------thathim
        self.bog_thathim_h_1 = 0  # hour
        self.bog_thathim_m_1 = 0  # minute
        # ---bog-BUTTON--
        # -unjan-chhangi
        self.bog_u_ch_btn_1 = None
        # -chhadong--sudong-
        self.bog_ato_man_1 = None
        # ---------------------------------yudong--fan-1
        # -salchang 1
        self.s1_yudong_fan1_bohayul_1 = 0  # bohayul
        self.s1_yudong_fan1_temp_1 = 0  # dongchank undo(temp)
        self.s1_yudong_fan1_humi_1 = 0  # dongchank subdo(humi)
        # -salchang 2
        self.s2_yudong_fan1_bohayul_1 = 0  # bohayul
        self.s2_yudong_fan1_temp_1 = 0  # dongchank undo(temp)
        self.s2_yudong_fan1_humi_1 = 0  # dongchank subdo(humi)
        # -salchang 3
        self.s3_yudong_fan1_bohayul_1 = 0  # bohayul
        self.s3_yudong_fan1_temp_1 = 0  # dongchank undo(temp)
        self.s3_yudong_fan1_humi_1 = 0  # dongchank subdo(humi)
        # bohayul bojang
        self.yudong_fan1_bohayul_bojang_1 = 0
        # --yudong--fan-1--BUTTON--
        # -unjan-chhangi
        self.yudong_fan1_u_ch_btn_1 = None
        # -chhadong--sudong-
        self.yudong_fan1_ato_man_1 = None
        # ---------------------------------yudong--fan-2
        # -salchang 1
        self.s1_yudong_fan2_bohayul_1 = 0  # bohayul
        self.s1_yudong_fan2_temp_1 = 0  # dongchank undo(temp)
        self.s1_yudong_fan2_humi_1 = 0  # dongchank subdo(humi)
        # -salchang 2
        self.s2_yudong_fan2_bohayul_1 = 0  # bohayul
        self.s2_yudong_fan2_temp_1 = 0  # dongchank undo(temp)
        self.s2_yudong_fan2_humi_1 = 0  # dongchank subdo(humi)
        # -salchang 3
        self.s3_yudong_fan2_bohayul_1 = 0  # bohayul
        self.s3_yudong_fan2_temp_1 = 0  # dongchank undo(temp)
        self.s3_yudong_fan2_humi_1 = 0  # dongchank subdo(humi)
        # bohayul bhojang
        self.yudong_fan2_bohayul_bojang_1 = 0
        # --yudong--fan-2--BUTTON--
        # -unjan-chhangi
        self.yudong_fan2_u_ch_btn_1 = None
        # -chhadong--sudong-
        self.yudong_fan2_ato_man_1 = None

        # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++   SENSOR VARIABLE DECLEAR  +++++++++++++++++

        # +++++++++++++++++++++++++++++++++++++++  ENVIRONMENT OUT  SENSOR VARIABLE DECLEAR +++++  (global for all)
        self.envout_temp_1 = 0
        self.envout_humi_1 = 0
        self.envout_co2_1 = 0
        self.envout_solar_light_1 = 0
        self.rain_1 = 0
        # ++++++++++++++++++++++++++++++++++++++++  ENVIRONMENT IN SENSOR VARIABLE DECLEAR +++
        self.env_in_temp_r_1 = 0
        self.envin_temp_1 = None
        self.envin_humi_1 = None
        self.envin_co2_1 = None
        self.envin_solar_light_1 = None  # ---- (This is also Global for all)
        # --------HMI variable

        # ++++++++++++++++++++++++++++++++++++++++++  SOIL SENSOR VARIABLE DECLEAR +++++
        self.soil_temp_1 = 0
        self.soil_ph_1 = 0
        self.soil_ec_1 = 0
        self.soil_moisture_1 = 0
        self.soil_n_1 = 0
        self.soil_p_1 = 0
        self.soil_k_1 = 0
        # ++++++++++++++++++++++++++++++++++++++++++++ FETTILIZER SENSOR  VARIAB LE DECLEAR++
        self.ftz_n_1 = 0
        self.ftz_p_1 = 0
        self.ftz_k_1 = 0
        self.ftz_ec_1 = 0
        self.ftz_ph_1 = 0

        # +++++++++++++++++++++++++++++++++++++++++++++ WASTE SENSOR  VARIABLE DECLEAR ++
        self.waste_temp_1 = 0
        self.waste_n_1 = 0
        self.waste_p_1 = 0
        self.waste_k_1 = 0
        self.waste_ec_1 = 0
        self.waste_ph_1 = 0
        # +++++++++++++++++++++++++++++++++++++++++++++++  VPD SENSOR VARIABLE DECLEAR +++
        # self.vpd_1 = 0
        # +++++++++++++++++++++++++++++++++++++++++++++++ RTC VARIABLE +++
        self.c_hour_1 = 0
        self.c_min_1 = 0
        self.c_second_1 = 0
