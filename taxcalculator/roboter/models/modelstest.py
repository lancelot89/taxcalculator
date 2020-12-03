# from roboter.models import calculator
from roboter.views import console


DEFAULT_ROBOT_NAME = 'Roboko'


class Robot(object):
    def __init__(self, name=DEFAULT_ROBOT_NAME, speak_color='green'):
        self.neme = name
        self.speak_color = speak_color

    def hello(self):
        while True:
            template = console.get_template('hello.txt', self.speak_color)


Robot().hello()
