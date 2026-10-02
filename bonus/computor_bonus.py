import sys
from utils import parse_terms, get_fraction_str, format_reduced


def ft_sqrt(number):
    if number < 0:
        raise ValueError("Cannot calculate square root of a negative number.")
    if number == 0:
        return 0.0

    # On demarre a une valeur toujours >= sqrt(number) : la suite de Newton
    # est alors strictement decroissante, donc elle termine forcement.
    guess = float(number)
    if guess < 1.0:
        guess = 1.0

    while True:
        new_guess = 0.5 * (guess + (number / guess))
        # Plus aucun progres possible en flottant : on tient la racine.
        if new_guess >= guess:
            return guess
        guess = new_guess


def clean_zero(value):
    # Evite d'afficher "-0.0" quand le resultat vaut zero.
    if value == 0:
        return 0.0
    return value


def solve(polynomial, degree):
    a = polynomial.get(2, 0.0)
    b = polynomial.get(1, 0.0)
    c = polynomial.get(0, 0.0)
    # ax^2+bx+c

    # --- BONUS : AFFICHAGE DES ETAPES ---
    print("\n--- RESOLUTION STEPS ---")
    print(f"Coefficients: a={a}, b={b}, c={c}")
    # ------------------------------------

    # 4 * X^0 = 0 ou 2 * X^0 = 2 * X^0
    if degree == 0:
        print("Degree is 0. Checking if c == 0.")  # Step
        if c == 0:
            print("Any real number is a solution.")
        else:
            print("No solution.")

    # 2 * X^1 + 4 * X^0 = 0 -> X = -c / b
    elif degree == 1:
        print(f"Linear equation: {b}X = {-c}")  # Step

        res = clean_zero(-c / b)
        if b.is_integer() and c.is_integer():
            frac = get_fraction_str(-c, b)
            print(f"The solution is:\n{res} (or {frac})")
        else:
            print(f"The solution is:\n{res}")

    # 3 * X^2 + 2 * X^1 + 4 * X^0 = 0
    elif degree == 2:
        delta = (b * b) - (4 * a * c)

        # Step
        print(f"Calculating Delta: b^2 - 4ac = {b}^2 - 4 * {a} * {c}")
        print(f"Delta = {delta}")

        if delta > 0:
            print("Delta > 0 -> 2 real solutions.")  # Step
            print("Discriminant is strictly positive, the two solutions are:")
            sqrt_delta = ft_sqrt(delta)

            # (-b +- sqrt(delta)) / 2a
            sol1 = clean_zero((-b - sqrt_delta) / (2 * a))
            sol2 = clean_zero((-b + sqrt_delta) / (2 * a))

            print(f"{sol1}\n{sol2}")

            if sqrt_delta.is_integer() and a.is_integer() and b.is_integer():
                print("\n(Fraction form:)")
                print(get_fraction_str(-b - sqrt_delta, 2 * a))
                print(get_fraction_str(-b + sqrt_delta, 2 * a))

        elif delta == 0:
            print("Delta == 0 -> 1 unique solution.")  # Step
            print("Discriminant is zero, the solution is:")
            # -b / 2a
            sol = clean_zero(-b / (2 * a))

            if a.is_integer() and b.is_integer():
                frac = get_fraction_str(-b, 2 * a)
                print(f"{sol} (or {frac})")
            else:
                print(f"{sol}")

        else:  # delta < 0
            print("Delta < 0 -> 2 complex solutions.")  # Step
            print(
                "Discriminant is strictly negative, "
                "the two complex solutions are:"
            )
            sqrt_delta = ft_sqrt(-delta)
            reel = clean_zero(-b / (2 * a))
            imag = sqrt_delta / (2 * a)

            # "X + i * Y"
            print(f"{reel} - i * {abs(imag)}")
            print(f"{reel} + i * {abs(imag)}")

            if sqrt_delta.is_integer() and a.is_integer() and b.is_integer():
                print("\n(Fraction form:)")
                frac_reel = get_fraction_str(-b, 2 * a)
                # abs() sur le denominateur : la partie imaginaire est affichee
                # en valeur absolue, le signe est deja porte par le "+"/"-".
                frac_imag = get_fraction_str(sqrt_delta, abs(2 * a))
                print(f"{frac_reel} - i * {frac_imag}")
                print(f"{frac_reel} + i * {frac_imag}")

    print("------------------------\n")


def main():

    # ----------PARSING----------

    if len(sys.argv) != 2:
        print("Usage: python3 computor_bonus.py \"5 + 4 * X - 9.3 * X^2 = 1\"")
        return

    equation = sys.argv[1].replace(" ", "")

    if equation.count('=') != 1:
        print("Syntax Error: The equation must contain exactly one '=' sign.")
        return

    lhs_str, rhs_str = equation.split('=')

    if not lhs_str or not rhs_str:
        print("Syntax Error: One side of the equation is empty.")
        return

    try:
        lhs_terms = parse_terms(lhs_str)
        rhs_terms = parse_terms(rhs_str)
    except ValueError as e:
        print(f"Syntax Error: {e}")
        return

    # ----------REDUCTION----------

    # Dictionnaire { degre (int) : coef (float) }
    polynomial = {}

    def add_term(coef, exposant, signe_global=1):
        degree = int(exposant)
        valeur = float(coef) * signe_global

        if degree in polynomial:
            polynomial[degree] += valeur
        else:
            polynomial[degree] = valeur

    for coef, exposant in lhs_terms:
        add_term(coef, exposant, 1)

    for coef, exposant in rhs_terms:
        add_term(coef, exposant, -1)

    print(f"Reduced form: {format_reduced(polynomial)}")

    # ----------CALCUL DU DEGRE----------

    degree = 0
    for d in polynomial:
        if polynomial[d] != 0:
            if d > degree:
                degree = d

    print(f"Polynomial degree: {degree}")

    if degree > 2:
        print(
            "The polynomial degree is strictly greater than 2, "
            "I can't solve."
        )
        return

    try:
        solve(polynomial, degree)
    except OverflowError:
        print("Math Error: The numbers are too big to be calculated.")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
