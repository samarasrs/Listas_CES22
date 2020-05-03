
def is_palindrome(nome):
    word=list(nome)
    word_reverse=word[::-1]
    if word==word_reverse:
        return True
    else:
        return False

'''
print(is_palindrome('abba'))
print(not is_palindrome('abab'))
print(is_palindrome('tenet'))
print(not is_palindrome('banana'))
print(is_palindrome('straw warts'))
print(is_palindrome('a'))
print(is_palindrome('')) #uma string vazia é palíndromo
'''





