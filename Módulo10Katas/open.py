""" def main():
    open("/path/to/mars.jpg")

if __name__ == '__main__':
    main() """


""" try:
    open('config.txt')
except FileNotFoundError:
    print("Couldn't find the config.txt file!") """

def water_left(astronauts, water_left, days_left):
    daily_usage = astronauts * 11
    total_usage = daily_usage * days_left
    total_water_left = water_left - total_usage
    return f"Total water left after {days_left} days is: {total_water_left} liters"