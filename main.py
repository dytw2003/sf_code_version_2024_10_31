<<<<<<< HEAD
# main.py
# CHANGE FOR THE OTHER HOUSE
# rst_1
import uasyncio as asyncio
import gc
import network
import machine
import json
from md.atc_bc import bc_1f_atc, bc_2f_atc, bc_3f_atc, bc_4f_atc, bc_5f_atc, bc_6f_atc, bc_7f_atc, bc_8f_atc   # , bc_9f_atc,bc_10f_atc, bc_11f_atc, bc_12f_atc
from md.atc_ac import fegi_fan_control, hongi_fan_control #, bog_control, sumag_control, fog_control_s1, fog_control_s2, fog_control_s3, co2_control
from md.load import load_csv_to_var_mqtt  # load_csv_to_var,
# from md.atc_fb import fw_2f_atc_s1, fw_2f_atc_s2, fw_2f_atc_s3
# from md.atc_fb import bw_2f_atc_s1, bw_2f_atc_s2, bw_2f_atc_s3
# from md.atc_fb import fw_1f_atc_s1, fw_1f_atc_s2, fw_1f_atc_s3, fw_1f_atc_s4, fw_1f_atc_s5, fw_1f_atc_s6
# from md.atc_fb import bw_1f_atc_s1, bw_1f_atc_s2, bw_1f_atc_s3, bw_1f_atc_s4, bw_1f_atc_s5, bw_1f_atc_s6
from md.atc_sw import sw_3f_right_atc_s1, sw_3f_right_atc_s2, sw_3f_right_atc_s3
from md.atc_sw import sw_3f_left_atc_s1, sw_3f_left_atc_s2, sw_3f_left_atc_s3

from md.atc_sw import sw_2f_right_atc_s1, sw_2f_right_atc_s2, sw_2f_right_atc_s3
from md.atc_sw import sw_2f_left_atc_s1, sw_2f_left_atc_s2, sw_2f_left_atc_s3

from md.atc_sw import sw_1f_right_atc_s1, sw_1f_right_atc_s2, sw_1f_right_atc_s3, sw_1f_right_atc_s4, sw_1f_right_atc_s5, sw_1f_right_atc_s6
from md.atc_sw import sw_1f_left_atc_s1, sw_1f_left_atc_s2, sw_1f_left_atc_s3, sw_1f_left_atc_s4, sw_1f_left_atc_s5, sw_1f_left_atc_s6  





from md.atc_cw_n import cw_3f_right_atc_s1, cw_3f_right_atc_s2, cw_3f_right_atc_s3
from md.atc_cw_n import cw_3f_left_atc_s1, cw_3f_left_atc_s2, cw_3f_left_atc_s3

from md.atc_cw_n import cw_2f_right_atc_s1, cw_2f_right_atc_s2, cw_2f_right_atc_s3
from md.atc_cw_n import cw_2f_left_atc_s1, cw_2f_left_atc_s2, cw_2f_left_atc_s3

from md.atc_cw_n import cw_1f_right_atc_s1, cw_1f_right_atc_s2, cw_1f_right_atc_s3, cw_1f_right_atc_s4, cw_1f_right_atc_s5, cw_1f_right_atc_s6
from md.atc_cw_n import cw_1f_left_atc_s1, cw_1f_left_atc_s2, cw_1f_left_atc_s3, cw_1f_left_atc_s4, cw_1f_left_atc_s5, cw_1f_left_atc_s6

from md.mnc import ac_control_1, ac_control_2, ac_control_3, ac_control_4, ac_control_5, ac_control_6, ac_control_7, ac_control_8

from md.mnc import bc_control_1, bc_control_2, bc_control_3, bc_control_4, bc_control_5, bc_control_6, bc_control_7, bc_control_8 #, bc_control_9, bc_control_10, bc_control_11, bc_control_12
#from md.mnc import fw_control_1f, bw_control_1f, fw_control_2f, bw_control_2f

from md.mnc import sd_control_left_1f, sd_control_left_2f, sd_control_left_3f, sd_control_right_1f, sd_control_right_2f, sd_control_right_3f

from md.mnc import cw_control_left_1f, cw_control_left_2f, cw_control_left_3f, cw_control_right_1f, cw_control_right_2f, cw_control_right_3f

from md.sv import store_var

from md.psv import publish_sensor

from md.fs import flag_to_oc
from md.am import am_status
from md.rn import read_rain_status
from md.rs import read_sensors
from md.rtc import current_rtc
from md.var import VariableData
from md.io import GPIOController
from md.simple import MQTTClient
# if master is connected

uart_hmi = machine.UART(5, baudrate=115200)  # Example UART initialization
var = VariableData()
gpio = GPIOController()
network_connected = False  # Flag to track network status
cloud_client = None  # Cloud MQTT client
local_client = None  # Local MQTT client


async def check_network_connection(retries=5, delay=2):
    global network_connected
    nic = network.LAN()
    nic.active(True)
    attempt = 0
    while attempt < retries and not network_connected:
        try:
            if nic.isconnected():
                print("-----------------------Ethernet connected")
                print("IP Address:", nic.ifconfig()[0])
                network_connected = True
            else:
                print(
                    f"Attempt {attempt + 1} failed: No Ethernet connection. Retrying...")
                attempt += 1
        except OSError as e:
            print(f"Network check failed with error: {e}")
        await asyncio.sleep(delay)

    if not network_connected:
        print("Failed to connect to Ethernet after multiple attempts.")
# Common MQTT callback for CLOUD clients


def mqtt_callback_cloud(topic, msg):
    global cloud_client
    global local_client
    try:
        msg_decoded = msg.decode('utf-8').strip()
        print(f"Received MQTT message: {msg_decoded}")
        try:
            json_data = json.loads(msg_decoded)
            for switch_name, switch_state in json_data.items():
                # Pass cloud_client or missing argument here
                asyncio.create_task(
                    store_var(var, switch_name, switch_state, local_client, cloud_client))
        except ValueError:  # Catch ValueError instead of JSONDecodeError
            switch_data = msg_decoded.split(":")
            if len(switch_data) == 2:
                switch_name = switch_data[0].strip().strip('{"}')
                switch_state = switch_data[1].strip().strip('"}')
                # Pass cloud_client or missing argument here
                asyncio.create_task(
                    store_var(var, switch_name, switch_state, local_client, cloud_client))
            else:
                print(f"Invalid message format: {msg_decoded}")
    except Exception as e:
        print("Error processing MQTT message:", e)

