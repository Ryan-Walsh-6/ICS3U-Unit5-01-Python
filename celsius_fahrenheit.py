#!/usr/bin/env python3

# created by: Ryan Walsh
# created on: December 2020
# this program has a function that converts celsius to fahrenheit

def fahrenheit():
    # this program has a function that converts celsius to fahrenheit

    # input, process & output
    while True:
        temp_celsius = input("Enter a temperature (°C): ")
        print("\n", end="")
        try:
            temp_celsius = int(temp_celsius)
            temp_fahrenheit = (9/5) * temp_celsius + 32
            print("{0}°C is equal to {1}°F".format(temp_celsius,
                                                   temp_fahrenheit))
            break
        except Exception:
            print("{0} is not a temperature. Please enter a temperature."
                  .format(temp_celsius))
            print("\n", end="")


def main():
    # this function just calls other functions

    # call function
    fahrenheit()


if __name__ == "__main__":
    main()
