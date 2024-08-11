# Списковы, словарные сборки
# Задача

first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']

first_result  = [len(f_string) for f_string in first_strings if len(f_string) > 4]
second_result  = [(f_string, s_string) for f_string in first_strings  for s_string in second_strings
                  if len(f_string) == len(s_string)]
third_result  = {st : len(st) for st in first_strings + second_strings
                 if len(st) % 2 == 0}

print(first_result)
print(second_result)
print(third_result)


