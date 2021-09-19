import numpy as np

# numpy - Numerical Python.
# NumPy is a Python library used for working with arrays.

# list1 = ['12','123213','1231231123']
# print(list1)


arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
print(arr)
print(np.__version__)
print(type(arr))

arr = np.array([[1, 2, 3], [4, 5, 6]])
print(arr)
print('---------------------------')
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
print(arr)

print('---------------------------')
a = np.array(42)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)

print('---------------------------')

arr = np.array([1, 2, 3, 4], ndmin=5)

print(arr)
print('number of dimensions :', arr.ndim)

print('--------------------------------')
arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

print('2nd element on 1st dim: ', arr[0, 1])

print('----------------------------')
arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

print('5th element on 2nd dim: ', arr[1, 4])
print('------------------------')

arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

print(arr[0, 1, 2])

print('----------------------')
arr = np.array([1, 2, 3, 4, 5, 6, 7])

print(arr[1:5:2])
print(arr[4:])
print(arr[:4])

print('----------------------')
arr = np.array([1, 2, 3, 4], dtype='i')

print(arr)
print(arr.dtype)

print('----------------------')

arr = np.array([1.1, 2.1, 3.1])

newarr = arr.astype('f')

print(newarr)
print(newarr.dtype)

print('--------------------------------')
arr = np.array([1, 2, 3, 4, 5])
x = arr.copy()
arr[0] = 42

print(arr)
print(x)

print('-------------------')
arr = np.array([1, 2, 3, 4, 5])
x = arr.view()
arr[0] = 42

print(arr)
print(x)

print('--------------------')
arr = np.array([1, 2, 3, 4, 5])
x = arr.view()
x[0] = 31

print(arr)
print(x)

print('-------------------')
arr = np.array([1, 2, 3, 4, 5])

x = arr.copy()
y = arr.view()

print(x.base)
print(y.base)

print('--------------------')
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

print(arr.shape)
print('----------------------------')
arr = np.array([1, 2, 3, 4], ndmin=5)

arr2 = np.array([1, 2, 3, 4], ndmin=2)

arr3 = np.array([[1, 2, 3, 4], [5, 6, 7, 8]], ndmin=2)

print(arr)
print('shape of array :', arr.shape)

print(arr2)
print('shape of array :', arr2.shape)

print(arr3)
print('shape of array :', arr3.shape)

print('------------------------')
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

newarr = arr.reshape(4, 3)

print(newarr)

print('-------------------------')
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

newarr = arr.reshape(2, 3, 2)

print(newarr)

print('-----------------')
arr = np.array([[1, 2, 3], [4, 5, 6]])

for x in arr:
    print(x)

print('------------------------')
arr = np.array([[1, 2, 3], [4, 5, 6]])

for x in arr:
    for y in x:
        print(y)

print('-----------------')
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

for x in arr:
    print(x)

print('-----------------------')
arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

for x in np.nditer(arr):
    print(x)

print('-----------------------')
arr1 = np.array([1, 2, 3])

arr2 = np.array([4, 5, 6])

arr = np.concatenate((arr1, arr2))

print(arr)

print('-----------------------')
arr1 = np.array([[1, 2], [3, 4]])

arr2 = np.array([[5, 6], [7, 8]])

arr = np.concatenate((arr1, arr2), axis=1)

print(arr)

print('-----------------------')
arr1 = np.array([1, 2, 3])

arr2 = np.array([4, 5, 6])

arr = np.stack((arr1, arr2), axis=1)

print(arr)

print('-----------------------')
arr1 = np.array([1, 2, 3])

arr2 = np.array([4, 5, 6])

arr = np.hstack((arr1, arr2))

print(arr)

print('-----------------------')
arr1 = np.array([1, 2, 3])

arr2 = np.array([4, 5, 6])

arr = np.vstack((arr1, arr2))

print(arr)

print('-----------------------')
arr1 = np.array([1, 2, 3])

arr2 = np.array([4, 5, 6])

arr = np.dstack((arr1, arr2))

print(arr)

print('-----------------------')
arr = np.array([1, 2, 3, 4, 5, 6])

newarr = np.array_split(arr, 3)

print(newarr)

print('-----------------------')
arr = np.array([1, 2, 3, 4, 5, 6])

newarr = np.array_split(arr, 4)

print(newarr)

print('-----------------------')
arr = np.array([1, 2, 3, 4, 5, 6])

newarr = np.array_split(arr, 3)

print(newarr[0])
print(newarr[1])
print(newarr[2])

print('-----------------------')
arr = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]])

newarr = np.array_split(arr, 3)

print(newarr)

print('-----------------------')
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])

newarr = np.array_split(arr, 3, axis=1)

print(newarr)

print('-----------------------')
arr = np.array([1, 2, 3, 4, 5, 4, 4])

x = np.where(arr == 4)

print(x)

print('-----------------------')
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])

x = np.where(arr % 2 == 0)

print(x)

print('-----------------------')
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])

x = np.where(arr % 2 == 1)

print(x)

print('-----------------------')
arr = np.array([6, 7, 8, 9])

x = np.searchsorted(arr, 7)

print(x)

print('-----------------------')
arr = np.array([6, 7, 8, 9])

x = np.searchsorted(arr, 7, side='right')

print(x)

print('-----------------------')
arr = np.array([1, 3, 5, 7])

x = np.searchsorted(arr, [2, 4, 6])

print(x)

print('-----------------------')

arr = np.array([3, 2, 0, 1])

print(np.sort(arr))

print('-----------------------')
arr = np.array(['banana', 'cherry', 'apple'])

print(np.sort(arr))

print('-----------------------')

arr = np.array([True, False, True])

print(np.sort(arr))

print('-----------------------')
arr = np.array([[3, 2, 4], [5, 0, 1]])

print(np.sort(arr))

print('-----------------------')
