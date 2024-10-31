import uasyncio as asyncio
import json
import os

## CHANGE FOR THE OTHER HOUSE
## "_1"

async def store_var(var, name, state, client_local,client_cloud):
    """Store variable and queue updates for asynchronous CSV file storage."""
    MQTT_TOPIC_MANUAL_cloud = b"dytw_1/manual"    
    MQTT_TOPIC_AUTO_cloud = b"dytw_1/auto"

    # MQTT_TOPIC_MANUAL_local= b"dytw_1/manual"
    # MQTT_TOPIC_AUTO_local = b"dytw_1/auto"

    ######for the synchronous 
    
    # Update the variable data
    setattr(var, name, state)
    # cloud publish
    if client_cloud:
        print(f'publishing to the cloud')
        client_cloud.publish(MQTT_TOPIC_MANUAL_cloud, json.dumps({str(name): state}))
        client_cloud.publish(MQTT_TOPIC_AUTO_cloud, json.dumps({str(name): state}))

    # ## local publish
    # if client_local:
    #     print(f'publishing to the local')
    #     client_local.publish(MQTT_TOPIC_MANUAL_local, json.dumps({str(name): state}))
    #     client_local.publish(MQTT_TOPIC_AUTO_local, json.dumps({str(name): state}))



