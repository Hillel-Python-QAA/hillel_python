list1 = ["1,2,3,4", "1,2,3,4,50", "qwerty1,2,3"]

def element_sum(my_list: list):
    """
    :param my_list: list of strings that contain numbers divided by comma
    :return: numbers sum for each list element
    """
    for element in my_list:
        elem_sum = 0
        split_element = element.split(",")
        for item in split_element:
            elem_sum += int(item)
        print(elem_sum)


try:
    element_sum(list1)
except Exception:
    print("Не можу це зробити")
