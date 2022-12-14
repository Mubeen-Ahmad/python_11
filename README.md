<details>
<summary> <h2>What is Python? What are the benefits of using Python ?</h2></summary>
  
- ## Python is a high-level, interpreted, general-purpose programming language. 
  - #### Being a general-purpose language, it can be used to build almost any type of application with the right tools/libraries.
  
  - #### Additionally, python supports objects, modules, threads, exception-handling, and automatic memory management which help in modelling real-world problems and building applications to solve these problems.

- ## Benefits of using Python

  - #### Python is a general-purpose programming language that has a simple, easy-to-learn syntax that emphasizes readability and therefore reduces the cost of program maintenance. Moreover, the language is capable of scripting, is completely open-source, and supports third-party packages encouraging modularity and code reuse.
  
  - #### Its high-level data structures, combined with dynamic typing and dynamic binding, attract a huge community of developers for Rapid Application Development and deployment.

</details>

 <details>
<summary> <h2>Type Checking </h2></summary>
  
  - ### There are two Types of Checking.
    - #### Type checking is the process of verifying and enforcing constraints of types in values. 
    - #### Type checking means checking that each opeartion should receive proper no of arguments and proper data type.<br> like `12 + '1'`
    - #### Here `12` int data type and `'1'` is the character data type So It's Possible to sum of integer and Character<br> So They Decide that they generate the Error or Not

</details>

<details>
<summary> <h2>What is a strongly and weakly typed Checking Languages ?</h2></summary>
  
- ### A strongly typed programming language is always pending of their variable data type.
  - #### This is because the system checks the object type before an operation requiring a certain type is called on such variable giving either a compilation error or runtime error.
  
  - #### In a strongly-typed language, such as Python, `"1" + 2` will result in a type error since these languages don't allow for "type-coercion" (implicit conversion of data types).
---  
- ### Weakly typed languages are those where type confusion can happen and eventually produce errors that are difficult to find and detect, which differ them from strongly type languages where these kinds of errors are caught either in compilation time or runtime.  
  - #### Weakly-typed language, such as Javascript, will simply output `"1" + 2 = 12` as result.
  

</details>

<details>
<summary> <h2>Stages of Checking Languages </h2></summary>
  
- ### There are Two Stages of Checking
  - #### Static
  - #### Dynamic 
  
- #### In Static Type Languages Data Types are checked before execution.<br>Example of c language
  ```
  #include <stdio.h>
  void main(){
      int x;
      x = 3;
      printf("%d",x);
    }
  ```
  
  - #### In statically typed languages the type of the variables checked at the compile time of the variable declaration.<br>Statically programming languages check the type of the variable or object while the code enters the compiler.
  - #### In Static typed languages once if a variable is initialized to a data-type it cannot be assigned to the variable of a different type.
  - #### Statically typed languages are faster than dynamically typed languages.
  - #### Some statically typed languages are Java ,C , C++. Etc
  
---
  
- #### A language is considered as Dynamically typed language if the variable type of the language is checked at the runtime of the code compilation or code interpretation.
  - #### In such type of programming languages, we don???t need to initialize a variable with its type
  - #### We can declare a variable by writing the name at left and the value at the left of the variable name<br>Example of python
  ```
         x = 4
         print(x)
  ```
  - #### Some dynamically typed languages are: python, Java Script, Php Etc.
  
 ---
  
 - ### Differences
| Static Type   | Dynamic Type    | 
| :------------ |:---------------:|
| Type Checking is completed at compile Time             | Type Checking is completed at RunTime                     |
| Explicit type declarations are usually required        | Explicit type declarations are not required               |
| Errors are detected Earlier                            | Errors are detected later durning Exection                |
| Variables assignments are static and cannot be changed | Variables assignments are dynamic can be altered          |
| Produces more optimized code                           | Produces less optimized code, runtime errors are possible |
  

</details>

<details>
<summary> <h2>Static Binding VS Dynamic Binding ?</h2></summary>
 
  - ### In Static Binding Once we declare the variable than we cant not change the data Type and value of same variable
  
  ```
  #include <stdio.h>
  void main(){
    int x = 3;
    int x = 3;
    char x = 'c';
    printf("%d",x);
  }
  output is Error
  ```
  
  - ### In Dynamic Languages we are change the variable data type and its value
  
  ```
  x = 4
  print(x)

# now change the value
  x = 5
  print(x)

# Now change its Data type
  x = 'Hello'
  print(x)
 ```
