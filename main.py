def longest_common_prefix(string1, string2, string3):
    """
    Returns the longest common prefix of three strings.
    
    :param string1: First input string
    :param string2: Second input string
    :return: Longest common prefix of the two strings
    """
    # Initialize an empty string to hold the common prefix
    common_prefix = ""
    
    # Iterate through both strings up to the length of the shorter one
    for i in range(min(len(string1), len(string2), len(string3))):
        # If characters at the same position are the same, add to common prefix
        if string1[i] == string2[i] == string3[i]:
            common_prefix += string1[i]
        #if the characters differ, break the loop and return the common prefix found so far
        else:
            break
    return common_prefix

print(longest_common_prefix("flower", "flow", "flight"))  # Example usage, should return "fl"
print(longest_common_prefix("dog", "racecar", "car"))  # Example usage, should return ""