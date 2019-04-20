import copy

# STEP 1: DATA 

def cartesian_product_2(set_a, set_b):  
    # define cartesian product of two sets
	result =[] 
	for i in range(0, len(set_a)): 
		for j in range(0, len(set_b)): 
			if type(set_a[i]) != list:		 
				set_a[i] = [set_a[i]] 
			temp = [num for num in set_a[i]] 	 
			temp.append(set_b[j])			 
			result.append(sorted(temp))		
	return result 

def cartesian_product_more(max,repeat):  
    # define cartesian product of more than 3 sets 
    repeat > 0
    container = []
    if repeat == 1:
        for i in range(0,max):
            container.append([i])
        return container 
    else:
        return sorted(cartesian_product_2(cartesian_product_more(max,repeat-1),list(range(0,max))))
       

### in the following, we remove the duplicate elements in the list

def simplify(list): # remove the duplicate copies 
	final_list = [] 
	for num in list: 
		if num not in final_list: 
			final_list.append(num) 
	return final_list 

def generate_lists(max, heap):
    First_lists = cartesian_product_more(max,heap)
    return simplify(First_lists)



# STEP 2: FIND THE NEXT POSITION AFTER THE FIRST MOVE

def next_position(list): # find the next position
    result_list= [] 
    for index,i in enumerate(list):
        for k in range(0,i):
            new_copy = copy.deepcopy(list) # 单向复制
            new_copy[index]= k
            result_list.append(sorted(new_copy))
    return simplify(result_list)

# STEP 3: COMPARE

def make_tuple(list):   # turn list to tuple
    tuple_1=[]
    for element in list:
        tuple_1.append(tuple(element))
    return tuple_1

print(next_position([0,0]))

####================================================####

p_position=[]

def nim_solution(max,heap):
    position = generate_lists(max,heap)
    for item in position:
        A_1 = make_tuple(p_position)
        A_2 = make_tuple(next_position(item))
        cap = set(A_1).intersection(A_2)
        if not cap:
            p_position.append(item)
    return p_position

print(nim_solution(5,3))




 