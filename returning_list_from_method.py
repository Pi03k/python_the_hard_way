#!/usr/bin/env python3
# escaping characters. single and double quotes. returning multiple values as
# list.


def main():
    print("Let's practice evertyhing.")
    print('You\'d need to know \'bout escapes with \\ that do:')

    poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \nthe needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
    """

    print("----------")
    print(poem)
    print("----------")

    five = 10 - 2 + 3 - 6
    print(f"This should be five: {five}")

    startPoint = 10000
    beans, jars, crates = secretFormula(startPoint)
    print("With a starting point of {}".format(startPoint))
    print(f"We'd have {beans} beans, {jars} jars and {crates} crates.")

    startPoint /= 10
    print("We can also do this way:")
    formula = secretFormula(startPoint)
    print("We'd have {} beans, {} jars and {} crates.".format(*formula))


def secretFormula(started):
    jellyBeans = started * 500
    jars = jellyBeans / 10000
    crates = jars / 100
    return jellyBeans, jars, crates


if __name__ == "__main__":
    main()
