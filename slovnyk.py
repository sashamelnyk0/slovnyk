a=int(input('Ця програма має 2 функції: 1)Сортувати  слова в алфавітному порядку. 2)Рахувати букви в тексті. Виберіть що ви хочете: 1 або 2:'))
if a==1:
    text=input(str('Введіть текст:'))
    n=sorted(text.split())
    print(set(n))
elif a==2:
    word=str(input('Введіть текст:'))
    d={}
    for i in set(word):
        d[i]=word.count(i)
    print(d)