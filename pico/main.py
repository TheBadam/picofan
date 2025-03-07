from machine import Pin, PWM, UART
from time import sleep

DEFAULT_LVL = 0.1
MAX_DUTY_CYCLE = 65535
TEMP_TO_LVL_MAP = {
    50: 0.20,
    53: 0.25,
    55: 0.30,
    57: 0.35,
    60: 0.45,
    65: 1.00 
}

def get_duty(current_temp):
    if current_temp is None:
        print(f"DEFAULT_FAN_LVL: {DEFAULT_LVL}, CURRENT_TEMP: {current_temp}, MAX_TEMP: N/A")
        return MAX_DUTY_CYCLE * DEFAULT_LVL
    
    fan_lvl = DEFAULT_LVL
    c_temps = list(TEMP_TO_LVL_MAP.keys())
    c_temps.sort()

    for config_temp in c_temps:
        fan_lvl = TEMP_TO_LVL_MAP[config_temp]
        if current_temp < config_temp:
            break
    print(f"FAN_LVL: {fan_lvl}, CURRENT_TEMP: {current_temp}, MAX_TEMP: {config_temp}") 
    return MAX_DUTY_CYCLE * fan_lvl


SLEEP_TIME = 5

PWM_FAN_FREQUENCY = 25000
PWM_PIN = 29

uart = UART(0, baudrate=9600, tx=Pin(0), rx=Pin(1))

pwm29 = PWM(Pin(PWM_PIN))
pwm29.freq(PWM_FAN_FREQUENCY)

while True:
    if uart.any():
        rcvChar = uart.read()
        str_temp = rcvChar.decode()
    try:
        temp = float(str_temp)
    except:
        temp = None
    duty = get_duty(temp)
    pwm29.duty_u16(int(duty))
    sleep(SLEEP_TIME)