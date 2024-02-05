#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    result_list = []
    try:
        for i in range(list_length):
            try:
                if i < len(my_list_1) and i < len(my_list_2):
                    try:
                        result = my_list_1[i] / my_list_2[i]
                    except ZeroDivisionError:
                        result = 0
                        print("division by 0")
                    except (TypeError, ValueError):
                        result = 0
                        print("wrong type")
                else:
                    raise IndexError("out of range")
            except IndexError as e:
                print(e)
                result = 0
            finally:
                result_list.append(result)
    except Exception as e:
        print("An error occurred:", e)
    finally:
        return result_list
