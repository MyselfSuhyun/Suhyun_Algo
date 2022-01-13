def use_keyword_arg_unpacking(**params):
    for k in params.keys():
        print("{0}: {1}".format(k, params[k]))

print("use_keyword_arg_unpacking()의 호출")
use_keyword_arg_unpacking(a=1, b=2, c=3)
