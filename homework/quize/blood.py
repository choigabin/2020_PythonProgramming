result = {"A": 0, "B": 0, "AB": 0, "O": 0}
students = ['A', 'A', 'A', 'O', 'B', 'B', 'O', 'AB', 'AB', 'O']
for a in students:
    result[a] += 1
print("{'A': %d, 'O': %d, 'B': %d, 'AB': %d}" % (result["A"], result["O"], result["B"], result["AB"]))