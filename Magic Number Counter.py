def foo(a, b, c, *options):
    ## Возвращаем количество полученных аргументов
    return len(options)

def bar(a, b, c, **options):
    ## Если магическое число = 7, то вернуть истина
    if options.get("magicnumber") == 7:
      return True
    else:
      return False

print(foo(1, 2, 3, 4))
print(bar(1, 2, 3, magicnumber = 7))