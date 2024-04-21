# To write gcd(a,b) as a linear combination of a and b using integer combination i.e au + bv = gcd(a,b)=1

"""

let a = 73, b = 25, To find the GCD
73 = 25(2) + 23
25 = 23(1) + 2
23 = 2(11) + 1

Rearranging above eqns,
73 + 25(-2) = 23
25 + 23(-1) = 2
23 + 2(-11) = 1

The quotients can be obtained by -(a//b). Let the above quotients be q0,q1,q2. Then the eqns become,

73 + 25q0 = 23 --(iii)
25 + 23q1 = 2 --(ii)
23 + 2q2  = 1 --(i)

Writing L.H.S of (i) form in following form



x(23) + y(2), [x=1,y=q2] --- General form


substituting 2 from (ii),
x(23) + y(25 + 23q1)

Rearranging..

y(25) + (x+q1.y)23, -- (nxt)

Comparing nxt with general form as well as with (ii)
We get,
{
t= x (previous x)
x = y,
y = t+y.q2 [q2 is the previous quotient].
} can be applied until we run out of quotient to get x,y. Then..

73x + 25y = gcd(73,25)



Need to expand on it.




"""


def extendedEuclideanAlgorithm(a, b):
    if b > a:
        a, b = b, a

    quotient = []
    remainder = a % b
    while remainder != 0:
        quotient.append(-(a // b))
        a = b
        b = remainder
        remainder = a % b

    if len(quotient) == 0:
        x = 0
        y = 1
        return x, y
    else:
        x = 1
        y = quotient[len(quotient) - 1]
        i = len(quotient) - 2
        while i >= 0:
            t = x
            x = y
            y = t + y * quotient[i]
            i = i - 1

        return x, y, b


def main():
    print(extendedEuclideanAlgorithm(73, 25))


if __name__ == "__main__":
    main()
