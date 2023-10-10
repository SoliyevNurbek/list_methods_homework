def main(fruits):
    """
    Given a list called Fruits, it contains at least one apple. Find how many apples are on the list and return.
    Args:
        fruits(list): parameter
    Returns:
        int: return answer
    """
    i=0
    k=0
    while fruits:
        if fruits.pop()=="olma":
            k+=1
    return k
print(main(["olma","uzum","olma","nok"]))