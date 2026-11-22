def bubble_sort(n: list[int]) -> list[int]:
    """Сортирует список целых чисел методом пузырька"""
    if not isinstance(n, list):
        raise TypeError("n должен быть списком")
    if any(type(x) is not int for x in n):
        raise TypeError("элементы n должны быть целыми числами")
    copy_n = n.copy()
    length = len(n)
    for _ in range(length-1):
        swapped = False
        for i in range(length-1):
            if copy_n[i] > copy_n[i+1]:
                copy_n[i], copy_n[i+1] = copy_n[i+1], copy_n[i]
                swapped = True
        if not swapped:
            break
        length -= 1
    return copy_n



def merge(left: list[int], right: list[int]) -> list[int]:
    """Объединяет два отсортированных списка в один"""
    i = j = 0
    res  = []
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1
    res.extend(left[i:])
    res.extend(right[j:])
    return res


def merge_sort(n: list[int]) -> list[int]:
    """Сортирует список целых чисел методом слияния"""
    if not isinstance(n, list):
        raise TypeError("n должен быть списком")
    if any(type(x) is not int for x in n):
        raise TypeError("элементы n должны быть целыми числами")
    if len(n) <= 1:
        return n.copy()
    middle = len(n) // 2
    left = merge_sort(n[:middle])
    right = merge_sort(n[middle:])
    return merge(left, right)





