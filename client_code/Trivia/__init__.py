from ._anvil_designer import TriviaTemplate
from anvil import *
import random

questions = ["What’s the longest side of a Right-Angle Triangle?", "When did World War 2 Start?", "How many sides are on a nonagon?", "Who is the owner of Amazon?", "What day is Valentine’s day?", "True or False? Canada is part of the US.", "What is the Capital City of Belgium?", "True or False? Neptune is smaller than Uranus.", "What library has the most books?", "What year did Queen Elizabeth die?"]
answers = ["Hypotenuse", "1939", "9", "Jeff Bezos", "Feburary 14", "False", "Brussels", "True", "The London Library", "2022"]
selected = 1


class Trivia(TriviaTemplate):
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

  @handle("button_2", "click")
  def button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    quest = self.quText.content
    selected = random.randint(1,10)
    quest = questions(selected)
    self.quText.content = str(quest)
  
  @handle("button_1", "click")
  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    answer = self.ansText.content
    answer = answers(selected)
    self.ansText.content = str(answer)

