from PayrollSystem import PayrollSystem
from SalaryEmployee import SalaryEmployee
from HourlyEmployee import HourlyEmployee
from CommissionEmployee import CommissionEmployee

salary_employee = SalaryEmployee(1, "Валерий Задорожный", 1500)
hourly_employee = HourlyEmployee(2, "Илья Кромин", 40, 15)
commission_employee = CommissionEmployee(3, "Николай Хорольский", 1000, 250)

more_worker = HourlyEmployee(4, "Василий", 60, 15)
payroll_system = PayrollSystem()
payroll_system.calculate([
    salary_employee,
    hourly_employee,
    commission_employee,
    more_worker
])

## Постарался разбить на большее количество модулей, чтобы лучше усвоить.
## Можно было сделать проще. Сделать 3 файла: employee(все работники), payroll(расчёт) и main(ввод и вывод)
