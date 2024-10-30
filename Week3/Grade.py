Score = int(input("กรุณากรอกคะแนนของท่าน : "))
if Score > 100:
    print("ไม่สามารถใส่คะแนนมากกว่า 100")
elif Score < 0:
    print("ไม่สามารถใส่คะแนนน้อยกว่า 0")
elif Score >= 80:
    print("4")
elif Score >= 75:
    print("3.5")
elif Score >= 70:
    print("3")
elif Score >= 65:
    print("2.5")
elif Score >= 60:
    print("2")
elif Score >= 55:
    print("1.5")
elif Score >= 50:
    print("1")
else:
    print("0\nแก้ 0 ป่าว")
    Adjustment = str(input("แก้ป่าว(ํYes or No) : "))
    if Adjustment == "Yes":
        Miss = 50 - Score
        print(f"ขาด {Miss} คะแนน")
    else:
        print("ว้ายติด 0")