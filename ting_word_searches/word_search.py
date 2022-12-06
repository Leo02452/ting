def exists_word(word, instance):
    search_result_list = []
    for file in instance._data:
        occurrency_list = []
        for index, line in enumerate(file['linhas_do_arquivo'], start=1):
            if word.lower() in line.lower():
                occurrency_list.append({ 'linha': index })
        if len(occurrency_list):
            search_result_list.append({
                'palavra': word,
                'arquivo': file['nome_do_arquivo'],
                'ocorrencias': occurrency_list
            })
    return search_result_list


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
