import re 

operatorom = "-"
a = 4
b = 2

result = eval(f"{a} {operatorom} {b}")
print(f"\nA megoldás: {result}")


# eval művelet, string adat tipust konvertálása logikai műveletté 

string = "12-5+10"
numbers = re.findall(r'(\d+)\s*([-+*/])\s*(\d+)', string)

print(numbers)  # Output: ['42', '10']

print(type(numbers))

print(type(string))




    
for i in range(1, len(string), 2):
    for j in numbers:
        sajt = list(j)
        print(sajt) # Output:
        
        
    

