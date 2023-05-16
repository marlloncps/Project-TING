from ting_file_management.queue import Queue


def exists_word(word, instance):
    files_info = []

    for i in range(len(instance)):
        file_info = {
            'palavra': word,
            'arquivo': instance.search(i)['nome_do_arquivo'],
            'ocorrencias': []
        }
        rows = instance.search(i)['linhas_do_arquivo']

        for j in range(len(rows)):
            if word.lower() in rows[j].lower():
                file_info['ocorrencias'].append({'linha': j+1})

        if file_info['ocorrencias']:
            files_info.append(file_info)

    return files_info


def search_by_word(word, instance: Queue):
    for index in range(len(instance)):
        result = []
        words_found = []
        file = instance.search(index)
        for index, line in enumerate(file['linhas_do_arquivo']):
            if word.lower() in line.lower():
                words_found.append({'linha': index + 1, 'conteudo': line})
        if words_found:
            result.append({
                'palavra': word,
                'arquivo': file['nome_do_arquivo'],
                'ocorrencias': words_found,
            })
    return result
