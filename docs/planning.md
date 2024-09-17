# Graph repr and metadata

-  Abstract Syntax Tree (AST): Tree representation of the abstract syntactic structure of source code. Helps capture the structure of both original and obfuscated JavaScript code.
    - eg. body: [{type: "ExpressionStatement",expression: {type: "CallExpression",callee: {type: "Identifier",name: "alert"},arguments: [{type: "Literal",value: "XSS",raw: "\"XSS\""}]}}]
- Control Flow Graph (CFG): A CFG represents all paths that might be traversed through a program during its execution. This could be particularly useful for understanding obfuscated code where control flow has been altered. (eg. flattened control flow)
    - eg. s_1, s_2, if() s_3, else s_4 etc
- Data Flow Graph (DFG): A DFG shows how data moves through the program
    - eg. x = 5, y = x, z = y, ...
- Token sequences: Tokenizing the code and representing it as sequences could help the model learn patterns in both clear and obfuscated code.
- Metadata: obfuscation technique used, complexity, JS funcs used in XSS, code length, entropy

# Obfuscation techniques

- Default Obfuscation (DE): Involved replacing identifier names with meaningless, randomly generated strings, and simplifying the code to reduce readability.
- Dead Code Injection (DCI): Inserted random, unrelated code blocks into the source code to make it more difficult to understand.
- Control Flow Flattening (CFF): Altered the program's control flow, making the execution order less obvious and harder to follow.
- Split String (SS): Split long strings into shorter chunks to obscure information that might otherwise be easily readable