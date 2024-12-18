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
   
    def __str__(self):
        polynomial_str = "f(x) = "
        terms_str = []
        for term in sorted(self.__terms):
            power = term[0]
            coefficient = term[1]
            if power == 0:
                terms_str.append(f"{coefficient}")
            elif power == 1:
                terms_str.append(f"{coefficient}x")
            else:
                terms_str.append(f"{coefficient}x^{power}")
        polynomial_str += " + ".join(terms_str)
        return polynomial_str
    
X = Polynomial()

X.add_term(0,1)
X.add_term(1,2)
X.add_term(2,3)
X.add_term(3,4)
print(X)
X.calculate(2)