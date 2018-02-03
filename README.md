## helot_configuration
## Adds a configuration object to helot namespace.

Exports a configuration object that can be used to hold application settings
loadable from json, yaml and direct assignment using python attribute access
syntax.
  
This library is favouring simplicity over comprehension while it allows the user
to easily build on top of it, in case that he wants to specialize its behaviour.

## Installation
#### Using pip
```
pip3 install helot_configuration
sudo python3 setup.py install
```

#### Source code
```
git clone https://github.com/jpazarzis/helot_configuration
```

## Importing

To import the package you can use either style:

```python
from helot.configuration import configuration
```

or

```python
import helot.configuration.configuration as configuration
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