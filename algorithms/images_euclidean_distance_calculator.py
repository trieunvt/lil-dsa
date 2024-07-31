# author:   trieunvt
# file:     images_euclidean_distance_calculator.py
# date:     31 Jul 2024
# version:  v1.0.0
# brief:    Images Euclidean Distance Calculator.

import sys
from PIL import Image

# Calculate image histograms
def calculate_histogram(image_path):
    image = Image.open(image_path).convert("L")
    # image.show()
    return image.histogram()

# Calculate the images Euclidean distance
def calculate_euclidean_distance(histogram1, histogram2):
    square_distance = i = 0
    while i < len(histogram1) and i < len(histogram2):
        square_distance += (histogram1[i]-histogram2[i])**2
        i += 1

    return square_distance**(1 / 2)

# The main program
def main():
    # Check for the correct number of arguments
    if len(sys.argv) != 3 and len(sys.argv) != 4:
        print("USAGE: python images_euclidean_distance_calculator.py [image1_path] [image2_path]")
        print("       python images_euclidean_distance_calculator.py [image1_path] [image2_path] [image3_path]")
        return

    print("IMAGES EUCLIDEAN DISTANCE CALCULATOR", end="\n\n")

    if len(sys.argv) == 3:
        # Calculate image histograms
        histogram1 = calculate_histogram(sys.argv[1])
        histogram2 = calculate_histogram(sys.argv[2])

        # Calculate the images Euclidean distance
        print("Images Euclidean Distance:",
              calculate_euclidean_distance(histogram1, histogram2))

    if len(sys.argv) == 4:
        # Calculate image histograms
        histogram1 = calculate_histogram(sys.argv[1])
        histogram2 = calculate_histogram(sys.argv[2])
        histogram3 = calculate_histogram(sys.argv[3])

        # Calculate the images Euclidean distance
        distance12 = calculate_euclidean_distance(histogram1, histogram2)
        distance13 = calculate_euclidean_distance(histogram1, histogram3)

        if distance12 > distance13:
            print("Comparison: Image3 is more similar to Image1 than Image2")
        elif distance12 < distance13:
            print("Comparison: Image2 is more similar to Image1 than Image3")
        else:
            print("Comparison: Image1 is similar to Image2 as same as Image3")

if __name__ == "__main__":
    main()
