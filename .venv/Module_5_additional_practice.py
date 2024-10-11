# Дополнительное практическое задание по модулю 5

class Database:
    def __init__(self):
        self.data = {}

    def add_user(self, username, password):
        self.data[username] = password


class User:
    """
    Класс пользователя, содержащий атрибуты: логин и пароль (с подтверждением)

    """

    def __init__(self, username, password, password_confirm):
        self.username = username
        if password == password_confirm:
            self.password = password

def check_pswd(pswd):
    overlap = set()
    check = True
    reason = str
    letters_app ={'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'}
    letters_low = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'}
    symbols = {'!', '#', '$', '%', '^', '&', '*', '(', ')', '—', '_ ', '+', '=', ';', ':', ',' '.', '/', '?', '|', '`', '~', '[', ']'}
    numbers = {'0','1','2','3','4','5','6','7','8','9'}

    i = 0
    for i in range(len(pswd)):
        overlap.add(pswd[i])
        i+=1
    if len(overlap) < 6:
        check = False
        reason = "The password must contain more than 6 characters"
        print(reason)
    elif len(list(overlap & letters_app)) == 0:
        check = False
        reason =  "The password must contain at least one uppercase letter"
    elif len(list(overlap & letters_low)) == 0:
        check = False
        reason =  "The password must contain at least one lowercase letter "
    elif len(list(overlap & symbols)) == 0:
        check = False
        reason =  "The password must contain at least one special symbol"
    elif len(list(overlap & numbers)) == 0:
        check = False
        reason =  "The password must contain at least one digit"
    return check, reason

if __name__ == '__main__':

    database = Database()
    while True:
#        choice = input('Hello! Select the action: \n1 - Enter\n2 - Registration:\n')
        user = User(username :=input("Enter username   : "), password1 := input("Enter password   : "), password2 := input("Re-Enter password: ")) # "моржовый оператор"
        print (username)
        print (password1)
        print (password2)
        if password1 != password2:
            print("Passwords don't match!")
            exit()
        flag, reason = check_pswd(password1)
        if flag == False:
            print (reason)
            exit()
    database.add_user(user.username, user.password)
    print("Successful complete!")
    exit()
print(database.data)
exit()