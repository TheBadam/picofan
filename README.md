# picofan
Control PWM fan with Raspberry Pico RP2040 over UART from Raspberry Pi 4

## raspberry
Monitor temp of CPU and broadcast to serial

## enable serial

run : `sudo raspi-config`  
select: `interfacing => serial`  
configure:
```
Select NO to: Would you like a login console...
Select YES to: Would you like the serial port hardware ...
```

reboot  

## clone git

clone repo to `<repo-root>`

## make venv

`python -m venv <somewhere>/picofan`  
```
source <somewhere>/picovan/bin/activate
pip install -r <repo-root>/picofan/raspberry/requirements.txt
```

## run service

create service `sudo nano /etc/systemd/system/cpu_temp.service`:
```
[Unit]
Description = Broadcast CPU temp
After = network.target

[Service]
Type = simple
ExecStart = <venv-location>/bin/python3 <repo-root>/picofan/raspberry/rpi_server.py
Restart = always

[Install]
WantedBy=multi-user.target
```

run `sudo systemctl daemon-reload`  
run `sudo systemctl start cpu_temp`  
run `sudo systemctl enable cpu_temp`  
check `sudo systemctl status cpu_temp`  
debug `journalctl -u cpu_temp.service`  