calls = 0

def count_calls():
    global calls
    calls += 1
    return calls

def string_info(string_a):
    count_calls()
    t_string_info = tuple()
    t_string_info = (len(string_a), string_a.upper(), string_a.lower())
    return t_string_info

def  is_contains(string_b, list_to_search):
    count_calls()
    cond = False
    a = string_b.lower()
    for i in range(0, len(list_to_search)):
        b = list_to_search[i]
        b = b.lower()
        if a == b:
            cond = True
    return cond


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)