</details>

<details>
  
<summary> <h2>Strong Typed Weak Type Dynamic and Static?</h2></summary>

- ### Some languages are Static they follow the rule of  Weak Type

- ### Some languages are Dynamic they follow the rule of Strong Type

- ### So Clear this Concept With this image

<img src="images/diff.png" />

- ### e.g python is the Dynamic Type They are follow the rule of Strong Type
- ### JavaScript is the Dynamic Type They are follow the rule of  Weak Type
- ### C is the Static Type They are follow the rule of Weak Type
</details>

---
# Lets Start Python

<details>
<summary> <h2>Tokens, Identifers, Keywords, Variables</h2></summary>

<a href="https://github.com/Mubeen-Ahmad/python_11/blob/main/Python/2_Tokens_Variables_Keywords_Identifers_Literals/1_Tokens_(Theory).ipynb
">What is Tokens</a>

<a href="https://github.com/Mubeen-Ahmad/python_11/blob/main/Python/2_Tokens_Variables_Keywords_Identifers_Literals/2_Identifers_and_keywords.ipynb">Identifers and Keywords</a>

<a href="https://github.com/Mubeen-Ahmad/python_11/blob/main/Python/2_Tokens_Variables_Keywords_Identifers_Literals/3_variables.ipynb">Variables</a>
</details>

<details>
<summary> <h2>Data Types</h2></summary>

- ### There are several built-in data types in Python. Although, Python doesn't require data types to be defined explicitly during variable declarations type errors are likely to occur if the knowledge of data types and their compatibility with each other are neglected. 

- ### Python provides type() and isinstance() functions to check the type of these variables. These data types can be grouped into the following categories

- #### 1. **None Type:** **None** keywork represents the null values in Python. Boolean equality operation can be performed using these NoneType objects.

- #### 2. **Numeric Type:** There are three distinct numeric types - `integers`, `floating-point numbers` and `complex numbers`. Additionally, `booleans` are a sub-type of integers.

- #### 3. **Sequence Types:** According to Python Docs, there are three basic Sequence Types - `string` `lists`, `tuples`, and `range` objects. Sequence types have the `in` and `not in` operators defined for their traversing their elements. These operators share the same priority as the comparison operations.

- #### 4. **Mapping Types:** A mapping object can map hashable values to random objects in Python. Mappings objects are mutable and there is currently only one standard mapping type, the `dictionary`.

- #### 5. **Set Types:** Currently, Python has two built-in set types - `set` and `frozenset`. `set` type is mutable and supports methods like *add()* and *remove()*. `frozenset` type is immutable and can't be modified after creation.

- #### 6. **Callable Types:** Callable types are the types to which function call can be applied. They can be **user-defined functions, instance methods, generator functions**, and some other **built-in functions, methods** and **classes**.

---

<details>
  
<summary> <h3>Sequential Data Type</h3></summary>
<h4>Strings</h4>

??? <a href="https://github.com/Mubeen-Ahmad/python_11/blob/main/Python/4_Strings/1_strings.ipynb">Strings</a><br>
??? <a href="https://github.com/Mubeen-Ahmad/python_11/blob/main/Python/4_Strings/2_Strings_Methods.ipynb">Strings Methods</a><br>
??? <a href="https://github.com/Mubeen-Ahmad/python_11/blob/main/Python/4_Strings/3_String_Interning_in_Memory.ipynb">Strings Interning in Memory</a><br><br>

<h4>List</h4>
??? <a href="https://github.com/Mubeen-Ahmad/python_11/blob/main/Python/5_List/1_list.ipynb">List</a><br><br>

<h4>Tuple</h4>
??? <a href="https://github.com/Mubeen-Ahmad/python_11/blob/main/Python/6_Tuple/1_Tuple.ipynb">Tuple</a>


</details>


<details>
  
<summary> <h3>Sets Type</h3></summary>
<h4>Set</h4>
??? <a href="https://github.com/Mubeen-Ahmad/python_11/blob/main/Python/7_Set/1_set.ipynb">Set</a><br>
??? <a href="https://github.com/Mubeen-Ahmad/python_11/blob/main/Python/7_Set/2_sets_methods.ipynb">Set Methods</a><br>
??? <a href="https://github.com/Mubeen-Ahmad/python_11/blob/main/Python/7_Set/3_frozen_set.ipynb">Frozensets</a>

