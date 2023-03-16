"""
problem E:

The Golden Valley Clothing Warehouse has a lot of winter stock it wants to sell off quickly to
make room for spring and summer clothing that is coming in soon. The manager came up with
quite a complicated sale policy, which you now have the job of implementing.
Here are the rules the manager put in place:
Items are given a circular sticker with a colour – they are called “dots”, hence red dot, yellow dot
etc. Each dot represents a particular percentage discount as listed here.

Colour Dot      Discount %
Red                45
Green              30
Blue               20
Yellow             15
Orange             10
White              5

In addition, the manager has given out discount coupons! Any customer who presents one of
these receives an extra 5% discount after the “dot” discounts have been calculated.
You have to work out the discounted price for each item presented. As your program has to run
on the point of sale terminal, you must round the price to the nearest cent (0.5 is rounded up).
If a customer is paying cash, you must then round the price up or down to the nearest 10 cents.
If the right most digit of the cents is from 0 to 5 inclusive, it is rounded down to 0, otherwise the
cents are rounded up to the next 10.

Input:

The first line of input will be a single positive integer, N, which is the number of purchases to
process (0 < N <= 100). There will then follow N lines, each representing a single purchase.
Each line will have the following format, items being separated by spaces.
<original price> <dot> <coupon> <payment>
<original price> The price of the item before any discount. A decimal number with 2 places
of decimals.
New Zealand Programming Contest 2015
<dot> The dot colour, using a single upper case letter, the first letter of the
colour.
<coupon> C if the customer presented a discount coupon, X if not.
<payment> C if the customer paid cash, P (for plastic) if they did not.

Output:

For each purchase in the input, output a single line which is the discounted price. It must be in
the format
$d.cc
i.e. a dollar sign, the dollar amount, a decimal point and the cents with 2 digits. If the dollar
amount is 0, then the zero must be displayed.
"""