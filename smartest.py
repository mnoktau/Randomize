import random

# Ana bulucu fonksiyonu
def ana_bulucu():
    arr = ["0", "2", "8", "84", "1", "9", "7", "16", "93", "99", "3", "75", "10"]
    while True:
        random_number = random.choice(arr)
        if random_number == "0":
            return bulucu_ilk_sayi()

# İlk sayı bulucu fonksiyonu
def bulucu_ilk_sayi():
    arr = ["0", "2", "8", "84", "1", "9", "7", "16", "93", "99", "3", "75", "10"]
    birA = random.choice(arr)
    return birA, bulucu_ikinci_sayi(birA)

# İkinci sayı bulucu fonksiyonu
def bulucu_ikinci_sayi(birA):
    arr = ["0", "2", "8", "84", "1", "9", "7", "16", "93", "99", "3", "75", "10"]
    sayar = 0
    ulasici = []

    while True:
        random_number2 = random.choice(arr)
        if random_number2 == "0" and sayar == 0:
            birB = birA
            return birB
        elif random_number2 == "0" and sayar != 0:
            birB = ulasici[sayar - 1]
            return birB
        else:
            sayar += 1
            ulasici.append(random_number2)

# First Nine Digits'i yazdırma fonksiyonu
def print_first_nine_digits():
    results = []
    for _ in range(5):
        result = ana_bulucu()
        if result:
            results.append(result)

    # Sonuçları tek bir string halinde birleştir
    combined_number = ''.join(item for tup in results for item in tup)
    first_nine_digits = combined_number[:9]
    
    # first_nine_digits'i yazdır
    print(f"First Nine Digits: {first_nine_digits}")

# First Nine Digits'i yazdır
print_first_nine_digits()
