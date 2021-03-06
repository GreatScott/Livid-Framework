import Live
from LividConstants import *

from _Framework.TransportComponent import TransportComponent
from RGBButtonElement import RGBButtonElement
from Elementary import Elementary

class LividTransportComponent(TransportComponent, Elementary):
  def __init__(self, play = None, stop = None, bpm_down = None, bpm_up = None, **kwargs):
    TransportComponent.__init__(self)
    Elementary.__init__(self, **kwargs)

    if play is not None:
      self.play_button = self.button(play, off_color = PURPLE) 
      self.set_play_button(self.play_button)
    if stop is not None:
      self.stop_button = self.button(stop, on_color = RED, off_color = RED) 
      self.set_stop_button(self.stop_button)

    
    self.setup_bpm_control(bpm_up, bpm_down)

  
  def setup_bpm_control(self, bpm_up, bpm_down):
    if bpm_up:
      self.bpm_up = self.button(bpm_up, off_color = PURPLE)
      self.bpm_up.add_value_listener(self.adjust_bpm, True)
      self.bpm_up.send_value(PURPLE)
    if bpm_down:
      self.bpm_down = self.button(bpm_down)
      self.bpm_down.add_value_listener(self.adjust_bpm, True)
      self.bpm_down.send_value(PURPLE)

  def adjust_bpm(self, value, sender):
    if value > 0:
      if sender == self.bpm_up:
        adjust = 0.5
      else:
        adjust = -0.5
      self.song().tempo = self.song().tempo + adjust
