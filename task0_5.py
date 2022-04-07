def area_of_triangle(length_A, length_B, length_C):
    semi_perimeter = 1/2 * (length_A + length_B + length_C)
    area_squared = (semi_perimeter * (semi_perimeter - length_A) * (semi_perimeter - length_B) * (semi_perimeter-length_C))
    return area_squared ** (1/2)

print(area_of_triangle(3, 4, 5))
