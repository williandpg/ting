def exists_word(word, instance):
    """Aqui irá sua implementação"""
    word = word.lower()
    word_list = []
    for file_data in instance.queue:
        file_name = file_data["nome_do_arquivo"]
        word_data = []
        for idx, line in enumerate(file_data["linhas_do_arquivo"], start=1):
            if word in line.lower():
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
