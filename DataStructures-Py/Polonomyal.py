class Polynomial:

    __terms = []

    def __init__(self):
        self.__terms = []  

    def add_term(self, power, coefficient):
        
        if coefficient != 0:
            self.__terms.append([power, coefficient])

    def calculate(self, x):
        result = 0
        for term in self.__terms:
            power = term[0]
            coefficient = term[1]
            result += coefficient * (x ** power)
        polynomial_str = f"f({x}) = {result}"
        print(polynomial_str)
        return result
    def print_polynomial(self):
        
        polynomial_str = "f(x) = "
        terms_str = []
        for term in sorted(self.__terms, reverse=True):
            power = term[0]
            coefficient = term[1]
            if power == 0:
                terms_str.append(f"{coefficient}")
            elif power == 1:
                terms_str.append(f"{coefficient}x")
            else:
                terms_str.append(f"{coefficient}x^{power}")
        polynomial_str += " + ".join(terms_str)
        print(polynomial_str)

