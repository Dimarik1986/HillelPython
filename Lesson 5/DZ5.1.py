import keyword
import string
test_variables = ["","_", "__", "___", "x", "get_value", "get value", "get!value", "some_super_puper_value",
                  "Get_value" ,"get_Value", "getValue", "3m", "m3", "assert", "assert_exception"]


for test_variable in test_variables:
    if len(test_variable) > 0:
        if test_variable in keyword.kwlist:
            print(test_variable, "=>", False)
        elif test_variable.find("__") != -1:
            print(test_variable, "=>", False)
        elif test_variable[0] =="_":
            print(test_variable, "=>", True)
        elif not test_variable[0].isnumeric() and test_variable.islower() and test_variable.find(" ") == -1:
            for mark_punctuation in string.punctuation.replace("_", ""):
                if mark_punctuation in test_variable:
                    print(test_variable, "=>", False)
                    break
            else:
                print(test_variable, "=>", True)
        else:
            print(test_variable, "=>", False)
    else:
        print(test_variable, "=>", False)
