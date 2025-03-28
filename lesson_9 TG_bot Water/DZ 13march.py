# Принимать на вход строку с информацией о продажах в формате: "товар:количество", разделённую запятыми.
# Нужно преобразовывать эту строку в словарь, где ключ – название товара, а значение – суммарное количество продаж.
# Пример ввода:
# "яблоко:10,банан:5,яблоко:7,апельсин:3"
# Пример вывода:
# "{ яблоко:17,банан:5,апельсин:3 }"

tov = 'яблоко:10,банан:50,яблоко:71,лимон:6,апельсин:32,курага:20,маракуя:12,банан:15,ананас:5,персик:8,курага:6'
spisok = tov.split(',')
frukty = []
county = []
print('spisok:',spisok)
for elem in spisok:
    frukt = []
    count = []
    for i, simb in enumerate(elem):
        if simb != ':':
            frukt.append(simb)
        elif simb == ':':

            try:
                count.append(elem[i+1])
            except:
                pass

            try:
                count.append(elem[i+2])
            except:
                pass

            frukt_ = ''.join(frukt)
            count_ = ''.join(count)
            frukty.append(frukt_)
            county.append(int(count_))
            break
print()
print('frukty:', frukty)
print('county:', county)

# print(dict(zip(frukty,county)))
has_duplicates = len(set(frukty)) != len(frukty)
print('Есть дубликаты? -',has_duplicates)
print()

if has_duplicates:
    counter = 0
    for ind, element in enumerate(frukty):
    # for ind in range(len(frukty)):
        print('frukty for:', frukty)

        try:
            print('ind:', ind)
            print('Берем элемент с индексом ', counter)
            frukt_etalon = frukty[counter]
            print('Это:', frukt_etalon)
        except Exception as e:
            print("Ошибка в 1:", e)
        try:
            flag_sovpadeny = False
            for i in range(len(frukty)):
                print('i+1:', i+1)
                if frukt_etalon == frukty[i+1]:
                    print( f'Дубликат frukt_etalon: {frukt_etalon} и frukty[i+1]: {frukty[i+1]}' )
                    print( f'Индекс дубликата  frukt_etalon: {frukty.index(frukt_etalon)}  frukty[i+1]: {i+1}  ' )
                    if i+1 != frukty.index(frukt_etalon):
                        dubll2 = frukty.pop(i+1)
                        dubll1 = frukty.pop(frukty.index(frukt_etalon))
                        print( f'Удалили {dubll1} и {dubll2}' )
                        print('frukty if2:', frukty)
                        flag_sovpadeny = True
                        print()
                # else:
                #     print( f'Сравнивали: {frukt_etalon} и {frukty[i+1]}' )


        except Exception as e:
            print("Ошибка в 2:", e)

        if flag_sovpadeny == False:
            counter += 1
            print(f'Совпадений небыло: {frukt_etalon} - ')
            print()
            continue
    print('frukty_0:',tov)
    print('frukty:',frukty)



