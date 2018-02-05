# helot_common
Adds the common library to helot library.
  
This library is favouring simplicity over comprehension while it allows the user

to easily build on top of it, in case that he wants to specialize its behaviour.

## Installation

#### Using pip
```
pip3 install helot_common
```

#### Source code
```
git clone https://github.com/jpazarzis/helot_common
sudo python3 setup.py install
```

The exposed components from common are the following: 

### configuration
Exports a configuration object that can be used to hold application settings
loadable from json, yaml and direct assignment using python attribute access
syntax.

## Importing

To import the package you can use either style:

```python
from helot.common import configuration
```

or

```python
import helot.common.configuration as configuration
```

The following syntax:
```python
import helot
helot.configuration
```

will not work and will produce the following exception:
```
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: module 'helot' has no attribute 'configuration'
```

## Examples
#### Initialize from json file

Save the following file as john_doe.json
```
{
  "name": "John Doe",
  "job": "Developer",
  "skills": {
        "languages": ["C++", "Python", "Java"],
        "operating_systems": ["Linux", "Windows]
  }
}
```

Save the following python script as test1.py:
```python
from helot.configuration import configuration
configuration.initialize('john_doe.json')
print(configuration.name)
print(configuration.job)
print(configuration.skills.languages)
```

Running test1.py produces the following output:
```
ubuntu@ubuntu-xenial:~$ python3 test1.py 
John Doe
Developer
['C++', 'Python', 'Java']
```


#### Initialize from yaml file

Save the following file as john_doe.yaml
```
name: Martin D'vloper
job: Developer
skills:
    languages:
        - C++
        - C#
        - Python
```

Save the following python script as test2.py:
```python
from helot.configuration import configuration
configuration.initialize('john_doe.yaml')
print(configuration.name)
print(configuration.job)
print(configuration.skills.languages)
```

Running test2.py produces the following output:
```
ubuntu@ubuntu-xenial:~$ python3 test2.py 
John Doe
Developer
['C++', 'Python', 'Java']
```
#### Common use cases

```
>>> from helot.common import configuration as c
>>> c.initialize({'a': 1})
>>> c.a
1
>>> print(c)
_Configuration
a: 1
>>> c.reset()
>>> print(c)
_Configuration
>>> c.initialize(a='test')
>>> print(c)
_Configuration
        a: test
>>> with open('test.json', 'w') as f:
...     f.write('{"a": "test" }')
...
14
>>> c.initialize('test.json', name='unknown')
>>> c.name
'unknown'
>>> c.a
'test'
```
