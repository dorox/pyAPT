from __future__ import absolute_import, division
from .controller import Controller

class LTS150(Controller):
  """
  A controller for a LTS150 stage.
  """
  def __init__(self,*args, **kwargs):
    super(LTS150, self).__init__(*args, **kwargs)

    # Note:

    self.max_velocity = 50.0 #[mm/s]
    self.max_acceleration = 50.0 #[mm/s]

    #TODO: check if values below are correct

    # The BSC20x series and MST602 stepper controllers include a Trinamics encoder with a 
    # resolution of 2048 microsteps per full step, giving 409600 micro-steps per revolution
    # for a 200 step motor. 

    # Values below are Trinamic converted values for position(us), velocity(us/s) and
    # acceleration (us/sec^2)

    self.position_scale = 409600
    self.velocity_scale = 21987328
    self.acceleration_scale = 4506

    self.linear_range = (0,150)


