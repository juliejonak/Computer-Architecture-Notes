# Lecture II: Bitwise Operations

<br> a. [Additional Resources](#Additional-Resources)  
<br> b. [](#)
<br> c. [](#)
<br> d. [](#)
<br> e. [](#)
<br> f. [](#)
<br> g. [](#)
<br> h. [](#)
<br>  
<br>


## Additional Resources

[Bitwise Operations](https://www.youtube.com/watch?v=0PNyhnIEsXE)  

<br>


[Conversion Methods Between Bases](https://www.robotroom.com/NumberSystems.html)  

[Endianess](https://en.wikipedia.org/wiki/Endianness)  

<br>

## Convert Binary to Decimal

Let's practice converting a binary string to a decimal string with code, to fully understand how both base systems work.

> str = "1010"  

In decimal, this number is 10. How do we know this?

There are four places shown in this binary string. We'll code a representation.

<br>

```
str = "1010"

def to_decimal(num_string, base):
    # Turn the string into a list of individual characters
    digit_list = list(num_string)

    # Reverse the string to look at each character in the correct order
    digit_list.reverse()

    value = 0

    for i in range(len(digit_list)):
        print(f"{int(digit_list[i])} in the {base ** i}'s place' ")
        value += int(digit_list[i]) * (base ** i)

    print(f"The final number is {value}")
```

<br>

This prints out in the terminal:

<br>

```
0 in the 1's place' 
1 in the 2's place' 
0 in the 4's place' 
1 in the 8's place'
The final number is 10 
```

<br>

This shows us how many to count by each place holder in binary (the 2's, 4's, 8's, etc). Any time the binary conversion feels confusing about how to count, this can help clarify it.

<br>
<br>

## Logical Expressions

We represent logic using different code such as the `and` in Python or `&&` in JavaScript.

A logic table can represent the logic of a statement, like so:

<br>

```

A and B

A   B   A and B 
---------------
0   0      0
0   1      0
1   0      0
1   1      1

```

<br>

A and B are only true when A _and_ B are true.

We could code this like so:

<br>

```
for A in [False, True]:
    for B in [False, True]:
        print(f"{A} - {B} --> {A and B}")
```

<br>

Which prints to show:
  
> False - False --> False  
> False - True --> False  
> True - False --> False  
> True - True --> True  

This shows us the case in which A and B is true.

<br>

There is also `or` which checks if either A or B is True. How does that differ from `xor`?

`xor` stands for `exclusive or` -- exclusively, A _or_ B must be True.

What would the truth table for `or` v `xor` look like?

<br>

```

A   B   A or B 
---------------
0   0      0
0   1      1
1   0      1
1   1      1


A   B   A xor B 
---------------
0   0      0
0   1      1
1   0      1
1   1      0
```

<br>

This means it looks for exclusive _or_ true statements, not _and_. A OR B, but never A and B.

This differs from the traditional `or` statement because `or` would consider A and B as True because it only requires _at least_ one to be True (A can be true or B can be true or both can be).

`xor` only accepts when _only_ one (A OR B) is true, not both.

<br>







## Bitwise Operations

In Python, the ampersand `&` is different than using the logic of `and`.










