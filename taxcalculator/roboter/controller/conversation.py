from roboter.models import robot


def talk_calculation():
    calculation_robot = robot.CalculationRobot()
    calculation_robot.hello()
    tax_list = calculation_robot.tax_calculation()
    calculation_robot.good_bye(tax_list)
