basic_salary=int(input('Enter your basic salary:'))
allowances=basic_salary*0.1
allowances=allowances+basic_salary
deductions=basic_salary*0.003
days_worked=int(input('Enter your days worked:'))

gross_salary = (basic_salary + allowances)
print('Monthly gross salary:',round(gross_salary))

daily_salary = basic_salary / 31
print('daily salary:',round(daily_salary))

total_deductions = (deductions / 31) * days_worked
if days_worked < 31:
    print('Detucted amount:',round(total_deductions))

taxable_salary = gross_salary - total_deductions
print('taxable salary:',round(taxable_salary))

tax = taxable_salary * 0.1
print('Tax:',round(tax))

net_salary = taxable_salary - tax
print('Net salary:',round(net_salary))


    

