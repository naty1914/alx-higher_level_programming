#include <Python.h>

/**
 * print_python_list_info - Prints some basic info about Python lists
 * @p: Pointer
 * Return: Void
 */


void print_python_list_info(PyObject *p)
{

PyObject *list_item;
Py_ssize_t list_size, list_allocated, x;
const char *type_name;


list_allocated = ((PyListObject *)p)->allocated;
list_size = PyList_Size(p);


printf("[*] Size of the Python List = %ld\n", list_size);
printf("[*] Allocated = %ld\n", list_allocated);

for (x = 0; x < list_size; ++x)
{
list_item = PyList_GetItem(p, x);
type_name = Py_TYPE(list_item)->tp_name;
printf("Element %ld: %s\n", x, type_name);
}


}
