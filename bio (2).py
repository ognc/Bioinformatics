def return_sequence(name): #возвращает словарь, ключи - заголовки, значения - все строки, скленные вместе в одну
    with open(name) as file:
        id_sequences = {}
        for line in file:
            line = line.strip()
            if line.startswith('>'):
                id = line
            if not line.startswith('>') and line != '':
                if id in id_sequences:
                    id_sequences[id] += line
                else:
                    id_sequences[id] = line
    return(id_sequences)



def kmp():
    #for_search_file, where_to_search_file = input().split(' ')
    for_search_file = 'searchthis.fa' #вставь путь к файлу подстроки
    where_to_search_file='searchthere.fa' #вставь путь к файлу строки

    for_search =  return_sequence(for_search_file)
    print(for_search[list(for_search.keys())[0]])
    where_to_search = return_sequence(where_to_search_file)



    def PrefixFunction(string):
        Prefixes = [0 for _ in range(len(string))]
        j = 0
        i = 1
        while i < len(string):
            if string[i] == string[j]:
                Prefixes[i] = j + 1
                i += 1
                j += 1
            else:
                if j == 0:
                    Prefixes[i] = 0
                    i += 1
                else:
                    j = Prefixes[j-1]
        return(Prefixes)

    for a in where_to_search:
        print(where_to_search[a])
        all_hail = for_search[list(for_search.keys())[0]] + '$' + where_to_search[a]
        counter = 0
        prefixes = PrefixFunction(all_hail)
        for _ in range(len(prefixes)):
            if prefixes[_] == len(for_search[list(for_search.keys())[0]]):
                print(_ - 2 * len(for_search[list(for_search.keys())[0]]) + 1)
                counter += 1
        if counter == 0:
            print(-1)



kmp()