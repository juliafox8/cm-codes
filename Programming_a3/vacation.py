def vacation(places, temps, costs, temp_min):
    indexs_with_high_enough_temps = []

    for i in range (len(temps)):
        temp = temps[i]
        #looking up temp and setting it to the 1,2,3 i value (ith)
        if temp >= temp_min: 
            indexs_with_high_enough_temps.append(i)
    
    if len(indexs_with_high_enough_temps) ==  0:
        return "Home"


    min_cost_index = indexs_with_high_enough_temps[0] 

    for i in indexs_with_high_enough_temps:
        cost= costs[i]
        if cost <= costs[min_cost_index]:
            min_cost_index = i 

    return(places[min_cost_index])

    