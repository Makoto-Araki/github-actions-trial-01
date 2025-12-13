import pytest
from utils.names import NameDivider

class TestNameDivider:
    def setup_method(self):
        self.divider = NameDivider()

    def test_half_width_space(self):
        family, first = self.divider.divide("山田 太郎")
        assert family == "山田"
        assert first == "太郎"

    def test_full_width_space(self):
        family, first = self.divider.divide("山田　太郎")
        assert family == "山田"
        assert first == "太郎"

    def test_multiple_spaces(self):
        family, first = self.divider.divide("山田 　 太郎")
        assert family == "山田"
        assert first == "太郎"

    def test_leading_and_trailing_spaces(self):
        family, first = self.divider.divide(" 山田　太郎 ")
        assert family == "山田"
        assert first == "太郎"

    def test_invalid_name_raises_error(self):
        with pytest.raises(ValueError):
            self.divider.divide("山田")

    def test_non_string_input_raises_error(self):
        with pytest.raises(ValueError):
            self.divider.divide(None)