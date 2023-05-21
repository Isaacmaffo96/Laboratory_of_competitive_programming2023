"""
Launch a method and format output

:obj: object instance
:methodName: name of the method to be run
:printObj: turn on/off object print
:params: optional name parameters for the method
"""
def test(obj, methodName, printObj=True, **params):

    # print test params
    print("Method:\t{}".format(methodName), end="")
    if params:
        print(", Params: [", end="")
        for p, v in params.items():
            print(" {}:{} ".format(p, v), end="")
        print("]", end="")
    print()

    # get method
    m = getattr(obj, methodName)

    # run the test
    result = None
    try:
        result = m(*params.values())
    except RuntimeError as e:
        print("Runtime error: " + str(e))

    # print test result
    print("Result:\t{}".format(result))
    # str(obj)
    if printObj:
        print("Obj:\t{}".format(obj))
    print("---")
