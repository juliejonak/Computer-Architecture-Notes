# Lecture 1: Basics, Number Bases

<br> a. [Additional Resources](#Additional-Resources)  
<br> b. [Number Bases](#Number-Bases)  
<br> c. [](#)  
<br> d. [](#)  
<br> e. [](#)  
<br> f. [](#)  
<br> g. [](#)  
<br> h. [](#)  
<br>   
<br>




## Additional Resources

[CPU and Components](https://www.youtube.com/watch?v=Ae6zRhgMatc)  

[Number Bases and Conversions](https://www.youtube.com/watch?v=umwSs9fNegY)  

[Project Repo](https://github.com/LambdaSchool/Computer-Architecture)  

[Lecture I Recording: Brady Fukumoto]()  

<br>

[How to count binary on your hand](https://www.youtube.com/watch?v=Bke95oWWZII).  

[Binary Explained Simply](http://www.steves-internet-guide.com/binary-numbers-explained/)  

[Counting Systems Explained](https://ryanstutorials.net/binary-tutorial/)  

[Hexadecimal Basics](https://learn.sparkfun.com/tutorials/hexadecimal/all) 

<br> 

This week we'll be working on a [single project repo](https://github.com/LambdaSchool/Computer-Architecture). Tonight's project is working on `ls8` in the repository.

Focus on reading the ReadMe carefully and exploring documentation.

<br>

## Number Bases

`Binary`, `Hexadecimal` and `Decimal` are the three numbers bases we're most concerned with.

> Hexa = base 16  
> Dec = base 10  
> Bi = base 2  

But what does this mean?

If we have 12 apples, we might be looking for a way to _count_ the apples and express them to someone else.

Depending on which base you count with, the final number count may be different, even though the number of apples remains the same. We could also count in letters, returning letter `L` to represent 12. It's still 12 apples, but if we're counting in base _alphabet_, we'd say there are L apples.

It’s important to understand that when you have 12 apples on the table, it’s still the same number of apples regardless of whether or not you say there are “12 apples” (decimal), or “C apples” (hexadecimal), or “1100 apples” (binary).

The count of the number of items doesn’t change just because we refer to it in a numbering system of a different base.

In binary, everything is expressed in 1's and 0's (charge or no charge).

<br>

In base 10, we are used to expressing numbers based on 10s. For example, the number 123 is:

> 100 = 1 one hundreds
> 20 = 2 tens
> 3 = 3 1's

Think of it this way -- we use digits 1-9 to count up to a base of 10. When we reach a base of 10, we move over one digit.

> 09
> 10

We could also think of the tens place as 10^1 (ten to the power of one), and the hundreds place as 10^2 (ten to the power of two), etc.
<br> 

Binary is similar, except that our base is 2, so we only use the digits 0 and 1 as placeholders. Computers use binary because 0 or 1 indicates either passing a charge or not.

In binary, we write it like so:

> 0b00 = 0
> 0b01 = 1
> 0b10 = 2
> 0b11 = 3
> 0b100 = 4

Each digit place holds up to 1, so we count by increasing from 0 to 1 with each number. 00 to 01 to 10, much like we count in base 10 from 08 to 09 to 10.

The places are similar to base 10, in that the 1's place is 2^0, the 2's place is 2^1, the 4's place is 2^2, and the 8's place is 2^3.

<br>

Let's compare how we build the number 7352 in binary and decimal:

> 0b11100011
> 128 place, 64 place, 32 place, 16 place, 8 place, 4 place, 2 place, 1 place
> 128 + 64 + 32 + 0 + 0 + 0 + 2 + 1

> 7352
> 1000 place, 100 place, 10 place, 1 place
> 7000 + 300 + 50 + 2

Base 10 tells us that we have 7 1000's, 3 100's, etc..

Base 2 (Binary) tells us that we have 1 128, 1 64, 1 32, 0 16s, etc..

In Hexadecimal...

Hexadecimal is a base-16 number system. That means there are 16 possible digits used to represent numbers. 10 of the numerical values you're probably used to seeing in decimal numbers: 0, 1, 2, 3, 4, 5, 6, 7, 8, and 9.

Those values still represent the same value you're used to. The remaining six digits are represented by A, B, C, D, E, and F, which map out to values of 10, 11, 12, 13, 14, and 15.

Remember the places are 16^0, 16^1, 16^2, etc..

> 0xA32F
> 4096 place, 256 place, 16 place, 1 place
> 40960 + 768 + 32 + 15
> 41775

The larger the base, the more compact numbers can be. In hexadecimal, this number looks very small but is in fact quite large.

<br>

[How to count binary on your hand](https://www.youtube.com/watch?v=Bke95oWWZII).  

[Binary Explained Simply](http://www.steves-internet-guide.com/binary-numbers-explained/)  

[Counting Systems Explained](https://ryanstutorials.net/binary-tutorial/)  

[Hexadecimal Basics](https://learn.sparkfun.com/tutorials/hexadecimal/all)  

<br>









