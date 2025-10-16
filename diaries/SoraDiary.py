from diaries.AbstractDiary import AbstractDiary

# 日記データを設定するクラス
class SoraDiary(AbstractDiary):
    def get_date(self):
        return "2025-10-16"

    def get_summary(self):
        return "今日は、オブジェクト指向及びプログラム演習の授業があった。GitHubの使い方について学んだが、" \
        "まだ完全には理解できないので、復習が必要だと感じた。"

    def get_author(self):
        return "Sora"