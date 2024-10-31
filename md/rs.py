import machine
import uasyncio as asyncio
from md.var import VariableData

var = VariableData()

# for the other house 
# _1

uart_in = machine.UART(6, baudrate=9600, parity=None, stop=1)
uart_out = machine.UART(7, baudrate=9600, parity=None, stop=1)

# Queries for the sensors
##query_soil_3pin = b'\x0B\x03\x00\x00\x00\x07\x04\xA2'
query_soil_4pin = b'\x03\x03\x00\x00\x00\x07\x05\xEA'

query_env_out = b'\x01\x03\x00\x00\x00\x13\x04\x07'  # if 2 -- 04  34
query_env_in = b'\x01\x03\x00\x00\x00\x13\x04\x07'

query_waste = b'\x07\x03\x00\x00\x00\x03\x05\xAD'


async def query_sensor(query, uart, description):
    uart.write(query)
    await asyncio.sleep_ms(900)  # 300 ms is the best but we can incresee
    response = uart.read()
    if response:
        print(f"Received response from {description}: OK!! {response}")
    else:
        print(f"No response received from {description}.")
    return response

# ======== Waste sensor # Waste sensor reading


async def read_waste(var):
    try:
        response = await query_sensor(query_waste, uart_in, "waste sensor")
        if response:
            start_index = response.find(b'\x07\x03')
            if start_index != -1:
                data = response[start_index]
                if data:
                    # comment devided when master slave
                    var.waste_ec_1 = int.from_bytes(data[3:5], 'big')/100
                    # comment devided when master slave
                    var.waste_ph_1 = int.from_bytes(data[5:7], 'big')/10
                    # var.waste_temp_1 = int.from_bytes(response[7:9], 'big')

                # print("waste_temp_1:", var.waste_temp_1)
                    print("waste_ec_1:", var.waste_ec_1)
                    print("waste_ph_1:", var.waste_ph_1)

            else:
                print("No response from waste sensor.")
    except Exception as e:
        print(f"Error parsing waste sensor data: {e}")



# ======== 3-PIN Soil sensor (Second sensor)
async def read_soil(var):
    try:
        response = await query_sensor(query_soil_4pin, uart_in, "soil sensor----------22")
        if response:
            start_index = response.find(b'\x03\x03')  # Start of valid response
            if start_index != -1:
                data = response[start_index:]
                if len(data) >= 17:  # Ensure we have enough bytes to parse
                    # Extract each sensor value by its correct byte offset
                    var.soil_temp_1 = int.from_bytes(
                        data[3:5], 'big') / 10  # 3-4: Temp
                    var.soil_moisture_1 = int.from_bytes(
                        data[5:7], 'big') / 10  # 5-6: Moisture
                    var.soil_ec_1 = int.from_bytes(
                        data[7:9], 'big') / 1000  # 7-8: EC
                    var.soil_ph_1 = int.from_bytes(
                        data[9:11], 'big') / 100  # 9-10: pH
                    var.soil_n_1 = int.from_bytes(
                        data[11:13], 'big')  # 11-12: Nitrogen
                    var.soil_p_1 = int.from_bytes(
                        data[13:15], 'big')  # 13-14: Phosphorus
                    var.soil_k_1 = int.from_bytes(
                        data[15:17], 'big')  # 15-16: Potassium

                    # Print parsed values
                    print("soil-temp:", var.soil_temp_1)
                    print("soil-moisture:", var.soil_moisture_1)
                    print("soil-ec:", var.soil_ec_1)
                    print("soil-ph:", var.soil_ph_1)
                    print("soil-nitrogen:", var.soil_n_1)
                    print("soil-phosphorus:", var.soil_p_1)
                    print("soil-potassium:", var.soil_k_1)
                else:
                    print("Incomplete data received for soil sensor 2.")
            else:
                print("No valid data found for soil -----------sensor 2.")
        else:
            print("No response from Soil sensor 2.")
    except Exception as e:
        print(f"Error reading Soil sensor----122: {e}")


