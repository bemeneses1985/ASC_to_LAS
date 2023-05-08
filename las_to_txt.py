# Install required libraries using:
# !pip uninstall laspy
# !pip install laspy==1.5.1
# numpy

import laspy
import numpy as np

def las_to_txt(las_file, txt_file):
    # Open the LAS file in read-only mode
    inFile = laspy.file.File(las_file, mode='r')

    # Read the x, y, and z data from the LAS file
    x = inFile.x
    y = inFile.y
    z = inFile.z

    # Combine the x, y, and z data into a single array
    data = np.column_stack((x, y, z))

    # Write the data to the TXT file
    np.savetxt(txt_file, data, delimiter=' ', fmt='%.6f')

if __name__ == "__main__":
    # Replace these with your file names
    las_file = 'your_output_file.las'
    txt_file = 'example.txt'

    # Call the function to convert the LAS file to TXT
    las_to_txt(las_file, txt_file)

    # Print a success message
    print(f"Successfully converted {las_file} to {txt_file}")