# Common MQTT callback for LOCAL clients


def mqtt_callback_local(topic, msg):
    global local_client
    global cloud_client
    try:
        msg_decoded = msg.decode('utf-8').strip()
        print(f"Received MQTT message: {msg_decoded}")
        try:
            json_data = json.loads(msg_decoded)
            for switch_name, switch_state in json_data.items():
                # Pass local_client or missing argument here
                asyncio.create_task(
                    store_var(var, switch_name, switch_state, local_client, cloud_client))
        except ValueError:  # Catch ValueError instead of JSONDecodeError
            switch_data = msg_decoded.split(":")
            if len(switch_data) == 2:
                switch_name = switch_data[0].strip().strip('{"}')
                switch_state = switch_data[1].strip().strip('"}')
                # Pass client or missing argument here
                asyncio.create_task(
                    store_var(var, switch_name, switch_state, local_client, cloud_client))
            else:
                print(f"Invalid message format: {msg_decoded}")
    except Exception as e:
        print("Error processing MQTT message:", e)
# Setup cloud MQTT client


async def setup_cloud_mqtt():
    global cloud_client
    MQTT_BROKER = "www.dytw.kr"
    MQTT_PORT = 1883
    MQTT_TOPIC_SUBSCRIBE = b"dytw"  #----------- change the topic ID 
    MQTT_CLIENT_ID = "cloud_dytw--s---h1"

    cloud_client = MQTTClient(MQTT_CLIENT_ID, MQTT_BROKER, port=MQTT_PORT)
    try:
        cloud_client.connect()
        cloud_client.set_callback(mqtt_callback_cloud)
        cloud_client.subscribe(MQTT_TOPIC_SUBSCRIBE)
        print("Connected to cloud MQTT broker and subscribed to topic.")
    except Exception as e:
        print("Error connecting to cloud MQTT broker:", e)

# Setup local MQTT client


async def setup_local_mqtt():
    global local_client
    MQTT_BROKER = "172.30.1.70"  # Local broker IP
    MQTT_PORT = 1883
    MQTT_TOPIC_SUBSCRIBE = b"dytw"
    MQTT_CLIENT_ID = "local_dytw--id-h1"

    local_client = MQTTClient(MQTT_CLIENT_ID, MQTT_BROKER, port=MQTT_PORT)

    # if not want to subscribe
    try:
        local_client.connect()
        local_client.set_callback(mqtt_callback_local)
        local_client.subscribe(MQTT_TOPIC_SUBSCRIBE)
        print("Connected to local MQTT broker and subscribed to topic.")
    except Exception as e:
        print("Error connecting to local MQTT broker:", e)

# Task to handle both clients


async def mqtt_task():
    global cloud_client, local_client
    mqtt_failure_count = 0
    max_failures = 10

    while True:
        if cloud_client:
            try:
                cloud_client.check_msg()
            except OSError as e:
                print(f"Cloud MQTT OSError: {e}. Attempting to reconnect.")
                mqtt_failure_count += 1
                cloud_client = None
                if mqtt_failure_count >= max_failures:
                    print("Cloud MQTT failed multiple times. Resetting the board...")
                    machine.reset()

        if local_client:
            try:
                local_client.check_msg()
            except OSError as e:
                print(f"Local MQTT OSError: {e}. Attempting to reconnect.")
                mqtt_failure_count += 1
                local_client = None
                if mqtt_failure_count >= max_failures:
                    print("Local MQTT failed multiple times. Resetting the board...")
                    machine.reset()

        await asyncio.sleep(0.1)


# ====================================== CLOUD NETWORK_MONITOR
async def network_monitor_cloud():
    global network_connected, cloud_client
    while True:
        if not network_connected:
            await check_network_connection()
            if network_connected:
                await setup_cloud_mqtt()
                asyncio.create_task(mqtt_task())
        else:
            if cloud_client:
                try:
                    if not network.LAN().isconnected():
                        print("Ethernet connection lost. Reconnecting...")
                        network_connected = False
                        cloud_client.disconnect()  # Clean up the current cloud_client
                        cloud_client = None  # Reset the client
                except Exception as e:
                    print(f"Error checking network: {e}")
                    network_connected = False
        await asyncio.sleep(1)  # Adjust frequency as needed

# ====================================== LOCAL NETWORK_MONITOR


async def network_monitor_local():
    global network_connected, local_client
    while True:
        if not network_connected:
            await check_network_connection()
            if network_connected:
                await setup_local_mqtt()
                asyncio.create_task(mqtt_task())
        else:
            if local_client:
                try:
                    if not network.LAN().isconnected():
                        print("Ethernet connection lost. Reconnecting...")
                        network_connected = False
                        local_client.disconnect()  # Clean up the current local_client
                        local_client = None  # Reset the local_client
                except Exception as e:
                    print(f"Error checking network: {e}")
                    network_connected = False
        await asyncio.sleep(1)  # Adjust frequency as needed


# ====================================== CLOUD PUBLISHING SENSOR

async def publish_rst_task_cloud():
    while True:
        try:
            if cloud_client:
                print("Publishing to cloud client...")
                await load_csv_to_var_mqtt(cloud_client, var)
                # await publish_sensor(var, cloud_client)
            else:
                print("Cloud client is not available")
        except Exception as e:
            print("Error in cloud publish_sensor task:", e)
        await asyncio.sleep(1)


async def publish_rst_task_local():
    while True:
        try:
            if local_client:
                print("Publishing to local client...")
                await load_csv_to_var_mqtt(local_client, var)
                # await publish_sensor(var, local_client)
            else:
                print("Local client is not available")
        except Exception as e:
            print("Error in local publish_sensor task:", e)
        await asyncio.sleep(1)


