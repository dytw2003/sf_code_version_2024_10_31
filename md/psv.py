import asyncio
# from var import VariableData
# from simple import MQTTClient
import json

# var = VariableData()
# NEED TO CHANGE FOR OTHER HOUSE

# _1":
# _1,


async def rst_atmn(var, client):
    # Topics

    MQTT_TOPIC_RSTATMN = "dytw_1/rstatmn"
    if not var.rst_atmn_flg:
        var.rst_atmn_flg = True
        rst_atmn = {
            "auto_manual_1": var.auto_manual_1,
            "rst_1": var.rst_1,
        }
        # Publish sensor data
        client.publish(MQTT_TOPIC_RSTATMN, json.dumps(rst_atmn))
#         await asyncio.sleep(3)
        var.rst_atmn_flg = False


async def sensor(var, client):
    # Topics
    MQTT_TOPIC_SENSOR = "dytw_1/sensor"
    if not var.psv_sen_flg:
        var.psv_sen_flg = True

        sensor_data = {
            "envout_temp_1": var.envout_temp_1,
            "envout_humi_1": var.envout_humi_1,
            "envout_co2_1": var.envout_co2_1,
            "envout_light_intensity_1": var.envout_solar_light_1,
            "rain_status_1": var.rain_1,
            "envin_temp_1": var.envin_temp_1,
            "envin_humi_1": var.envin_humi_1,
            "envin_co2_1": var.envin_co2_1,
            "envin_light_intensity_1": var.envin_solar_light_1,
            "soil_temp_1": var.soil_temp_1,
            "soil_ph_1": var.soil_ph_1,
            "soil_ec_1": var.soil_ec_1,
            "soil_moisture_1": var.soil_moisture_1,
            "waste_ec_1": var.waste_ec_1,
            "waste_ph_1": var.waste_ph_1,
        }

        # Publish sensor data
        client.publish(MQTT_TOPIC_SENSOR, json.dumps(sensor_data))

        # await asyncio.sleep(3)
        var.psv_sen_flg = False


async def manual(var, client):
    MQTT_TOPIC_MANUAL = "dytw_1/manual"
    if not var.psv_man_flg:
        var.psv_man_flg = True
        # Manual Data JSON
        manual_data = {
            "chuk_ch_1f_o_1": var.chuk_ch_1f_o_1,
            "chuk_ch_1f_c_1": var.chuk_ch_1f_c_1,
            "chuk_ch_2f_o_1": var.chuk_ch_2f_o_1,
            "chuk_ch_2f_c_1": var.chuk_ch_2f_c_1,
            "chuk_ch_3f_o_1": var.chuk_ch_3f_o_1,
            "chuk_ch_3f_c_1": var.chuk_ch_3f_c_1,
            "chuk_uu_1f_o_1": var.chuk_uu_1f_o_1,
            "chuk_uu_1f_c_1": var.chuk_uu_1f_c_1,
            "chuk_uu_2f_o_1": var.chuk_uu_2f_o_1,
            "chuk_uu_2f_c_1": var.chuk_uu_2f_c_1,
            "chuk_uu_3f_o_1": var.chuk_uu_3f_o_1,
            "chuk_uu_3f_c_1": var.chuk_uu_3f_c_1,
            "chan_ch_1f_o_1": var.chan_ch_1f_o_1,
            "chan_ch_1f_c_1": var.chan_ch_1f_c_1,
            "chan_ch_2f_o_1": var.chan_ch_2f_o_1,
            "chan_ch_2f_c_1": var.chan_ch_2f_c_1,
            "chan_ch_3f_o_1": var.chan_ch_3f_o_1,
            "chan_ch_3f_c_1": var.chan_ch_3f_c_1,
            "chan_uu_1f_o_1": var.chan_uu_1f_o_1,
            "chan_uu_1f_c_1": var.chan_uu_1f_c_1,
            "chan_uu_2f_o_1": var.chan_uu_2f_o_1,
            "chan_uu_2f_c_1": var.chan_uu_2f_c_1,
            "chan_uu_3f_o_1": var.chan_uu_3f_o_1,
            "chan_uu_3f_c_1": var.chan_uu_3f_c_1,
            "fw_o_1": var.fw_o_1,
            "fw_c_1": var.fw_c_1,
            "bw_o_1": var.bw_o_1,
            "bw_c_1": var.bw_c_1,
            "bhc_1_o_1": var.bhc_1_o_1,
            "bhc_1_c_1": var.bhc_1_c_1,
            "bhc_2_o_1": var.bhc_2_o_1,
            "bhc_2_c_1": var.bhc_2_c_1,
            "bhc_3_o_1": var.bhc_3_o_1,
            "bhc_3_c_1": var.bhc_3_c_1,
            "bhc_4_o_1": var.bhc_4_o_1,
            "bhc_4_c_1": var.bhc_4_c_1,
            "bhc_5_o_1": var.bhc_5_o_1,
            "bhc_5_c_1": var.bhc_5_c_1,
            "bhc_6_o_1": var.bhc_6_o_1,
            "bhc_6_c_1": var.bhc_6_c_1,
            "bhc_7_o_1": var.bhc_7_o_1,
            "bhc_7_c_1": var.bhc_7_c_1,
            "bhc_8_o_1": var.bhc_8_o_1,
            "bhc_8_c_1": var.bhc_8_c_1,
            "bhc_9_o_1": var.bhc_9_o_1,
            "bhc_9_c_1": var.bhc_9_c_1,
            "bhc_10_o_1": var.bhc_10_o_1,
            "bhc_10_c_1": var.bhc_10_c_1,
            "bhc_11_o_1": var.bhc_11_o_1,
            "bhc_11_c_1": var.bhc_11_c_1,
            "bhc_12_o_1": var.bhc_12_o_1,
            "bhc_12_c_1": var.bhc_12_c_1,
            "yudong_fan_1_cy_1": var.yudong_fan_1_cy_1,
            "yudong_fan_1_uc_1": var.yudong_fan_1_uc_1,
            "yudong_fan_2_cy_1": var.yudong_fan_2_cy_1,
            "yudong_fan_2_uc_1": var.yudong_fan_2_uc_1,
            "sumag_1": var.sumag_1,
            "bogwangdong_1": var.bogwangdong_1,
            "fog_valve_1": var.fog_valve_1,
            "hongi_fan_1": var.hongi_fan_1,
            "fegi_fan_1": var.fegi_fan_1,
            "co2_1": var.co2_1,
        }
        # Publish manual data
        client.publish(MQTT_TOPIC_MANUAL, json.dumps(manual_data))
        # await asyncio.sleep(4)
        var.psv_man_flg = False