async def read_env_in(var):
    try:
        response = await query_sensor(query_env_in, uart_in, "env in senso----11111111111111111")
        if response:
            start_index = response.find(b'\x01\x03')
            if start_index != -1:
                data = response[start_index:]
                if data:
                    raw_temp = int.from_bytes(data[3:5], 'big') / 10
                    raw_hum = int.from_bytes(data[5:7], 'big') / 10
                    raw_co2 = int.from_bytes(data[13:15], 'big')
                    raw_sun = int.from_bytes(data[37:39], 'big')

                    # Check conditions for envin
                    if raw_temp < 60:
                        var.envin_temp_1 = raw_temp
                        var.env_in_temp_r_1=raw_temp
                    else:
                        print("Temperature data unexpected")
                    if raw_hum < 99:
                        var.envin_humi_1 = raw_hum
                    else:
                        print("Humidity data unexpected")
                    if raw_co2 < 999:
                        var.envin_co2_1 = raw_co2
                    else:
                        print("CO2 data unexpected")
                    if raw_sun < 999:
                        var.envin_solar_light_1 = raw_sun
                    else:
                        print("Solar light data unexpected")

                    # Convert to hex strings for HMI
                    var.eih_temp_1 = int.from_bytes(response[3:5], 'big')
                    var.eih_humi_1 = int.from_bytes(response[5:7], 'big')
                    var.eih_co2_1 = int.from_bytes(response[13:15], 'big')
                    var.eih_solar_light_1 = int.from_bytes(
                        response[37:39], 'big')

                    print("env-in-temp:", var.envin_temp_1)
                    print("env-in-humi:", var.envin_humi_1)
                    print("env-in-co2:", var.envin_co2_1)
                    print("env-in-light:", var.envin_solar_light_1)
            else:
                print(
                    "Invalid response ---- environment in------ structure, retrying...")
        else:
            print("No response from environment in sensor.")
    except Exception as e:
        print(f"Error parsing environment in sensor data: {e}")

    await asyncio.sleep(1)  # Wait for a second before retrying


async def read_env_out(var):
    try:
        response = await query_sensor(query_env_out, uart_out, "env out sensor")
        if response:
            start_index = response.find(b'\x01\x03')
            if start_index != -1:
                data = response[start_index:]
                if data:
                    raw_temp = int.from_bytes(data[3:5], 'big') / 10
                    raw_hum = int.from_bytes(data[5:7], 'big') / 10
                    raw_co2 = int.from_bytes(data[13:15], 'big')
                    raw_sun = int.from_bytes(data[37:39], 'big')
                    # Check conditions for envin
                    if raw_temp < 60:
                        var.envout_temp_1 = raw_temp
                    else:
                        print("Temperature data unexpected")
                    if raw_hum < 99:
                        var.envout_humi_1 = raw_hum
                    else:
                        print("Humidity data unexpected")
                    if raw_co2 < 999:
                        var.envout_co2_1 = raw_co2
                    else:
                        print("CO2 data unexpected")
                    if raw_sun < 999:
                        var.envout_solar_light_1 = raw_sun
                    else:
                        print("Solar light data unexpected")

                    #

                    print("env-in-temp:", var.envout_temp_1)
                    print("env-in-humi:", var.envout_humi_1)
                    print("env-in-co2:", var.envout_co2_1)
                    print("env-in-light:", var.envout_solar_light_1)
            else:
                print(
                    "Invalid response ---- environment out------structure, retrying...")
        else:
            print("No response from environment --out--sensor.")
    except Exception as e:
        print(f"Error parsing environment --out--sensor data: {e}")

    await asyncio.sleep(1)  # Wait for a second before retrying
# Sequentially read each sensor


async def read_sensors(var):
    while True:
        # Reading sensors one by one, waiting for the previous response before proceeding
        
        await read_env_in(var)
        await asyncio.sleep(2)

        await read_soil(var)
        await asyncio.sleep(2)

        await read_waste(var)
        await asyncio.sleep(2)

        await read_env_out(var)
        await asyncio.sleep(2)


# async def main():
#     asyncio.create_task(read_sensors(var))
#     while True:
#         await asyncio.sleep(1)

# # Run the main function
# asyncio.run(main())
