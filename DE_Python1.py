def unique_names(nama01, nama02):
    nama01_set = set(nama01)
    nama02_set = set(nama02)
    return list(nama01_set.union(nama02_set))

nama01 = ["Ava", "Emma", "Olivia"]
nama02 = ["Olivia", "Sophia", "Emma"]
print(unique_names(nama01, nama02)) 
