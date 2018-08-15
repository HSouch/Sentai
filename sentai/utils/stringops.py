def trim_string(val, new_length):
    val = str(val)
    if len(val) > new_length + 1:
        return val[0: new_length + 1]
    else:
        return val
