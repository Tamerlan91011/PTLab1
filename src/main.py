# -*- coding: utf-8 -*-
import argparse
import sys

from YamlDataReader import YamlDataReader
from StudentCalculator import StudentCalculator

def get_path_from_arguments(args) -> str:
    parser = argparse.ArgumentParser(description="Path to datafile")
    parser.add_argument("-p", dest="path", type=str, required=True,
                        help="Path tp datafile")
    args = parser.parse_args(args)
    return args.path


def main():
    path = get_path_from_arguments(sys.argv[1:])

    reader = YamlDataReader()
    students = reader.read(path)
    print("Students: ", students)

    bestStudentsCount = StudentCalculator(students).getBestStudentsCount()

    print(f"Have {bestStudentsCount} best students")
    # rating = CalcRating(students).calc()
    # print("Rating: ", rating)


if __name__ == "__main__":
    main()
