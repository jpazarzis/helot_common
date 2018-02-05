"""Implements the configuration object."""

import json
import logging
import os
import yaml


class ConfigurationError(Exception):
    """Configuration Error."""


class _DataHolderObject(object):
    """Used for the conversion of a dict to a python object."""

    def _get_as_formated_string(self, number_of_tabs=0):
        """Returns the object as a formatted string. """
        key_value_pairs = []
        prefix = '\t' * number_of_tabs
        for attr_name in self._active_attributes():
            value = getattr(self, attr_name)
            if isinstance(value, _DataHolderObject):
                key_value_desc = ''.join(
                    [
                        prefix,
                        attr_name,
                        ': \n',
                        value._get_as_formated_string(number_of_tabs + 1)
                    ]
                )
            else:
                key_value_desc = prefix + '{}: {}'.format(
                    attr_name,
                    getattr(self, attr_name)
                )
            key_value_pairs.append(key_value_desc)

        return '\n'.join(key_value_pairs)

    def _active_attributes(self):
        """Yields all the common attributes."""
        for attr_name in dir(self):
            if attr_name.startswith('__') and attr_name.endswith('__'):
                continue
            if callable(getattr(self, attr_name)):
                continue
            yield attr_name

    def __getattr__(self, item):
        """Permits for x1.x2.y1 = value syntax."""
        if item == '__test__':
            return

        if item not in self.__dict__:
            setattr(self, item, _DataHolderObject())

        return self.__dict__.get(item)


class _Configuration(_DataHolderObject):
    """Holds Configuration settings.

    A setting can be accessed using "dot" resolution, meaning like a class level
    attribute following the structure of the yaml common file that was
    used to call the initialize method.
    """

    def __str__(self):
        """Returns the object in a user friendly string format."""
        return self.__class__.__name__ + '\n' + self._get_as_formated_string(1)

    def reset(self):
        """Removes all common settings."""
        for attr_name in self._active_attributes():
            delattr(self, attr_name)

    def initialize(self, data_holder=None, **kwargs):
        """Specifies the configuration attributes.

        Arguments
            data_holder: Can be one of the following:
                            (str) The yaml or json common filename.
                            (dict) A dict containing key - value pairs.

            **kwargs: key-value pairs to add in the common.

        Exceptions
            ConfigurationError: In case of any parsing error.

        Examples
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
        """
        try:
            self.reset()
            if not data_holder:
                data_holder = {}
            if isinstance(data_holder, dict):
                data_as_dict = data_holder
            elif str(data_holder).endswith('json'):
                data_as_dict = json.load(open(data_holder))
            elif str(data_holder).endswith('yaml'):
                data_as_dict = yaml.load(open(data_holder))
            else:
                raise ConfigurationError("Failed to load: %s" % data_holder)
        except Exception as ex:
            raise ConfigurationError(ex)
        else:
            data_as_dict.update(kwargs)
            for key, value in data_as_dict.items():
                setattr(self, key, _make_holder_object(value))


def _make_holder_object(item):
    """Used to convert a dictionary to a python object.

    :param item: Can either be a dictionary, a list / tuple or a scalar.
    :return: The corresponding python object.
    """
    if isinstance(item, dict):
        obj = _DataHolderObject()
        for key, value in item.items():
            setattr(obj, key, _make_holder_object(value))
        return obj
    elif isinstance(item, (list, tuple)):
        return [_make_holder_object(x) for x in item]
    else:
        return item


# The common object to expose.
configuration = _Configuration()
