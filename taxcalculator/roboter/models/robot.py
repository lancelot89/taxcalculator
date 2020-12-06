from roboter.models import calculator
from roboter.models import csvmodel
from roboter.views import console

DEFAULT_ROBOT_NAME = 'Roboko'


class Robot(object):
    def __init__(self,
                 name=DEFAULT_ROBOT_NAME,
                 user_name=',',
                 speak_color='green'):
        self.name = name
        self.user_name = user_name
        self.speak_color = speak_color

    def hello(self):
        while True:
            print(self.name)
            template = console.get_template('hello.txt', self.speak_color)
            user_name = input(template.substitute({'robot_name': self.name}))

            if user_name:
                self.user_name = user_name.title()
                break


class CalculationRobot(Robot):
    def __init__(self, name=DEFAULT_ROBOT_NAME):
        super().__init__(name=name)
        self.calculator_model = calculator.CalculationModel()
        self.csv_model = csvmodel.TaxModel()

    def _hello_decorator(func):
        def wrapper(self):
            if not self.user_name:
                self.hello()
            return func(self)
        return wrapper

    @_hello_decorator
    def tax_calculation(self):
        cal = self.calculator_model
        csvmodel = self.csv_model
        template = console.get_template('calculation.txt', self.speak_color)
        print(template.substitute({'user_name': self.user_name}))
        input_list = self.input_robot()
        input_list['income_life_sum'] = cal.income_life_insurance(
            input_list['life_list'])
        input_list['resident_life_sum'] = cal.resident_life_insurance(
            input_list['life_list'])
        input_list['deduction_sum'] = self.deduction_sum()
        tax_list = cal.calculate(input_list)

        csvmodel.save(tax_list)
        return tax_list

    def input_robot(self):

        annual_income = int(input('年収を入力してください：'))
        insurance_fee = int(input('社会保険料を入力してください：'))
        print('生命保険の各支払い分を入力してください')
        life_fee = int(input('生命保険：'))
        care_fee = int(input('介護医療保険：'))
        pension_fee = int(input('個人年金保険：'))
        life_list = [life_fee, care_fee, pension_fee]
        input_list = {
            'annual_income': annual_income,
            'insurance_fee': insurance_fee,
            'life_list': life_list
        }
        return input_list

    def deduction_sum(self):
        blue_template = console.get_template(
            'bluedeclaration.txt', self.speak_color)
        basic_template = console.get_template('e-tax.txt', self.speak_color)
        blue_deduction = None
        income_basic_deduction = None
        resident_basic_deduction = None
        blue_yes = input(blue_template.substitute({
            'user_name': self.user_name
        }))
        if blue_yes.lower() == 'y' or blue_yes.lower() == 'yes':
            blue_deduction = 650000
        else:
            blue_deduction = 100000

        basic_yes = input(basic_template.substitute({
            'user_name': self.user_name
        }))
        if basic_yes.lower() == 'y' or basic_yes.lower() == 'yes':
            income_basic_deduction = 380000
            resident_basic_deduction = 330000
        else:
            income_basic_deduction = 280000
            resident_basic_deduction = 230000

        income_deduction_sum = blue_deduction + income_basic_deduction
        resident_basic_deduction = blue_deduction + resident_basic_deduction
        deduction_sum = {
            'income_deduction_sum': income_deduction_sum,
            'resident_basic_deduction': resident_basic_deduction
        }

        return deduction_sum

    def good_bye(self, tax_list):
        template = console.get_template('good_bye.txt', self.speak_color)
        print(template.substitute({
            'user_name': self.user_name
        }))
        for name, fee in tax_list.items():
            print(name, fee)
