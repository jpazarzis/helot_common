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

#### Usage

To import the package you can use either style:

```python
from helot import configuration
```

```python
import helot.configuration
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
