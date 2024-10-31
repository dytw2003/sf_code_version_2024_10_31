# load.py

import uasyncio as asyncio
import os
# Define the CSV file path
import json

# from md.mg import send_data_to_hmi

# Function to load CSV data into the var module


# async def get_csv(var, uart):
#     # Check if the file exists and is not empty using os.stat
#     response_data = {"rst1_h":"rst"}
#     if not var.ld_flg:
#         try:
#             await send_data_to_hmi(uart, response_data)
#             setattr(var,"ld_flg",True)
#         except OSError as e:
#             print(f"Error reading file: {e}")

#     else:
#         print(f"Skipping   SENDING THE QUERY FOR TE SETTING VALUES TO MASTER  ::FLAG::{var.ld_flg}  -------------.")

async def get_csv_mqtt(client, var):
    # Check if the file exists and is not empty using os.stat
    MQTT_TOPIC_RSTATMN="dytw"    
    if not var.ld_flg:
        try:
            mqtt_msg = {"rst1_h":"rst"}
            client.publish(MQTT_TOPIC_RSTATMN, json.dumps(mqtt_msg))
            setattr(var,"ld_flg",True)
        except OSError as e:
            print(f"Error reading file: {e}")

    else:
        print(f"Skipping   SENDING THE QUERY FOR TE SETTING VALUES TO MASTER  ::FLAG::{var.ld_flg}  -------------.")
# Helper function to convert string values to appropriate types


# Periodic loader using uasyncio.sleep for MicroPython compatibility
async def load_csv_to_var_mqtt(client, var):
    while True:
        await get_csv_mqtt(client, var)
        await asyncio.sleep(60)  # Delay between loads


# async def load_csv_to_var(var, uart):
#     while True:
#         await get_csv(var, uart)
#         await asyncio.sleep(60)  # Delay between loads

