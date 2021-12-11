array = [ 8 , 3 , 1 , 2 ]
max_sum = -1
best_config = []
temp_array = array

for config in range ( 0 , len ( array ) ) :
    
    temp_sum = 0
    
    for multi in range ( 0 , len ( temp_array ) ) :
        temp_sum += ( temp_array [ multi ] ) * multi
        
    if temp_sum > max_sum :
        max_sum = temp_sum
        best_config = temp_array.copy()
    
    temp = temp_array [ 0 ]
    temp_array.remove ( temp )
    temp_array.append ( temp )

print ( best_config , max_sum )