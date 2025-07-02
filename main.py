def longest_common_prefix(list_of_strings):
    """
    Returns the longest common prefix of a list of strings.
    
    :param: list of strings
    :return: Longest common prefix of the three strings
    """
    # assume the first string is the longest common prefix
    prefix = list_of_strings[0] 
    # if the list of strings is empty, return an empty string
    if not list_of_strings:
        return ""
    else:
    # iterate through the list of strings from the second string to the end
        for string in list_of_strings[1:]:
    # compare the other strings with the first string. As long as the other strings do not start with the assumed prefix, shorten the prefix by one character
            while string.startswith(prefix) is False:
                prefix = prefix[:-1]
                # if the prefix becomes empty, return an empty string
                if not prefix:
                    return ""
    # return the longest common prefix after finishing the iteration
        return prefix
def test_case(actual, expected):
    if actual is not None:
        if actual == expected:
            status = "Pass"
        else:
            status = "Nope"

        print(f"Actual: {actual:<24} Expected: {expected:<24} Result: {status}")


# Tests for Problem 6
print("\nProblem 6")
test_case(longest_common_prefix(["flower", "flow", "flight"]), "fl")
test_case(longest_common_prefix(["dog", "racecar", "car"]), "")
test_case(longest_common_prefix(["alone"]), "alone")
test_case(longest_common_prefix(["", "", ""]), "")
test_case(longest_common_prefix(["short", "shortest", "sh"]), "sh")
test_case(longest_common_prefix(["", "abc", "abd"]), "")
test_case(longest_common_prefix(["interview", "internet", "internal"]), "inter")