async def auto_publish(on_condition, json_data, client):
    MQTT_TOPIC_AUTO = "dytw_1/auto"
    if on_condition == "ON":
        client.publish(MQTT_TOPIC_AUTO, json.dumps(json_data))
    else:
        print(" not auto mode")


async def auto(var, client):

    if not var.psv_ato_flg:
        var.psv_ato_flg = True
        # chukjang

        auto_chuk1f = {
            "rain_max_temp_1": var.rain_max_temp_1,
            "chuk_ch_1f_oc_1": var.chuk_ch_1f_oc_1,
            "chuk_uu_1f_oc_1": var.chuk_uu_1f_oc_1,
            "motor_1f_chuk_1": var.motor_1f_chuk_1,
            "s1_1f_chuk_temp_1": var.s1_1f_chuk_temp_1,
            "s1_1f_chuk_o_h_1": var.s1_1f_chuk_o_h_1,
            "s1_1f_chuk_o_m_1": var.s1_1f_chuk_o_m_1,
            "s1_1f_chuk_c_h_1": var.s1_1f_chuk_c_h_1,
            "s1_1f_chuk_c_m_1": var.s1_1f_chuk_c_m_1,
            "s1_1f_chuk_stp_1": var.s1_1f_chuk_stp_1,
            "s2_1f_chuk_temp_1": var.s2_1f_chuk_temp_1,
            "s2_1f_chuk_o_h_1": var.s2_1f_chuk_o_h_1,
            "s2_1f_chuk_o_m_1": var.s2_1f_chuk_o_m_1,
            "s2_1f_chuk_c_h_1": var.s2_1f_chuk_c_h_1,
            "s2_1f_chuk_c_m_1": var.s2_1f_chuk_c_m_1,
            "s2_1f_chuk_stp_1": var.s2_1f_chuk_stp_1,
            "s3_1f_chuk_temp_1": var.s3_1f_chuk_temp_1,
            "s3_1f_chuk_o_h_1": var.s3_1f_chuk_o_h_1,
            "s3_1f_chuk_o_m_1": var.s3_1f_chuk_o_m_1,
            "s3_1f_chuk_c_h_1": var.s3_1f_chuk_c_h_1,
            "s3_1f_chuk_c_m_1": var.s3_1f_chuk_c_m_1,
            "s3_1f_chuk_stp_1": var.s3_1f_chuk_stp_1,
            "s4_1f_chuk_temp_1": var.s4_1f_chuk_temp_1,
            "s4_1f_chuk_o_h_1": var.s4_1f_chuk_o_h_1,
            "s4_1f_chuk_o_m_1": var.s4_1f_chuk_o_m_1,
            "s4_1f_chuk_c_h_1": var.s4_1f_chuk_c_h_1,
            "s4_1f_chuk_c_m_1": var.s4_1f_chuk_c_m_1,
            "s4_1f_chuk_stp_1": var.s4_1f_chuk_stp_1,
            "s5_1f_chuk_temp_1": var.s5_1f_chuk_temp_1,
            "s5_1f_chuk_o_h_1": var.s5_1f_chuk_o_h_1,
            "s5_1f_chuk_o_m_1": var.s5_1f_chuk_o_m_1,
            "s5_1f_chuk_c_h_1": var.s5_1f_chuk_c_h_1,
            "s5_1f_chuk_c_m_1": var.s5_1f_chuk_c_m_1,
            "s5_1f_chuk_stp_1": var.s5_1f_chuk_stp_1,
            "s6_1f_chuk_temp_1": var.s6_1f_chuk_temp_1,
            "s6_1f_chuk_o_h_1": var.s6_1f_chuk_o_h_1,
            "s6_1f_chuk_o_m_1": var.s6_1f_chuk_o_m_1,
            "s6_1f_chuk_c_h_1": var.s6_1f_chuk_c_h_1,
            "s6_1f_chuk_c_m_1": var.s6_1f_chuk_c_m_1,
            "s6_1f_chuk_stp_1": var.s6_1f_chuk_stp_1,
            "chuk_1f_ch_btn_1": var.chuk_1f_ch_btn_1,
            "chuk_1f_uu_btn_1": var.chuk_1f_uu_btn_1,
            "chuk_1f_rain_ud_btn_1": var.chuk_1f_rain_ud_btn_1,
            "chuk_1f_ato_man_1": var.chuk_1f_ato_man_1,
        }

        auto_chuk2f = {
            "chuk_ch_2f_oc_1": var.chuk_ch_2f_oc_1,
            "chuk_uu_2f_oc_1": var.chuk_uu_2f_oc_1,
            "motor_2f_chuk_1": var.motor_2f_chuk_1,
            "s1_2f_chuk_temp_1": var.s1_2f_chuk_temp_1,
            "s1_2f_chuk_o_h_1": var.s1_2f_chuk_o_h_1,
            "s1_2f_chuk_o_m_1": var.s1_2f_chuk_o_m_1,
            "s1_2f_chuk_c_h_1": var.s1_2f_chuk_c_h_1,
            "s1_2f_chuk_c_m_1": var.s1_2f_chuk_c_m_1,
            "s1_2f_chuk_stp_1": var.s1_2f_chuk_stp_1,
            "s2_2f_chuk_temp_1": var.s2_2f_chuk_temp_1,
            "s2_2f_chuk_o_h_1": var.s2_2f_chuk_o_h_1,
            "s2_2f_chuk_o_m_1": var.s2_2f_chuk_o_m_1,
            "s2_2f_chuk_c_h_1": var.s2_2f_chuk_c_h_1,
            "s2_2f_chuk_c_m_1": var.s2_2f_chuk_c_m_1,
            "s2_2f_chuk_stp_1": var.s2_2f_chuk_stp_1,
            "s3_2f_chuk_temp_1": var.s3_2f_chuk_temp_1,
            "s3_2f_chuk_o_h_1": var.s3_2f_chuk_o_h_1,
            "s3_2f_chuk_o_m_1": var.s3_2f_chuk_o_m_1,
            "s3_2f_chuk_c_h_1": var.s3_2f_chuk_c_h_1,
            "s3_2f_chuk_c_m_1": var.s3_2f_chuk_c_m_1,
            "s3_2f_chuk_stp_1": var.s3_2f_chuk_stp_1,
            "chuk_2f_ch_btn_1": var.chuk_2f_ch_btn_1,
            "chuk_2f_uu_btn_1": var.chuk_2f_uu_btn_1,
            "chuk_2f_ato_man_1": var.chuk_2f_ato_man_1,
        }

        auto_chuk3f = {
            "chuk_ch_3f_oc_1": var.chuk_ch_3f_oc_1,
            "chuk_uu_3f_oc_1": var.chuk_uu_3f_oc_1,
            "motor_3f_chuk_1": var.motor_3f_chuk_1,
            "s1_3f_chuk_temp_1": var.s1_3f_chuk_temp_1,
            "s1_3f_chuk_o_h_1": var.s1_3f_chuk_o_h_1,
            "s1_3f_chuk_o_m_1": var.s1_3f_chuk_o_m_1,
            "s1_3f_chuk_c_h_1": var.s1_3f_chuk_c_h_1,
            "s1_3f_chuk_c_m_1": var.s1_3f_chuk_c_m_1,
            "s1_3f_chuk_stp_1": var.s1_3f_chuk_stp_1,
            "s2_3f_chuk_temp_1": var.s2_3f_chuk_temp_1,
            "s2_3f_chuk_o_h_1": var.s2_3f_chuk_o_h_1,
            "s2_3f_chuk_o_m_1": var.s2_3f_chuk_o_m_1,
            "s2_3f_chuk_c_h_1": var.s2_3f_chuk_c_h_1,
            "s2_3f_chuk_c_m_1": var.s2_3f_chuk_c_m_1,
            "s2_3f_chuk_stp_1": var.s2_3f_chuk_stp_1,
            "s3_3f_chuk_temp_1": var.s3_3f_chuk_temp_1,
            "s3_3f_chuk_o_h_1": var.s3_3f_chuk_o_h_1,
            "s3_3f_chuk_o_m_1": var.s3_3f_chuk_o_m_1,
            "s3_3f_chuk_c_h_1": var.s3_3f_chuk_c_h_1,
            "s3_3f_chuk_c_m_1": var.s3_3f_chuk_c_m_1,
            "s3_3f_chuk_stp_1": var.s3_3f_chuk_stp_1,
            "chuk_3f_ch_btn_1": var.chuk_3f_ch_btn_1,
            "chuk_3f_uu_btn_1": var.chuk_3f_uu_btn_1,
            "chuk_3f_ato_man_1": var.chuk_3f_ato_man_1,
        }

    # chanjang

        auto_chan1f = {
            "rain_max_temp_1": var.rain_max_temp_1,
            "chan_ch_1f_oc_1": var.chan_ch_1f_oc_1,
            "chan_uu_1f_oc_1": var.chan_uu_1f_oc_1,
            "motor_1f_chan_1": var.motor_1f_chan_1,
            "s1_1f_chan_temp_1": var.s1_1f_chan_temp_1,
            "s1_1f_chan_o_h_1": var.s1_1f_chan_o_h_1,
            "s1_1f_chan_o_m_1": var.s1_1f_chan_o_m_1,
            "s1_1f_chan_c_h_1": var.s1_1f_chan_c_h_1,
            "s1_1f_chan_c_m_1": var.s1_1f_chan_c_m_1,
            "s1_1f_chan_stp_1": var.s1_1f_chan_stp_1,
            "s2_1f_chan_temp_1": var.s2_1f_chan_temp_1,
            "s2_1f_chan_o_h_1": var.s2_1f_chan_o_h_1,
            "s2_1f_chan_o_m_1": var.s2_1f_chan_o_m_1,
            "s2_1f_chan_c_h_1": var.s2_1f_chan_c_h_1,
            "s2_1f_chan_c_m_1": var.s2_1f_chan_c_m_1,
            "s2_1f_chan_stp_1": var.s2_1f_chan_stp_1,
            "s3_1f_chan_temp_1": var.s3_1f_chan_temp_1,
            "s3_1f_chan_o_h_1": var.s3_1f_chan_o_h_1,
            "s3_1f_chan_o_m_1": var.s3_1f_chan_o_m_1,
            "s3_1f_chan_c_h_1": var.s3_1f_chan_c_h_1,
            "s3_1f_chan_c_m_1": var.s3_1f_chan_c_m_1,
            "s3_1f_chan_stp_1": var.s3_1f_chan_stp_1,
            "s4_1f_chan_temp_1": var.s4_1f_chan_temp_1,
            "s4_1f_chan_o_h_1": var.s4_1f_chan_o_h_1,
            "s4_1f_chan_o_m_1": var.s4_1f_chan_o_m_1,
            "s4_1f_chan_c_h_1": var.s4_1f_chan_c_h_1,
            "s4_1f_chan_c_m_1": var.s4_1f_chan_c_m_1,
            "s4_1f_chan_stp_1": var.s4_1f_chan_stp_1,
            "s5_1f_chan_temp_1": var.s5_1f_chan_temp_1,
            "s5_1f_chan_o_h_1": var.s5_1f_chan_o_h_1,
            "s5_1f_chan_o_m_1": var.s5_1f_chan_o_m_1,
            "s5_1f_chan_c_h_1": var.s5_1f_chan_c_h_1,
            "s5_1f_chan_c_m_1": var.s5_1f_chan_c_m_1,
            "s5_1f_chan_stp_1": var.s5_1f_chan_stp_1,
            "s6_1f_chan_temp_1": var.s6_1f_chan_temp_1,
            "s6_1f_chan_o_h_1": var.s6_1f_chan_o_h_1,
            "s6_1f_chan_o_m_1": var.s6_1f_chan_o_m_1,
            "s6_1f_chan_c_h_1": var.s6_1f_chan_c_h_1,
            "s6_1f_chan_c_m_1": var.s6_1f_chan_c_m_1,
            "s6_1f_chan_stp_1": var.s6_1f_chan_stp_1,
            "chan_1f_ch_btn_1": var.chan_1f_ch_btn_1,
            "chan_1f_uu_btn_1": var.chan_1f_uu_btn_1,
            "chan_1f_rain_ud_btn_1": var.chan_1f_rain_ud_btn_1,
            "chan_1f_ato_man_1": var.chan_1f_ato_man_1,
        }

        auto_chan2f = {
            "chan_ch_2f_oc_1": var.chan_ch_2f_oc_1,
            "chan_uu_2f_oc_1": var.chan_uu_2f_oc_1,
            "motor_2f_chan_1": var.motor_2f_chan_1,
            "s1_2f_chan_temp_1": var.s1_2f_chan_temp_1,
            "s1_2f_chan_o_h_1": var.s1_2f_chan_o_h_1,
            "s1_2f_chan_o_m_1": var.s1_2f_chan_o_m_1,
            "s1_2f_chan_c_h_1": var.s1_2f_chan_c_h_1,
            "s1_2f_chan_c_m_1": var.s1_2f_chan_c_m_1,
            "s1_2f_chan_stp_1": var.s1_2f_chan_stp_1,
            "s2_2f_chan_temp_1": var.s2_2f_chan_temp_1,
            "s2_2f_chan_o_h_1": var.s2_2f_chan_o_h_1,
            "s2_2f_chan_o_m_1": var.s2_2f_chan_o_m_1,
            "s2_2f_chan_c_h_1": var.s2_2f_chan_c_h_1,
            "s2_2f_chan_c_m_1": var.s2_2f_chan_c_m_1,
            "s2_2f_chan_stp_1": var.s2_2f_chan_stp_1,
            "s3_2f_chan_temp_1": var.s3_2f_chan_temp_1,
            "s3_2f_chan_o_h_1": var.s3_2f_chan_o_h_1,
            "s3_2f_chan_o_m_1": var.s3_2f_chan_o_m_1,
            "s3_2f_chan_c_h_1": var.s3_2f_chan_c_h_1,
            "s3_2f_chan_c_m_1": var.s3_2f_chan_c_m_1,
            "s3_2f_chan_stp_1": var.s3_2f_chan_stp_1,
            "chan_2f_ch_btn_1": var.chan_2f_ch_btn_1,
            "chan_2f_uu_btn_1": var.chan_2f_uu_btn_1,
            "chan_2f_ato_man_1": var.chan_2f_ato_man_1,
        }

        auto_chan3f = {
            "chan_ch_3f_oc_1": var.chan_ch_3f_oc_1,
            "chan_uu_3f_oc_1": var.chan_uu_3f_oc_1,
            "motor_3f_chan_1": var.motor_3f_chan_1,
            "s1_3f_chan_temp_1": var.s1_3f_chan_temp_1,
            "s1_3f_chan_o_h_1": var.s1_3f_chan_o_h_1,
            "s1_3f_chan_o_m_1": var.s1_3f_chan_o_m_1,
            "s1_3f_chan_c_h_1": var.s1_3f_chan_c_h_1,
            "s1_3f_chan_c_m_1": var.s1_3f_chan_c_m_1,
            "s1_3f_chan_stp_1": var.s1_3f_chan_stp_1,
            "s2_3f_chan_temp_1": var.s2_3f_chan_temp_1,
            "s2_3f_chan_o_h_1": var.s2_3f_chan_o_h_1,
            "s2_3f_chan_o_m_1": var.s2_3f_chan_o_m_1,
            "s2_3f_chan_c_h_1": var.s2_3f_chan_c_h_1,
            "s2_3f_chan_c_m_1": var.s2_3f_chan_c_m_1,
            "s2_3f_chan_stp_1": var.s2_3f_chan_stp_1,
            "s3_3f_chan_temp_1": var.s3_3f_chan_temp_1,
            "s3_3f_chan_o_h_1": var.s3_3f_chan_o_h_1,
            "s3_3f_chan_o_m_1": var.s3_3f_chan_o_m_1,
            "s3_3f_chan_c_h_1": var.s3_3f_chan_c_h_1,
            "s3_3f_chan_c_m_1": var.s3_3f_chan_c_m_1,
            "s3_3f_chan_stp_1": var.s3_3f_chan_stp_1,
            "chan_3f_ch_btn_1": var.chan_3f_ch_btn_1,
            "chan_3f_uu_btn_1": var.chan_3f_uu_btn_1,
            "chan_3f_ato_man_1": var.chan_3f_ato_man_1,
        }
    # # front back windows
    #     auto_fwbw = {
    #         "fw_oc_1": var.fw_oc_1,
    #         "bw_oc_1": var.bw_oc_1,
    #         "mfwbw_1": var.mfwbw_1,
    #         "s1fwbwt_1": var.s1fwbwt_1,
    #         "s1fwbw_oh_1": var.s1fwbw_oh_1,
    #         "s1fwbw_om_1": var.s1fwbw_om_1,
    #         "s1fwbw_ch_1": var.s1fwbw_ch_1,
    #         "s1fwbw_cm_1": var.s1fwbw_cm_1,
    #         "s1fwbw_st_1": var.s1fwbw_st_1,
    #         "s2fwbwt_1": var.s2fwbwt_1,
    #         "s2fwbw_oh_1": var.s2fwbw_oh_1,
    #         "s2fwbw_om_1": var.s2fwbw_om_1,
    #         "s2fwbw_ch_1": var.s2fwbw_ch_1,
    #         "s2fwbw_cm_1": var.s2fwbw_cm_1,
    #         "s2fwbw_st_1": var.s2fwbw_st_1,
    #         "s3fwbwt_1": var.s3fwbwt_1,
    #         "s3fwbw_oh_1": var.s3fwbw_oh_1,
    #         "s3fwbw_om_1": var.s3fwbw_om_1,
    #         "s3fwbw_ch_1": var.s3fwbw_ch_1,
    #         "s3fwbw_cm_1": var.s3fwbw_cm_1,
    #         "s3fwbw_st_1": var.s3fwbw_st_1,
    #         "s4fwbwt_1": var.s4fwbwt_1,
    #         "s4fwbw_oh_1": var.s4fwbw_oh_1,
    #         "s4fwbw_om_1": var.s4fwbw_om_1,
    #         "s4fwbw_ch_1": var.s4fwbw_ch_1,
    #         "s4fwbw_cm_1": var.s4fwbw_cm_1,
    #         "s4fwbw_st_1": var.s4fwbw_st_1,
    #         "s5fwbwt_1": var.s5fwbwt_1,
    #         "s5fwbw_oh_1": var.s5fwbw_oh_1,
    #         "s5fwbw_om_1": var.s5fwbw_om_1,
    #         "s5fwbw_ch_1": var.s5fwbw_ch_1,
    #         "s5fwbw_cm_1": var.s5fwbw_cm_1,
    #         "s5fwbw_st_1": var.s5fwbw_st_1,
    #         "s6fwbwt_1": var.s6fwbwt_1,
    #         "s6fwbw_oh_1": var.s6fwbw_oh_1,
    #         "s6fwbw_om_1": var.s6fwbw_om_1,
    #         "s6fwbw_ch_1": var.s6fwbw_ch_1,
    #         "s6fwbw_cm_1": var.s6fwbw_cm_1,
    #         "s6fwbw_st_1": var.s6fwbw_st_1,
    #         "fwb_1": var.fwb_1,
    #         "bwb_1": var.bwb_1,
    #         "fwbw_rb_1": var.fwbw_rb_1,
    #         "fwbw_am_1": var.fwbw_am_1,
    #     }

    # bohu curtain

        auto_bohu1 = {
            "bohu_1f_oc_1": var.bohu_1f_oc_1,
            "motor_1f_bohu_1": var.motor_1f_bohu_1,
            "s_1_bhc_temp_1": var.s_1_bhc_temp_1,
            "s_1_bhc_o_h_1": var.s_1_bhc_o_h_1,
            "s_1_bhc_o_m_1": var.s_1_bhc_o_m_1,
            "s_1_bhc_c_h_1": var.s_1_bhc_c_h_1,
            "s_1_bhc_c_m_1": var.s_1_bhc_c_m_1,
            "s_1_bhc_stp_1": var.s_1_bhc_stp_1,
            "bhc_1_u_ch_btn_1": var.bhc_1_u_ch_btn_1,
            "bhc_1_ato_man_1": var.bhc_1_ato_man_1,
        }

        auto_bohu2 = {
            "bohu_2f_oc_1": var.bohu_2f_oc_1,
            "motor_2f_bohu_1": var.motor_2f_bohu_1,
            "s_2_bhc_temp_1": var.s_2_bhc_temp_1,
            "s_2_bhc_o_h_1": var.s_2_bhc_o_h_1,
            "s_2_bhc_o_m_1": var.s_2_bhc_o_m_1,
            "s_2_bhc_c_h_1": var.s_2_bhc_c_h_1,
            "s_2_bhc_c_m_1": var.s_2_bhc_c_m_1,
            "s_2_bhc_stp_1": var.s_2_bhc_stp_1,
            "bhc_2_u_ch_btn_1": var.bhc_2_u_ch_btn_1,
            "bhc_2_ato_man_1": var.bhc_2_ato_man_1,
        }

        auto_bohu3 = {
            "bohu_3f_oc_1": var.bohu_3f_oc_1,
            "motor_3f_bohu_1": var.motor_3f_bohu_1,
            "s_3_bhc_temp_1": var.s_3_bhc_temp_1,
            "s_3_bhc_o_h_1": var.s_3_bhc_o_h_1,
            "s_3_bhc_o_m_1": var.s_3_bhc_o_m_1,
            "s_3_bhc_c_h_1": var.s_3_bhc_c_h_1,
            "s_3_bhc_c_m_1": var.s_3_bhc_c_m_1,
            "s_3_bhc_stp_1": var.s_3_bhc_stp_1,
            "bhc_3_u_ch_btn_1": var.bhc_3_u_ch_btn_1,
            "bhc_3_ato_man_1": var.bhc_3_ato_man_1,
        }

        auto_bohu4 = {
            "bohu_4f_oc_1": var.bohu_4f_oc_1,
            "motor_4f_bohu_1": var.motor_4f_bohu_1,
            "s_4_bhc_temp_1": var.s_4_bhc_temp_1,
            "s_4_bhc_o_h_1": var.s_4_bhc_o_h_1,
            "s_4_bhc_o_m_1": var.s_4_bhc_o_m_1,
            "s_4_bhc_c_h_1": var.s_4_bhc_c_h_1,
            "s_4_bhc_c_m_1": var.s_4_bhc_c_m_1,
            "s_4_bhc_stp_1": var.s_4_bhc_stp_1,
            "bhc_4_u_ch_btn_1": var.bhc_4_u_ch_btn_1,
            "bhc_4_ato_man_1": var.bhc_4_ato_man_1,
        }

        auto_bohu5 = {
            "bohu_5f_oc_1": var.bohu_5f_oc_1,
            "motor_5f_bohu_1": var.motor_5f_bohu_1,
            "s_5_bhc_temp_1": var.s_5_bhc_temp_1,
            "s_5_bhc_o_h_1": var.s_5_bhc_o_h_1,
            "s_5_bhc_o_m_1": var.s_5_bhc_o_m_1,
            "s_5_bhc_c_h_1": var.s_5_bhc_c_h_1,
            "s_5_bhc_c_m_1": var.s_5_bhc_c_m_1,
            "s_5_bhc_stp_1": var.s_5_bhc_stp_1,
            "bhc_5_u_ch_btn_1": var.bhc_5_u_ch_btn_1,
            "bhc_5_ato_man_1": var.bhc_5_ato_man_1,
        }

        auto_bohu6 = {
            "bohu_6f_oc_1": var.bohu_6f_oc_1,
            "motor_6f_bohu_1": var.motor_6f_bohu_1,
            "s_6_bhc_light_lux_1": var.s_6_bhc_light_lux_1,
            "s_6_bhc_temp_1": var.s_6_bhc_temp_1,
            "s_6_bhc_o_h_1": var.s_6_bhc_o_h_1,
            "s_6_bhc_o_m_1": var.s_6_bhc_o_m_1,
            "s_6_bhc_c_h_1": var.s_6_bhc_c_h_1,
            "s_6_bhc_c_m_1": var.s_6_bhc_c_m_1,
            "s_6_bhc_stp_1": var.s_6_bhc_stp_1,
            "bhc_6_u_ch_btn_1": var.bhc_6_u_ch_btn_1,
            "bhc_6_ato_man_1": var.bhc_6_ato_man_1,
        }

        auto_bohu7 = {
            "bohu_7f_oc_1": var.bohu_7f_oc_1,
            "motor_7f_bohu_1": var.motor_7f_bohu_1,
            "s_7_bhc_temp_1": var.s_7_bhc_temp_1,
            "s_7_bhc_o_h_1": var.s_7_bhc_o_h_1,
            "s_7_bhc_o_m_1": var.s_7_bhc_o_m_1,
            "s_7_bhc_c_h_1": var.s_7_bhc_c_h_1,
            "s_7_bhc_c_m_1": var.s_7_bhc_c_m_1,
            "s_7_bhc_stp_1": var.s_7_bhc_stp_1,
            "bhc_7_u_ch_btn_1": var.bhc_7_u_ch_btn_1,
            "bhc_7_ato_man_1": var.bhc_7_ato_man_1,
        }
        auto_bohu7 = {
            "bohu_7f_oc_1": var.bohu_7f_oc_1,
            "motor_7f_bohu_1": var.motor_7f_bohu_1,
            "s_7_bhc_temp_1": var.s_7_bhc_temp_1,
            "s_7_bhc_o_h_1": var.s_7_bhc_o_h_1,
            "s_7_bhc_o_m_1": var.s_7_bhc_o_m_1,
            "s_7_bhc_c_h_1": var.s_7_bhc_c_h_1,
            "s_7_bhc_c_m_1": var.s_7_bhc_c_m_1,
            "s_7_bhc_stp_1": var.s_7_bhc_stp_1,
            "bhc_7_u_ch_btn_1": var.bhc_7_u_ch_btn_1,
            "bhc_7_ato_man_1": var.bhc_7_ato_man_1,
        }

        auto_bohu8 = {
            "bohu_8f_oc_1": var.bohu_8f_oc_1,
            "motor_8f_bohu_1": var.motor_8f_bohu_1,
            "s_8_bhc_temp_1": var.s_8_bhc_temp_1,
            "s_8_bhc_o_h_1": var.s_8_bhc_o_h_1,
            "s_8_bhc_o_m_1": var.s_8_bhc_o_m_1,
            "s_8_bhc_c_h_1": var.s_8_bhc_c_h_1,
            "s_8_bhc_c_m_1": var.s_8_bhc_c_m_1,
            "s_8_bhc_stp_1": var.s_8_bhc_stp_1,
            "bhc_8_u_ch_btn_1": var.bhc_8_u_ch_btn_1,
            "bhc_8_ato_man_1": var.bhc_8_ato_man_1,
        }

        # auto_bohu9 = {
        #     "bohu_9f_oc_1": var.bohu_9f_oc_1,
        #     "motor_9f_bohu_1": var.motor_9f_bohu_1,
        #     "s_9_bhc_temp_1": var.s_9_bhc_temp_1,
        #     "s_9_bhc_o_h_1": var.s_9_bhc_o_h_1,
        #     "s_9_bhc_o_m_1": var.s_9_bhc_o_m_1,
        #     "s_9_bhc_c_h_1": var.s_9_bhc_c_h_1,
        #     "s_9_bhc_c_m_1": var.s_9_bhc_c_m_1,
        #     "s_9_bhc_stp_1": var.s_9_bhc_stp_1,
        #     "bhc_9_u_ch_btn_1": var.bhc_9_u_ch_btn_1,
        #     "bhc_9_ato_man_1": var.bhc_9_ato_man_1,
        # }

        # auto_bohu10 = {
        #     "bohu_10f_oc_1": var.bohu_10f_oc_1,
        #     "motor_10f_bohu_1": var.motor_10f_bohu_1,
        #     "s_10_bhc_temp_1": var.s_10_bhc_temp_1,
        #     "s_10_bhc_o_h_1": var.s_10_bhc_o_h_1,
        #     "s_10_bhc_o_m_1": var.s_10_bhc_o_m_1,
        #     "s_10_bhc_c_h_1": var.s_10_bhc_c_h_1,
        #     "s_10_bhc_c_m_1": var.s_10_bhc_c_m_1,
        #     "s_10_bhc_stp_1": var.s_10_bhc_stp_1,
        #     "bhc_10_u_ch_btn_1": var.bhc_10_u_ch_btn_1,
        #     "bhc_10_ato_man_1": var.bhc_10_ato_man_1,
        # }

        # auto_bohu11 = {
        #     "bohu_11f_oc_1": var.bohu_11f_oc_1,
        #     "motor_11f_bohu_1": var.motor_11f_bohu_1,
        #     "s_11_bhc_temp_1": var.s_11_bhc_temp_1,
        #     "s_11_bhc_o_h_1": var.s_11_bhc_o_h_1,
        #     "s_11_bhc_o_m_1": var.s_11_bhc_o_m_1,
        #     "s_11_bhc_c_h_1": var.s_11_bhc_c_h_1,
        #     "s_11_bhc_c_m_1": var.s_11_bhc_c_m_1,
        #     "s_11_bhc_stp_1": var.s_11_bhc_stp_1,
        #     "bhc_11_u_ch_btn_1": var.bhc_11_u_ch_btn_1,
        #     "bhc_11_ato_man_1": var.bhc_11_ato_man_1,
        # }

        # auto_bohu12 = {
        #     "bohu_12f_oc_1": var.bohu_12f_oc_1,
        #     "motor_12f_bohu_1": var.motor_12f_bohu_1,
        #     "s_12_bhc_temp_1": var.s_12_bhc_temp_1,
        #     "s_12_bhc_o_h_1": var.s_12_bhc_o_h_1,
        #     "s_12_bhc_o_m_1": var.s_12_bhc_o_m_1,
        #     "s_12_bhc_c_h_1": var.s_12_bhc_c_h_1,
        #     "s_12_bhc_c_m_1": var.s_12_bhc_c_m_1,
        #     "s_12_bhc_stp_1": var.s_12_bhc_stp_1,
        #     "bhc_12_u_ch_btn_1": var.bhc_12_u_ch_btn_1,
        #     "bhc_12_ato_man_1": var.bhc_12_ato_man_1,
        # }

        auto_fh = {
            "fegi_oc_1": var.fegi_oc_1,
            "hongi_oc_1": var.hongi_oc_1,
            "fegi_fan_temp_1": var.fegi_fan_temp_1,
            "fegi_fan_o_h_1": var.fegi_fan_o_h_1,
            "fegi_fan_o_m_1": var.fegi_fan_o_m_1,
            "fegi_fan_c_h_1": var.fegi_fan_c_h_1,
            "fegi_fan_c_m_1": var.fegi_fan_c_m_1,
            "hongi_fan_temp_1": var.hongi_fan_temp_1,
            "hongi_fan_o_h_1": var.hongi_fan_o_h_1,
            "hongi_fan_o_m_1": var.hongi_fan_o_m_1,
            "hongi_fan_c_h_1": var.hongi_fan_c_h_1,
            "hongi_fan_c_m_1": var.hongi_fan_c_m_1,
            "fegi_hongi_u_ch_btn_1": var.fegi_hongi_u_ch_btn_1,
            "fegi_hongi_ato_man_1": var.fegi_hongi_ato_man_1,
        }

        # auto_co2 = {
        #     "co2_oc_1": var.co2_oc_1,
        #     "co2_khoun_1": var.co2_khoun_1,
        #     "co2_chhaun_1": var.co2_chhaun_1,
        #     "co2_nongdo_1": var.co2_nongdo_1,
        #     "co2_u_ch_btn_1": var.co2_u_ch_btn_1,
        #     "co2_ato_man_1": var.co2_ato_man_1,
        # }

        # auto_fog = {
        #     "fog_oc_1": var.fog_oc_1,
        #     "s1_fog_valve_humi_1": var.s1_fog_valve_humi_1,
        #     "s1_fog_valve_run_time_1": var.s1_fog_valve_run_time_1,
        #     "s1_fog_valve_stop_time_1": var.s1_fog_valve_stop_time_1,
        #     "s2_fog_valve_humi_1": var.s2_fog_valve_humi_1,
        #     "s2_fog_valve_run_time_1": var.s2_fog_valve_run_time_1,
        #     "s2_fog_valve_stop_time_1": var.s2_fog_valve_stop_time_1,
        #     "s3_fog_valve_humi_1": var.s3_fog_valve_humi_1,
        #     "s3_fog_valve_run_time_1": var.s3_fog_valve_run_time_1,
        #     "s3_fog_valve_stop_time_1": var.s3_fog_valve_stop_time_1,
        #     "fog_valve_u_ch_btn_1": var.fog_valve_u_ch_btn_1,
        #     "fog_valve_ato_man_1": var.fog_valve_ato_man_1,
        # }

        # auto_sumag = {
        #     "sumag_oc_1": var.sumag_oc_1,
        #     "sumag_yallim_h_1": var.sumag_yallim_h_1,
        #     "sumag_yallim_m_1": var.sumag_yallim_m_1,
        #     "sumag_thathim_h_1": var.sumag_thathim_h_1,
        #     "sumag_thathim_m_1": var.sumag_thathim_m_1,
        #     "sumag_u_ch_btn_1": var.sumag_u_ch_btn_1,
        #     "sumag_ato_man_1": var.sumag_ato_man_1,
        # }

        # auto_bog = {
        #     "bog_oc_1": var.bog_oc_1,
        #     "bog_yallim_h_1": var.bog_yallim_h_1,
        #     "bog_yallim_m_1": var.bog_yallim_m_1,
        #     "bog_thathim_h_1": var.bog_thathim_h_1,
        #     "bog_thathim_m_1": var.bog_thathim_m_1,
        #     "bog_u_ch_btn_1": var.bog_u_ch_btn_1,
        #     "bog_ato_man_1": var.bog_ato_man_1,
        # }
        # auto_bog = {
        #     "bog_oc_1": var.bog_oc_1,
        #     "bog_yallim_h_1": var.bog_yallim_h_1,
        #     "bog_yallim_m_1": var.bog_yallim_m_1,
        #     "bog_thathim_h_1": var.bog_thathim_h_1,
        #     "bog_thathim_m_1": var.bog_thathim_m_1,
        #     "bog_u_ch_btn_1": var.bog_u_ch_btn_1,
        #     "bog_ato_man_1": var.bog_ato_man_1,
        # }

        # auto_yudong_1 = {
        #     "yudong_fan1_oc_1": var.yudong_fan1_oc_1,
        #     "s1_yudong_fan1_bohayul_1": var.s1_yudong_fan1_bohayul_1,
        #     "s1_yudong_fan1_temp_1": var.s1_yudong_fan1_temp_1,
        #     "s1_yudong_fan1_humi_1": var.s1_yudong_fan1_humi_1,
        #     "s2_yudong_fan1_bohayul_1": var.s2_yudong_fan1_bohayul_1,
        #     "s2_yudong_fan1_temp_1": var.s2_yudong_fan1_temp_1,
        #     "s2_yudong_fan1_humi_1": var.s2_yudong_fan1_humi_1,
        #     "s3_yudong_fan1_bohayul_1": var.s3_yudong_fan1_bohayul_1,
        #     "s3_yudong_fan1_temp_1": var.s3_yudong_fan1_temp_1,
        #     "s3_yudong_fan1_humi_1": var.s3_yudong_fan1_humi_1,
        #     "yudong_fan1_bohayul_bojang_1": var.yudong_fan1_bohayul_bojang_1,
        #     "yudong_fan1_u_ch_btn_1": var.yudong_fan1_u_ch_btn_1,
        #     "yudong_fan1_ato_man_1": var.yudong_fan1_ato_man_1,
        # }

        # auto_yudong_2 = {
        #     "yudong_fan2_oc_1": var.yudong_fan2_oc_1,
        #     "s1_yudong_fan2_bohayul_1": var.s1_yudong_fan2_bohayul_1,
        #     "s1_yudong_fan2_temp_1": var.s1_yudong_fan2_temp_1,
        #     "s1_yudong_fan2_humi_1": var.s1_yudong_fan2_humi_1,
        #     "s2_yudong_fan2_bohayul_1": var.s2_yudong_fan2_bohayul_1,
        #     "s2_yudong_fan2_temp_1": var.s2_yudong_fan2_temp_1,
        #     "s2_yudong_fan2_humi_1": var.s2_yudong_fan2_humi_1,
        #     "s3_yudong_fan2_bohayul_1": var.s3_yudong_fan2_bohayul_1,
        #     "s3_yudong_fan2_temp_1": var.s3_yudong_fan2_temp_1,
        #     "s3_yudong_fan2_humi_1": var.s3_yudong_fan2_humi_1,
        #     "yudong_fan2_bohayul_bojang_1": var.yudong_fan2_bohayul_bojang_1,
        #     "yudong_fan2_u_ch_btn_1": var.yudong_fan2_u_ch_btn_1,
        #     "yudong_fan2_ato_man_1": var.yudong_fan2_ato_man_1,
        # }

        # chukjang
        tasks = [
            # chuk
            auto_publish(var.chuk_1f_ato_man_1, auto_chuk1f, client),
            auto_publish(var.chuk_2f_ato_man_1, auto_chuk2f, client),
            auto_publish(var.chuk_3f_ato_man_1, auto_chuk3f, client),
            # chan
            auto_publish(var.chan_1f_ato_man_1, auto_chan1f, client),
            auto_publish(var.chan_2f_ato_man_1, auto_chan2f, client),
            auto_publish(var.chan_3f_ato_man_1, auto_chan3f, client),
            # # front back
            # auto_publish(var.fwbw_am_1, auto_fwbw, client),
            # bohu
            auto_publish(var.bhc_1_ato_man_1, auto_bohu1, client),
            auto_publish(var.bhc_2_ato_man_1, auto_bohu2, client),
            auto_publish(var.bhc_3_ato_man_1, auto_bohu3, client),
            auto_publish(var.bhc_4_ato_man_1, auto_bohu4, client),
            auto_publish(var.bhc_5_ato_man_1, auto_bohu5, client),
            auto_publish(var.bhc_6_ato_man_1, auto_bohu6, client),
            # auto_publish(var.bhc_7_ato_man_1, auto_bohu7, client),
            # auto_publish(var.bhc_8_ato_man_1, auto_bohu8, client),

            # auto_publish(var.bhc_9_ato_man_1, auto_bohu9, client),
            # auto_publish(var.bhc_10_ato_man_1, auto_bohu10, client),
            # auto_publish(var.bhc_11_ato_man_1, auto_bohu11, client),
            # auto_publish(var.bhc_12_ato_man_1, auto_bohu12, client),
            # other AC
            auto_publish(var.fegi_hongi_ato_man_1, auto_fh, client),
            # auto_publish(var.co2_ato_man_1, auto_co2, client),
            # auto_publish(var.fog_valve_ato_man_1, auto_fog, client),
            # auto_publish(var.sumag_ato_man_1, auto_sumag, client),
            # auto_publish(var.bog_ato_man_1, auto_bog, client),
            # auto_publish(var.yudong_fan1_ato_man_1, auto_yudong_1, client),
            # auto_publish(var.yudong_fan2_ato_man_1, auto_yudong_2, client),

        ]

        await asyncio.gather(*tasks)

        # await asyncio.sleep(3)
        var.psv_ato_flg = False


async def publish_sensor(var, client):
    await asyncio.gather(
        sensor(var, client),
        manual(var, client),
        auto(var, client),
        rst_atmn(var, client),


    )
