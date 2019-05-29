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

    def __str__(self):
        return f"{self.name} room is {self.description}."