async def publish_sensor_task_cloud():
    while True:
        try:
            if cloud_client:
                print("Publishing to cloud client...")
                # await load_csv_to_var_mqtt(cloud_client, var)
                await publish_sensor(var, cloud_client)
            else:
                print("Cloud client is not available")
        except Exception as e:
            print("Error in cloud publish_sensor task:", e)
        await asyncio.sleep(3)


async def publish_sensor_task_local():
    while True:
        try:
            if local_client:
                print("Publishing to local client...")
                # await load_csv_to_var_mqtt(local_client, var)
                await publish_sensor(var, local_client)
            else:
                print("Local client is not available")
        except Exception as e:
            print("Error in local publish_sensor task:", e)
        await asyncio.sleep(3)


async def reset_board_func():
    while True:
        if var.rst_1 == "ON":
            print("--------Resetting the board...---------")
            machine.reset()
        await asyncio.sleep(1)


async def non_network_tasks():
    # selector switch
    asyncio.create_task(am_status(var))
    # actuators flag
    #asyncio.create_task(flag_to_oc(var))
    # rtc
    asyncio.create_task(current_rtc(var))
    # rain
    asyncio.create_task(read_rain_status(var))

    # ================================================  SIDE WINDOWS  MANUAL
    asyncio.create_task(sd_control_left_1f(var, gpio))
    asyncio.create_task(sd_control_left_2f(var, gpio))
    asyncio.create_task(sd_control_left_3f(var, gpio))
    # # Right
    asyncio.create_task(sd_control_right_1f(var, gpio))
    asyncio.create_task(sd_control_right_2f(var, gpio))
    asyncio.create_task(sd_control_right_3f(var, gpio))
    # # ================================================= CEILING WINDOWS MANUAL
    # # Left
    asyncio.create_task(cw_control_left_1f(var, gpio))
    asyncio.create_task(cw_control_left_2f(var, gpio))
    asyncio.create_task(cw_control_left_3f(var, gpio))
    # # Right
    asyncio.create_task(cw_control_right_1f(var, gpio))
    asyncio.create_task(cw_control_right_2f(var, gpio))
    asyncio.create_task(cw_control_right_3f(var, gpio))
    # # # ================================================ FRONT/BACK WINDOES MANUAL
    # asyncio.create_task(fw_control_1f(var, gpio))
    # # BACK WINDOES
    # asyncio.create_task(bw_control_1f(var, gpio))
    # =========================================== BOHU CURTAIN MANUAL
    asyncio.create_task(bc_control_1(var, gpio))
    asyncio.create_task(bc_control_2(var, gpio))
    asyncio.create_task(bc_control_3(var, gpio))
    asyncio.create_task(bc_control_4(var, gpio))
    asyncio.create_task(bc_control_5(var, gpio))
    asyncio.create_task(bc_control_6(var, gpio))
    asyncio.create_task(bc_control_7(var, gpio))
    asyncio.create_task(bc_control_8(var, gpio))
    # asyncio.create_task(bc_control_9(var, gpio))
    # asyncio.create_task(bc_control_10(var, gpio))
    # asyncio.create_task(bc_control_11(var, gpio))
    # asyncio.create_task(bc_control_12(var, gpio))
    # # ============================================ AC CONTROL MANUAL
    asyncio.create_task(ac_control_1(var, gpio))
    asyncio.create_task(ac_control_2(var, gpio))
    asyncio.create_task(ac_control_3(var, gpio))
    asyncio.create_task(ac_control_4(var, gpio))
    asyncio.create_task(ac_control_5(var, gpio))
    asyncio.create_task(ac_control_6(var, gpio))
    asyncio.create_task(ac_control_7(var, gpio))
    asyncio.create_task(ac_control_8(var, gpio))

    # =========================================== CEILINGS WINDOWS AUTO
    # 1F
    # left
    asyncio.create_task(cw_1f_left_atc_s1(var, gpio))
    asyncio.create_task(cw_1f_left_atc_s2(var, gpio))
    asyncio.create_task(cw_1f_left_atc_s3(var, gpio))
    asyncio.create_task(cw_1f_left_atc_s4(var, gpio))
    asyncio.create_task(cw_1f_left_atc_s5(var, gpio))
    asyncio.create_task(cw_1f_left_atc_s6(var, gpio))
    # right
    asyncio.create_task(cw_1f_right_atc_s1(var, gpio))
    asyncio.create_task(cw_1f_right_atc_s2(var, gpio))
    asyncio.create_task(cw_1f_right_atc_s3(var, gpio))
    asyncio.create_task(cw_1f_right_atc_s4(var, gpio))
    asyncio.create_task(cw_1f_right_atc_s5(var, gpio))
    asyncio.create_task(cw_1f_right_atc_s6(var, gpio))
    # 2F
    # left
    asyncio.create_task(cw_2f_left_atc_s1(var, gpio))
    asyncio.create_task(cw_2f_left_atc_s2(var, gpio))
    asyncio.create_task(cw_2f_left_atc_s3(var, gpio))
    # right
    asyncio.create_task(cw_2f_right_atc_s1(var, gpio))
    asyncio.create_task(cw_2f_right_atc_s2(var, gpio))
    asyncio.create_task(cw_2f_right_atc_s3(var, gpio))
    # # 3F
    # # left
    asyncio.create_task(cw_3f_left_atc_s1(var, gpio))
    asyncio.create_task(cw_3f_left_atc_s2(var, gpio))
    asyncio.create_task(cw_3f_left_atc_s3(var, gpio))
    # right
    asyncio.create_task(cw_3f_right_atc_s1(var, gpio))
    asyncio.create_task(cw_3f_right_atc_s2(var, gpio))
    asyncio.create_task(cw_3f_right_atc_s3(var, gpio))
    # ============================================== SIDE WINDOWS AUTO
    # 1f
    # LEFT
    asyncio.create_task(sw_1f_left_atc_s1(var, gpio))
    asyncio.create_task(sw_1f_left_atc_s2(var, gpio))
    asyncio.create_task(sw_1f_left_atc_s3(var, gpio))
    asyncio.create_task(sw_1f_left_atc_s4(var, gpio))
    asyncio.create_task(sw_1f_left_atc_s5(var, gpio))
    asyncio.create_task(sw_1f_left_atc_s6(var, gpio))
    # RIGHT
    asyncio.create_task(sw_1f_right_atc_s1(var, gpio))
    asyncio.create_task(sw_1f_right_atc_s2(var, gpio))
    asyncio.create_task(sw_1f_right_atc_s3(var, gpio))
    asyncio.create_task(sw_1f_right_atc_s4(var, gpio))
    asyncio.create_task(sw_1f_right_atc_s5(var, gpio))
    asyncio.create_task(sw_1f_right_atc_s6(var, gpio))
    # 2f
    # LEFT
    asyncio.create_task(sw_2f_left_atc_s1(var, gpio))
    asyncio.create_task(sw_2f_left_atc_s2(var, gpio))
    asyncio.create_task(sw_2f_left_atc_s3(var, gpio))
    # RIGHT
    asyncio.create_task(sw_2f_right_atc_s1(var, gpio))
    asyncio.create_task(sw_2f_right_atc_s2(var, gpio))
    asyncio.create_task(sw_2f_right_atc_s3(var, gpio))
    # # 3f
    # # LEFT
    asyncio.create_task(sw_3f_left_atc_s1(var, gpio))
    asyncio.create_task(sw_3f_left_atc_s2(var, gpio))
    asyncio.create_task(sw_3f_left_atc_s3(var, gpio))
    # RIGHT
    asyncio.create_task(sw_3f_right_atc_s1(var, gpio))
    asyncio.create_task(sw_3f_right_atc_s2(var, gpio))
    asyncio.create_task(sw_3f_right_atc_s3(var, gpio))

    # # ========================================== FRONT/BACK WINDOWS AUTO
    # # 1f
    # # front
    # asyncio.create_task(fw_1f_atc_s1(var, gpio))
    # asyncio.create_task(fw_1f_atc_s2(var, gpio))
    # asyncio.create_task(fw_1f_atc_s3(var, gpio))
    # asyncio.create_task(fw_1f_atc_s4(var, gpio))
    # asyncio.create_task(fw_1f_atc_s5(var, gpio))
    # asyncio.create_task(fw_1f_atc_s6(var, gpio))
    # # back
    # asyncio.create_task(bw_1f_atc_s1(var, gpio))
    # asyncio.create_task(bw_1f_atc_s2(var, gpio))
    # asyncio.create_task(bw_1f_atc_s3(var, gpio))
    # asyncio.create_task(bw_1f_atc_s4(var, gpio))
    # asyncio.create_task(bw_1f_atc_s5(var, gpio))
    # asyncio.create_task(bw_1f_atc_s6(var, gpio))
    # # 2f
    # # front
    # asyncio.create_task(fw_2f_atc_s1(var, gpio))
    # asyncio.create_task(fw_2f_atc_s2(var, gpio))
    # asyncio.create_task(fw_2f_atc_s3(var, gpio))
    # # back
    # asyncio.create_task(fw_2f_atc_s1(var, gpio))
    # asyncio.create_task(fw_2f_atc_s2(var, gpio))
    # asyncio.create_task(fw_2f_atc_s3(var, gpio))
    # ==========================================BOHU CURTAIN AUTO
    asyncio.create_task(bc_1f_atc(var, gpio))
    asyncio.create_task(bc_2f_atc(var, gpio))
    asyncio.create_task(bc_3f_atc(var, gpio))
    asyncio.create_task(bc_4f_atc(var, gpio))
    asyncio.create_task(bc_5f_atc(var, gpio))
    asyncio.create_task(bc_6f_atc(var, gpio))
    asyncio.create_task(bc_7f_atc(var, gpio))
    asyncio.create_task(bc_8f_atc(var, gpio))
    #asyncio.create_task(bc_9f_atc(var, gpio))
    # asyncio.create_task(bc_10f_atc(var,gpio))
    # asyncio.create_task(bc_11f_atc(var,gpio))
    # asyncio.create_task(bc_12f_atc(var,gpio))
   # ============================================== AC CONTRO AUTO
    asyncio.create_task(fegi_fan_control(var, gpio))
    asyncio.create_task(hongi_fan_control(var, gpio))
    # asyncio.create_task(bog_control(var, gpio))
    # asyncio.create_task(sumag_control(var, gpio))
    # asyncio.create_task(fog_control_s1(var, gpio))
    # asyncio.create_task(fog_control_s2(var, gpio))
    # asyncio.create_task(fog_control_s3(var, gpio))
    # asyncio.create_task(co2_control(var, gpio))


