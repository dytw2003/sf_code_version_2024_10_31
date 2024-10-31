# for the motor Flag
import json
from md.var import VariableData
import uasyncio as asyncio
var = VariableData()

# NEED TO CHANGE FOR OTHER HOUSE
# _1_flg
# oc_1"


async def motor_flags(var):
   # MQTT_TOPIC_MANUAL = b"dytw_1"
   # CHUKJANG
    if var.chuk_ch_1f_o_1_flg == True:
        setattr(var, "chuk_ch_1f_oc_1", "OPEN")
        # client.publish(MQTT_TOPIC_MANUAL, json.dumps({"chuk_ch_1f_oc_1":"OPEN"}))

    if var.chuk_ch_1f_c_1_flg == True:
        setattr(var, "chuk_ch_1f_oc_1", "CLOSED")
        # client.publish(MQTT_TOPIC_MANUAL, json.dumps({"chuk_ch_1f_oc_1":"CLOSED"}))

    if var.chuk_ch_2f_o_1_flg == True:
        setattr(var, "chuk_ch_2f_oc_1", "OPEN")
        # client.publish(MQTT_TOPIC_MANUAL, json.dumps({"chuk_ch_2f_oc_1":"OPEN"}))
    if var.chuk_ch_2f_c_1_flg == True:
        setattr(var, "chuk_ch_2f_oc_1", "CLOSED")
        # client.publish(MQTT_TOPIC_MANUAL, json.dumps({"chuk_ch_2f_oc_1":"CLOSED"}))

    if var.chuk_ch_3f_o_1_flg == True:
        setattr(var, "chuk_ch_3f_oc_1", "OPEN")
        # client.publish(MQTT_TOPIC_MANUAL, json.dumps({"chuk_ch_3f_oc_1":"OPEN"}))
    if var.chuk_ch_3f_c_1_flg == True:
        setattr(var, "chuk_ch_3f_oc_1", "CLOSED")
        # client.publish(MQTT_TOPIC_MANUAL, json.dumps({"chuk_ch_3f_oc_1":"CLOSED"}))
    # right uuchuk
    if var.chuk_uu_1f_o_1_flg == True:
        setattr(var, "chuk_uu_1f_oc_1", "OPEN")
        # client.publish(MQTT_TOPIC_MANUAL, json.dumps({"chuk_uu_1f_oc_1":"OPEN"}))
    if var.chuk_uu_1f_c_1_flg == True:
        setattr(var, "chuk_uu_1f_oc_1", "CLOSED")
        # client.publish(MQTT_TOPIC_MANUAL, json.dumps({"chuk_uu_1f_oc_1":"CLOSED"}))

    if var.chuk_uu_2f_o_1_flg == True:
        setattr(var, "chuk_uu_2f_oc_1", "OPEN")
        # client.publish(MQTT_TOPIC_MANUAL, json.dumps({"chuk_uu_2f_oc_1":"OPEN"}))
    if var.chuk_uu_2f_c_1_flg == True:
        setattr(var, "chuk_uu_2f_oc_1", "CLOSED")
        # client.publish(MQTT_TOPIC_MANUAL, json.dumps({"chuk_uu_2f_oc_1":"CLOSED"}))

    if var.chuk_uu_3f_o_1_flg == True:
        setattr(var, "chuk_uu_3f_oc_1", "OPEN")
        # client.publish(MQTT_TOPIC_MANUAL, json.dumps({"chuk_uu_3f_oc_1":"OPEN"}))
    if var.chuk_uu_3f_c_1_flg == True:
        setattr(var, "chuk_uu_3f_oc_1", "CLOSED")
        # client.publish(MQTT_TOPIC_MANUAL, json.dumps({"chuk_uu_3f_oc_1":"CLOSED"}))


