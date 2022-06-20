class Employee:
    def __init__(self, name, gross_salary):
        self.name = name
        self.gross_salary = gross_salary
        self.contributions = 0.00

    def get_name(self):
        return self.name

    def calculate_net_salary(self):
        a = self.gross_salary
        c = round(round(a * 0.0976, 2) + round(a * 0.015, 2) + round(a * 0.0245, 2), 2)
        d = round(a - c, 2)
        e = round(d * 0.09, 2)
        f = round(d * 0.0775, 2)
        g = 111.25
        h = round(a - g - c, 0)
        i = round(h * 0.18, 2) - 46.33
        j = round(i - f, 0)
        k = round(a - c - e - j, 2)
        return k

    def calculate_contributions(self):
        a = self.gross_salary
        contributions = round(
            round(a * 0.0976, 2) + round(a * 0.065, 2) + round(a * 0.0193, 2) + round(a * 0.0245, 2) + round(a * 0.001,
                                                                                                             2), 2)
        self.contributions = contributions
        return contributions

    def calculate_total_cost(self):
        return self.gross_salary + self.contributions


results = []
sum_of_total_costs = 0

print("Podaj liczbę pracowników:")
number_of_employees = int(input())
for x in range(number_of_employees):
    print("Podaj imię pracownika")
    name_from_input = input()
    print("Podaj wynagrodzenie brutto pracownika")
    gross_salary_from_input = float(input())
    employee = Employee(name_from_input, gross_salary_from_input)
    calculated_net_salary = '%.2f' % employee.calculate_net_salary()
    calculated_contributions = '%.2f' % employee.calculate_contributions()
    calculated_total_cost = '%.2f' % employee.calculate_total_cost()
    results.append(
        employee.get_name() + "\nWynagrodzenie netto: " + calculated_net_salary + " Składki pracodawcy: " + calculated_contributions + " Łączny koszt na pracownika: " + calculated_total_cost)
    sum_of_total_costs = sum_of_total_costs + employee.calculate_total_cost()
for y in range(len(results)):
    print(results[y])
print("\nŁączny koszt dla pracodawcy: " + ('%.2f' % sum_of_total_costs))
