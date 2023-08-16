#!/usr/bin/python3
"""Defines unittests for base.py.

Unittest classes:
    TestBaseInstantiation - line 21
    TestBaseToJsonString - line 108
    TestBaseSaveToFile - line 154
    TestBaseFromJsonString - line 232
    TestBaseCreate - line 286
    TestBaseLoadFromFile - line 338
    TestBaseSaveToFileCSV - line 404
    TestBaseLoadFromFileCSV - line 482
"""
import os
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBaseInstantiation(unittest.TestCase):
    """Unittests for testing instantiation of the Base class."""

    def test_no_arg(self):
        base1 = Base()
        base2 = Base()
        self.assertEqual(base1.id, base2.id - 1)

    def test_three_bases(self):
        base1 = Base()
        base2 = Base()
        base3 = Base()
        self.assertEqual(base1.id, base3.id - 2)

    def test_None_id(self):
        base1 = Base(None)
        base2 = Base(None)
        self.assertEqual(base1.id, base2.id - 1)

    def test_unique_id(self):
        self.assertEqual(12, Base(12).id)

    def test_nb_instances_after_unique_id(self):
        base1 = Base()
        base2 = Base(12)
        base3 = Base()
        self.assertEqual(base1.id, base3.id - 1)

    def test_id_public(self):
        base = Base(12)
        base.id = 15
        self.assertEqual(15, base.id)

    def test_nb_instances_private(self):
        with self.assertRaises(AttributeError):
            print(Base(12)._Base__nb_instances)

    def test_str_id(self):
        self.assertEqual("hello", Base("hello").id)

    def test_float_id(self):
        self.assertEqual(5.5, Base(5.5).id)

    def test_complex_id(self):
        self.assertEqual(complex(5), Base(complex(5)).id)

    def test_dict_id(self):
        self.assertEqual({"a": 1, "b": 2}, Base({"a": 1, "b": 2}).id)

    def test_bool_id(self):
        self.assertEqual(True, Base(True).id)

    def test_list_id(self):
        self.assertEqual([1, 2, 3], Base([1, 2, 3]).id)

    def test_tuple_id(self):
        self.assertEqual((1, 2), Base((1, 2)).id)

    def test_set_id(self):
        self.assertEqual({1, 2, 3}, Base({1, 2, 3}).id)

    def test_frozenset_id(self):
        self.assertEqual(frozenset({1, 2, 3}), Base(frozenset({1, 2, 3})).id)

    def test_range_id(self):
        self.assertEqual(range(5), Base(range(5)).id)

    def test_bytes_id(self):
        self.assertEqual(b'Python', Base(b'Python').id)

    def test_bytearray_id(self):
        self.assertEqual(bytearray(b'abcefg'), Base(bytearray(b'abcefg')).id)

    def test_memoryview_id(self):
        self.assertEqual(memoryview(b'abcefg'), Base(memoryview(b'abcefg')).id)

    def test_inf_id(self):
        self.assertEqual(float('inf'), Base(float('inf')).id)

    def test_NaN_id(self):
        self.assertNotEqual(float('nan'), Base(float('nan')).id)

    def test_two_args(self):
        with self.assertRaises(TypeError):
            Base(1, 2)