</details>




<details>
  <summary> <h3>Mapping Type</h3></summary>
<h4>Dictionary</h4>
??? <a href="https://github.com/Mubeen-Ahmad/python_11/blob/main/Python/8_Dictionary/1_dictionary.ipynb">Dictionary</a><br>
??? <a href="https://github.com/Mubeen-Ahmad/python_11/blob/main/Python/8_Dictionary/2_dictionary_methods.ipynb">Dictionary Methods</a><br>
</details>


<details>
  <summary> <h3>Numeric Data Type</h3></summary>

<h4>Numeric Data Types</h4>
??? <a href="https://github.com/Mubeen-Ahmad/python_11/blob/main/Python/3_Numbers/1_Numbers_(int).ipynb">Integers</a><br>
??? <a href="https://github.com/Mubeen-Ahmad/python_11/blob/main/Python/3_Numbers/2_Float.ipynb">Float</a><br>
??? <a href="https://github.com/Mubeen-Ahmad/python_11/blob/main/Python/3_Numbers/4_Boolean.ipynb">Boolean</a><br><br>
<h4>Type Conversion</h4>
??? <a href="https://github.com/Mubeen-Ahmad/python_11/blob/main/Python/3_Numbers/5_Type_Conversion.ipynb">Type Conversion</a><br><br>
<h4>Math Module</h4>
??? <a href="https://github.com/Mubeen-Ahmad/python_11/blob/main/Python/3_Numbers/6_math_library.ipynb">Math module</a><br><br>
<h4>Number Interning</h4>
??? <a href="https://github.com/Mubeen-Ahmad/python_11/blob/main/Python/3_Numbers/7_Numbers_Interning.ipynb">Number Interning</a><br><br>



</details>
</details>

<details>
  <summary> <h2>Operators</h2></summary>

??? <a href="https://github.com/Mubeen-Ahmad/python_11/blob/main/Python/9_Operators/1_Arithmetic.ipynb">Arithmetic</a><br>
??? <a href="https://github.com/Mubeen-Ahmad/python_11/blob/main/Python/9_Operators/2_Comparison.ipynb">Comparison</a><br>
??? <a href="https://github.com/Mubeen-Ahmad/python_11/blob/main/Python/9_Operators/3_Logical.ipynb">Logical</a><br>
??? <a href="https://github.com/Mubeen-Ahmad/python_11/blob/main/Python/9_Operators/4_Identity.ipynb">Identity</a><br>
??? <a href="https://github.com/Mubeen-Ahmad/python_11/blob/main/Python/9_Operators/5_Membership.ipynb">Membership</a><br>
??? <a href="https://github.com/Mubeen-Ahmad/python_11/blob/main/Python/9_Operators/6_Bitwise.ipynb">Bitwise</a><br>
??? <a href="https://github.com/Mubeen-Ahmad/python_11/blob/main/Python/9_Operators/7_Assignment.ipynb">Assignment</a><br>
??? <a href="https://github.com/Mubeen-Ahmad/python_11/blob/main/Python/9_Operators/8_Precedence_and_Associativity.ipynb">Precedence and Associativity</a><br>

</details>


<details>
  <summary> <h2>Conditional Statement</h2></summary>
??? <a href="https://github.com/Mubeen-Ahmad/python_11/blob/main/Python/10_Conditional_Statements/1_conditions_statements.ipynb">Conditions Statements</a><br>
</details>


<details>
  <summary> <h2>Loops</h2></summary>
??? <a href="https://github.com/Mubeen-Ahmad/python_11/blob/main/Python/11_Loops/iterators.ipynb">Iterator VS Iterable</a><br>
??? <a href="https://github.com/Mubeen-Ahmad/python_11/blob/main/Python/11_Loops/loops.ipynb">for and while loop</a><br>
??? <a href="https://github.com/Mubeen-Ahmad/python_11/blob/main/Python/11_Loops/break_and_continue.ipynb">break continue and use of else in loop</a><br>
??? <a href="https://github.com/Mubeen-Ahmad/python_11/blob/main/Python/11_Loops/loops_use_in_datatypes.ipynb">Use of Loops in DataTypes</a><br>

</details>

