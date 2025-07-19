# ==========???#clear ith bit

# x = 13
# n = 2

# x = ~(1 << n) & x  
# # print(x)


# ========toggel ith bit =======

x = 13
n = 2

x = 1 << n ^ x
print(x)


x = 1 << n ^ x  
print(x)