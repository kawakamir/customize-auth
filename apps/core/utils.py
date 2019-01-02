def union_dict(*args):
    ret = {}
    for arg in args:
        ret.update(arg)
    return ret
