from .file_management import txt_importer


def process(path_file, instance):
    """Aqui irá sua implementação"""
    for file in instance._items:
        if file["nome_do_arquivo"] == path_file:
            print(f"Arquivo {path_file} já processado")
            return

    data = txt_importer(path_file)
    if data is not None:
        file_data = {
            "nome_do_arquivo": path_file,
            "qtd_linhas": len(data),
            "linhas_do_arquivo": data
        }
        instance.enqueue(file_data)
        print(file_data)


def remove(instance):
    """Aqui irá sua implementação"""
    if len(instance) == 0:
        print("Fila vazia")
        return

    file = instance.dequeue()
    print(f"Arquivo {file['nome_do_arquivo']} removido da fila")
    return file


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
