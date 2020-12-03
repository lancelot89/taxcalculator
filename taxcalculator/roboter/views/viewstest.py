import os
import string

import termcolor

# with open('C:/Users/izayo/Documents/work/taxcalculator/taxcalculator/roboter/templates/hello.txt', 'r', encoding='utf-8') as template_file:
#     color = None
#     contents = template_file.read()
#     contents = contents.rstrip(os.linesep)
#     contents = '{splitter}{sep}{contents}{sep}{splitter}{sep}'.format(
#         contents=contents, splitter="=" * 60, sep=os.linesep)
#     contents = termcolor.colored(contents, color)
#     t = string.Template(contents)
#     con = t.substitute(robot_name='Taka')
#     print(con)

import console

DEFAULT_ROBOT_NAME = 'Roboko'


class Robot(object):
    def __init__(self, name=DEFAULT_ROBOT_NAME, speak_color='green'):
        self.name = name
        print(name)
        self.speak_color = speak_color

    def hello(self):
        print(self.name)
        template = console.get_template('hello.txt', self.speak_color)
        input(template.substitute({'robot_name': self.name}))


robot = Robot()
robot.hello()