async def main():
    try:
        print("Starting the main loop...")
        # sensors
        asyncio.create_task(read_sensors(var))
        # Local and cloud Network monitor
        asyncio.create_task(network_monitor_cloud())
        # asyncio.create_task(network_monitor_local())
        # publish psv.py to the local and cloud
        asyncio.create_task(publish_sensor_task_cloud())
        # asyncio.create_task(publish_sensor_task_local())
       # Reset query send to the Cloud and Local
        asyncio.create_task(publish_rst_task_cloud())
        # asyncio.create_task(publish_rst_task_local())
        # GPIO control Auto/Manual
        asyncio.create_task(non_network_tasks())

        while True:
            # Debug memory usage periodically
            gc.collect()
            free_memory = gc.mem_free()
            allocated_memory = gc.mem_alloc()
            total_memory = free_memory + allocated_memory
            print("Free Memory: {} bytes".format(free_memory))
            print("Allocated Memory: {} bytes".format(allocated_memory))
            print("Total Memory: {} bytes".format(total_memory))

            await asyncio.sleep(5)
    except Exception as e:
        print(f"Unexpected error in main loop: {e}")

# Start the main loop
asyncio.run(main())
=======
# main.py
# CHANGE FOR THE OTHER HOUSE
# rst_1
import uasyncio as asyncio
import gc
import network
import machine
import json
from md.atc_bc import bc_1f_atc, bc_2f_atc, bc_3f_atc, bc_4f_atc, bc_5f_atc, bc_6f_atc, bc_7f_atc, bc_8f_atc   # , bc_9f_atc,bc_10f_atc, bc_11f_atc, bc_12f_atc
from md.atc_ac import fegi_fan_control, hongi_fan_control #, bog_control, sumag_control, fog_control_s1, fog_control_s2, fog_control_s3, co2_control
from md.load import load_csv_to_var_mqtt  # load_csv_to_var,
# from md.atc_fb import fw_2f_atc_s1, fw_2f_atc_s2, fw_2f_atc_s3
# from md.atc_fb import bw_2f_atc_s1, bw_2f_atc_s2, bw_2f_atc_s3
# from md.atc_fb import fw_1f_atc_s1, fw_1f_atc_s2, fw_1f_atc_s3, fw_1f_atc_s4, fw_1f_atc_s5, fw_1f_atc_s6
# from md.atc_fb import bw_1f_atc_s1, bw_1f_atc_s2, bw_1f_atc_s3, bw_1f_atc_s4, bw_1f_atc_s5, bw_1f_atc_s6
from md.atc_sw import sw_3f_right_atc_s1, sw_3f_right_atc_s2, sw_3f_right_atc_s3
from md.atc_sw import sw_3f_left_atc_s1, sw_3f_left_atc_s2, sw_3f_left_atc_s3

