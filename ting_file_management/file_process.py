import sys

from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    if path_file in str(instance._data):
        return None
    file_lines = txt_importer(path_file)
    file_dict = {
        'nome_do_arquivo': path_file,
        'qtd_linhas': len(file_lines),
        'linhas_do_arquivo': file_lines
    }
    instance.enqueue(file_dict)
    print(file_dict)


def remove(instance):
    result = instance.dequeue()
    if result == None:
        return sys.stdout.write('Não há elementos\n')
    path_file = result['nome_do_arquivo']
    return sys.stdout.write(f'Arquivo {path_file} removido com sucesso\n') 


def file_metadata(instance, position):
    try:
        file_dict = instance.search(position)
        sys.stdout.write(f'{file_dict}')
    except IndexError:
        sys.stderr.write('Posição inválida')
