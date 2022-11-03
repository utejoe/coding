from datetime import datetime
time = datetime.now()
time_template = "Date/time: {M}/{D}/{Y} [H]:[Min]"
print(time_template.format(M=time.month, D=time.day, Y=time.year, H=time.hour, Min=time.minute))
