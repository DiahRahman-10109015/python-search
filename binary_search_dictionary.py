def binary_search_dictionary(word, dictionary):
    left = 0
    right = len(dictionary) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if dictionary[mid][0] == word:
            return dictionary[mid][1]
        elif dictionary[mid][0] < word:
            left = mid + 1
        else:
            right = mid - 1
            
    return "Definisi tidak ditemukan."

# Kamus yang sudah diurutkan berdasarkan kata kunci
dictionary = [
    ["Apple", "Buah Apel"],
    ["Banana", "Buah Pisang"],
    ["Cat", "Kucing"],
    ["Duck", "Bebek"],
    ["Elephant", "Gajah"]
]

# Kata yang ingin dicari artinya dalam bahasa indonesia
word = "Elephant"

# Mencari arti kata
meaning = binary_search_dictionary(word, dictionary)

# Menampilkan arti kata
print("Definisi dari kata", word, "adalah", meaning)