<details>
  <summary> <h2>Callable Types</h2></summary>
    <details>
    <summary> <h3>Functions</h3></summary>
    ??? <a href="https://github.com/Mubeen-Ahmad/python_11/blob/main/Python/12_Functions/1_function.ipynb">Functions</a><br>
    ??? <a href="https://github.com/Mubeen-Ahmad/python_11/blob/main/Python/12_Functions/closer_Function.ipynb">Closer Function</a><br> 
    ??? <a href="https://github.com/Mubeen-Ahmad/python_11/blob/main/Python/12_Functions/2_args_kwargs.ipynb">Args and Kwargs</a><br>
    ??? <a href="https://github.com/Mubeen-Ahmad/python_11/blob/main/Python/12_Functions/3_recursion.ipynb">Recursion</a><br>
    ??? <a href="https://github.com/Mubeen-Ahmad/python_11/blob/main/Python/12_Functions/4_pass_by_value_or_refference.ipynb">Pass By Value or Refference ?</a><br>
    ??? <a href="https://github.com/Mubeen-Ahmad/python_11/blob/main/Python/12_Functions/5_NameSpace_and_LEGB_rule.ipynb">Namespace and LEGB Rule</a><br>
    ??? <a href="https://github.com/Mubeen-Ahmad/python_11/blob/main/Python/12_Functions/6_doc_string.ipynb">Doc String</a><br>
    ??? <a href="https://github.com/Mubeen-Ahmad/python_11/blob/main/Python/12_Functions/7_lambda_(Anonmyous)_Function.ipynb">Lambda Anonmyous Function</a><br>
    
 </details>
 
 <details>
     <summary> <h3>Generators</h3></summary>
    ??? <a href="https://github.com/Mubeen-Ahmad/python_11/blob/main/Python/13_Generators/Generator.ipynb">Generators</a><br>
 </details>

 <details>
     <summary> <h3>Decoractors</h3></summary>
    ??? <a href="https://github.com/Mubeen-Ahmad/python_11/blob/main/Python/14%20Decorators/decoractors.ipynb">Decoractors</a><br>
    ??? <a href="https://github.com/Mubeen-Ahmad/python_11/blob/main/Python/14%20Decorators/difference_in_decoractor_and_function_call.ipynb">Understand Difference in @function VS function()() </a><br>
    
</details>
 
 <details>
     <summary> <h3>OOP</h3></summary>
    ??? <a href="https://github.com/Mubeen-Ahmad/python_11/blob/main/Python/15_OOP/1_class_and_object.ipynb">Class and Object</a><br>
    ??? <a href="https://github.com/Mubeen-Ahmad/python_11/blob/main/Python/15_OOP/2_init_and_new_constructor.ipynb">Constructor (init and new)</a><br>
    ??? <a href="https://github.com/Mubeen-Ahmad/python_11/blob/main/Python/15_OOP/3_class_attributes.ipynb">Class Attributes and Class Variables</a><br>	
    ??? <a href="https://github.com/Mubeen-Ahmad/python_11/blob/main/Python/15_OOP/4_Instance_Variables.ipynb">Instance Variables</a><br>
    ??? <a href="https://github.com/Mubeen-Ahmad/python_11/blob/main/Python/15_OOP/5_Methods.ipynb">Methods and Difference between in Function and Method</a><br>
    ??? <a href="https://github.com/Mubeen-Ahmad/python_11/blob/main/Python/15_OOP/6_Class_Method.ipynb">Class Method</a><br>	
    ??? <a href="https://github.com/Mubeen-Ahmad/python_11/blob/main/Python/15_OOP/7_instance_Method.ipynb">Instance Method</a><br>	
    ??? <a href="https://github.com/Mubeen-Ahmad/python_11/blob/main/Python/15_OOP/8_Static_Method.ipynb">Static Method</a><br>
    ??? <a href="https://github.com/Mubeen-Ahmad/python_11/blob/main/Python/15_OOP/9_Decoractors_in_OOP.ipynb">Decoractors in Opp and __call__ Constructor</a><br>
    ??? <a href="https://github.com/Mubeen-Ahmad/python_11/blob/main/Python/15_OOP/10_property_decorator.ipynb">@property Decoractor and Concept of getter , setter, and deleter </a><br>	

    
 </details>
 
 
</details>

 <details>
     <summary> <h2>Comprehension</h2></summary>
    ??? <a href="https://github.com/Mubeen-Ahmad/python_11/blob/main/Python/11_Loops/comprehension.ipynb">Comprehension</a><br>
 </details>






