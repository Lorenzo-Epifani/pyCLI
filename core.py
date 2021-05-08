import op.functions as operations
print(' \n****Data Influencer CLI**** \n\n')
operations._help()

def start_core():
    input_op = input("Enter the command: ")
    op_call = operations.op_list.get(input_op, operations._err)
    op_call()
    start_core()
    
start_core()