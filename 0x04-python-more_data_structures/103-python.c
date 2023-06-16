#include <stdio.h>
#include <Python.h>

void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);
/**
 * print_python_list - a function that print some
 * basic info about Python lists
 * @p: python object
 */

void print_python_list(PyObject *p)
{
	Py_ssize_t size = 0;
	PyObject *in_list;

	if (PyList_Check(p))
	{
		size = ((PyVarObject *)p)->ob_size;
		printf("[*] Python list info\n");
		printf("[*] Size of the Python List = %ld\n", size);
		printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

		for (Py_ssize_t i = 0; i < size; i++)
		{
			in_list = ((PyListObject *)p)->ob_item[i];
			printf("Element %ld: %s\n", i, in_list->ob_type->tp_name);

			if (strcmp(in_list->ob_type->tp_name, "bytes") == 0)
				print_python_bytes(in_list);
		}
	}
}

/**
 * print_python_bytes - a function that print some basic
 * info about Python bytes objects
 * @p: python object
 */

void print_python_bytes(PyObject *p)
{
	char *s = NULL;
	Py_ssize_t len = 0, i;

	printf("[.] bytes object info\n");

	if (!PyBytes_Check(p))
		printf("  [ERROR] Invalid Bytes Object\n");
	else
	{
		len = ((PyVarObject *)p)->ob_size;
		s = ((PyBytesObject *)p)->ob_sval;

		printf("  size: %ld\n", len);
		printf("  trying string: %.*s\n",(int) len, s);

		if (len > 10)
			len = 10;
		else
			len++;
      
		printf("  first %ld bytes: ", len);

		for (i = 0; i < len - 1; i++)
			printf("%02x ", (unsigned char)s[i]);

		printf("%02x\n", (unsigned char)s[len - 1]);
	}
}
