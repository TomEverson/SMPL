# SMPL (SiMple Programming Language)

![SMPL Logo](./logo.png)

SMPL (SiMple Programming Language) is a minimalistic programming language created as a final class project. It is not intended for practical use but rather serves as an educational tool to explore basic language design and implementation concepts.

## Features

- **Simplicity**: The language is designed to be as simple as possible to focus on basic programming language constructs.
- **Syntax**: Easy-to-understand syntax for learning purposes.
- **Modes**:
  - **Interpreted**: Executes code directly without needing to convert it to another form.
  - **Transpiled**: Transforms the code into another high-level language, allowing for cross-platform compatibility.
  - **Compiled**: Converts the code into machine code for direct execution, offering performance benefits.
- **No Dependencies**: SMPL has no external dependencies, making it easy to run on any system without requiring additional libraries or setups.
- **Short Codebase**: The entire implementation of SMPL is only 205 lines of code, making it compact and easy to understand.

## Support

- **Variables**
  - Strings
  - Number
  - Boolean
  - Multi-Line Strings
- **Condition**
- **I/O Operation**
- **Funtions**
- **Loops ( Recursion )**

## Modes

- **Interpreted**: The language can be run directly through Python interpreter.
- **Transpiled**: The language code can be converted into Python for further use.
- **Compiled**: The code can be compiled into an executable Python File ( Requires PyInstaller )

## Installation

To use SMPL, clone this repository and follow the steps below to run the language interpreter.
Make sure you have Python 3.x installed on your machine.

```bash
git clone https://github.com/yourusername/smpl.git
cd smpl
python main.py rps.smpl --interpretor
```

Or, you could also create your own smpl file, and run

```bash
touch main.smpl
python main.py main.smpl --interpretor
```

For transpiled mode

```bash
touch main.smpl
python main.py main.smpl --transpiler
```

Or, you could compile ( Need PyInstaller )

```bash
touch main.smpl
python main.py main.smpl --compiler
```

## Learn SMPL

### Variable Declaring

In SMPL, variables are declared using the `LET` keyword. You can declare variables to store different types of data such as strings, numbers, booleans, and multi-line strings.

#### Syntax:

```smpl
LET <variable_name> BE <value>
```

#### Example:

```smpl
LET PLAYER_NAME BE "John"

LET PLAYER_AGE BE 25

LET IS_PLAYER_READY BE TRUE

LET WELCOME_MESSAGE BE """
Welcome to the game!
Enjoy playing Rock-Paper-Scissors.
"""
```

### User Input

In SMPL, you can get input from the user using the `INPUT` command. This allows you to prompt the user for a value, which can then be stored in a variable. You can specify the type of input expected, such as a string or an integer.

#### Syntax:

```smpl
LET <variable_name> BE <input_type> INPUT WITH "<prompt>"
```

#### Example:

```bash
LET USER_NAME BE STRING INPUT WITH "Enter your name: "

LET PLAYER_DECISION BE INTEGER INPUT WITH "1.ROCK, 2.PAPER, 3.SCISSORS"
```

### Output

In SMPL, you can display information to the user using the `OUTPUT` command. This is useful for printing text, results, or any other information you want the user to see.

#### Syntax:

```smpl
OUTPUT <message>
```

#### Example

```smpl
OUTPUT "Welcome to the game!"
OUTPUT "You have chosen: " + PLAYER_DECISION
```

### Control Flow

In SMPL, you can control the flow of execution using conditional statements (`IF`, `ELSE IF`, `ELSE`) and loops (`WHILE`). This allows you to create more dynamic and interactive programs.

#### Conditional Statements

Conditional statements are used to make decisions in your program. The `IF` statement evaluates a condition, and based on whether it’s true or false, different blocks of code are executed.

#### Syntax:

```smpl
IF <condition>
    <code_to_execute_if_true>
ELSE IF <condition>
    <code_to_execute_if_true>
ELSE
    <code_to_execute_if_false>
```

#### Example:

```smpl
IF PLAYER_DECISION IS EQUAL TO 1
    OUTPUT "You chose Rock!"
ELSE IF PLAYER_DECISION IS EQUAL TO 2
    OUTPUT "You chose Paper!"
ELSE
    OUTPUT "You chose Scissors!"
```

### Comparison Operators

In SMPL, comparison operators are used to compare values and determine the flow of execution in control statements like `IF`, `ELSE IF`, and `WHILE`. These operators evaluate conditions and return `TRUE` or `FALSE`.

#### List of Comparison Operators:

- **IS EQUAL TO**: Checks if two values are equal.

  - Syntax: `value1 IS EQUAL TO value2`
  - Example: `IF PLAYER_DECISION IS EQUAL TO 1`

- **IS NOT EQUAL TO**: Checks if two values are not equal.

  - Syntax: `value1 IS NOT EQUAL TO value2`
  - Example: `IF PLAYER_DECISION IS NOT EQUAL TO 2`

- **IS GREATER THAN**: Checks if the first value is greater than the second.

  - Syntax: `value1 IS GREATER THAN value2`
  - Example: `IF COUNT IS GREATER THAN 3`

- **IS LESS THAN**: Checks if the first value is less than the second.
  - Syntax: `value1 IS LESS THAN value2`
  - Example: `IF COUNT IS LESS THAN 5`

#### Example:

```smpl
LET PLAYER_DECISION BE 2
IF PLAYER_DECISION IS EQUAL TO 1
    OUTPUT "You chose Rock!"
ELSE IF PLAYER_DECISION IS EQUAL TO 2
    OUTPUT "You chose Paper!"
ELSE
    OUTPUT "You chose Scissors!"
```

### Functions

In SMPL, functions allow you to group a block of code that can be executed multiple times, making your code more modular and reusable. Functions in SMPL can take parameters and return values.

#### Syntax:

```smpl
FUNCTION <function_name>(<parameter1>, <parameter2>, ...)
    <code_to_execute>
```

#### Example:

```smpl
FUNCTION GREET(PLAYER_NAME)
    OUTPUT "Hello, " + PLAYER_NAME + "!"

GREET("John")
```

### USE

In SMPL, the `USE` keyword allows a function to access and modify global variables. Without `USE`, a function can only work with local variables (those defined inside the function). The `USE` keyword enables a function to "mutate" or update the value of global variables, making it possible to affect the program's state outside of the function.

#### Syntax:

```smpl
FUNCTION <function_name>(<parameter1>, <parameter2>, ...)
    USE <global_variable>
    <code_to_execute>
```

#### Example

```smpl
LET PLAYER_SCORE BE 0

FUNCTION INCREMENT_SCORE(POINTS)
    USE PLAYER_SCORE
    LET PLAYER_SCORE BE PLAYER_SCORE + POINTS

INCREMENT_SCORE(10)
OUTPUT PLAYER_SCORE
```

### RANDOM

In SMPL, the `RANDOM` keyword allows you to generate random values, which can be useful for tasks such as selecting random numbers, making decisions, or simulating randomness in games.

#### Syntax:

```smpl
LET <variable_name> BE RANDOM INTEGER BETWEEN <min_value> AND <max_value>
```

#### Example

```smpl
LET CPU_DECISION BE RANDOM INTEGER BETWEEN 1 AND 3
```
