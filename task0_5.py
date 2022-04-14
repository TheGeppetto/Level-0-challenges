def area_of_triangle(length_a, length_b, length_c):
    semi_perimeter = 1/2 * (length_a + length_b + length_c)
    area_squared = (semi_perimeter * (semi_perimeter - length_a) * (semi_perimeter - length_b) * (semi_perimeter-length_c))
    return area_squared ** (1/2)

print(area_of_triangle(3, 4, 5))
