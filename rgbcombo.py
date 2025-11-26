#!/usr/bin/env python3
# Created By: Abdul
# Date: 11/20/2025
# Program to show all valid color combos


def main():

    # for loop to iterate through all red combinations
    for red in range(0, 256, 1):
        # for loop to iterate through all green combinations
        for green in range(0, 256, 1):
            # for loop to iterate through all blue combinations
            for blue in range(0, 256, 1):
                # print the rgb values with correct colors
                print(
                    f"\033[1;38;2;{red};{green};{blue}mRGB({red}, {green}, {blue})\033[0m"
                )


if __name__ == "__main__":
    main()
