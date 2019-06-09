#!/usr/bin/env python3

def convert_string_to_version_component_numbers(s):
    """
    Waypoin 1 Convert a Semantic Versioning Component Number String to a Tuple,
    write a Python function that takes an argument s

    @param: a string representation of a semantic versioning 3-component
    number (at least 1)
    @return: a tuple composed of 3 integers (major, minor, patch).
    """
    try:
        list_number = s.split(".")
        major = int(list_number[0])
        if s.count('.') == 2:
            minor = int(list_number[1])
            patch = int(list_number[2])
        elif s.count('.') == 1:
            minor = int(list_number[1])
            patch = 0
        else:
            minor = 0
            patch = 0
        return major, minor, patch
    except Exception:
        return "Not value !!"


def compare_versions(this, other):
    """
    Waypoin 2 Compare version, write a Python function to compare versions
    that takes two argument this and other.

    @param: this both tuples composed of 3 integers (major, minor, patch) each
            other both tuples composed of 3 integers (major, minor, patch) each
    @returns: 1 if this is above other
              0 if this equals other
             -1 if this is below other
    """
    if this > other:
        return 1
    elif this < other:
        return -1
    else:
        return 0


class Version:
    """
    Waypoint 3 Write a Class Version
    Write a Python class Version which class construction.

    @param: arg1, arg2. arg3: optional arguments
    @return: Version object with three attributes: major, minor, patch
    """
    def __init__(self, arg1, arg2=0, arg3=0):
        self.arg1 = arg1
        self.arg2 = arg2
        self.arg3 = arg3
        self.major, self.minor, self.patch = self.get_version()


    def get_version(self):
        if type(self.arg1) == str:
            return convert_string_to_version_component_numbers(self.arg1)
        elif type(self.arg1) == tuple:
            return self.arg1
        elif type(self.arg1) == int:
            return self.arg1, self.arg2, self.arg3

    def __repr__(self):
        """
        Waypoint 4 Compute "Official" String Representations
        Write the instance method __repr__ to compute the “official”
        string representation of a Version object.

        @return: a string representation of a valid Python expression that
        could be used to recreate an object with the same value.
        """
        return "Version" + str(self.get_version())


    def __str__(self):
        """
        Waypoint 5 Compute "Informal" String Representation
        Write the instance method __str__ to compute the "informal" or
        nicely printable string representation of a Version object.

        @return: "informal" or nicely printable string representation
        of a Version object.
        """
        return ('.'.join(str(num) for num in self.get_version()))

    # Waypoint 6: Compare Version Instances
    def __lt__(self, other):
        flag = compare_versions(self.get_version(), other.get_version())
        if flag == -1:
            return True
        else:
            return False


    def __le__(self, other):
        flag = compare_versions(self.get_version(), other.get_version())
        if flag == -1 or flag == 0:
            return True
        else:
            return False


    def __eq__(self, other):
        flag = compare_versions(self.get_version(), other.get_version())
        if flag == 0:
            return True
        else:
            return False


    def __ne__(self, other):
        flag = compare_versions(self.get_version(), other.get_version())
        if flag != 0:
            return True
        else:
            return False


    def __gt__(self, other):
        flag = compare_versions(self.get_version(), other.get_version())
        if flag == 1:
            return True
        else:
            return False


    def __ge__(self, other):
        flag = compare_versions(self.get_version(), other.get_version())
        if flag == 1 or flag == 0:
            return True
        else:
            return False


def main():
    pass


if __name__ == '__main__':
    main()
