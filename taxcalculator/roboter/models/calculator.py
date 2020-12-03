import math

annual_income = int(input('年収を入力してください：'))
insurance_fee = int(input('社会保険料を入力してください：'))
print('生命保険の各支払い分を入力してください')
life_fee = int(input('生命保険：'))
care_fee = int(input('介護医療保険：'))
pension_fee = int(input('個人年金保険：'))
life_list = [life_fee, care_fee, pension_fee]


def life_insurance(life_list):
    life_insurance_fee = 0
    for life_individual in life_list:
        if life_individual <= 20000:
            life_insurance_fee += life_individual
            continue

        elif life_individual <= 40000:
            life_insurance_fee += (life_individual/2) + 10000
            continue

        elif life_individual <= 80000:
            life_insurance_fee += (life_individual/4) + 20000
            continue

        else:
            life_insurance_fee += 40000
            continue

    return life_insurance_fee


basic_deduction = 380000
taxable_income = annual_income - \
    (insurance_fee + life_insurance(life_list) + basic_deduction)


def income_tax(taxable_income):

    income_tax_rate = {'A': [0.05, 0], 'B': [0.1, 97500], 'C': [0.2, 427500], 'D': [
        0.23, 636000], 'E': [0.33, 1536000], 'F': [0.4, 2796000], 'G': [0.45, 4796000]}

    if annual_income <= 1950000:
        income_tax = (annual_income *
                      income_tax_rate['A'][0]) - (income_tax_rate['A'][1])
        return math.floor(income_tax)

    elif annual_income <= 3300000:
        income_tax = (annual_income *
                      income_tax_rate['B'][0]) - (income_tax_rate['B'][1])
        return math.floor(income_tax)

    elif annual_income <= 6950000:
        income_tax = (annual_income *
                      income_tax_rate['C'][0]) - (income_tax_rate['C'][1])
        return math.floor(income_tax)

    elif annual_income <= 9000000:
        income_tax = (annual_income *
                      income_tax_rate['D'][0]) - (income_tax_rate['D'][1])
        return math.floor(income_tax)

    elif annual_income <= 18000000:
        income_tax = (annual_income *
                      income_tax_rate['E'][0]) - (income_tax_rate['E'][1])
        return math.floor(income_tax)

    elif annual_income <= 40000000:
        income_tax = (annual_income *
                      income_tax_rate['F'][0]) - (income_tax_rate['F'][1])
        return math.floor(income_tax)

    else:
        income_tax = (annual_income *
                      income_tax_rate['G'][0]) - (income_tax_rate['G'][1])
        return math.floor(income_tax)


print(income_tax(annual_income))
