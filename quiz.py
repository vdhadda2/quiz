"""
-----------------------------------------------------------------------
Question 1.

Given two int values, return True if one is negative and one is
positive. Except if the parameter "negative" is True, then return True
only if both are negative.
-----------------------------------------------------------------------

"""


def pos_neg(a, b, negative):
    pass
public boolean posNeg(int a, int b,boolean negative) {
    if (negative && a < 0 && b < 0) {
    return true;
    }
    else if (!negative && ((a < 0 && b > 0) || (a > 0 && b < 0))) {
    return true;
    }
    return false;
    }

# Expected outputs:

print(pos_neg(1, -1, False))
# True
print(pos_neg(-1, 1, False))
# True
print(pos_neg(-4, -5, True))
# True
print(pos_neg(-2, -5, False))
# False
print(pos_neg(1, 2, False))
# False


"""
-----------------------------------------------------------------------
Question 2.

A year with 366 days is called a leap year. Leap years are necessary to
keep the calendar synchronized with the sun because the earth revolves
around the sun once every 365.25 days. Actually, that figure is not
entirely precise, and for all dates after 1582 the Gregorian correction
applies. Usually years that are divisible by 4 are leap years, for
example 1996. However, years that are divisible by 100 (for example,
1900) are not leap years, but years that are divisible by 400 are leap
years (for example, 2000).
-----------------------------------------------------------------------

"""
welcome the user
        prompt for input of INPUT_YEAR type = int
        store the input in constants INPUT_YEAR

        if INPUT_YEAR < 1582
            out put "i can not count that far back. I Can only evaluate years after 1582."
        else if ((INPUT_YEAR % 4 == 0 && INPUT_YEAR % 100 > 0) OR (INPUT_YEAR % 400 == 0))
            out put "INPUT_YEAR is a leap year"
        else
            out put "INPUT_YEAR is a leap year


def leap_year(year):
    pass


# When you've completed your function, uncomment the
# following lines and run this file to test!

# print(leap_year(1900))
# print(leap_year(2016))
# print(leap_year(2017))
# print(leap_year(2000))




"""
-----------------------------------------------------------------------
Question 3:

Write a function with loops that computes the sum of all squares between
1 and n (inclusive).
-----------------------------------------------------------------------

"""
public class
{
public static void main(String []args ) {
    Scanner reader = new Scanner(System.in);
    int n = 1;
    int sum = 0;
    while (n <= 100) {
        n = (n*n);
        n++;

    sum = (sum + n);
    }
    System.out.println(sum);
}
}


def sum_squares(n):
    pass

# When you've completed your function, uncomment the
# following lines and run this file to test!

# print(sum_squares(1))
# print(sum_squares(100))