# chanjaang

    if var.chan_ch_1f_o_1_flg == True:
        setattr(var, "chan_ch_1f_oc_1", "OPEN")
        # client.publish(MQTT_TOPIC_MANUAL, json.dumps({"chan_ch_1f_oc_1":"OPEN"}))
    if var.chan_ch_1f_c_1_flg == True:
        setattr(var, "chan_ch_1f_oc_1", "CLOSED")
        # client.publish(MQTT_TOPIC_MANUAL, json.dumps({"chan_ch_1f_oc_1":"CLOSED"}))

    if var.chan_ch_2f_o_1_flg == True:
        setattr(var, "chan_ch_2f_oc_1", "OPEN")
        # client.publish(MQTT_TOPIC_MANUAL, json.dumps({"chan_ch_2f_oc_1":"OPEN"}))
    if var.chan_ch_2f_c_1_flg == True:
        setattr(var, "chan_ch_2f_oc_1", "CLOSED")
        # client.publish(MQTT_TOPIC_MANUAL, json.dumps({"chan_ch_2f_oc_1":"CLOSED"}))

    if var.chan_ch_3f_o_1_flg == True:
        setattr(var, "chan_ch_3f_oc_1", "OPEN")
        # client.publish(MQTT_TOPIC_MANUAL, json.dumps({"chan_ch_3f_oc_1":"OPEN"}))
    if var.chan_ch_3f_c_1_flg == True:
        setattr(var, "chan_ch_3f_oc_1", "CLOSED")
        # client.publish(MQTT_TOPIC_MANUAL, json.dumps({"chan_ch_3f_oc_1":"CLOSED"}))
    # right uuchuk
    if var.chan_uu_1f_o_1_flg == True:
        setattr(var, "chan_uu_1f_oc_1", "OPEN")
        # client.publish(MQTT_TOPIC_MANUAL, json.dumps({"chan_uu_1f_oc_1":"OPEN"}))
    if var.chan_uu_1f_c_1_flg == True:
        setattr(var, "chan_uu_1f_oc_1", "CLOSED")
        # client.publish(MQTT_TOPIC_MANUAL, json.dumps({"chan_uu_1f_oc_1":"CLOSED"}))

    if var.chan_uu_2f_o_1_flg == True:
        setattr(var, "chan_uu_2f_oc_1", "OPEN")
        # client.publish(MQTT_TOPIC_MANUAL, json.dumps({"chan_uu_2f_oc_1":"OPEN"}))
    if var.chan_uu_2f_c_1_flg == True:
        setattr(var, "chan_uu_2f_oc_1", "CLOSED")
        # client.publish(MQTT_TOPIC_MANUAL, json.dumps({"chan_uu_2f_oc_1":"CLOSED"}))

    if var.chan_uu_3f_o_1_flg == True:
        setattr(var, "chan_uu_3f_oc_1", "OPEN")
        # client.publish(MQTT_TOPIC_MANUAL, json.dumps({"chan_uu_3f_oc_1":"OPEN"}))
    if var.chan_uu_3f_c_1_flg == True:
        setattr(var, "chan_uu_3f_oc_1", "CLOSED")
        # client.publish(MQTT_TOPIC_MANUAL, json.dumps({"chan_uu_3f_oc_1":"CLOSED"}))

    # ------------ fron and back smart farm windows
    if var.fw_c_1_flg == True:
        setattr(var, "fw_oc_1", "CLOSED")
        # client.publish(MQTT_TOPIC_MANUAL, json.dumps({"fw_oc_1":"CLOSED"}))
    if var.fw_o_1_flg == True:
        setattr(var, "fw_oc_1", "OPEN")
        # client.publish(MQTT_TOPIC_MANUAL, json.dumps({"fw_oc_1":"OPEN"}))
    if var.bw_c_1_flg == True:
        setattr(var, "bw_oc_1", "CLOSED")
        # client.publish(MQTT_TOPIC_MANUAL, json.dumps({"bw_oc_1":"CLOSED"}))
    if var.bw_o_1_flg == True:
        setattr(var, "bw_oc_1", "OPEN")
        # client.publish(MQTT_TOPIC_MANUAL, json.dumps({"bw_oc_1":"OPEN"}))


