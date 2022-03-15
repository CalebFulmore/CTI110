#get values
color1 = int(input())
color2 = int(input())
color3 = int(input())

colorlist = (color1, color2, color3)

#find minimum value
minvalue = min(colorlist)

#display each value minum the mininum
print(color1 - minvalue, color2- minvalue, color3 - minvalue)