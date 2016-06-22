from Queue import *
def braces(values):
    result = []
    close_braces = "}])"
    input_stack = []

    index = 0

    for s in values:
        index += 1
        if s not in close_braces:
            input_stack.append(s)
            result.append(s)
        else:
            brace = input_stack.pop()
            if s == "}" and brace != "{":
                result.append("NO")
                return result
            if s == "]" and brace != "[":
                result.append("NO")
                return result
            if s == ")" and brace != "(":
                result.append("NO")
                return result
    result[0] = "YES"
    return result


values = []
values.append("{")
values.append("}")
values.append("[")
values.append("]")
values.append("(")
values.append(")")

#print braces(values)

values1 = []
values1.append("{")
values1.append("[")
values1.append("}")
values1.append("]")
values1.append("}")

print braces(values1)