# Пространство имен

def test_function():

    def inner_function():
        result = str('Я в области видимости функции test_function')
        print(result)
        return result
    result = inner_function()
    return result

result = test_function()
# result_1 = inner_function()