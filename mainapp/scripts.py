#Create your views here.
def success(msg):
    # Create a dictionary named 'response' with two key-value pairs
    response={
        'status_code':0, # Key 'status_code' with value 0
        'data':msg       # Key 'data' with value 'msg' (the input parameter)
    }
    # Return the 'response' dictionary
    return response

def error(msg):
    # Create a dictionary with error details
    response={
        'status_code':1, # Status code indicating error
        'data':msg  # Error message
    }
    # Return the 'response' dictionary
    return response