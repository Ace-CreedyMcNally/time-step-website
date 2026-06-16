from ._anvil_designer import DiceTemplate
from anvil import *


class Dice(DiceTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    super().__init__(**properties)

    # Any code you write here will run before the form opens.

  @handle("Score", "click")
  def Score_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('Score')

  @handle("Trivia", "click")
  def Trivia_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('Trivia')

  @handle("Dice", "click")
  def Dice_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('Dice')
