#include <Python.h>
/**
 * print_python_list_info - function that prints some basic info about Python lists
 * @p: python object
 * @Return: void
*/
void print_python_list_info(PyObject *p)
{
Py_ssize_t size = PyList_Size(p);
Py_ssize_t i;

printf("[*] Size of the Python List = %lu\n", size);
printf("[*] Allocated = %lu\n", ((PyListObject *)p)->allocated);
for (i = 0; i < Py_SIZE(p); i++)
printf("Element %ld: %s\n", i, Py_TYPE(PyList_GetItem(p, i))->tp_name);
}
