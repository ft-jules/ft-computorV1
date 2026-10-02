import re


# Un terme = un signe optionnel, puis :
#   - soit un nombre suivi d'un X optionnel  (5, 5*X, 4X, 9.3*X^2)
#   - soit un X seul                         (X, X^2)
# Rien d'autre n'est accepte : tout caractere hors de ce motif est une erreur.
TERM_PATTERN = re.compile(
    r"(?P<sign>[-+]?)"
    r"(?:"
    r"(?P<coef>\d+(?:\.\d+)?|\.\d+)(?:\*?(?P<xa>X)(?:\^(?P<expa>\d+))?)?"
    r"|"
    r"(?P<xb>X)(?:\^(?P<expb>\d+))?"
    r")",
    re.IGNORECASE,
)


def ft_gcd(a, b):  # plus grand diviseur commun

    while b:
        a, b = b, a % b
    return a


def format_coef(value):
    # 4.0 -> "4", mais 9.3 reste "9.3"
    if value == int(value):
        return str(int(value))
    return str(value)


def get_fraction_str(numerator, denominator):

    if not (numerator.is_integer() and denominator.is_integer()):
        return str(numerator / denominator)

    num = int(numerator)
    denom = int(denominator)

    if denom == 0:
        return "Undefined"

    if denom < 0:
        num = -num
        denom = -denom

    common = ft_gcd(abs(num), abs(denom))

    reduced_num = num // common
    reduced_denom = denom // common

    if reduced_denom == 1:
        return str(reduced_num)

    return f"{reduced_num}/{reduced_denom}"


def format_reduced(polynomial):
    # Forme reduite : on saute les coefficients nuls, ils n'apportent rien.
    parts = []

    for degree in sorted(polynomial):
        coef = polynomial[degree]
        if coef == 0:
            continue

        if not parts:
            sign = "-" if coef < 0 else ""
        else:
            sign = " - " if coef < 0 else " + "

        parts.append(f"{sign}{format_coef(abs(coef))} * X^{degree}")

    if not parts:
        return "0 = 0"

    return "".join(parts) + " = 0"


def parse_terms(expression):

    expression = expression.replace(" ", "")

    if not expression:
        raise ValueError("empty side of the equation.")

    terms = []
    position = 0

    while position < len(expression):
        match = TERM_PATTERN.match(expression, position)

        if match is None:
            # Le signe est valide, c'est ce qui suit qui ne l'est pas :
            # on pointe le vrai caractere fautif.
            faute = position
            if expression[faute] in "+-":
                faute += 1
            if faute >= len(expression):
                raise ValueError(
                    f"dangling '{expression[position]}' "
                    "at the end of the expression."
                )
            raise ValueError(
                f"unexpected character '{expression[faute]}' "
                f"at position {faute + 1}."
            )

        # Deux termes colles sans operateur ("X^2X") : c'est une faute.
        if position > 0 and not match.group("sign"):
            raise ValueError(f"missing '+' or '-' at position {position + 1}.")

        # ----------LOGIQUE DE DEDUCTION----------

        coef_str = match.group("coef")
        coef = 1.0 if coef_str is None else float(coef_str)

        if match.group("sign") == "-":
            coef = -coef

        if match.group("xa") or match.group("xb"):
            exposant = match.group("expa") or match.group("expb")
            degree = 1 if exposant is None else int(exposant)
        else:
            degree = 0

        terms.append((coef, degree))
        position = match.end()

    return terms
