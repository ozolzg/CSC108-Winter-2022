dollars = int(input())
cents = int(input())

total_number_of_cents = dollars * 100 + cents
original_price = (((total_number_of_cents * 85) + 50) // 100)

print(str(original_price // 100) + ' ' + str(original_price % 100))

