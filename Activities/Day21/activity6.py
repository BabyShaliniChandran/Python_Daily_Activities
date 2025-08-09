employee="Abi"
hours_worked=45.75
hourly_rate=350.50
bonus=1500
target_hours=40

print("{0:*^50}".format("employee report"))
print()
print()
print(f"{"Employee name:":>25}{employee:>15}")
print(f"{"Hours worked:":>25}{hours_worked:>15}")
print(f"{"Target Hours:":>25}{target_hours:>15}")
print(f"{"Overtime:":>25}{hours_worked-target_hours:>15}")
print(f"{"Total Pay:":>25}${(hours_worked*hourly_rate)+bonus+:011.2f}")

