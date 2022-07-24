# [Programming Paradigm - Shipping Yard](https://gist.github.com/fandywie/7dab4c9914f3d37dfd336da02db9fb11)

**NOTES: In Java or others, we could do something like `private`, `public`, or `protected` to enhance encapsulation. Yet, in Python, it is not possible. Moreover, Python also don't support overloading for polymorphism.**

### `Perahu`

`Perahu` is an abstract class (inherits from `ABC`, python abstract class) which has an attribute `owner`, an abstract method `get_cost()`, and a static method `horn()`. 

### `PerahuLayar`

`PerahuLayar` inherits `Perahu` class and has additional attributes `number_of_sail`, `cost_per_sail`, and an override method of abstract method `get_cost()`.

### `PerahuMotor`

`PerahuMotor` inherits `Perahu` class and has additional attributes `number_of_motor`, `cost_per_motor`, an override method of abstract method `get_cost()`, and an override method of static method `horn()`.

### `KapalPesiar`

`PerahuMotor` inherits `Perahu` class and has additional attributes `captain`, `number_of_crew`, `cost_captain`, `cost_per_crew`, an override method of abstract method `get_cost()`, and an override method of static method `horn()`.

---

This project was developed for SIRCLO | Technical Test Software Engineer Backend.
