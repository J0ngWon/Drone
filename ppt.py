import robomaster
from robomaster import robot


robomaster.config.LOCAL_IP_STR= "192.168.10.2"
tl_drone=robot.Drone()
tl_drone.initialize()
tl_flight = tl_drone.flight

version=tl_drone.get_sdk_version()

SN=tl_drone.get_sn()
cel=tl_drone.get_temp()

battery_module = robot.battery.TelloBattery(tl_drone)

battery_value = battery_module.get_battery()

print("시리얼번호:",SN)

print("배터리:",battery_value)

print("온도",cel)

tl_flight.takeoff().wait_for_completed()

for i in range(4):

   tl_flight.forward(33).wait_for_completed()

   tl_flight.rotate(90).wait_for_completed()





tl_flight.land()

tl_drone.close()
