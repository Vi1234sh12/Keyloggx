import matplotlib.pyplot as plt

log_file = open("project/key_log.txt", "r+")

chars = 0
lines = 0
letters = []
counted = {}
new_dict = {}

for i in log_file.read():
    if i == '\n':
        lines += 1
    chars += 1
    letters.append(i)

key_string = "".join(letters)
word_string = key_string.replace('\n', " ")
final_keywords_list = word_string.split()

for letter in final_keywords_list:
    letr = str(letter)
    if letr in counted:
        counted[letr] += 1
    else:
        counted[letr] = 1

for item in counted:
    if counted[str(item)] >= 3:
        new_dict[str(item)] = counted[str(item)]

print(lines, "Lines", " || ", chars, "Character",
      " || ", len(final_keywords_list), "Words")
print('\n')

plt.title('KEYLOG ANALYSIS', fontsize=20)
plt.bar(range(len(new_dict)), list(new_dict.values()))
plt.xticks(range(len(new_dict)), list(new_dict.keys()))

plt.show()

new_log_file = open('new-log.txt', 'w+')
for line in counted:
    if line != '\n':
        new_log_file.write(str(line))
        new_log_file.write("          ")
        new_log_file.write(str(counted[line]))
        new_log_file.write('\n')
        new_log_file.write('\n')

    
