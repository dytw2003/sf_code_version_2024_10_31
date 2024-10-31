from pyb import Pin
## NEED TO CHANGE FOR OTHER HOUSE
     #_1":

class GPIOController:
    def __init__(self):
        # Define GPIO pin mappings with user-friendly names
        self.pin_mappings = {
            #  gpio "D9~D20"

            "chan_ch_1f_o_1": "D9",
            "chan_ch_1f_c_1": "D10",
            "chan_uu_1f_o_1": "D11",  # uu chuk
            "chan_uu_1f_c_1": "D12",
            # 2 floor

            "chan_ch_2f_o_1": "D13",
            "chan_ch_2f_c_1": "D14",
            "chan_uu_2f_o_1": "D15",  # uu chuk
            "chan_uu_2f_c_1": "D16",

            "chan_ch_3f_o_1": "D17",
            "chan_ch_3f_c_1": "D18",
            "chan_uu_3f_o_1": "D19",  # uu chuk
            "chan_uu_3f_c_1": "D20",

            "bhc_5_o_1": "D21",  # chhanjang bohu
            "bhc_5_c_1": "D22",
            "bhc_6_o_1": "D23",  # chhanjang chhagong mak
            "bhc_6_c_1": "D24",

            # 1 floor
            "chuk_ch_1f_o_1": "D25",
            "chuk_ch_1f_c_1": "D26",
            "chuk_uu_1f_o_1": "D27",  # uu chuk
            "chuk_uu_1f_c_1": "D28",
            # 2 floor
            "chuk_ch_2f_o_1": "D29",
            "chuk_ch_2f_c_1": "D30",
            "chuk_uu_2f_o_1": "D31",  # uu chuk
            "chuk_uu_2f_c_1": "D32",
            # # 3 floor
            "chuk_ch_3f_o_1": "D41",
            "chuk_ch_3f_c_1": "D42",
            "chuk_uu_3f_o_1": "D43",  # uu chuk
            "chuk_uu_3f_c_1": "D44",
            # # gpio "D21~D32"
            # # chhan jang  ------
            # # 1 floor
            
            # # 3 flo


            # # gpio ("D41~D54")
            # # bohu curtain---
            "bhc_1_o_1": "D45",  # chhan myang bohu
            "bhc_1_c_1": "D46",
            "bhc_2_o_1": "D47",  # chhwa chuk myon bohu
            "bhc_2_c_1": "D48",
            "bhc_3_o_1": "D49",  # uu chuk myon bohu
            "bhc_3_c_1": "D50",
            "bhc_4_o_1": "D51",  # hu myon bohu
            "bhc_4_c_1": "D52",
            
            "bhc_7_o_1": "D53",  # chhanjang finil
            "bhc_7_c_1": "D54",
            "bhc_8_o_1": "D55",  # chhanjang finil
            "bhc_8_c_1": "D56",
            # Gpio ("D55~D63")
            # sudong-2-- page 3
              # -sumag
            # "bogwangdong_1":"D57", #flash_light
            "fegi_fan_1": "D57",
            "fog_valve_1": "D58", 
            "co2_1": "D59",  # -fog valve  
            "hongi_fan_1": "D60",
            #"sumag_1": "D60",       
            "nangbangi_1": "D61",  # -co2
            "sp01_1": "D62",
            "bogwangdong_1": "D63",  # flash_light
            "sumag_1": "D64",
            #
            "yudong_fan_1_cy_1": "D65",  # -yudong fan 1 # chhak/ yak             
            "yudong_fan_2_cy_1": "D66",  # yudong fan2     # chhak/ yak
            "yudong_fan_1_uc_1": "D67", # unjan / chhangji(ON/OFF)
            "yudong_fan_2_uc_1": "D68",  # unjan / chhangji(ON/OFF)

        }

        self.init_gpio_pins()

    # THIS METHOD IS TO CHECK THE --AVAILABILITY OF THE PINS --
    def init_gpio_pins(self):
        for pin_name in self.pin_mappings:
            pin_id = self.pin_mappings[pin_name]
            try:
                pin = Pin(pin_id, Pin.OUT)
                pin.off()  # Set pins initially to OFF state
                print(f"Initialized pin {pin_name} ({pin_id}) successfully.")
            except ValueError as e:
                print(f"Error initializing pin {pin_name} ({pin_id}): {e}")

    # THIS METHOD IS TO -- TUREN--ON--
    def turn_on_pins(self, pin_name):

        pin_id = self.pin_mappings.get(pin_name)
        if pin_id:
            pin = Pin(pin_id, Pin.OUT)
            pin.on()
            print(f'{pin_id},is ON')

    # THIS METHOD IS TO -- TUREN--OFF--
    def turn_off_pins(self, pin_name):
        pin_id = self.pin_mappings.get(pin_name)
        if pin_id:
            pin = Pin(pin_id, Pin.OUT)
            pin.off()
            print(f'{pin_id},is OFF')
