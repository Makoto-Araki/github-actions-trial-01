from utils.names import NameDivider

def main():
    """ メインクラス
    """

    # 初期化
    divider = None

    # 処理対象
    customers = [
        "山田 太郎",
        "佐藤　花子",
        "鈴木  　一郎",
        "  高橋　次郎  ",
    ]

    # 処理開始
    try:

        # インスタンス生成
        divider = NameDivider()

        # 処理対象の姓名分離
        for full_name in customers:
            try:
                family_name, first_name = divider.divide(full_name)
                print(f"{family_name} {first_name}")
            except ValueError as e:
                print(f"エラー: {full_name} ({e})")
    
    # 例外処理
    except:
        pass

    # 後処理
    finally:
        if divider:
            divider = None

if __name__ == "__main__":
    main()
