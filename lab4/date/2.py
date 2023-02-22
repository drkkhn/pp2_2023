from datetime import datetime,timedelta 
keshe = datetime.now() - timedelta(1)
bugin = datetime.now()
erten = datetime.now() + timedelta(1)
print(f"Yestaday: {keshe}\n")
print(f"Today: {bugin}\n")
print(f"Tomorrow: {erten}\n")
