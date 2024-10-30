#!/usr/bin/env python
import uuid
import pathlib as Path


def create_directory_by_datetime_jp_name(in_parent_path: Path) -> Path:
    """
    年月日時分秒の名前を付けたディレクトリを作成.
    ディレクトリ名には日本語が入っている

    Release Notes:
        - 1.0.0 (2024-10-29): 新規作成.
        - 1.1.0 (2024-10-30): 親ディレクトリが存在しな場合は親ディレクトリ作成.

    @version: 1.1.0
    """

    from datetime import datetime

    # 現在日付をフォルダ名として取得
    directory_name = datetime.now().strftime("%Y年%m月%d日_%H時%M分%S秒")
    directory_path: Path = in_parent_path / directory_name
    # ディレクトリ作成
    # ディレクトリがない場合は作成される
    directory_path.mkdir(parents=True, exist_ok=True)

    return directory_path


def random_num() -> int:
    """
    ユニークなランダム値を取得

    Release Notes:
        - 1.0.0 (2024-10-10): 新規作成.

    @version: 1.0.0
    """

    guid = uuid.uuid1()
    return int.from_bytes(guid.bytes, byteorder="big", signed=True) >> 64


def guid() -> str:
    """
    GUIDを取得

    Release Notes:
        - 1.0.0 (2024-10-10): 新規作成.

    @version: 1.0.0
    """

    return str(uuid.uuid1())


def frange(start, end, step):
    """
    開始値、終了値、ステップ値に浮動小数点数値を受け取る関数.

    Release Notes:
        - 1.0.0 (2024-10-10): 新規作成.

    @version: 1.0.0
    """

    if step == 0:
        raise ValueError("step must not be zero")

    start = float(start)
    end = float(end)
    step = float(step)

    # range関数と同様な振る舞いにする
    if abs(step) > abs(start - end):
        return [start]
    if step > 0 and end - start < 0:
        return []
    elif step < 0 and end - start > 0:
        return []

    exp = len(str(step).split(".")[1])  # 丸める際に使用する桁数
    result = [start]
    val = start
    if step > 0:
        while (val := round(val + step, exp)) < end:
            result.append(val)
    else:
        while (val := round(val + step, exp)) > end:
            result.append(val)

    return result
