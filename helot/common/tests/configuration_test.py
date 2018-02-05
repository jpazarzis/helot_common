"""Tests the configuration class."""

import os
import unittest

from helot.common import ConfigurationError
from helot.common import configuration
from helot.common.configuration import _DataHolderObject

_CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))
_RESOURCES_DIR = os.path.join(_CURRENT_DIR, 'resources')
_YAML_CONIFIGURATION_FILENAME = os.path.join(_RESOURCES_DIR, 'sample.yaml')
_JSON_CONIFIGURATION_FILENAME = os.path.join(_RESOURCES_DIR, 'sample.json')
_BAD_JSON_CONIFIGURATION_FILENAME = os.path.join(_RESOURCES_DIR, 'bad.json')
_BAD_YAML_CONIFIGURATION_FILENAME = os.path.join(_RESOURCES_DIR, 'invalid.yaml')


class TestConfiguration(unittest.TestCase):
    def setUp(self):
        configuration.reset()

    def test_testing_mode(self):
        configuration.initialize(_YAML_CONIFIGURATION_FILENAME)
        self.assertEqual(configuration.name, "Martin D'vloper")
        self.assertEqual(configuration.job, "Developer")
        self.assertEqual(configuration.skill, "Elite")
        self.assertEqual(configuration.employed, True)
        self.assertEqual(configuration.age, 24)
        self.assertEqual(configuration.foods, ['Apple', 'Mango', 1234])
        self.assertEqual(configuration.languages.perl, 'Elite')
        self.assertEqual(configuration.languages.object_oriented.best,
                         ['C++', 'C#'])
        self.assertEqual(configuration.languages.object_oriented.great, 'Java')

    def test_instantiation_of_configuration(self):
        with self.assertRaises(TypeError):
            _ = configuration()

    def test_non_existing_attribute(self):
        x = configuration.junk
        self.assertTrue(isinstance(x, _DataHolderObject))
        configuration.junk = 'junk'
        self.assertTrue(isinstance(configuration.junk, str))
        self.assertEqual(configuration.junk, 'junk')
        configuration.junk1.junk = 'junk'
        self.assertTrue(isinstance(configuration.junk1, _DataHolderObject))
        self.assertEqual(configuration.junk1.junk, 'junk')
        self.assertTrue(isinstance(configuration.junk1.junk, str))
        configuration.j1.j2.j3.j4.j5 = 'junk'
        self.assertEqual(configuration.j1.j2.j3.j4.j5, 'junk')

    def test_setting_new_configuration_attribute(self):
        configuration.junk = 'this is junk'
        self.assertEqual(configuration.junk, 'this is junk')

    def test_data_holder_object(self):
        x = _DataHolderObject()
        x.t1.t2.t3 = [1, 2]
        self.assertListEqual(x.t1.t2.t3, [1, 2])

    def test_assignments(self):
        configuration.host = 'localhost'
        self.assertTrue(isinstance(configuration.host, str))
        configuration.reset()
        configuration.host = 'localhost'
        self.assertTrue(isinstance(configuration.host, str))

    def test_json_initialization(self):
        configuration.initialize(_JSON_CONIFIGURATION_FILENAME)
        self.assertEqual(configuration.name, "Martin D'vloper")
        self.assertEqual(configuration.job, "Developer")
        self.assertEqual(configuration.skill, "Elite")
        self.assertEqual(configuration.employed, True)
        self.assertEqual(configuration.age, 24)
        self.assertEqual(configuration.foods, ['Apple', 'Mango', 1234])
        self.assertEqual(configuration.languages.perl, 'Elite')
        self.assertEqual(configuration.languages.object_oriented.best,
                         ['C++', 'C#'])
        self.assertEqual(configuration.languages.object_oriented.great, 'Java')

    def test_bad_yaml(self):
        with self.assertRaises(ConfigurationError):
            configuration.initialize(_BAD_YAML_CONIFIGURATION_FILENAME)

    def test_bad_json(self):
        with self.assertRaises(ConfigurationError):
            configuration.initialize(_BAD_JSON_CONIFIGURATION_FILENAME)

    def test_non_existing_filename(self):
        with self.assertRaises(ConfigurationError):
            configuration.initialize("invalid.nonexisting")

    def test_dict_initialization(self):
        values_as_dict = {
            "name": "Martin D'vloper",
            "job": "Developer",
            "skill": "Elite",
            "employed": True,
            "age": 24,
            "foods": [
                "Apple",
                "Mango",
                1234
            ],
            "languages": {
                "perl": "Elite",
                "python": "Elite",
                "pascal": "Lame",
                "object_oriented": {
                    "best": [
                        "C++",
                        "C#"
                    ],
                    "great": "Java"
                }
            },
            "mysql": {
                "host": "localhost",
                "user": "root",
                "passwd": "vagrant",
                "db": "test"
            }
        }
        configuration.initialize(values_as_dict)
        self.assertEqual(configuration.name, "Martin D'vloper")
        self.assertEqual(configuration.job, "Developer")
        self.assertEqual(configuration.skill, "Elite")
        self.assertEqual(configuration.employed, True)
        self.assertEqual(configuration.age, 24)
        self.assertEqual(configuration.foods, ['Apple', 'Mango', 1234])
        self.assertEqual(configuration.languages.perl, 'Elite')
        self.assertEqual(configuration.languages.object_oriented.best,
                         ['C++', 'C#'])
        self.assertEqual(configuration.languages.object_oriented.great, 'Java')

    def test_direct_initalization(self):
        languages = {
            "perl": "Elite",
            "python": "Elite",
            "pascal": "Lame",
            "object_oriented": {
                "best": [
                    "C++",
                    "C#"
                ],
                "great": "Java"
            }
        }

        configuration.initialize(name="Martin D'vloper", job="Developer",
                                 skill="Elite", employed=True,
                                 foods=["Apple", "Mango", 1234],
                                 languages=languages)
        self.assertEqual(configuration.name, "Martin D'vloper")
        self.assertEqual(configuration.job, "Developer")
        self.assertEqual(configuration.skill, "Elite")
        self.assertEqual(configuration.employed, True)
        self.assertEqual(configuration.foods, ['Apple', 'Mango', 1234])
        self.assertEqual(configuration.languages.object_oriented.best,
                         ['C++', 'C#'])

    def test_mixed_json_initialization(self):
        configuration.initialize(_JSON_CONIFIGURATION_FILENAME,
                                 junk='some junk')
        self.assertEqual(configuration.name, "Martin D'vloper")
        self.assertEqual(configuration.foods, ['Apple', 'Mango', 1234])
        self.assertEqual(configuration.languages.perl, 'Elite')
        self.assertEqual(configuration.languages.object_oriented.best,
                         ['C++', 'C#'])
        self.assertEqual(configuration.languages.object_oriented.great, 'Java')
        self.assertEqual(configuration.junk, 'some junk')

    def test_mixed_yaml_initialization(self):
        configuration.initialize(_YAML_CONIFIGURATION_FILENAME,
                                 junk='some junk')
        self.assertEqual(configuration.name, "Martin D'vloper")
        self.assertEqual(configuration.foods, ['Apple', 'Mango', 1234])
        self.assertEqual(configuration.languages.perl, 'Elite')
        self.assertEqual(configuration.languages.object_oriented.best,
                         ['C++', 'C#'])
        self.assertEqual(configuration.languages.object_oriented.great, 'Java')
        self.assertEqual(configuration.junk, 'some junk')