# bho hu cutton
    # 1
    if var.bhc_1_o_1_flg == True:
        setattr(var, "bohu_1f_oc_1", "OPEN")
        # client.publish(MQTT_TOPIC_MANUAL, json.dumps({"bohu_1f_oc_1":"OPEN"}))
    if var.bhc_1_c_1_flg == True:
        setattr(var, "bohu_1f_oc_1", "CLOSED")
        # client.publish(MQTT_TOPIC_MANUAL, json.dumps({"bohu_1f_oc_1":"CLOSED"}))
    # 2
    if var.bhc_2_o_1_flg == True:
        setattr(var, "bohu_2f_oc_1", "OPEN")
        # client.publish(MQTT_TOPIC_MANUAL, json.dumps({"bohu_2f_oc_1":"OPEN"}))
    if var.bhc_2_c_1_flg == True:
        setattr(var, "bohu_2f_oc_1", "CLOSED")
        # client.publish(MQTT_TOPIC_MANUAL, json.dumps({"bohu_2f_oc_1":"CLOSED"}))
    # 3
    if var.bhc_3_o_1_flg == True:
        setattr(var, "bohu_3f_oc_1", "OPEN")
        # client.publish(MQTT_TOPIC_MANUAL, json.dumps({"bohu_3f_oc_1":"OPEN"}))
    if var.bhc_3_c_1_flg == True:
        setattr(var, "bohu_3f_oc_1", "CLOSED")
        # client.publish(MQTT_TOPIC_MANUAL, json.dumps({"bohu_3f_oc_1":"CLOSED"}))
    # 4
    if var.bhc_4_o_1_flg == True:
        setattr(var, "bohu_4f_oc_1", "OPEN")
        # client.publish(MQTT_TOPIC_MANUAL, json.dumps({"bohu_4f_oc_1":"OPEN"}))
    if var.bhc_4_c_1_flg == True:
        setattr(var, "bohu_4f_oc_1", "CLOSED")
        # client.publish(MQTT_TOPIC_MANUAL, json.dumps({"bohu_4f_oc_1":"CLOSED"}))
    # 5
    if var.bhc_5_o_1_flg == True:
        setattr(var, "bohu_5f_oc_1", "OPEN")
        # client.publish(MQTT_TOPIC_MANUAL, json.dumps({"bohu_5f_oc_1":"OPEN"}))
    if var.bhc_5_c_1_flg == True:
        setattr(var, "bohu_5f_oc_1", "CLOSED")
        # client.publish(MQTT_TOPIC_MANUAL, json.dumps({"bohu_5f_oc_1":"CLOSED"}))
    # 6
    if var.bhc_6_o_1_flg == True:
        setattr(var, "bohu_6f_oc_1", "OPEN")
        # client.publish(MQTT_TOPIC_MANUAL, json.dumps({"bohu_6f_oc_1":"OPEN"}))
    if var.bhc_6_c_1_flg == True:
        setattr(var, "bohu_6f_oc_1", "CLOSED")
        # client.publish(MQTT_TOPIC_MANUAL, json.dumps({"bohu_6f_oc_1":"CLOSED"}))
    # 7
    if var.bhc_7_o_1_flg == True:
        setattr(var, "bohu_7f_oc_1", "OPEN")
        # client.publish(MQTT_TOPIC_MANUAL, json.dumps({"bohu_7f_oc_1":"OPEN"}))
    if var.bhc_7_c_1_flg == True:
        setattr(var, "bohu_7f_oc_1", "CLOSED")
        # client.publish(MQTT_TOPIC_MANUAL, json.dumps({"bohu_7f_oc_1":"CLOSED"}))


async def flag_to_oc(var):
    while True:
        await motor_flags(var)
        await asyncio.sleep(2)
