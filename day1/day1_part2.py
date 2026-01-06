zero = 0
value = 50

####PARTE 2
with open("input.txt", 'r', encoding='utf-8') as f:
    for line in f:
        line = line.strip()
        direction = line[0] #L or R
        temp_value = int(line[1:]) #tutto quello che c'è nella riga dopo L o R
        step = 0 #ogni singolo passo
        if direction == "L":
            step = -1 #muovo il valore indietro di 1
        else: #direction == "R"
            step = 1 #muovo il valore avanti di 1
        for n in range(temp_value):
            value = (value+step)%100
            if value == 0: 
              zero+=1


print("zero parte 1: ",zero)
        #print(direction)
    #print([line.strip() for line in f if line.strip()])