from md.atc_sw import sw_2f_right_atc_s1, sw_2f_right_atc_s2, sw_2f_right_atc_s3
from md.atc_sw import sw_2f_left_atc_s1, sw_2f_left_atc_s2, sw_2f_left_atc_s3

from md.atc_sw import sw_1f_right_atc_s1, sw_1f_right_atc_s2, sw_1f_right_atc_s3, sw_1f_right_atc_s4, sw_1f_right_atc_s5, sw_1f_right_atc_s6
from md.atc_sw import sw_1f_left_atc_s1, sw_1f_left_atc_s2, sw_1f_left_atc_s3, sw_1f_left_atc_s4, sw_1f_left_atc_s5, sw_1f_left_atc_s6  





from md.atc_cw_n import cw_3f_right_atc_s1, cw_3f_right_atc_s2, cw_3f_right_atc_s3
from md.atc_cw_n import cw_3f_left_atc_s1, cw_3f_left_atc_s2, cw_3f_left_atc_s3

from md.atc_cw_n import cw_2f_right_atc_s1, cw_2f_right_atc_s2, cw_2f_right_atc_s3
from md.atc_cw_n import cw_2f_left_atc_s1, cw_2f_left_atc_s2, cw_2f_left_atc_s3

from md.atc_cw_n import cw_1f_right_atc_s1, cw_1f_right_atc_s2, cw_1f_right_atc_s3, cw_1f_right_atc_s4, cw_1f_right_atc_s5, cw_1f_right_atc_s6
from md.atc_cw_n import cw_1f_left_atc_s1, cw_1f_left_atc_s2, cw_1f_left_atc_s3, cw_1f_left_atc_s4, cw_1f_left_atc_s5, cw_1f_left_atc_s6

from md.mnc import ac_control_1, ac_control_2, ac_control_3, ac_control_4, ac_control_5, ac_control_6, ac_control_7, ac_control_8

from md.mnc import bc_control_1, bc_control_2, bc_control_3, bc_control_4, bc_control_5, bc_control_6, bc_control_7, bc_control_8 #, bc_control_9, bc_control_10, bc_control_11, bc_control_12
#from md.mnc import fw_control_1f, bw_control_1f, fw_control_2f, bw_control_2f

from md.mnc import sd_control_left_1f, sd_control_left_2f, sd_control_left_3f, sd_control_right_1f, sd_control_right_2f, sd_control_right_3f

from md.mnc import cw_control_left_1f, cw_control_left_2f, cw_control_left_3f, cw_control_right_1f, cw_control_right_2f, cw_control_right_3f

from md.sv import store_var

from md.psv import publish_sensor

from md.fs import flag_to_oc
from md.am import am_status
from md.rn import read_rain_status
from md.rs import read_sensors
from md.rtc import current_rtc
from md.var import VariableData
from md.io import GPIOController
from md.simple import MQTTClient
# if master is connected

uart_hmi = machine.UART(5, baudrate=115200)  # Example UART initialization
var = VariableData()
gpio = GPIOController()
network_connected = False  # Flag to track network status
cloud_client = None  # Cloud MQTT client
local_client = None  # Local MQTT client


async def check_network_connection(retries=5, delay=2):
    global network_connected
    nic = network.LAN()
    nic.active(True)
    attempt = 0
    while attempt < retries and not network_connected:
        try:
            if nic.isconnected():
                print("-----------------------Ethernet connected")
                print("IP Address:", nic.ifconfig()[0])
                network_connected = True
            else:
                print(
                    f"Attempt {attempt + 1} failed: No Ethernet connection. Retrying...")
                attempt += 1
        except OSError as e:
            print(f"Network check failed with error: {e}")
        await asyncio.sleep(delay)

    if not network_connected:
        print("Failed to connect to Ethernet after multiple attempts.")
# Common MQTT callback for CLOUD clients


def mqtt_callback_cloud(topic, msg):
    global cloud_client
    global local_client
    try:
        msg_decoded = msg.decode('utf-8').strip()
        print(f"Received MQTT message: {msg_decoded}")
        try:
            json_data = json.loads(msg_decoded)
            for switch_name, switch_state in json_data.items():
                # Pass cloud_client or missing argument here
                asyncio.create_task(
                    store_var(var, switch_name, switch_state, local_client, cloud_client))
        except ValueError:  # Catch ValueError instead of JSONDecodeError
            switch_data = msg_decoded.split(":")
            if len(switch_data) == 2:
                switch_name = switch_data[0].strip().strip('{"}')
                switch_state = switch_data[1].strip().strip('"}')
                # Pass cloud_client or missing argument here
                asyncio.create_task(
                    store_var(var, switch_name, switch_state, local_client, cloud_client))
            else:
                print(f"Invalid message format: {msg_decoded}")
    except Exception as e:
        print("Error processing MQTT message:", e)

