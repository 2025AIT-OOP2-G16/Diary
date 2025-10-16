from diaries.AbstractDiary import AbstractDiary
class NakashimaDiary(AbstractDiary):
    def get_date(self):
        return "2025-10-16"
    
    def get_summary(self):
        return """今日はオブジェクト指向プログラミング演習2のグループワークだった"""
    
    def get_author(self):
        return "Nakashima"