class ExpressionEvaluator:
    def __init__(self):
        self.operators = {
            "+": (1, lambda x, y: x + y),
            "-": (1, lambda x, y: x - y),
            "*": (2, lambda x, y: x * y),
            "/": (2, lambda x, y: x / y)
        }
    
    def evaluate_expression(self, expression):
        tokens = expression.split()
        output_queue = []
        operator_stack = []

        for token in tokens:
            if token.isnumeric():
                output_queue.append(float(token))
            elif token in self.operators:
                while operator_stack and operator_stack[-1] != "(" and self.operators[token][0] <= self.operators[operator_stack[-1]][0]:
                    output_queue.append(operator_stack.pop())
                operator_stack.append(token)
            elif token == "(":
                operator_stack.append(token)
            elif token == ")":
                while operator_stack[-1] != "(":
                    output_queue.append(operator_stack.pop())
                operator_stack.pop()

        while operator_stack:
            output_queue.append(operator_stack.pop())
        
        value_stack = []
        for token in output_queue:
            if isinstance(token, float):
                value_stack.append(token)
            elif token in self.operators:
                y = value_stack.pop()
                x = value_stack.pop()
                result = self.operators[token][1](x, y)
                value_stack.append(result)

        return value_stack[0]

# Create an instance of ExpressionEvaluator
evaluator = ExpressionEvaluator()

# Evaluate an expression
expression = "3 + 4 * 2 / ( 1 - 5 )"
result = evaluator.evaluate_expression(expression)
print(f"The result of '{expression}' is:", result)
