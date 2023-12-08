from ply.yacc import yacc
# --- Parser

def p_program(p):
    '''program : class_declaration'''
    pass

def p_class_decleration(p):
    '''class_declaration : CLASS ID LEFT_BRACE list RIGHT_BRACE'''
    pass

def p_list(p):
    '''list : declration_list list 
            | empty'''
    pass

def p_declration_list(p):
    '''declration_list : field_declaration 
                       | method_declaration'''
    pass

def p_field_declaration(p):
    '''field_declaration : declarators ID SEMICOLON'''
    pass

def p_method_declaration(p):
    '''method_declaration : declarators ID OPEN_PAR inside_method_exp CLOSE_PAR LEFT_BRACE inside_method_st RIGHT_BRACE'''
    pass

def p_inside_method_exp(p):
    '''inside_method_exp : parameter_list 
                         | empty'''
    pass

def p_inside_method_st(p):
    '''inside_method_st : statment_exist return_exist'''
    pass

def p_statment_exist(p):
    '''statment_exist : statment_loop
                      | empty '''
    pass

def p_return_exist(p):
    '''return_exist : RETURN expresstion SEMICOLON 
                    | empty '''
    pass

def p_declarators(p):
    '''declarators : declare_type_exist static_exist type'''
    pass

def p_declare_type_exist(p):
    '''declare_type_exist : declare_type 
                          | empty '''
    pass

def p_declare_type(p):
    '''declare_type : PUBLIC 
                    | PRIVATE '''
    pass

def p_static_exist(p):
    '''static_exist : STATIC 
                    | empty '''
    pass

def p_type(p):
    '''type : prim_type 
            | class_type 
            | arr_type'''
    pass

def p_prim_type(p):
    '''prim_type : INT 
                 | BOOLEAN 
                 | DOUBLE 
                 | FLOAT 
                 | STRING 
                 | CHAR 
                 | VOID'''
    pass

def p_class_type(p):
    '''class_type : ID'''
    pass

def p_arr_type(p):
    '''arr_type : arr_typed LBRACKET RBRACKET 
                | arr_typed LBRACKET NUMBER RBRACKET'''
    pass

def p_arr_typed(p):
    '''arr_typed : INT 
                 | class_type'''
    pass

def p_parameter_list(p):
    '''parameter_list : type ID inputt'''
    pass

def p_inputt(p):
    '''inputt : input inputt 
              | empty'''
    pass

def p_input(p):
    '''input : COMMAS type ID'''
    pass

def p_statment_loop(p):
    '''statment_loop : statment statment_loop 
                     | statment'''
    pass

def p_statment(p):
    '''statment : if_statment 
                | while_statment 
                | declare_var
                | call_function
                | define_arr
                | assign'''
    pass

def p_assign(p):
    '''assign : ID EQUAL_OP expresstion SEMICOLON'''
    pass

def p_if_statment(p):
    '''if_statment : IF OPEN_PAR expresstion CLOSE_PAR LEFT_BRACE statment_loop RIGHT_BRACE 
                   | IF OPEN_PAR expresstion CLOSE_PAR LEFT_BRACE statment_loop RIGHT_BRACE ELSE LEFT_BRACE statment_loop RIGHT_BRACE
                   | IF OPEN_PAR expresstion CLOSE_PAR statment_loop  
                   | IF OPEN_PAR expresstion CLOSE_PAR statment_loop ELSE statment_loop'''
    pass

def p_while_statment(p):
    '''while_statment : WHILE OPEN_PAR expresstion CLOSE_PAR statment_loop
                      | WHILE OPEN_PAR expresstion CLOSE_PAR LEFT_BRACE statment_loop RIGHT_BRACE'''
    pass

def p_declare_var(p):
    '''declare_var : type ID EQUAL_OP expresstion SEMICOLON'''
    pass

def p_reference(p):
    '''reference : half_reference exist_id '''
    pass

def p_half_reference(p):
    '''half_reference : THIS 
                      | ID '''
    pass

def p_exist_id(p):
    '''exist_id : id_loop 
                | empty'''
    pass

def p_id_loop(p):
    '''id_loop : DOT ID reference 
               | empty '''
    pass

def p_argument_exist(p):
    '''argument_exist : argument_list 
                      | empty'''
    pass

def p_argument_list(p):
    '''argument_list : expresstion argument_list_exist '''
    pass

def p_argument_list_exist(p):
    '''argument_list_exist : argument_list_loop 
                           | empty'''
    pass

def p_argument_list_loop(p):
    '''argument_list_loop : COMMAS expresstion argument_list_loop 
                          | empty'''
    pass

def p_call_function(p):
    '''call_function : reference OPEN_PAR argument_exist CLOSE_PAR SEMICOLON'''
    pass

def p_exist_expresstion(p):
    '''exist_expresstion : '''
    pass

def p_define_arr(p):
    '''define_arr : reference exist_exp_arr expresstion SEMICOLON'''
    pass

def p_exist_exp_arr(p):
    '''exist_exp_arr : exp_arr 
                     | empty'''
    pass

def p_exp_arr(p):
    '''exp_arr : LBRACKET expresstion RBRACKET'''
    pass

def p_binop(p):
    '''binop : PLUS 
             | MINUS
             | TIMES
             | DIVIDE
             | MODULUS
             | ASSIGN_OP
             | LOGICAL_AND
             | LOGICAL_OR
             | GREATER_THAN
             | LESS_THAN
             | GREATER_THAN_OR_EQUAL_TO
             | LESS_THAN_OR_EQUAL_TO'''
    pass

def p_unop(p):
    '''unop : MINUS'''
    pass

def p_anop(p):
    '''anop : DECREMENT 
            | INCREMENT'''
    pass

def p_expresstion(p):
    '''expresstion : reference exist_exp_arr expresstion 
                   | reference OPEN_PAR argument_exist CLOSE_PAR
                   | OPEN_PAR expresstion CLOSE_PAR
                   | NUMBER
                   | ID
                   | TRUE_BOOOLEAN
                   | FALSE_BOOLEAN
                   | INT LBRACKET expresstion RBRACKET
                   | ID LBRACKET expresstion RBRACKET
                   | expresstion binop expresstion
                   | unop expresstion
                   | expresstion anop
                   | NEW ID OPEN_PAR CLOSE_PAR'''
    pass

def p_empty(p):
    " empty :"
    pass
"""
def p_error(p):
    print(f'Syntax error at {p.value!r}')"""

def p_error(p):
    if p == None :
        tok = 'end of file !'
    else :
        tok = f"{p.type}({p.value})on line {(p.lineno  )}"
    print(f"Synyax error : Uexpexted {tok}")
