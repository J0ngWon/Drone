import robomaster
from robomaster import robot

robomaster.config.LOCAL_IP_STR= "192.168.10.2"
tl_drone=robot.Drone()
tl_drone.initialize()
tl_flight = tl_drone.flight

tl_flight.takeoff().wait_for_completed()
tl_flight.land()

tl_drone.close()