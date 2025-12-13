import re
from typing import Tuple

class NameDivider:
    """ 顧客の氏名を姓(Family Name)と名(First Name)に分離するクラス
    """

    def divide(self, full_name: str) -> Tuple[str, str]:
        """ 氏名文字列を姓と名に分離して返す
        """

        if not isinstance(full_name, str):
            raise ValueError("氏名は文字列で指定してください")

        # 半角・全角スペースをまとめて区切りとして分割
        parts = re.split(r"[ \u3000]+", full_name.strip())

        if len(parts) < 2:
            raise ValueError("氏名は姓と名をスペース区切りで指定してください")

        # 姓(Family Name)
        family_name = parts[0]

        # 名(First Name)
        first_name = parts[1]

        if not family_name or not first_name:
            raise ValueError("姓または名が空です")

        # 姓(Family Name)と名(First Name)を返す
        return family_name, first_name
