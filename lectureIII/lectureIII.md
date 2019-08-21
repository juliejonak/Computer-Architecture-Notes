# Lecture III: The System Stack

<br> a. [Additional Resources](#Additional-Resources)   
<br> b. [](#)  
<br> c. [](#)   
<br> d. [](#)   
<br> e. [](#)   
<br> f. [](#)   
<br> g. [](#)   
<br> h. [](#)   
<br> i. [](#)   
<br>
<br>


## Additional Resources

[The CPU Stack](https://youtu.be/vAy5rXxUwoc)  

[CPU Interrupts](https://youtu.be/w3gDDg_kORk)  

[CS19 Lecture III: The System Stack Recording: Brady Fukumoto](https://www.youtube.com/watch?v=nCghJadoRYU&feature=youtu.be)

<br>

[Memory Layout of C Programs](https://www.geeksforgeeks.org/memory-layout-of-c-program/)  

[Explain a Call Stack in a Nutshell](https://stackoverflow.com/questions/10057443/explain-the-concept-of-a-stack-frame-in-a-nutshell)  


<br>

## Stacks

_Starts at 18:30 on the recording_

What is a stack?

A structure that holds a collection of items in a FILO structure: first in, last out (unlike a queue). Think of it like a stack of pancakes. The newest ones are eaten first.

It uses push and pop to add and remove items from the stack.

Within the LS8 project, our memory is not a complex data structure - it's simply a 128 long list. We can treat it like a stack by using it as a list with `push()` and `pop()`. An advantage of a stack over a queue is that we don't need to bitshift to add or remove items from the stack.














