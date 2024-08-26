def filtrar_aprovados(info:list) -> list|None:
    print(info)
    if not isinstance(info, list):
        raise TypeError('O argumento passado está incorreto')
    