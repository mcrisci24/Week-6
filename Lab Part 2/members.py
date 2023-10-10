library_members = []                    # Creates a list that can include all library members

def register_member(name):                  # Defines a function that adds new members to library member list
    if name not in library_members:         # If name not present in system add as new member
        library_members.append(name)        # Adds new member name to list

def find_member(name):                      # Defines a function that cane find current member in library list
    return name in library_members          # If name in library_members list then return member name
