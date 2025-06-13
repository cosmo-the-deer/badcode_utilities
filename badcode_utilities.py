# made by cosmo the deer

# ==============================
def can_str_be_int(string):
    
    """
    check if the passed string "string" can be
    converted to int if true it returns true
    else it returns false
    """

    try:
        int(string)
        return True
    except ValueError:
        return False

# ==============================
def str_to_int_or_none(string):
    
    if can_str_be_int(string):
        return int(string)
    else:
        return None

# =====================
def get_yn_bool(text):

    gput = ""
    while gput != "y" and gput != "n":
        gput = input(text).lower()
    return True if gput == "y" else False

# =====================
def get_yn_str(text):

    gput = ""
    while gput.lower() != "y" and gput.lower() != "n":
        gput = input(text)
    return gput

#======================
#print(get_yn_str(">"))