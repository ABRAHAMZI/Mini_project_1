import sys
# import logging
from logger2 import logging   ##-->we use this to use logging for this exception errors

## this error exception is common for entire code
## using try, catch-raise custom exception |error message here is given
## error is error i provide- can customize


def error_message_detail(error,error_detail:sys):
    _,_,exc_tb=error_detail.exc_info()
    file_name=exc_tb.tb_frame.f_code.co_filename
    error_message="ABRAHAM -Error occured in python script name[{0}] line number [{1}] error message[{2}]".format(
        file_name,exc_tb.tb_lineno,str(error))
    return error_message
    

class CustomException(Exception):
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message)## intialize or inherit the exception class
        self.error_message=error_message_detail(error_message,error_detail=error_detail)

    def __str__(self):## exception here it will be printed
        return self.error_message
    
if __name__=="__main__":
    try:
        a=1/0
    except Exception as e:
        logging.info("Divide by Zero Error")
        raise CustomException(e,sys)
    

