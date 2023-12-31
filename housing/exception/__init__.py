import os
import sys

class HousingException(Exception):
    
    def __init__(self,error_message:Exception,error_detail:sys):
        super().__init__(error_message)
        self.error_message=HousingException.get_detailed_error_message(error_message=error_message,
                                                                       error_detail=error_detail)

    @staticmethod
    def get_detailed_error_message(error_message:Exception,error_detail:sys) -> str:
        '''
        error_message: object of Exception
        error_detail: object of sys module
        '''
        _,_,exec_tb=error_detail.exc_info()

        file_name=exec_tb.tb_frame.f_code.co_filename
        line_no=exec_tb.tb_frame.f_lineno
        error_message=f"Error occured in the filename:{file_name} at line number:{line_no} and error message:{error_message}"
        return error_message       
    

    def __str__(self):
        return self.error_message
    

    def __repr__(str)->str:
        return HousingException.__name__.str()
