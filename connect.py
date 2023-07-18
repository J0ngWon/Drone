import robomaster
from robomaster import robot

robomaster.config.LOCAL_IP_STR= "192.168.10.2"
tl_drone=robot.Drone()
tl_drone.initialize()

version=tl_drone.get_sdk_version()

SN=tl_drone.get_sn()
print("drobe sn:",SN)

tl_drone.close()