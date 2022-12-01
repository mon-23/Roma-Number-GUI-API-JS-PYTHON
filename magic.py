

bio = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

def work_1(inp):
    cache = []
    sum_value = 0
    for i in inp:
        if i == 'I' or i == 'V' or i == 'X' or i == 'L' or i == 'C' or i == 'D' or i == 'M':
            cache.append(bio[i])
        else:
            return 'wrong letter'

    if len(cache) > 2:
        if cache[-2] and cache[-3] < cache[-1]:
            return 'wrong string'

    while cache != []:
        if len(cache) > 1:
            if cache[-1]  > cache[-2]:
                if cache[-1] == 5 and cache[-2] == 1 or cache[-1] == 50 and cache[-2] == 10 or cache[-1] == 500 and cache[-2] == 100 or cache[-1] == 10 and cache[-2] == 1 or cache[-1] == 100 and cache[-2] == 10 or cache[-1] == 1000 and cache[-2] == 100:
                    sum_value += (cache[-1] - cache[-2])
                    del cache[-1]
                    del cache[-1]
                else:
                    return 'wrong string2'
            else:
                sum_value += cache[-1]
                del cache[-1]    
        else:
            sum_value += cache[0]
            del cache[-1]
    return sum_value




l_1 = [1, 5, 10, 50, 100, 500, 1000]
l_2 = ['I', 'V', 'X', 'L', 'C', 'D', 'M']


def work_2(inp):
    char = ''
    counter = 2
    if int(inp) > 0:
        num = int(inp)
        while num != 0:
            if num >= 1000:
                char += l_2[-1]
                num -= l_1[-1]
            else:
                if num >= l_1[-counter]:
                    char += l_2[-counter]
                    num -= l_1[-counter]
                else:
                    counter += 1

### OBEN STRING ERSTELLEN / UNTEN STRING FORMATIEREN (SONDERFÄLLE) ###

        char = list(char)
        if len(char) >= 4:
            new_char = []
            a = 0
            b = 1
            y = 2
            z = 3
            while len(char) != 0:
                if len(char) >= 4:
                    if char[a] and char[b] and char[y] and char[z] == char[a]:
                        if len(new_char) > 0:
                            if ((bio[new_char[-1]] + bio[char[a]] + bio[char[b]] + bio[char[y]] + bio[char[z]] != 9) and (bio[new_char[-1]] + bio[char[a]] + bio[char[b]] + bio[char[y]] + bio[char[z]] != 90) and (bio[new_char[-1]] + bio[char[a]] + bio[char[b]] + bio[char[y]] + bio[char[z]] != 900)): 
                                for i in range(len(l_2)):
                                    if char[a] == l_2[i]:
                                        new_char.append(char[a])
                                        new_char.append(l_2[i+1])
                                        del char[0:4]
                                        break
                            else:
                                for i in range(len(l_2)):
                                    if new_char[-1] == l_2[i]:
                                        del new_char[-1]
                                        new_char.append(l_2[i-1])
                                        new_char.append(l_2[i+1])
                                        del char[0:4]
                                        break
                        else:
                            for i in range(len(l_2)):
                                if char[a] == l_2[i]:
                                    new_char.append(char[a])
                                    new_char.append(l_2[i+1])
                                    del char[0:4]
                                    break
                    else:
                        new_char += char[a]
                        del char[a]
                else:
                    for i in char:
                        new_char.append(i)
                        del char[a]
                        break
            return ''.join(new_char)        
        else:
            return ''.join(char)
    else:
        return 'No number'













