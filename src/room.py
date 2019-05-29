# Implement a class to hold room information. This should have name and
# description attributes.

"""
, n_to, s_to, e_to, w_to

        self.n_to = n_to
        self.s_to = s_to
        self.e_to = e_to
        self.w_to = w_to

"""


class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
