def is_palindrome(string:str)-> bool:
    string = string.lower()
    indesejados = "! ? , . ; : - _ "
    desejados = [c for c in string if c not in indesejados]
    palavras = "".join(desejados)
    inverso = ""
    for letra  in range(len(palavras) -1 , -1 , -1):
        inverso += palavras[letra]
    if inverso == palavras:
        return True
    else: 
        return False



is_palindrome("Anotaram a data da maratona!")
    
