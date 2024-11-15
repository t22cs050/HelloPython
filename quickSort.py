def quick_sort(data):
    if len(data) <= 1:
        return data
    pivot = data.pop(0)
    left = [i for i in data if i <= pivot]
    right = [i for i in data if i > pivot]

    left = quick_sort(left)
    right = quick_sort(right)

    return left + [pivot] + right


d = [3, 1, 4, 5, 2]

print(quick_sort(d))
