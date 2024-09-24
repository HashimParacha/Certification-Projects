import numpy as np


def Calculate():
    
    Get_input = (input("PLEASE ENTER NINE DIGITS: "))
    
    if Get_input.isdigit() and len(Get_input) == 9:
        
        Creating_list = [int (i) for i in Get_input]

        
       
        matrix = np.array(Creating_list).reshape(3, 3)
     
        calculations = {
            
            'mean'     : [matrix.mean(axis=0), matrix.mean(axis=1), matrix.mean()],
            'variance' : [matrix.var(axis=0), matrix.var(axis=1), matrix.var()],
            'std'      : [matrix.std(axis=0), matrix.std(axis=1), matrix.std()],
            'Max'      : [matrix.max(axis=0), matrix.max(axis=1), matrix.max()],
            'Min'      : [matrix.min(axis=0), matrix.min(axis=1), matrix.min()],
            'Sum'      : [matrix.sum(axis=0), matrix.sum(axis=1), matrix.sum()]
            
        }
        
        print(calculations) 
            

    else:
        print ("PLEASE ENTER THE EXACT 9 DIGITS.")
        
   

Calculate()
