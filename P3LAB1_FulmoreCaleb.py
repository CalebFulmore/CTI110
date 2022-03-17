#get color values
c1 = int(input())
c2 = int(input())
c3 = int(input())
smallest = 0

#find smallest value
if c1 <= c2 :
    if c1 <= c3 :
        smallest = c1
        
if c2 <= c1:
    if c2 <= c3:
        smallest = c2

if c3 <= c2 :
    if c3 <= c1 :
        smallest = c3

#subtract smallest value from three numbers
print(c1 - smallest, c2 - smallest, c3 - smallest)

        


