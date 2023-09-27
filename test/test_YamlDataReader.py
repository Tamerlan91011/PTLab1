# -*- coding: utf-8 -*-
import pytest
from src.YamlDataReader import YamlDataReader


class TestYamlDataReader:
    @pytest.fixture()
    def file_and_data_content(self) -> tuple[str, list[dict[str, set]]]:
        file = """
        - Иванов Иван Иванович:
            математика: 80
            программирование: 90
            литература: 76
        - Петров Петр Петрович:
            математика: 100
            социология: 90
            химия: 61
        """
               
        data = [
            {
                "Иванов Иван Иванович":
                {"математика": 80, "программирование": 90, "литература": 76}},
            {
                "Петров Петр Петрович":
                {"математика": 100, "социология": 90, "химия": 61}
            }
            ]
        return file, data

    @pytest.fixture()
    def filepath_and_data(self,
                          file_and_data_content: tuple[str, list[dict[str, set]]],
                          tmpdir) -> tuple[str, list[dict[str, set]]]:
        p = tmpdir.mkdir("datadir").join("my_data.txt")
        p.write_text(file_and_data_content[0], encoding='utf-8')
        return str(p), file_and_data_content[1]

    def test_read(self, filepath_and_data: tuple[str, list[dict[str, set]]]) -> None:
        file_content = YamlDataReader().read(filepath_and_data[0])
        assert file_content == filepath_and_data[1]
