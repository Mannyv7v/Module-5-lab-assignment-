#Emmanuel Velazquez
#2/15/24

#Problem 1: This program prints "Hello, world" 100 times
for i in range(100):
    print("Hello, World!")

#Assume you have a list of numbers 12, 10, 32, 3, 66, 17, 42, 99, 20
#Problem 2a: Write a loop that prints each of the numbers on a new line.
for number in (12,10,32,3,66,17,42,99,20):
    print(number)

#problem 2b: Write a loop that prints each number and its square on a new line
for number in(12,10,32,3,66,17,42,99,20):
    square = number ** 2
    print(number, "square is", square)

#problem 3: program draws polygon based on user input and then fills it
import turtle
def draw_regular_polygon(sides, length, line_color, fill_color):
    # Create turtle object
    polygon_turtle = turtle.Turtle()

    # Set line color
    polygon_turtle.pencolor(line_color)

    # Set fill color
    polygon_turtle.fillcolor(fill_color)

    # Draw and fill the regular polygon
    polygon_turtle.begin_fill()
    for _ in range(sides):
        polygon_turtle.forward(length)
        polygon_turtle.left(360 / sides)
    polygon_turtle.end_fill()

    # Close the turtle graphics window when clicked
    turtle.exitonclick()

def main():
    # Get user input
    sides = int(input("Enter the number of sides: "))
    length = int(input("Enter the length of the side: "))
    line_color = input("Enter the line color: ")
    fill_color = input("Enter the fill color: ")

    # Draw the regular polygon
    draw_regular_polygon(sides, length, line_color, fill_color)

if __name__ == "__main__":
    main()

#Problem 4: Prints a range between 1 and 50. Identifies if a number is divisible by 3, 5 or both.
for number in range(1,51):
    if number % 3 == 0 and number % 5 == 0:
        print("Number is divisible by both")
    elif number % 3 == 0:
        print("Number only divisible by 3")
    elif number % 5 == 0:
        print("Number only divisible by 5")
    else:
        print(number)

#Problem 5: this program draws a pentagon
import turtle

pentagon_turtle = turtle.Turtle()
window = turtle.Screen()
for i in range(5):
    pentagon_turtle.forward(50)
    pentagon_turtle.left(72)
turtle.exitonclick()
