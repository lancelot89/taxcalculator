import math


class CalculationModel(object):
    def __init__(self, csv_file=None, *args, **kwargs):
        if not csv_file:
            # csv_file = self.get_csv_file_path()
            pass

    def income_life_insurance(self, life_list):
        income_life_insurance_fee = 0
        for life_individual in life_list:
            if life_individual <= 20000:
                income_life_insurance_fee += life_individual
                continue

            elif life_individual <= 40000:
                income_life_insurance_fee += (life_individual / 2) + 10000
                continue

            elif life_individual <= 80000:
                income_life_insurance_fee += (life_individual / 4) + 20000
                continue

            else:
                income_life_insurance_fee += 40000
                continue
        if income_life_insurance_fee >= 120000:
            income_life_insurance_fee = 120000

        return income_life_insurance_fee

    def resident_life_insurance(self, life_list):
        resident_life_insurance_fee = 0
        for life_individual in life_list:
            if life_individual <= 12000:
                resident_life_insurance_fee += life_individual
                continue

            elif life_individual <= 32000:
                resident_life_insurance_fee += (life_individual / 2) + 6000
                continue

            elif life_individual <= 56000:
                resident_life_insurance_fee += (
                    life_individual / 4) + 14000
                continue

            else:
                resident_life_insurance_fee += 28000
                continue
        if resident_life_insurance_fee >= 70000:
            resident_life_insurance_fee = 70000

        return resident_life_insurance_fee

    def income_tax(self, taxable_income):

        income_tax_rate = {
            'A': [0.05, 0],
            'B': [0.1, 97500],
            'C': [0.2, 427500],
            'D': [0.23, 636000],
            'E': [0.33, 1536000],
            'F': [0.4, 2796000],
            'G': [0.45, 4796000]
        }

        if taxable_income <= 1950000:
            income_tax = (taxable_income *
                          income_tax_rate['A'][0]) - (income_tax_rate['A'][1])
            return math.floor(income_tax)

        elif taxable_income <= 3300000:
            income_tax = (taxable_income *
                          income_tax_rate['B'][0]) - (income_tax_rate['B'][1])
            return math.floor(income_tax)

        elif taxable_income <= 6950000:
            income_tax = (taxable_income *
                          income_tax_rate['C'][0]) - (income_tax_rate['C'][1])
            return math.floor(income_tax)

        elif taxable_income <= 9000000:
            income_tax = (taxable_income *
                          income_tax_rate['D'][0]) - (income_tax_rate['D'][1])
            return math.floor(income_tax)

        elif taxable_income <= 18000000:
            income_tax = (taxable_income *
                          income_tax_rate['E'][0]) - (income_tax_rate['E'][1])
            return math.floor(income_tax)

        elif taxable_income <= 40000000:
            income_tax = (taxable_income *
                          income_tax_rate['F'][0]) - (income_tax_rate['F'][1])
            return math.floor(income_tax)

        else:
            income_tax = (taxable_income *
                          income_tax_rate['G'][0]) - (income_tax_rate['G'][1])
            return math.floor(income_tax)

    def calculate(self, input_list):
        taxable_income = input_list['annual_income'] - \
            (input_list['insurance_fee'] +
             input_list['income_life_sum'] +
             input_list['deduction_sum']['income_deduction_sum'])

        resident_taxable_income = input_list['annual_income'] - \
            (input_list['insurance_fee'] +
             input_list['resident_life_sum'] +
             input_list['deduction_sum']['resident_basic_deduction'])

        income_tax = self.income_tax(taxable_income)
        resident_tax = math.floor(resident_taxable_income * 0.1)
        health_insurance_tax = math.floor(
            ((resident_taxable_income*0.0714)+39900) +
            ((resident_taxable_income*0.0229)+12300))
        max_housetown_tax = math.floor((resident_tax*0.28744)+2000)
        tax_list = {
            '所得税': income_tax,
            '住民税': resident_tax,
            '健康保険料': health_insurance_tax,
            'ふるさと納税限度額': max_housetown_tax
        }
        return tax_list
