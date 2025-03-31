import numpy as np
weights = np.random.randn(2)
while True:
 cmd = input("Enter 'start' to proceed or 'Q' to quit: ").lower()
 if cmd == 'start':

  hours_studied = int(input("Enter the hours studied: "))
  hours_slept = int(input("Enter the hours slept: "))

  inputs = np.array([hours_studied, hours_slept])

  predicted_score = np.dot(inputs, weights) 
  actual_score = int(input("Enter your actual score: "))
  
  
  if actual_score != predicted_score:
   for x in range(5):
    error = actual_score - predicted_score
    nw1 = weights[0] + (error * inputs[0] * 0.1)
    nw2 = weights[1] + (error * inputs[1] * 0.1)
    weights = np.array([nw1, nw2]) 
    predicted_score = np.dot(inputs, weights)  
  
        
  print(f"Predicted score - {predicted_score}, Actual score - {actual_score}")
      
         
     
 elif cmd == 'q':
    print('goodbye!')
    quit()
 else:
   print("Please enter a valid command")


# new weight=old weight+(learning rate×error×input)
