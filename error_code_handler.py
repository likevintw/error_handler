
# version: v1.0.1

import enum
from collections import defaultdict

def error_code_packer(error_tuple: tuple, param: dict):
    error_code, error_msg = error_tuple.value
    error_msg = error_msg.format_map(defaultdict(str, **param))
    return (error_code, error_msg)


class ErrorCode(enum.Enum):
    error_1 = (1, 'error_example')
    error_2 = (2, 'example: {group_id}')
    others = (10001, '{msg}')

def export_errorcode_errormsg_xls():
    with open('table_errorcode_errormsg.xls', 'w') as f:
        variable_dict = {}
        
        members = [attr for attr in dir(ErrorCode) if not callable(getattr(ErrorCode, attr)) and not attr.startswith("__")]
        for member in members:
            error_code , error_msg = None, None
            exec('error_code, error_msg = ErrorCode.{}.value'.format(member))
            variable_dict.update({error_code: error_msg})

        variable_sort_list = sorted(variable_dict.keys())
        f.write('Error Code\tError Message\r\n')

        for key in variable_sort_list:
            value = variable_dict[key]
            f.write('{error_code}\t{error_msg}\r\n'.format(error_code=key, error_msg=value))

def export_variable_errorcode_txt():
    with open('table_variable_errorcode.txt', 'w') as f:
        variable_dict = {}
        
        members = [attr for attr in dir(ErrorCode) if not callable(getattr(ErrorCode, attr)) and not attr.startswith("__")]
        for member in members:
            error_code , error_msg = None, None
            exec('error_code, error_msg = ErrorCode.{}.value'.format(member))
            variable_dict.update({member: error_code})
        
        for key, value in variable_dict.items():            
            f.write('{variable}={error_code}\r\n'.format(variable=key, error_code=value))  


if __name__ == '__main__':
    export_errorcode_errormsg_xls()
    export_variable_errorcode_txt()
