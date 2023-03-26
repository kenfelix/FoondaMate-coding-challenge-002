import re
from fractions import Fraction


def solve_linear_equation(equation: str) -> dict:

    equation = equation.replace(" ", "")  # remove all whitespace

    # detect equation to solve

    normal = is_normal(equation)

    if normal:
        return solveNormal(equation)

    return solveAdvance(equation)

def is_normal(equation: str) -> bool:

    # compile the regular expressions with IGNORECASE flag
    regex1 = re.compile(r"(^[+-]?\d*)[a-zA-Z]([+-]\d*)=([+-]?\d*)$", re.IGNORECASE)
    regex2 = re.compile(
        r"(^[+-]?\d*)(\([+-]?\d*[a-zA-Z][+-]\d*\))([+-]\d*)=([+-]?\d*)([+-]\d*)[a-zA-Z]$",
        re.IGNORECASE,
    )

    # check if regex1 matches and return True if it does
    if regex1.search(equation):
        return True

    # check if regex2 matches and return False if it does
    if regex2.search(equation):
        return False

    # if neither regex1 nor regex2 matches, raise an error
    raise ValueError("Invalid equation.")

def solveNormal(equation: str) -> dict:
    result: dict = {}

    matches = re.search(r"(^[+-]?\d*)([a-zA-Z])([+-]?\d*)=([+-]?\d*)$", equation)
    x = matches.group(2)
    a_str = matches.group(1)
    b_str = matches.group(3)
    c_str = matches.group(4)

    # convert a, b and c terms to floats
    if a_str == "":
        a = 1.0
    elif a_str == "-":
        a = -1.0
    else:
        a = float(a_str)

    b = float(b_str)
    c = float(c_str)

    # solve for x
    if b < 0:
        x_value = (c + abs(b)) / a
        result.update(
            {
                f"Add {int(abs(b))} to both sides": [
                    equation,
                    f"{equation.split('=')[0]}+{int(abs(b))}={equation.split('=')[1]}+{int(abs(b))}",
                ]
            }
        )
        result.update(
            {"Simplify the expression": f"{int(a)}{x}={int(c) + int(abs(b))}"}
        )
    else:
        x_value = (c - abs(b)) / a
        result.update(
            {
                f"Subtract {int(abs(b))} from both sides": [
                    equation,
                    f"{equation.split('=')[0]}-{int(abs(b))}={equation.split('=')[1]}-{int(abs(b))}",
                ]
            }
        )
        result.update(
            {"Simplify the expression": f"{int(a)}{x}={int(c) + int(abs(b))}"}
        )

    x_value = Fraction(x_value).limit_denominator(int(a))
    result.update(
        {
            "common": {
                "left_side": f"{int(a)}{x}",
                "right_side": f"{int(c) + int(abs(b))}",
                "denominator": int(a),
            }
        }
    )
    result.update({"Solution": f"{x}={x_value}"})

    return result


def solveAdvance(equation: str) -> dict:
    result: dict = {}
    matches = re.search(
        r"(^[+-]?\d*)(\([+-]?\d*[a-zA-Z][+-]\d*\))([+-]\d*)=([+-]?\d*)([+-]\d*)([a-zA-Z])$",
        equation,
    )
    x = matches.group(6)
    mul_str = matches.group(1)
    enclosed = re.search(r"([+-]?\d*)([a-zA-Z])([+-]\d*)", matches.group(2))
    a1_str = enclosed.group(1)
    b1_str = enclosed.group(3)
    b2_str = matches.group(3)
    c_str = matches.group(4)
    a2_str = matches.group(5)

    if a1_str == "":
        a1 = 1.0
    elif a1_str == "-":
        a1 = -1.0
    else:
        a1 = float(a1_str)

    if a2_str == "":
        a2 = 1.0
    elif a2_str == "-":
        a2 = -1.0
    else:
        a2 = float(a2_str)

    b1 = float(b1_str)
    b2 = float(b2_str)
    mul = float(mul_str)
    c = float(c_str)

    # solve for answer # 2(4x + 3) + 6 = 24 -4x
    result.update(
        {
            "Simplify the expression": {
                "Distribute": [
                    equation,
                    f"{int(mul * a1)}{x}{int(mul * b1):+}+{int(b2)}={int(c)}{int(a2):+}{x}",
                ],
                "Add the numbers": [
                    f"{int(mul * a1)}{x}{int(mul * b1):+}{int(b2):+}={int(c)}{int(a2):+}{x}",
                    f"{int(mul * a1)}{x}{(int(mul * b1)+int(b2)):+}={int(c)}{int(a2):+}{x}",
                ],
                "Rearrange items": [
                    f"{int(mul * a1)}{x}{(int(mul * b1)+int(b2)):+}={int(c)}{int(a2):+}{x}",
                    f"{int(mul * a1)}{x}{(int(mul * b1)+int(b2)):+}={int(a2)}{x}{int(c):+}",
                ],
            }
        }
    )
    a = (a1 * mul) - a2
    b = (b1 * mul) + b2

    new_c = 0
    if b < 0:
        result.update(
            {
                f"Add {int(abs(b))} to both sides": [f"{int(mul * a1)}{x}{(int(mul * b1)+int(b2)):+}={int(a2)}{x}{+int(c)}",
                                                     f"{int(mul * a1)}{x}{(int(mul * b1)+int(b2)):+}+{int(abs(b))}={int(a2)}{x}{int(c):+}+{int(abs(b))}",
                                                     f"{int(mul * a1)}{x}={int(a2)}{x}{int(c+abs(b)):+}"]                                                     
            }
        )
        new_c = int(c+abs(b))
        x_value = (c + abs(b)) / a
    else:
        result.update(
            {
                f"Subtract {int(abs(b))} from both sides": [f"{int(mul * a1)}{x}{(int(mul * b1)+int(b2)):+}={int(a2)}{x}{int(c):+}",
                                                            f"{int(mul * a1)}{x}{(int(mul * b1)+int(b2)):+}-{int(abs(b))}={int(a2)}{x}{int(c):+}-{int(abs(b))}",
                                                            f"{int(mul * a1)}{x}={int(a2)}{x}{int(c-abs(b)):+}"
                                                            ]
            }
        )
        new_c = int(c-abs(b))
        x_value = (c - abs(b)) / a

    if a2 < 0:
        result.update(
            {
                f"Add {int(abs(a2))}{x} to both sides": [
                    f"{int(mul * a1)}{x}+{int(abs(a2))}{x}={int(a2)}{x}+{int(abs(a2))}{x}{new_c:+}",
                    f"{int(mul * a1)+int(abs(a2))}{x}={new_c}"
                ]
            }
        )
    else:
        result.update(
            {
                f"Subtarct {int(abs(a2))}{x} from both sides": [
                    f"{int(mul * a1)}{x}-{int(abs(a2))}{x}={int(a2)}{x}-{int(abs(a2))}{x}{new_c:+}",
                    f"{int(mul * a1)-int(abs(a2))}{x}={new_c}"
                ]
            }
        )
    x_value = Fraction(x_value).limit_denominator(int(a))
    result.update(
        {
            "common": {
                "left_side": f"{int(a)}{x}",
                "right_side": f"{new_c}",
                "denominator": int(a),
            }
        }
    )
    result.update({"Solution": f"{x}={x_value}"})
    return result
