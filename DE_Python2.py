def pipeline(*funcs):
    def helper(arg):
        for elem in funcs:
            arg = elem(arg)
        return arg

    return helper
