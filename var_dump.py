TAB = "   "
PRINTABLE = ["str", "int", "float", "complex", "bool", "bytes", "bytearray", "memoryview", "NoneType"]

def VAR_DUMP(v, level=0):
    indent = _calc_indent(level)
    match type(v).__name__:
        case "tuple":
            return _dump_arr(v, level + 1, "\r\n" + indent + "(") + ")"
        case "list":
            return _dump_arr(v, level + 1, "\r\n" + indent + "[") + "]"
        case "set":
            return _dump_arr(v, level + 1, "\r\n" + indent + "{") + "}"
        case "dict":
            return _dump_obj(v, level + 1, "\r\n" + indent + "{") + "}"
        case _:
            return str(v)

def _dump_arr(arr, level, lead):
    indent = _calc_indent(level)
    result = lead
    count = 0
    for e in arr:
        count += 1
        if type(e).__name__ in PRINTABLE:
            if count == len(arr):
                result += "\r\n" + indent + str(e)
            else:
                result += "\r\n" + indent + str(e) + ","
        else:
            result += VAR_DUMP(e, level)
    return result + "\r\n" + _calc_indent(level-1)

def _dump_obj(obj, level, lead):
    indent = _calc_indent(level)
    result = lead
    keys = list(obj.keys())
    count = 0
    for key in keys:
        count += 1
        if count == len(keys):
            result += "\r\n" + indent + str(key) + " : " + VAR_DUMP(obj[key], level)
        else:
            result += "\r\n" + indent + str(key) + " : " + VAR_DUMP(obj[key], level)+ ","
    return result + "\r\n" + _calc_indent(level-1)

def _calc_indent(level):
    indent = ""
    i = 0
    while i < level:
        indent += TAB
        i += 1
    return indent

