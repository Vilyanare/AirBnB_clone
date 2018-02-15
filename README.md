# AirBnB_clone Command Interface
---
In this project we are creating a Command Interface for a Air BnB clone project.  It has file storage capabilites and an ability to interact with a number of data types that will later be added to.
---
## Instalation
Clone repository from [github](https://github.com/Vilyanare/AirBnB_clone.git "GitHub AirBnBclone project")</br>
Navigate to root directory of project ./AirBnBclone<br>
Start the console with ```./console.py``` or ```python3 console.py```

## Learning Objectives
Through this project the authors learned:
* How to create a Python package
* How to create a command interpreter in Python using the cmd module
* What Unit testing is
* How to implement unit testing in a large project
* How to serialize and deserialize a class
* How to write and read a JSON file
* How to manage datetime
* What is **kwargs and how to use it
* How to handle named arguments in a function

## Requirements
* All files will be interpreted on Ubuntu 14.04 LTS using python3
* A README.md file at the root of the folder
* All code is PEP8 compliant
* All files must be executable
* All modules should have documentation
* All classes should have documentation
* All functions should have a documentation

## File Descriptions
| **File** | **Description** |
| -------- | ----------- |
| `base_model` | This file creates an instance of the class BaseModel. It
defines all common attributes/methods for other classes. Attributes include:
id (string): a string with an uuid when an instance is created, created_at:
 assigned with the current datetime when an instance is created, updated_at:
 assigned with the current datetime when an instance is created and it will be
 updated every time the object gets changed |
| `file_storage` | This file creates an instance of the class FileStorage. It
 serializes instances to a JSON file and deserializes JSON file to instances.
 Attributes include: __file_path (private, string): that represents the path
 to the JSON file, __objects (dictionary): initialized empty, but will store
 all objects by class name and id. |

## Function Descriptions for BaseModel
| **Function** | **Description** |
| -------- | ----------- |
| `__str__` | Function should print class name, instance id, and its dictionary |
| `__repr__` | Function should print class name, instance id, and its dictionary |
| `save` | Function should update public instance attribute, updated_at with the current datetime |
| `to_dict` | Function should return a dictionary containing all keys/values ofthe instance's dictionary. It should add a key called 'class' correlating withthe class of the object. The attributes, created_at and updated_at must be converted to string objects in ISO format |
| `__init__` | Function should print use kwargs arguments to construct the
instance. Each key of the dictionary in kwargs is an attribute name and each
value of the dictionary is the value of the attribute name. If kwargs does not
exist, id and created_at attributes should be created as a new instance |

