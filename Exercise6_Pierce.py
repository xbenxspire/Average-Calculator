'''
Created on Sep 27, 2023
@author: Benjamin Pierce
This program reads all the numbers store in the file numbers.txt, calculates their average, and writes the result to a file called numbers_average.txt
'''
def main():

    # Read numbers from numbers.txt file
    with open('numbers.txt', 'r') as infile:
        contents = infile.read().strip().split(',')

    # Convert string numbers to integers
    numbers = [int(number) for number in contents]

    # Calculate average
    average = sum(numbers)/len(numbers)

    # Write average in new file
    with open('numbers_average.txt', 'w') as output_file:
        output_file.write(f'Average: {average}')
            
if __name__ == "__main__":
    main()