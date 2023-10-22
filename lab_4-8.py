sequence = input("a series of a, c, t, g")
complement_dict = ('a', 't', 'c', 'g', 't', 'a', 'g', 'c')
complementary_sequence = ''
for base in sequence:
    complementary_sequence += complement_dict[base]
print("Complemtary DNA Sequence:", complementary_sequence)