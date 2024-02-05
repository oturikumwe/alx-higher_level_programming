#include <Python.h>
#include <stdio.h>

/**
 * print_python_list - Prints information about Python lists
 * @p: A pointer to a PyObject list object
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t i, size;

	if (!PyList_Check(p))
	{
		printf("[ERROR] Invalid List Object\n");
		fflush(stdout);
		return;
	}

	size = PyList_Size(p);

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

	for (i = 0; i < size; i++)
	{
		printf("Element %ld: %s\n", i, Py_TYPE(PyList_GetItem(p, i))->tp_name);
		fflush(stdout);
	}
}

/**
 * print_python_bytes - Prints information about Python bytes objects
 * @p: A pointer to a PyObject bytes object
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t i, size;
	char *bytes_str;

	if (!PyBytes_Check(p))
	{
		printf("[ERROR] Invalid Bytes Object\n");
		fflush(stdout);
		return;
	}

	size = PyBytes_Size(p);
	bytes_str = PyBytes_AsString(p);

	printf("[.] bytes object info\n");
	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", bytes_str);

	printf("  first 10 bytes: ");
	for (i = 0; i < size && i < 10; i++)
		printf("%02x ", (unsigned char)bytes_str[i]);
	printf("\n");
	fflush(stdout);
}

/**
 * print_python_float - Prints information about Python float objects
 * @p: A pointer to a PyObject float object
 */
void print_python_float(PyObject *p)
{
	if (!PyFloat_Check(p))
	{
		printf("[ERROR] Invalid Float Object\n");
		fflush(stdout);
		return;
	}

	printf("[.] float object info\n");
	printf("  value: %f\n", ((PyFloatObject *)p)->ob_fval);
	fflush(stdout);
}
