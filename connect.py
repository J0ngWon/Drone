import robomaster
from robomaster import robot


robomaster.config.LOCAL_IP_STR= "192.168.10.2"
tl_drone=robot.Drone()
tl_drone.initialize()

version=tl_drone.get_sdk_version()

SN=tl_drone.get_sn()
cel=tl_drone.get_temp()

battery_module = robot.battery.TelloBattery(tl_drone)

# get_battery 메서드 호출하여 값을 변수에 저장
battery_value = battery_module.get_battery()

print("시리얼번호:",SN)

print("배터리:",battery_value)

print("온도",cel)
tl_drone.close()