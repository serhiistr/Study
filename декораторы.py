import webbrowser


def validator(func):
    def wrapper(url):
        if "." in url:
            func(url)
        else:
            print("You write the wrong address")
    return wrapper #в конце круглые скобки не добавлять. Иначе это будет сразу и выполнение этой функции


@validator # декоратор проверяет есть ли точка
def open_url(url):
    webbrowser.open(url)


open_url("https://google.com.ua")
