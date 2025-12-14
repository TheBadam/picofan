from gpiozero import CPUTemperature
import time
import serial

ser = serial.Serial ("/dev/ttyS0", 9600)  

while True:
    cpu = CPUTemperature()
    cpu_temp = (str(cpu.temperature))
    ser.write(str.encode(cpu_temp))
    time.sleep(5)
