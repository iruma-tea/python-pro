# 集合（set）を使って色を記録
all_colors = set()

with open('all-favorite-colors.txt') as favorite_colors_file:
    for line in favorite_colors_file:
        all_colors.add(line.strip())

print('琥珀' in all_colors)  # <3>
print('青' in all_colors)
