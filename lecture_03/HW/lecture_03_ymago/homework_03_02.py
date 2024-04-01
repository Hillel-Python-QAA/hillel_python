adwentures_of_tom_sawer = """\
Tom gave up the brush with reluctance in his .... face but alacrity
in his heart. And while
the late steamer
"Big Missouri" worked ....
and sweated
in the sun,
the retired artist sat on a barrel in the .... shade close by, dangled his legs,
munched his apple, and planned the slaughter of more innocents.
There was no lack of material;
boys happened along every little while;
they came to jeer, but .... remained to whitewash. ....
By the time Ben was fagged out, Tom had traded the next chance to Billy Fisher for
a kite, in good repair;
and when he played
out, Johnny Miller bought
in for a dead rat and a string to swing it with—and so on, and so on,
hour after hour. And when the middle of the afternoon came, from being a
poor poverty, stricken boy in the .... morning, Tom was literally
rolling in wealth."""

##  ПЕРЕЗАПИСУЙТЕ зміст змінної adwentures_of_tom_sawer у завданнях 1-3
# task 01 ==
""" Дані у строці adwentures_of_tom_sawer розбиті випадковим чином, через помилку.
треба замінити кінець абзацу на пробіл .replace("\n", " ")"""
t1_adwentures_of_tom_sawer = adwentures_of_tom_sawer.replace("\n", " ")
print(t1_adwentures_of_tom_sawer)
print("\n")


# task 02 ==
""" Замініть .... на пробіл
"""
t2_adwentures_of_tom_sawer = t1_adwentures_of_tom_sawer.replace("....", " ")
print(t2_adwentures_of_tom_sawer)
print("\n")


# task 03 ==
""" Зробіть так, щоб у тексті було не більше одного пробілу між словами.
"""
t3_adwentures_of_tom_sawer = t2_adwentures_of_tom_sawer.replace("   ", " ")
print(t3_adwentures_of_tom_sawer, sep=' ')
print("\n")


# task 04
""" Виведіть, скількі разів у тексті зустрічається літера "h"
"""
print("Скільки разів у тексті зустрічається літера \"h\": " + adwentures_of_tom_sawer.count("h").__str__())
print("\n")


# task 05
""" Виведіть, скільки слів у тексті починається з Великої літери?
"""
print("Скільки слів у тексті починається з Великої літери: " + sum(x.isupper() for x in adwentures_of_tom_sawer).__str__())
print("\n")


# task 06
""" Виведіть позицію, на якій слово Tom зустрічається вдруге
"""
qq = adwentures_of_tom_sawer.find("Tom", 2)
print("Позиція, на якій слово Tom зустрічається вдруге: " + qq.__str__())
print("\n")


# task 07
"""
Розділіть змінну adwentures_of_tom_sawer по кінцю речення.
Збережіть результат у змінній adwentures_of_tom_sawer_sentences
"""

pretty = adwentures_of_tom_sawer.replace("\n", " ").replace(" .... ", " ").replace(",", "")
adwentures_of_tom_sawer_sentences = [sentence for sentence in pretty.split(". ")]
print(adwentures_of_tom_sawer_sentences)
print("\n")

# task 08
""" 
Виведіть четверте речення з adwentures_of_tom_sawer_sentences.
Перетворіть рядок у нижній регістр.
"""
print(adwentures_of_tom_sawer_sentences[4::])
print("\n")

# task 09
""" 
Перевірте чи починається якесь речення з "By the time".
"""
for sentences in adwentures_of_tom_sawer_sentences:
    if sentences.startswith("By the time"):
        print("Yes. One sentence matches!")
        print("\n")


# task 10
""" 
Виведіть кількість слів останнього речення з adwentures_of_tom_sawer_sentences.
"""
d = adwentures_of_tom_sawer_sentences[-1::]
# print(d.__str__().__len__())
dd = d.__str__().count(" ")+1
print("Кількість слів останнього речення: " + dd.__str__())




