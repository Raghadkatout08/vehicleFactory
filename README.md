# vehicleFactory

This project is a vehicle factory system implemented using Object-Oriented Programming (OOP) principles in Python.

## Overview
The vehicle factory system consists of two main components:

- Car Department: Allows customers to request cars with specific requirements such as color, brand, number of doors, and fuel type.

- Motorcycle Department: Allows customers to request motorcycles with specific requirements such as model name and fuel type.

## Functionality
- Car Department
    * Customers can request cars with specific attributes such as color, brand, number of doors, and fuel type.
    * Each car object is counted, and the total number of cars created can be retrieved.

- Motorcycle Department
    * Customers can request motorcycles with specific attributes such as model name and fuel type.
    * Each motorcycle object is counted, and the total number of motorcycles created can be retrieved.

- Attributes Protection
    * All attributes are protected to ensure encapsulation.

- Abstract Methods
    * Common methods are defined as abstract methods in the parent class.

- String Representation
    * The __str__ method is implemented in both the Car and Motorcycle classes to display all attributes of the objects.

## Testing
* The project includes unit tests to ensure that all functionality works as expected.
* Test cases cover various scenarios for creating cars and motorcycles and checking the counts of each type of vehicle.

## Running the project
To run the project, follow these steps:

1. Clone the Repository: 
Clone the repository to your local machine using the following command:
```python 
git clone <repository_url>
```
Replace <repository_url> with the URL of your GitHub repository.

2. Navigate to the Project Directory: 
Navigate to the root directory of the cloned repository in your terminal or command prompt.

3. Activate the Virtual Environment: 
If you're using a virtual environment, activate it by running the appropriate activation command. For example, if you're using venv, activate it with:
```python 
source .venv/bin/activate
```

4. Run the Tests: 
Before running the project, it's a good practice to run the tests to ensure everything is working correctly. Use pytest to run the tests:
```pytest```

This command will automatically discover and run all the test cases in your project.