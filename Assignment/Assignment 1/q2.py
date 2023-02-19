wrong_sentence = input()

first_correction = wrong_sentence.replace(' ', ', ')
second_correction = first_correction.replace('and, ', 'and ')
third_correction = second_correction.replace(', ', ' ', 2)
final_correction = third_correction.replace(',,', ',')

print(final_correction)

# testing - not work
# correct_sentence = wrong_sentence.replace(' and', ', and')
# print(correct_sentence)
# it prints 2 comma - fix it