# Common MQTT callback for LOCAL clients


def mqtt_callback_local(topic, msg):
    global local_client
    global cloud_client
    try:
        msg_decoded = msg.decode('utf-8').strip()
        print(f"Received MQTT message: {msg_decoded}")
        try:
            json_data = json.loads(msg_decoded)
            for switch_name, switch_state in json_data.items():
                # Pass local_client or missing argument here
                asyncio.create_task(
                    store_var(var, switch_name, switch_state, local_client, cloud_client))
        except ValueError:  # Catch ValueError instead of JSONDecodeError
            switch_data = msg_decoded.split(":")
            if len(switch_data) == 2:
                switch_name = switch_data[0].strip().strip('{"}')
                switch_state = switch_data[1].strip().strip('"}')
                # Pass client or missing argument here
                asyncio.create_task(
                    store_var(var, switch_name, switch_state, local_client, cloud_client))
            else:
                print(f"Invalid message format: {msg_decoded}")
    except Exception as e:
        print("Error processing MQTT message:", e)
# Setup cloud MQTT client


async def setup_cloud_mqtt():
    global cloud_client
    MQTT_BROKER = "www.dytw.kr"
    MQTT_PORT = 1883
    MQTT_TOPIC_SUBSCRIBE = b"dytw"  #----------- change the topic ID 
    MQTT_CLIENT_ID = "cloud_dytw--s---h1"

    cloud_client = MQTTClient(MQTT_CLIENT_ID, MQTT_BROKER, port=MQTT_PORT)
    try:
        cloud_client.connect()
        cloud_client.set_callback(mqtt_callback_cloud)
        cloud_client.subscribe(MQTT_TOPIC_SUBSCRIBE)
        print("Connected to cloud MQTT broker and subscribed to topic.")
    except Exception as e:
        print("Error connecting to cloud MQTT broker:", e)

# Setup local MQTT client


async def setup_local_mqtt():
    global local_client
    MQTT_BROKER = "172.30.1.70"  # Local broker IP
    MQTT_PORT = 1883
    MQTT_TOPIC_SUBSCRIBE = b"dytw"
    MQTT_CLIENT_ID = "local_dytw--id-h1"

    local_client = MQTTClient(MQTT_CLIENT_ID, MQTT_BROKER, port=MQTT_PORT)

    # if not want to subscribe
    try:
        local_client.connect()
        local_client.set_callback(mqtt_callback_local)
        local_client.subscribe(MQTT_TOPIC_SUBSCRIBE)
        print("Connected to local MQTT broker and subscribed to topic.")
    except Exception as e:
        print("Error connecting to local MQTT broker:", e)

# Task to handle both clients


async def mqtt_task():
    global cloud_client, local_client
    mqtt_failure_count = 0
    max_failures = 10

    while True:
        if cloud_client:
            try:
                cloud_client.check_msg()
            except OSError as e:
                print(f"Cloud MQTT OSError: {e}. Attempting to reconnect.")
                mqtt_failure_count += 1
                cloud_client = None
                if mqtt_failure_count >= max_failures:
                    print("Cloud MQTT failed multiple times. Resetting the board...")
                    machine.reset()

        if local_client:
            try:
                local_client.check_msg()
            except OSError as e:
                print(f"Local MQTT OSError: {e}. Attempting to reconnect.")
                mqtt_failure_count += 1
                local_client = None
                if mqtt_failure_count >= max_failures:
                    print("Local MQTT failed multiple times. Resetting the board...")
                    machine.reset()

        await asyncio.sleep(0.1)


# ====================================== CLOUD NETWORK_MONITOR
async def network_monitor_cloud():
    global network_connected, cloud_client
    while True:
        if not network_connected:
            await check_network_connection()
            if network_connected:
                await setup_cloud_mqtt()
                asyncio.create_task(mqtt_task())
        else:
            if cloud_client:
                try:
                    if not network.LAN().isconnected():
                        print("Ethernet connection lost. Reconnecting...")
                        network_connected = False
                        cloud_client.disconnect()  # Clean up the current cloud_client
                        cloud_client = None  # Reset the client
                except Exception as e:
                    print(f"Error checking network: {e}")
                    network_connected = False
        await asyncio.sleep(1)  # Adjust frequency as needed

# ====================================== LOCAL NETWORK_MONITOR


async def network_monitor_local():
    global network_connected, local_client
    while True:
        if not network_connected:
            await check_network_connection()
            if network_connected:
                await setup_local_mqtt()
                asyncio.create_task(mqtt_task())
        else:
            if local_client:
                try:
                    if not network.LAN().isconnected():
                        print("Ethernet connection lost. Reconnecting...")
                        network_connected = False
                        local_client.disconnect()  # Clean up the current local_client
                        local_client = None  # Reset the local_client
                except Exception as e:
                    print(f"Error checking network: {e}")
                    network_connected = False
        await asyncio.sleep(1)  # Adjust frequency as needed


# ====================================== CLOUD PUBLISHING SENSOR

async def publish_rst_task_cloud():
    while True:
        try:
            if cloud_client:
                print("Publishing to cloud client...")
                await load_csv_to_var_mqtt(cloud_client, var)
                # await publish_sensor(var, cloud_client)
            else:
                print("Cloud client is not available")
        except Exception as e:
            print("Error in cloud publish_sensor task:", e)
        await asyncio.sleep(1)


async def publish_rst_task_local():
    while True:
        try:
            if local_client:
                print("Publishing to local client...")
                await load_csv_to_var_mqtt(local_client, var)
                # await publish_sensor(var, local_client)
            else:
                print("Local client is not available")
        except Exception as e:
            print("Error in local publish_sensor task:", e)
        await asyncio.sleep(1)


