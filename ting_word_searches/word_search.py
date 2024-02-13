def exists_word(word, instance):
    """Aqui irá sua implementação"""
    word_list = list()

    for i in instance._queue:
        file_name = i["nome_arquivo"]
        word_data = list()
        for idx, line in enumerate(i["linhas_do_arquivo"], start=1):
            if word.lower() in line.lower():
                word_data.append({"linha": idx})

        if word_data:
            word_list.append({
                "palavra": word,
                "arquivo": file_name,
                "ocorrencias": word_data
            })

    return word_list


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
