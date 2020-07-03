attendees = ["vijay", "mani", "eswar"]
attendees.append("Tanaka")
attendees.extend(["yasuge", "Guru"])
optional_attendees = ["Manuel","Dave"]
potential_attendees = attendees + optional_attendees;
print("There are", len(potential_attendees), "potential attendees currently")

to_line = ", ".join(attendees)
cc_line = ", ".join(optional_attendees)
print("To: " + to_line)
print("Cc: " + cc_line)
