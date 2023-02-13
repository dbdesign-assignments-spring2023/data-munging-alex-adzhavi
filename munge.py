f = open('data/raw_data.txt', 'r')
g = open('data/clean_data.csv', 'w')

count = 0

for x in f:
    if (count <= 6 or count >= 165): # Skip over the unnecessary rows
        count = count + 1
        continue
    x = x.strip()
    l = x.split()
    if (len(l) == 0): # If it is an empty row, then skip it
        count = count + 1
        continue
    if (l[0] == "Year" and count > 7): # Skip over the headings after the 8th row
        count = count + 1
        continue
    for i in range(len(l)-1):
        if (l[i] == "***"):
            l[i] = l[i-1] # We are missing the annual mean D-N in 1880, we will just estimate this with J-D in the same year
        if (l[i] == "****"):
            l[i] = str((int(l[1]) + int(l[2]))//2) # We are missing the DJF value, estimate by mean of J and F
        if (count == 7 or i == 0): # If the row is just the headers or the element is the year, then just write it
            g.write(l[i])
        else: # Otherwise, convert it into degrees F
            temp = (int(l[i])*1.8)/100
            g.write("{:.1f}".format(temp))
        if (i == len(l)-2): # Skip over the last column over years
            break
        else:
            g.write(",")
    count = count + 1
    g.write("\n")  

f.close()
g.close()  
