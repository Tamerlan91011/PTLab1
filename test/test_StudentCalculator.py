# -*- coding: utf-8 -*-
from src.StudentCalculator import StudentCalculator
import pytest


class TestStudentCalculator:
    @pytest.fixture()
    def input_data(self) -> tuple[list[dict[str, dict[str, int]]], int]:
        data = [
            {
                "Иванов Иван Иванович":
                {"математика": 80, "программирование": 90, "литература": 76}},
            {
                "Петров Петр Петрович":
                {"математика": 100, "социология": 90, "химия": 61}
            }
            ]

        result: int = 0

        return data, result

    def test_init_student_calculator(self,
                                     input_data:
                                         tuple[
                                             list[dict[str, dict[str, int]]],
                                             int]) -> None:
        calc = StudentCalculator(input_data[0])
        assert input_data[0] == calc.studentsList

    def test_get_best_student_count(self,
                                    input_data:
                                        tuple[
                                            list[dict[str, dict[str, int]]],
                                            int]) -> None:
        bestCount = StudentCalculator(input_data[0]).getBestStudentsCount()
        assert pytest.approx(bestCount) == input_data[1]
