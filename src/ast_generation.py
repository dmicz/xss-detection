import esprima

def generate_ast(js_code: str):
    """
    Generates an Abstract Syntax Tree (AST) from JavaScript code using Esprima.
    
    :param js_code: JavaScript code as a string
    :return: AST (Abstract Syntax Tree) representation of the code
    """
    try:
        ast = esprima.parseScript(js_code)
        return ast
    except Exception as e:
        print(f"Error parsing JavaScript code: {e}")
        return None
    
if __name__ == "__main__":
    js_code = "alert('XSS');"
    ast = generate_ast(js_code)
    if ast:
        print(ast)
