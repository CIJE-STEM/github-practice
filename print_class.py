'''
A class for printing messages to stdout 


'''



class printer_class:

    def __init__(self):
        self.default_message="Pleaes change this default message."

    def printer(self,message=''):
        if message == '':
            print(message)
        else: 
            print(self.default_message)