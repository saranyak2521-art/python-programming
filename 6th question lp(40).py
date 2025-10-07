from datetime import datetime, timedelta

# Sample doctor schedule
schedule = {"Dr. Smith":[9,10,11,14,15],"Dr. Lee":[10,11,13,14,16]}
appointments = {}

def display_slots(doctor):
    print(f"Available slots for {doctor}:", [h for h in schedule[doctor] if (doctor,h) not in appointments.values()])

def book(patient,doctor,hour):
    if hour in schedule[doctor] and (doctor,hour) not in appointments.values():
        appointments[patient]=(doctor,hour)
        print(f"{patient} booked with {doctor} at {hour}:00")
    else: print("Slot unavailable")

def modify(patient,new_doctor,new_hour):
    if patient in appointments:
        appointments[patient]=(new_doctor,new_hour)
        print(f"{patient}'s appointment updated to {new_doctor} at {new_hour}:00")
    else: print("No appointment to modify")

def cancel(patient):
    if patient in appointments:
        del appointments[patient]
        print(f"{patient}'s appointment canceled")
    else: print("No appointment to cancel")

def reminders():
    print("Upcoming appointments:")
    for p,(d,h) in appointments.items():
        print(f"{p} with {d} at {h}:00")

# Example usage
display_slots("Dr. Smith")
book("Alice","Dr. Smith",9)
book("Bob","Dr. Lee",10)
modify("Alice","Dr. Lee",11)
cancel("Bob")
reminders()
