name=input("Enter name: ")
print("\n")
print("Hello " + name + "!")
print("\n")
print("Let's count by even numbers!")
print("\n")
start= int(input("Enter start of the range: "))
end= int(input("Enter end of the range: "))
for num in range(start, end +1):
  if num % 2 == 0:
    print(num)
print("\n")
print("Let's count by odd numbers!")
print("\n")
x= int(input("Enter start of range: "))
y= int(input("Enter end of range: "))
for z in range(x, y + 1):
    if z % 2 != 0:
        print(z)
