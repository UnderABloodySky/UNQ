'''
Created on 26/08/2010

@author: Publico
'''

class Programa():
    '''
    Es un Programa que ejecuta instrucciones
    '''
    def __init__(self, instrucciones):
        self.instrucciones = instrucciones                
    def run(self):
        for inst in self.instrucciones:
            inst.run()
            
        
        
                    
        
        
 