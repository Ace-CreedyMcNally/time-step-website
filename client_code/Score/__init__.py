from ._anvil_designer import ScoreTemplate
from anvil import *


class Score(ScoreTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    super().__init__(**properties)

    # Any code you write here will run before the form opens.

  @handle("Score", "click")
  def Score_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('Score')
