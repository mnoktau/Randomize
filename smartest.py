import random
from datetime import datetime

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

# Tüm eşleşmeleri kontrol eden fonksiyon
def find_matching_digits(target_numbers):
    for target_number in target_numbers:
        print(f"\nChecking for target number: {target_number}")
        for _ in range(10):
            # Generate a random number between 1 and 9
            random_number = str(random.randint(1, 9))
            
            results = []
            for _ in range(5):
                result = ana_bulucu()
                if result:
                    results.append(result)

            # Combine the results into a single string
            combined_number = ''.join(item for tup in results for item in tup)
            first_nine_digits = combined_number[:9]

            # Find matching digits at the same position for target_number and random number
            for i in range(9):
                if i < len(first_nine_digits) and first_nine_digits[i] == target_number[i] == random_number:
                    print(f"Matching digit at position {i+1}: {first_nine_digits[i]} (Random Number: {random_number})")
                    break

# Find and print matching digits at the same position for both target numbers
find_matching_digits(["123456789", "987654321"])

# O anki zamanı al
now = datetime.now()

# Saliseyi al
milliseconds = now.microsecond // 10000

print("Şu anki salise:", milliseconds)
