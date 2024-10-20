## Movie Rental Refactoring

A classic refactoring problem from Chapter 1 of
_Refactoring: Improving the Design of Existing Code_ by Martin Fowler.  

This repository contains Python code translated from the Java version.

The runnable `main.py` creates a customer and prints a statement.


## Instructions

See [Movie Rental Refactoring, Part 1](https://cpske.github.io/ISP/assignment/movierental/movierental-part1) for description of the code and what to do.

Before and after each refactoring you should **run the unit tests**.

## Resources

See [Resources](https://cpske.github.io/ISP/assignment/movierental/movierental-part1#resources) in the assignment description.

## Rationale
**2.1** what refactoring signs (code smells) suggest this refactoring?

*Ans:* Data Class, because Rental only call Movie to get its price code.

**2.2** what design principle suggests this refactoring? Why?, because Rental only call Movie to get its price code.

*Ans:* Single Responsibility Principle, the Rental class is responsible for rental details and that should include pricing. The Movie class is responsible for keeping the information of movies, and movies don't set their own price.

**5.2** Location of `get_price_for_movie` and the reasons.

*Ans:* I put `get_price_for_movie` in the Rental class as a class method, because the Rental class is responsible for rental details, so the method to find price code should belong to this class according to Single Responsibility Principle.
Doing this also make the code has low coupling and high cohesion because only the Rental class uses the price codes. 