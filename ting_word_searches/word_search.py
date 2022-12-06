def get_word_ocurrencies(word, file, get_content):
    search_result_list = []
    occurrency_list = []
    for index, line in enumerate(file['linhas_do_arquivo'], start=1):
        if word.lower() in line.lower():
            if get_content:
                occurrency_list.append({'linha': index, 'conteudo': line})
            else:
                occurrency_list.append({'linha': index})
    if len(occurrency_list):
        search_result_list.append({
            'palavra': word,
            'arquivo': file['nome_do_arquivo'],
            'ocorrencias': occurrency_list
        })
    return search_result_list


def exists_word(word, instance, get_content=False):
    for file in instance._data:
        search_result_list = get_word_ocurrencies(word, file, get_content)
    return search_result_list


def search_by_word(word, instance):
    return exists_word(word, instance, True)
