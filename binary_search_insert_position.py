def binary_search_insert_position(data, target):
    left = 0
    right = len(data) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if data[mid] == target:
            return mid
        elif data[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
            
    return left

# Daftar data terurut
data = [2, 4, 6, 8, 10, 12, 14]

# Elemen Target
target = 11

# Mencari posisi untuk disisipkan
insert_position = binary_search_insert_position(data, target)

# Menampilkan hasil
print("Elemen", target, "dapat disisipkan pada indeks", insert_position, "untuk menjaga daftar tetap terurut")