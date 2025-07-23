arr = []
n=3
print(f"Enter {n} elements:")
for _ in range(n):
    arr.append(int(input()))
new_element = int(input("Enter the element to insert at the end: "))
arr.append(new_element)
print("Updated array:")
print(arr)
