# bounce.py
#
# Exercise 1.5

initial_height = int(100) 


for i in range(10): 
      bouncing_height = round (float(3 * initial_height / 5), 4)
        print(bouncing_height)
          initial_height = bouncing_height
            i = i + 1
 

