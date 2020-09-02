# Author: Nasser Zaher nzz5096@psu.edu
# Collaborator: Emma Mayhan: edm5255@psu.edu
# Collaborator: Kate Acosta: kaa5772@psu.edu
# Collaborator: Sapna Nattuvetty: ssn5171@psu.edu
temp = input("Enter temperature: ");
unit = input("Enter unit in F/f or C/c: ");

if unit=="c" or unit=="C":
  celsius = float(temp);
  fahrenheit = float(celsius * 1.8) + 32
  print(f"{celsius}° in Celsius is equivalent to {fahrenheit}° Fahrenheit.");
elif unit=="f" or unit == "F":
  fahrenheit = float(temp);
  celsius = float((fahrenheit - 32) * 5/9)
  print(f"{fahrenheit}° in Fahrenheit is equivalent to {celsius}° Celsius");
else:
  print("Invalid unit(" + unit + ").")