class TestBaseToJsonString(unittest.TestCase):
    """Unittests for testing to_json_string method of Base class."""

    def test_to_json_string_rectangle_type(self):
        rectangle = Rectangle(10, 7, 2, 8, 6)
        self.assertEqual(str, type(Base.to_json_string([rectangle.to_dictionary()])))

    def test_to_json_string_rectangle_one_dict(self):
        rectangle = Rectangle(10, 7, 2, 8, 6)
        self.assertTrue(len(Base.to_json_string([rectangle.to_dictionary()])) == 53)

    def test_to_json_string_rectangle_two_dicts(self):
        rectangle1 = Rectangle(2, 3, 5, 19, 2)
        rectangle2 = Rectangle(4, 2, 4, 1, 12)
        list_dicts = [rectangle1.to_dictionary(), rectangle2.to_dictionary()]
        self.assertTrue(len(Base.to_json_string(list_dicts)) == 106)

    def test_to_json_string_square_type(self):
        square = Square(10, 2, 3, 4)
        self.assertEqual(str, type(Base.to_json_string([square.to_dictionary()])))

    def test_to_json_string_square_one_dict(self):
        square = Square(10, 2, 3, 4)
        self.assertTrue(len(Base.to_json_string([square.to_dictionary()])) == 39)

    def test_to_json_string_square_two_dicts(self):
        square1 = Square(10, 2, 3, 4)
        square2 = Square(4, 5, 21, 2)
        list_dicts = [square1.to_dictionary(), square2.to_dictionary()]
        self.assertTrue(len(Base.to_json_string(list_dicts)) == 78)

    def test_to_json_string_empty_list(self):
        self.assertEqual("[]", Base.to_json_string([]))

    def test_to_json_string_none(self):
        self.assertEqual("[]", Base.to_json_string(None))

    def test_to_json_string_no_args(self):
        with self.assertRaises(TypeError):
            Base.to_json_string()

    def test_to_json_string_more_than_one_arg(self):
        with self.assertRaises(TypeError):
            Base.to_json_string([], 1)


class TestBaseSaveToFile(unittest.TestCase):
    """Unittests for testing save_to_file method of Base class."""

    @classmethod
    def tearDown(cls):
        """Delete any created files."""
        try:
            os.remove("Rectangle.json")
        except IOError:
            pass
        try:
            os.remove("Square.json")
        except IOError:
            pass
        try:
            os.remove("Base.json")
        except IOError:
            pass

    def test_save_to_file_one_rectangle(self):
        rectangle = Rectangle(10, 7, 2, 8, 5)
        Rectangle.save_to_file([rectangle])
        with open("Rectangle.json", "r") as fileobj:
            self.assertTrue(len(fileobj.read()) == 53)

    def test_save_to_file_two_rectangles(self):
        rectangle1 = Rectangle(10, 7, 2, 8, 5)
        rectangle2 = Rectangle(2, 4, 1, 2, 3)
        Rectangle.save_to_file([rectangle1, rectangle2])
        with open("Rectangle.json", "r") as fileobj:
            self.assertTrue(len(fileobj.read()) == 105)

    def test_save_to_file_one_square(self):
        square = Square(10, 7, 2, 8)
        Square.save_to_file([square])
        with open("Square.json", "r") as fileobj:
            self.assertTrue(len(fileobj.read()) == 39)

    def test_save_to_file_two_squares(self):
        square1 = Square(10, 7, 2, 8)
        square2 = Square(8, 1, 2, 3)
        Square.save_to_file([square1, square2])
        with open("Square.json", "r") as fileobj:
            self.assertTrue(len(fileobj.read()) == 77)

    def test_save_to_file_cls_name_for_filename(self):
        square = Square(10, 7, 2, 8)
        Base.save_to_file([square])
        with open("Base.json", "r") as fileobj:
            self.assertTrue(len(fileobj.read()) == 39)

    def test_save_to_file_overwrite(self):
        square = Square(9, 2, 39, 2)
        Square.save_to_file([square])
        square = Square(10, 7, 2, 8)
        Square.save_to_file([square])
        with open("Square.json", "r") as fileobj:
            self.assertTrue(len(fileobj.read()) == 39)

    def test_save_to_file_None(self):
        Square.save_to_file(None)
        with open("Square.json", "r") as fileobj:
            self.assertEqual("[]", fileobj.read())

    def test_save_to_file_empty_list(self):
        Square.save_to_file([])
        with open("Square.json", "r") as fileobj:
            self.assertEqual("[]", fileobj.read())

    def test_save_to_file_no_args(self):
        with self.assertRaises(TypeError):
            Rectangle.save_to_file()

    def test_save_to_file_more_than_one_arg(self):
        with self.assertRaises(TypeError):
            Square.save_to_file([], 1)


