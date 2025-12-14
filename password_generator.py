import string
import secrets

def contains_upper(password:str)->bool:
    for char in password:
        if char.upper():
            return True
        
    return False

def contains_punctuation(password:str)->bool:
    for char in password:
        if char in string.punctuation:
            return True
        
    return False

def generator_password(length:int, symbols:bool, uppercase:bool)-> str:
    combination: str = string.ascii_lowercase + string.digits

    if symbols:
        combination += string.punctuation

    if uppercase:
        combination += string.ascii_uppercase

    combination_length= len(combination)
    print(combination)
    new_password:str = ''

    for _ in range(length):
        new_password += combination[secrets.randbelow(combination_length)] 

    return new_password



if __name__ == '__main__':

    for i in range(1,6):
        new_pass:str  = generator_password(length=10, symbols=False, uppercase=True)
        specs: str = f'U: {contains_upper(new_pass)}, P: {contains_punctuation(new_pass)}'
        print(f'{i} --> {new_pass}({specs}) ')


# print(string.punctuation, string.ascii_uppercase, string.digits)

