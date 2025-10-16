from diaries.DiarySample import DiarySample
from diaries.NakashimaDiary import NakashimaDiary
from diaries.KazukiDiary import KazukiDiary
from diaries.MizunoDiary import MizunoDiary
# ↓のリストには、メンバーの各日記が格納されます。
diaries = [
    DiarySample(),
    NakashimaDiary(),
    KazukiDiary(),
    MizunoDiary(),
]

for d in diaries:
    print("---------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()
