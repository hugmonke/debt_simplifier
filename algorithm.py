import numpy as np

    
class Calculator:
    
    def __init__(self, listing):
        self.listing = listing             

                
                
    def debtors(self):
        """Returns dictionary of debtors and sum of their debts"""
        
        debt_dict = {}
        
        for row in self.listing:
            if row[1] not in debt_dict:
                debt_dict[row[1]] = int(row[2])
            else:
                debt_dict[row[1]] += int(row[2])
                          
        return debt_dict
                    
                          
    def creditors(self):
        """Returns dictionary of creditors and sum of their loans"""
        
        cred_dict = {} 
        for row in self.listing:
            if row[0] not in cred_dict:
                cred_dict[row[0]] = int(row[2])
            else:
                cred_dict[row[0]] += int(row[2])     
                      
        return cred_dict

    def repetition(self):
        """Create dictionary without redundant transactions"""
        
        debt_dict = self.debtors()
        cred_dict = self.creditors()    
        new_dict = debt_dict
        for debtor in debt_dict:
            if debtor in cred_dict:
                new_dict[debtor] = debt_dict[debtor] - cred_dict[debtor]    
            else:
                continue
            
        return new_dict
    
    def final_result(self):
        
        
        new_dict = self.repetition()
        
        giver = max(new_dict, key=lambda key: new_dict[key])    
        taker = min(new_dict, key=lambda key: new_dict[key])
        result_matrix = []
        if len(new_dict) == 0:
            return new_dict
        while new_dict[giver] > new_dict[taker]:
            giver = max(new_dict, key=lambda key: new_dict[key])    
            taker = min(new_dict, key=lambda key: new_dict[key])
            if new_dict[giver] >= abs(new_dict[taker]):
                result_matrix.append([giver, taker, abs(new_dict[taker])])
                new_dict[giver] = new_dict[giver] + new_dict[taker]
                new_dict[taker] = 0
            else:
                result_matrix.append([giver, taker, abs(new_dict[giver])])
                new_dict[taker] = new_dict[giver] + new_dict[taker]
                new_dict[giver] = 0
        else:
            return result_matrix
          
    def return_result(self):
        #result_matrix = np.asarray(self.final_result())
        result_matrix = self.final_result()
        for i in range(len(result_matrix)):
            print(result_matrix[i])   
        #result_matrix = np.asarray(result_matrix)
            
        return result_matrix
    
    
