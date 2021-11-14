'''
Клас SignedInt є моделлю для опису позитивних і від'ємних цілих чисел.
Кожен об'єкт класу описує одне ціле число за такою схемою:
- атрибут modulus містить int, який представляє абсолютне значення (модуль) числа
- атрибут sign містить рядок '-' або '+', який представляє знак числа.
Тож число -3 може бути описане об'єктом SignedInt(3, '-'),
а число 5 буде описане об'єктом SignedInt(5, '+')
Класс Matrix представляє собою список об'єктів SignedInt. Розмір списку задається
при створенні об'єкта класу Matrix, об'єкти SignedInt, які входять у цей список,
генеруються автоматично і додаються до атрибуту elements об'єкту Matrix.
Завдання:
- реалізувати обмеження на встановлення атрибуту sign. Можливі значення - рядок '-' або '+', інакше - ValueError
- реалізувати обмеження на встановлення атрибуту modulus. Можливі значення - цілі числа, інакше - ValueError
- реалізувати людино-читаємий вивід у звичному форматі представлення чисел зі знаком,
    так щоб str(SignedInt(7, '-')) повертало рядок '-7', а str(SignedInt(4, '+')) повертало рядок '4'
- реалізувати методи потрівняння об'єктів класу SignedInt за звичайною логікою, тобто
    SignedInt(5, '-') < SignedInt(1, '+')
    SignedInt(3, '+') > SignedInt(10, '-')
    SignedInt(2, '+') == SignedInt(2, '+')
    SignedInt(3, '+') <= SignedInt(5, '+')
    SignedInt(7, '-') >= SignedInt(8, '-')
- релізувати протокол ітератора для об'єкту класу Matrix, який дозволить ітерувати його атрибут elements.
Кожен реалізований метод має мати щонайменше один тест. Якщо у методі є розгалуження -
мають бути протестовані усі гілки.
'''

class SignedInt:

    def __init__(self, modulus, sign):
        self.modulus = modulus
        self.sign = sign

    def __str__(self):
        if self.sign == '-':
            return f'{self.sign}{self.modulus}'
        else:
            return str(self.modulus)

    @property
    def sign(self):
        return self._sign

    @sign.setter
    def sign(self, sign):
        if sign == '-' or sign == '+':
            self._sign = sign
        else:
            raise ValueError

    @property
    def modulus(self):
        return self._modulus

    @modulus.setter
    def modulus(self, modulus):
        if type(modulus) is int:
            self._modulus = modulus
        else:
            raise ValueError

    def change_modulus(self):
        if self.sign == '-':
            return self.modulus * -1
        else:
            return self.modulus


    def __eq__(self, other):
        return self.change_modulus() == other.change_modulus()

    def __lt__(self, other):
        return self.change_modulus() < other.change_modulus()

    def __le__(self, other):
        return self.change_modulus() <= other.change_modulus()

    def __gt__(self, other):
        return self.change_modulus() > other.change_modulus()

    def __ge__(self, other):
        return self.change_modulus() >= other.change_modulus()




class Matrix:

    elements = []

    def __init__(self, size):
        for index in range(size):
            modulus = pow(index, index)
            if index % 2:
                sign = '-'
            else:
                sign = '+'
            self.elements.append(SignedInt(modulus, sign))

    def __iter__(self):
        self.index_elments = 0
        return self

    def __next__(self):
        if self.index_elments < len(self.elements):
            _index = self.index_elments
            self.index_elments += 1
            return self.elements[_index]
        else:
            raise StopIteration


if __name__ == '__main__':
    signed_int = SignedInt(3, '-')
    signed_int1 = SignedInt(3, '+')
    signed_int2 = SignedInt(3, '+')

    matrix = Matrix(3)
    a = iter(matrix)


