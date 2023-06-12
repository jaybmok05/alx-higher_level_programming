#include <Python.h>
#include <object.h>
#include <listobject.h>

void print_python_list_info(PyObject *p)
{
	long int size = PyList_Size(p);
	PyListObject *obj = (PyListObject *) p;
	PyObject *item;
	const char *type_name;
	int index;

	printf("[*] Size of the Python List = %li\n", size);
	printf("[*] Allocated = %li\n", obj->allocated);

	for (index = 0; index < size; index++)
	{
		item = obj->ob_item[index];
		type_name = Py_TYPE(item)->tp_name;
		printf("Element %i: %s\n", index, type_name);
	}
}
