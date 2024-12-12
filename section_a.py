def circle_area(radius):
    pi = 3.14  
    area = pi * (radius ** 2) 
    return area

# Testing the function with a radius of 4
radius = 4
result = circle_area(radius)
print("The area of the circle with radius", radius, "is:", result)




# List of integers
numbers = [4, 7, 2, 9, 12, 15]

odd_sum = 0

for num in numbers:
    if num % 2 != 0:  # Checks if the number is odd
        odd_sum += num  

print("The sum of all odd numbers is:", odd_sum)




def calculate_operations(num1, num2):
    # Calculate sum, difference, product, and quotient
    sum_result = num1 + num2
    difference_result = num1 - num2
    product_result = num1 * num2
    quotient_result = num1 / num2 if num2 != 0 else "undefined" 

    # Returning result as a tuple
    return sum_result, difference_result, product_result, quotient_result

num1 = 10
num2 = 5
sum_result, difference_result, product_result, quotient_result = calculate_operations(num1, num2)

print(f"Sum: {sum_result}")
print(f"Difference: {difference_result}")
print(f"Product: {product_result}")
print(f"Quotient: {quotient_result}")



# the dictionary
student_info = {'name': 'Alice', 'age': 20, 'grade': 'A'}

# Updating the value of 'age' to 26
student_info['age'] = 26

# Adding a new key-value pair 'city': 'Kampala'
student_info['city'] = 'Kampala'

print(student_info)
