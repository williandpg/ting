from .file_management import txt_importer


def process(path_file, instance):
    """Aqui irá sua implementação"""
    for file in instance._queue:
            if file["nome_do_arquivo"] == path_file:
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


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
