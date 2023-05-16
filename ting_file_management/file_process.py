import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    instance_len = len(instance)

    for index in range(instance_len):
        check = instance.search(index)['nome_do_arquivo']
        if check == path_file:
            return None
    rows = txt_importer(path_file)

    formate = {
        'nome_do_arquivo': path_file,
        'qtd_linhas': len(rows),
        'linhas_do_arquivo': rows
    }

    formate_str = str(formate)

    instance.enqueue(formate)

    return sys.stdout.write(formate_str)


def remove(instance):
    try:
        path_file = instance.dequeue()['nome_do_arquivo']
        msg = f"Arquivo {path_file} removido com sucesso"
        print(msg)
    except IndexError:
        msg = "Não há elementos"
        print(msg)


def file_metadata(instance, position):
    if position < 0 or position >= len(instance):
        return sys.stderr.write("Posição inválida\n")

    metadata = instance.search(position)
    formate_str = str(metadata)
    return sys.stdout.write(formate_str)