class TestBaseFromJsonString(unittest.TestCase):
    """Unittests for testing from_json_string method of Base class."""

    def test_from_json_string_type(self):
        list_input = [{"id": 89, "width": 10, "height": 4}]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list, type(list_output))

    def test_from_json_string_one_rectangle(self):
        list_input = [{"id": 89, "width": 10, "height": 4, "x": 7}]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list_input, list_output)

    def test_from_json_string_two_rectangles(self):
        list_input = [
            {"id": 89, "width": 10, "height": 4, "x": 7, "y": 8},
            {"id": 98, "width": 5, "height": 2, "x": 1, "y": 3},
        ]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list_input, list_output)

    def test_from_json_string_one_square(self):
        list_input = [{"id": 89, "size": 10, "height": 4}]
        json_list_input = Square.to_json_string(list_input)
        list_output = Square.from_json_string(json_list_input)
        self.assertEqual(list_input, list_output)

    def test_from_json_string_two_squares(self):
        list_input = [
            {"id": 89, "size": 10, "height": 4},
            {"id": 7, "size": 1, "height": 7}
        ]
        json_list_input = Square.to_json_string(list_input)
        list_output = Square.from_json_string(json_list_input)
        self.assertEqual(list_input, list_output)

    def test_from_json_string_None(self):
        self.assertEqual([], Base.from_json_string(None))

    def test_from_json_string_empty_list(self):
        self.assertEqual([], Base.from_json_string("[]"))

    def test_from_json_string_no_args(self):
        with self.assertRaises(TypeError):
            Base.from_json_string()

    def test_from_json_string_more_than_one_arg(self):
        with self.assertRaises(TypeError):
            Base.from_json_string([], 1)


class TestBaseCreate(unittest.TestCase):
    """Unittests for testing create method of Base class."""

    def test_create_rectangle_original(self):
        rectangle1 = Rectangle(3, 5, 1, 2, 7)
        rectangle1_dict = rectangle1.to_dictionary()
        rectangle2 = Rectangle.create(**rectangle1_dict)
        self.assertEqual("[Rectangle] (7) 1/2 - 3/5", str(rectangle1))

    def test_create_rectangle_new(self):
        rectangle1 = Rectangle(3, 5, 1, 2, 7)
        rectangle1_dict = rectangle1.to_dictionary()
        rectangle2 = Rectangle.create(**rectangle1_dict)
        self.assertEqual("[Rectangle] (7) 1/2 - 3/5", str(rectangle2))

    def test_create_rectangle_is(self):
        rectangle1 = Rectangle(3, 5, 1, 2, 7)
        rectangle1_dict = rectangle1.to_dictionary()
        rectangle2 = Rectangle.create(**rectangle1_dict)
        self.assertIsNot(rectangle1, rectangle2)

    def test_create_rectangle_equals(self):
        rectangle1 = Rectangle(3, 5, 1, 2, 7)
        rectangle1_dict = rectangle1.to_dictionary()
        rectangle2 = Rectangle.create(**rectangle1_dict)
        self.assertNotEqual(rectangle1, rectangle2)

    def test_create_square_original(self):
        square1 = Square(3, 5, 1, 7)
        square1_dict = square1.to_dictionary()
        square2 = Square.create(**square1_dict)
        self.assertEqual("[Square] (7) 5/1 - 3", str(square1))

    def test_create_square_new(self):
        square1 = Square(3, 5, 1, 7)
        square1_dict = square1.to_dictionary()
        square2 = Square.create(**square1_dict)
        self.assertEqual("[Square] (7) 5/1 - 3", str(square2))

    def test_create_square_is(self):
        square1 = Square(3, 5, 1, 7)
        square1_dict = square1.to_dictionary()
        square2 = Square.create(**square1_dict)
        self.assertIsNot(square1, square2)

    def test_create_square_equals(self):
        square1 = Square(3, 5, 1, 7)
        square1_dict = square1.to_dictionary()
        square2 = Square.create(**square1_dict)
        self.assertNotEqual(square1, square2)


