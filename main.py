name=input("Enter name: ")
print("Hello " + name + "!")

print("Let's count by even numbers!")

start= int(input("Enter start of the range: "))
end= int(input("Enter end of the range: "))
for num in range(start, end +1):
  if num % 2 == 0:
    print(num)

print("Let's count by odd numbers!")

x= int(input("Enter start of range: "))
y= int(input("Enter end of range: "))
for z in range(x, y + 1):
    if z % 2 != 0:
        print(z)
