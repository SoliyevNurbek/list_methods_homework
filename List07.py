def main(list01):
    """
    A list of zeros and ones is given. Find how many zeros are involved and return.
    Args:
        list01(list): parameter
    Returns:
        int: return answer
    """
    k=0
    while list01:
        if list01.pop()==0:
            k+=1
    return k
print(main([0,1,0,0,0,1,1,0,0,1,0]))