class TestBaseLoadFromFile(unittest.TestCase):
    """Unittests for testing load_from_file_method of Base class."""

    @classmethod
    def tearDown(cls):
        """Delete any created files."""
        try:
            os.remove("Rectangle.json")
        except IOError:
            pass
        try:
            os.remove("Square.json")
        except IOError:
            pass

    def test_load_from_file_first_rectangle(self):
        rectangle1 = Rectangle(10, 7, 2, 8, 1)
        rectangle2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file([rectangle1, rectangle2])
        list_rectangles_output = Rectangle.load_from_file()
        self.assertEqual(str(rectangle1), str(list_rectangles_output[0]))

    def test_load_from_file_second_rectangle(self):
        rectangle1 = Rectangle(10, 7, 2, 8, 1)
        rectangle2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file([rectangle1, rectangle2])
        list_rectangles_output = Rectangle.load_from_file()
        self.assertEqual(str(rectangle2), str(list_rectangles_output[1]))

    def test_load_from_file_rectangle_types(self):
        rectangle1 = Rectangle(10, 7, 2, 8, 1)
        rectangle2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file([rectangle1, rectangle2])
        output = Rectangle.load_from_file()
        self.assertTrue(all(type(obj) == Rectangle for obj in output))

    def test_load_from_file_first_square(self):
        square1 = Square(5, 1, 3, 3)
        square2 = Square(9, 5, 2, 3)
        Square.save_to_file([square1, square2])
        list_squares_output = Square.load_from_file()
        self.assertEqual(str(square1), str(list_squares_output[0]))

    def test_load_from_file_second_square(self):
        square1 = Square(5, 1, 3, 3)
        square2 = Square(9, 5, 2, 3)
        Square.save_to_file([square1, square2])
        list_squares_output = Square.load_from_file()
        self.assertEqual(str(square2), str(list_squares_output[1]))

    def test_load_from_file_square_types(self):
        square1 = Square(5, 1, 3, 3)
        square2 = Square(9, 5, 2, 3)
        Square.save_to_file([square1, square2])
        output = Square.load_from_file()
        self.assertTrue(all(type(obj) == Square for obj in output))

    def test_load_from_file_no_file(self):
        output = Square.load_from_file()
        self.assertEqual([], output)

    def test_load_from_file_more_than_one_arg(self):
        with self.assertRaises(TypeError):
            Base.load_from_file([], 1)


class TestBaseSaveToFileCsv(unittest.TestCase):
    """Unittests for testing save_to_file_csv method of Base class."""

    @classmethod
    def tearDown(cls):
        """Delete any created files."""
        try:
            os.remove("Rectangle.csv")
        except IOError:
            pass
        try:
            os.remove("Square.csv")
        except IOError:
            pass
        try:
            os.remove("Base.csv")
        except IOError:
            pass

    def test_save_to_file_csv_one_rectangle(self):
        rectangle = Rectangle(10, 7, 2, 8, 5)
        Rectangle.save_to_file_csv([rectangle])
        with open("Rectangle.csv", "r") as fileobj:
            self.assertTrue("5,10,7,2,8", fileobj.read())

    def test_save_to_file_csv_two_rectangles(self):
        rectangle1 = Rectangle(10, 7, 2, 8, 5)
        rectangle2 = Rectangle(2, 4, 1, 2, 3)
        Rectangle.save_to_file_csv([rectangle1, rectangle2])
        with open("Rectangle.csv", "r") as fileobj:
            self.assertTrue("5,10,7,2,8\n2,4,1,2,3", fileobj.read())

    def test_save_to_file_csv_one_square(self):
        square = Square(10, 7, 2, 8)
        Square.save_to_file_csv([square])
        with open("Square.csv", "r") as fileobj:
            self.assertTrue("8,10,7,2", fileobj.read())

    def test_save_to_file_csv_two_squares(self):
        square1 = Square(10, 7, 2, 8)
        square2 = Square(8, 1, 2, 3)
        Square.save_to_file_csv([square1, square2])
        with open("Square.csv", "r") as fileobj:
            self.assertTrue("8,10,7,2\n3,8,1,2", fileobj.read())

    def test_save_to_file_csv_cls_name(self):
        square = Square(10, 7, 2, 8)
        Base.save_to_file_csv([square])
        with open("Base.csv", "r") as fileobj:
            self.assertTrue("8,10,7,2", fileobj.read())

    def test_save_to_file_csv_overwrite(self):
        square = Square(9, 2, 39, 2)
        Square.save_to_file_csv([square])
        square = Square(10, 7, 2, 8)
        Square.save_to_file_csv([square])
        with open("Square.csv", "r") as fileobj:
            self.assertTrue("8,10,7,2", fileobj.read())

    def test_save_to_file_csv_None(self):
        Square.save_to_file_csv(None)
        with open("Square.csv", "r") as fileobj:
            self.assertEqual("[]", fileobj.read())

    def test_save_to_file_csv_empty_list(self):
        Square.save_to_file_csv([])
        with open("Square.csv", "r") as fileobj:
            self.assertEqual("[]", fileobj.read())

    def test_save_to_file_csv_no_args(self):
        with self.assertRaises(TypeError):
            Rectangle.save_to_file_csv()

    def test_save_to_file_csv_more_than_one_arg(self):
        with self.assertRaises(TypeError):
            Square.save_to_file_csv([], 1)


