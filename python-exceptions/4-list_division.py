#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new = []
    i = 0

    while (i < list_length):
        result = 0
        try:
            result = my_list_1[i] / my_list_2[i]
            print("{:d}".format(result), end="")
        except ValueError:
            pass
        except TypeError:
            print("wrong type")
        except ZeroDivisionError:
            print("division by 0")
        except IndexError:
            print("out of range")
        finally:
            new.append(result)
            i += 1

    return new
