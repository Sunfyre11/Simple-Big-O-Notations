def matcher(lst, match):

    # Returns a boolean on whether the match value is present in the given list

    for item in lst:
        if item == match:
            return True
            # Returns True if the match value is present in the given list

    return False
    # ALernate result

# The BEST CASE occurs when the mtch value is first element of list
# The BEST CASE has constant runtime O(1)
# The WORST CASE occurs when the mtch value is not first element of list
# The WORST CASE has linear runtime O(n)