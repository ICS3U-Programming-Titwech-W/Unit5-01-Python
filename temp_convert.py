#!/usr/bin/env python3

# Created by: Titwech Wal
# Created on: May.5.2022
# This function lets you enter a temperature in degrees
# Celsius (as a decimal), and converts and displays
# the temperature in Farenheit.


def calculate_fahrenheit():

    # input from user
    celsius = int(input("Enter the tempeture in celsius to covert: "))
    print("")

    # process
    farenheit = (9/5)*celsius+32

    # output
    print("{}°C is equal to {}°F". format(celsius, farenheit))


def main():

    try:
        calculate_fahrenheit()
    except Exception:
        print("Please enter a vaild number")


if __name__ == "__main__":
    main()