class TestBaseLoadFromFileCsv(unittest.TestCase):
    """Unittests for testing load_from_file_csv method of Base class."""

    @classmethod
    def tearDown(cls):
        """Delete any created files."""
        try:
            os.remove("Rectangle.csv")
        except IOError:
            pass
        try:
            os.remove("Square.csv")
        except IOError:
            pass

    def test_load_from_file_csv_first_rectangle(self):
        rectangle1 = Rectangle(10, 7, 2, 8, 1)
        rectangle2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file_csv([rectangle1, rectangle2])
        list_rectangles_output = Rectangle.load_from_file_csv()
        self.assertEqual(str(rectangle1), str(list_rectangles_output[0]))

    def test_load_from_file_csv_second_rectangle(self):
        rectangle1 = Rectangle(10, 7, 2, 8, 1)
        rectangle2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file_csv([rectangle1, rectangle2])
        list_rectangles_output = Rectangle.load_from_file_csv()
        self.assertEqual(str(rectangle2), str(list_rectangles_output[1]))

    def test_load_from_file_csv_rectangle_types(self):
        rectangle1 = Rectangle(10, 7, 2, 8, 1)
        rectangle2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file_csv([rectangle1, rectangle2])
        output = Rectangle.load_from_file_csv()
        self.assertTrue(all(type(obj) == Rectangle for obj in output))

    def test_load_from_file_csv_first_square(self):
        square1 = Square(5, 1, 3, 3)
        square2 = Square(9, 5, 2, 3)
        Square.save_to_file_csv([square1, square2])
        list_squares_output = Square.load_from_file_csv()
        self.assertEqual(str(square1), str(list_squares_output[0]))

    def test_load_from_file_csv_second_square(self):
        square1 = Square(5, 1, 3, 3)
        square2 = Square(9, 5, 2, 3)
        Square.save_to_file_csv([square1, square2])
        list_squares_output = Square.load_from_file_csv()
        self.assertEqual(str(square2), str(list_squares_output[1]))

    def test_load_from_file_csv_square_types(self):
        square1 = Square(5, 1, 3, 3)
        square2 = Square(9, 5, 2, 3)
        Square.save_to_file_csv([square1, square2])
        output = Square.load_from_file_csv()
        self.assertTrue(all(type(obj) == Square for obj in output))

    def test_load_from_file_csv_no_file(self):
        output = Square.load_from_file_csv()
        self.assertEqual([], output)

    def test_load_from_file_csv_more_than_one_arg(self):
        with self.assertRaises(TypeError):
            Base.load_from_file_csv([], 1)


if __name__ == "__main__":
    unittest.main()
