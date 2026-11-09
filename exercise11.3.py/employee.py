
class Employee:
    """Menyimpan informasi karyawan."""

    def __init__(self, first_name, last_name, annual_salary):
        self.first_name = first_name
        self.last_name = last_name
        self.annual_salary = annual_salary

    def give_raise(self, amount=5000):
        """Menambahkan kenaikan gaji tahunan."""
        self.annual_salary += amount

#contoh penggunaan
employee = Employee('vrysa', 'sendhyca', 60000)

employee.give_raise()

print(employee.annual_salary)

#kalau ingin kenaikan $10.000:
employee.give_raise(10000)