print("This is weight converter. You can use any combination of metrics: mg \
(milligrams), g (grams), kg (kilograms), t (tons), st (stones), lb (pounds), \
oz (ounces), it (imperial tons), iq (imperial qintals)")
print("Enter request in format <data> <metric_from> to <metric to>")
line = input()

# coerce all units to metric gram
conversion = {
    "mg": 0.01,
    "g": 1,
    "kg": 1000,
    "t": 1000000,
    "st": 6350.29318,  # stone
    "lb": 453.59237,  # pound
    "oz": 28.349523125,  # ounce
}

try:
    data, metric_from, separator, metric_to = line.split(" ")
except ValueError:
    print("Wrong format. \
    Use \"<data> <metric_from> to <metric to>\" format")
    exit()
if metric_from not in conversion.keys():
    print("{} is bad metric".format(metric_from))
    exit()
elif metric_to not in conversion.keys():
    print("{} is bad metric".format(metric_to))
    exit()
elif not data or data == "0":
    print("Empty data - empty work. GOTO:HELL")
    exit()
try:
    data = float(data)
except ValueError:
    print("{} is bad data - GOTO:HELL".format(data))
    exit()


res = data * conversion.get(metric_from) / conversion.get(metric_to)
print(round(res, 3), metric_to, end=" ")
if res < 0:
    print("Negative mass, really? GOTO:NOBEL COMMITTEE")
