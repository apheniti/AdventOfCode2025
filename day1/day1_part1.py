zero = 0
value = 50

####PARTE 1
with open("input.txt", 'r', encoding='utf-8') as f:
    for line in f:
        line = line.strip()
        direction = line[0] #L or R
        temp_value = int(line[1:]) #tutto quello che c'è nella riga dopo L o R
        if direction == "L":
            value = (value-temp_value)%100
            #print(value)
        else:
            value = (value+temp_value)%100
            #print(value)
            
        if value == 0:
            zero+=1
            

print("zero parte 1: ",zero)
        #print(direction)
    #print([line.strip() for line in f if line.strip()])
