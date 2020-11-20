#!/usr/bin/env python3

# Created by Jonathan Pasco-Arnone
# Created on November 2020
# This program calculates the Area and perimeter of a rectangle

import math


def main():
    print("This program calculates the area and perimeter of a rectangle.")
    length_str = input("Please enter a length measurement: ")
    width_str = input("Please enter a width measurement: ")
    length = int(length_str)
    width = int(width_str)
    print("")
    print("If a rectangle has a length of " + length_str + "mm " +
          "and the width of " + width_str + "mm")
    area = width*length
    perimeter = width + width + length + length
    print("Then the Area is {:.2f}mm²".format(area))
    print("And the Perimeter is {:.2f}mm".format(perimeter))


if __name__ == "__main__":
    main()