async def publish_sensor_task_cloud():
    while True:
        try:
            if cloud_client:
                print("Publishing to cloud client...")
                # await load_csv_to_var_mqtt(cloud_client, var)
                await publish_sensor(var, cloud_client)
            else:
                print("Cloud client is not available")
        except Exception as e:
            print("Error in cloud publish_sensor task:", e)
        await asyncio.sleep(3)


async def publish_sensor_task_local():
    while True:
        try:
            if local_client:
                print("Publishing to local client...")
                # await load_csv_to_var_mqtt(local_client, var)
                await publish_sensor(var, local_client)
            else:
                print("Local client is not available")
        except Exception as e:
            print("Error in local publish_sensor task:", e)
        await asyncio.sleep(3)


async def reset_board_func():
    while True:
        if var.rst_1 == "ON":
            print("--------Resetting the board...---------")
            machine.reset()
        await asyncio.sleep(1)


async def non_network_tasks():
    # selector switch
    asyncio.create_task(am_status(var))
    # actuators flag
    #asyncio.create_task(flag_to_oc(var))
    # rtc
    asyncio.create_task(current_rtc(var))
    # rain
    asyncio.create_task(read_rain_status(var))

    # ================================================  SIDE WINDOWS  MANUAL
    asyncio.create_task(sd_control_left_1f(var, gpio))
    asyncio.create_task(sd_control_left_2f(var, gpio))
    asyncio.create_task(sd_control_left_3f(var, gpio))
    # # Right
    asyncio.create_task(sd_control_right_1f(var, gpio))
    asyncio.create_task(sd_control_right_2f(var, gpio))
    asyncio.create_task(sd_control_right_3f(var, gpio))
    # # ================================================= CEILING WINDOWS MANUAL
    # # Left
    asyncio.create_task(cw_control_left_1f(var, gpio))
    asyncio.create_task(cw_control_left_2f(var, gpio))
    asyncio.create_task(cw_control_left_3f(var, gpio))
    # # Right
    asyncio.create_task(cw_control_right_1f(var, gpio))
    asyncio.create_task(cw_control_right_2f(var, gpio))
    asyncio.create_task(cw_control_right_3f(var, gpio))
    # # # ================================================ FRONT/BACK WINDOES MANUAL
    # asyncio.create_task(fw_control_1f(var, gpio))
    # # BACK WINDOES
    # asyncio.create_task(bw_control_1f(var, gpio))
    # =========================================== BOHU CURTAIN MANUAL
    asyncio.create_task(bc_control_1(var, gpio))
    asyncio.create_task(bc_control_2(var, gpio))
    asyncio.create_task(bc_control_3(var, gpio))
    asyncio.create_task(bc_control_4(var, gpio))
    asyncio.create_task(bc_control_5(var, gpio))
    asyncio.create_task(bc_control_6(var, gpio))
    asyncio.create_task(bc_control_7(var, gpio))
    asyncio.create_task(bc_control_8(var, gpio))
    # asyncio.create_task(bc_control_9(var, gpio))
    # asyncio.create_task(bc_control_10(var, gpio))
    # asyncio.create_task(bc_control_11(var, gpio))
    # asyncio.create_task(bc_control_12(var, gpio))
    # # ============================================ AC CONTROL MANUAL
    asyncio.create_task(ac_control_1(var, gpio))
    asyncio.create_task(ac_control_2(var, gpio))
    asyncio.create_task(ac_control_3(var, gpio))
    asyncio.create_task(ac_control_4(var, gpio))
    asyncio.create_task(ac_control_5(var, gpio))
    asyncio.create_task(ac_control_6(var, gpio))
    asyncio.create_task(ac_control_7(var, gpio))
    asyncio.create_task(ac_control_8(var, gpio))

    # =========================================== CEILINGS WINDOWS AUTO
    # 1F
    # left
    asyncio.create_task(cw_1f_left_atc_s1(var, gpio))
    asyncio.create_task(cw_1f_left_atc_s2(var, gpio))
    asyncio.create_task(cw_1f_left_atc_s3(var, gpio))
    asyncio.create_task(cw_1f_left_atc_s4(var, gpio))
    asyncio.create_task(cw_1f_left_atc_s5(var, gpio))
    asyncio.create_task(cw_1f_left_atc_s6(var, gpio))
    # right
    asyncio.create_task(cw_1f_right_atc_s1(var, gpio))
    asyncio.create_task(cw_1f_right_atc_s2(var, gpio))
    asyncio.create_task(cw_1f_right_atc_s3(var, gpio))
    asyncio.create_task(cw_1f_right_atc_s4(var, gpio))
    asyncio.create_task(cw_1f_right_atc_s5(var, gpio))
    asyncio.create_task(cw_1f_right_atc_s6(var, gpio))
    # 2F
    # left
    asyncio.create_task(cw_2f_left_atc_s1(var, gpio))
    asyncio.create_task(cw_2f_left_atc_s2(var, gpio))
    asyncio.create_task(cw_2f_left_atc_s3(var, gpio))
    # right
    asyncio.create_task(cw_2f_right_atc_s1(var, gpio))
    asyncio.create_task(cw_2f_right_atc_s2(var, gpio))
    asyncio.create_task(cw_2f_right_atc_s3(var, gpio))
    # # 3F
    # # left
    asyncio.create_task(cw_3f_left_atc_s1(var, gpio))
    asyncio.create_task(cw_3f_left_atc_s2(var, gpio))
    asyncio.create_task(cw_3f_left_atc_s3(var, gpio))
    # right
    asyncio.create_task(cw_3f_right_atc_s1(var, gpio))
    asyncio.create_task(cw_3f_right_atc_s2(var, gpio))
    asyncio.create_task(cw_3f_right_atc_s3(var, gpio))
    # ============================================== SIDE WINDOWS AUTO
    # 1f
    # LEFT
    asyncio.create_task(sw_1f_left_atc_s1(var, gpio))
    asyncio.create_task(sw_1f_left_atc_s2(var, gpio))
    asyncio.create_task(sw_1f_left_atc_s3(var, gpio))
    asyncio.create_task(sw_1f_left_atc_s4(var, gpio))
    asyncio.create_task(sw_1f_left_atc_s5(var, gpio))
    asyncio.create_task(sw_1f_left_atc_s6(var, gpio))
    # RIGHT
    asyncio.create_task(sw_1f_right_atc_s1(var, gpio))
    asyncio.create_task(sw_1f_right_atc_s2(var, gpio))
    asyncio.create_task(sw_1f_right_atc_s3(var, gpio))
    asyncio.create_task(sw_1f_right_atc_s4(var, gpio))
    asyncio.create_task(sw_1f_right_atc_s5(var, gpio))
    asyncio.create_task(sw_1f_right_atc_s6(var, gpio))
    # 2f
    # LEFT
    asyncio.create_task(sw_2f_left_atc_s1(var, gpio))
    asyncio.create_task(sw_2f_left_atc_s2(var, gpio))
    asyncio.create_task(sw_2f_left_atc_s3(var, gpio))
    # RIGHT
    asyncio.create_task(sw_2f_right_atc_s1(var, gpio))
    asyncio.create_task(sw_2f_right_atc_s2(var, gpio))
    asyncio.create_task(sw_2f_right_atc_s3(var, gpio))
    # # 3f
    # # LEFT
    asyncio.create_task(sw_3f_left_atc_s1(var, gpio))
    asyncio.create_task(sw_3f_left_atc_s2(var, gpio))
    asyncio.create_task(sw_3f_left_atc_s3(var, gpio))
    # RIGHT
    asyncio.create_task(sw_3f_right_atc_s1(var, gpio))
    asyncio.create_task(sw_3f_right_atc_s2(var, gpio))
    asyncio.create_task(sw_3f_right_atc_s3(var, gpio))

    # # ========================================== FRONT/BACK WINDOWS AUTO
    # # 1f
    # # front
    # asyncio.create_task(fw_1f_atc_s1(var, gpio))
    # asyncio.create_task(fw_1f_atc_s2(var, gpio))
    # asyncio.create_task(fw_1f_atc_s3(var, gpio))
    # asyncio.create_task(fw_1f_atc_s4(var, gpio))
    # asyncio.create_task(fw_1f_atc_s5(var, gpio))
    # asyncio.create_task(fw_1f_atc_s6(var, gpio))
    # # back
    # asyncio.create_task(bw_1f_atc_s1(var, gpio))
    # asyncio.create_task(bw_1f_atc_s2(var, gpio))
    # asyncio.create_task(bw_1f_atc_s3(var, gpio))
    # asyncio.create_task(bw_1f_atc_s4(var, gpio))
    # asyncio.create_task(bw_1f_atc_s5(var, gpio))
    # asyncio.create_task(bw_1f_atc_s6(var, gpio))
    # # 2f
    # # front
    # asyncio.create_task(fw_2f_atc_s1(var, gpio))
    # asyncio.create_task(fw_2f_atc_s2(var, gpio))
    # asyncio.create_task(fw_2f_atc_s3(var, gpio))
    # # back
    # asyncio.create_task(fw_2f_atc_s1(var, gpio))
    # asyncio.create_task(fw_2f_atc_s2(var, gpio))
    # asyncio.create_task(fw_2f_atc_s3(var, gpio))
    # ==========================================BOHU CURTAIN AUTO
    asyncio.create_task(bc_1f_atc(var, gpio))
    asyncio.create_task(bc_2f_atc(var, gpio))
    asyncio.create_task(bc_3f_atc(var, gpio))
    asyncio.create_task(bc_4f_atc(var, gpio))
    asyncio.create_task(bc_5f_atc(var, gpio))
    asyncio.create_task(bc_6f_atc(var, gpio))
    asyncio.create_task(bc_7f_atc(var, gpio))
    asyncio.create_task(bc_8f_atc(var, gpio))
    #asyncio.create_task(bc_9f_atc(var, gpio))
    # asyncio.create_task(bc_10f_atc(var,gpio))
    # asyncio.create_task(bc_11f_atc(var,gpio))
    # asyncio.create_task(bc_12f_atc(var,gpio))
   # ============================================== AC CONTRO AUTO
    asyncio.create_task(fegi_fan_control(var, gpio))
    asyncio.create_task(hongi_fan_control(var, gpio))
    # asyncio.create_task(bog_control(var, gpio))
    # asyncio.create_task(sumag_control(var, gpio))
    # asyncio.create_task(fog_control_s1(var, gpio))
    # asyncio.create_task(fog_control_s2(var, gpio))
    # asyncio.create_task(fog_control_s3(var, gpio))
    # asyncio.create_task(co2_control(var, gpio))


async def main():
    try:
        print("Starting the main loop...")
        # sensors
        asyncio.create_task(read_sensors(var))
        # Local and cloud Network monitor
        asyncio.create_task(network_monitor_cloud())
        # asyncio.create_task(network_monitor_local())
        # publish psv.py to the local and cloud
        asyncio.create_task(publish_sensor_task_cloud())
        # asyncio.create_task(publish_sensor_task_local())
       # Reset query send to the Cloud and Local
        asyncio.create_task(publish_rst_task_cloud())
        # asyncio.create_task(publish_rst_task_local())
        # GPIO control Auto/Manual
        asyncio.create_task(non_network_tasks())

        while True:
            # Debug memory usage periodically
            gc.collect()
            free_memory = gc.mem_free()
            allocated_memory = gc.mem_alloc()
            total_memory = free_memory + allocated_memory
            print("Free Memory: {} bytes".format(free_memory))
            print("Allocated Memory: {} bytes".format(allocated_memory))
            print("Total Memory: {} bytes".format(total_memory))

            await asyncio.sleep(5)
    except Exception as e:
        print(f"Unexpected error in main loop: {e}")

# Start the main loop
asyncio.run(main())
>>>>>>> fca649c (first commit)
