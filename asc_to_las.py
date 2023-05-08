# Install required libraries using:
# !pip install pyntcloud
# !pip install laspy==2.0.2

import pandas as pd
from pyntcloud import PyntCloud
import laspy
import numpy as np

def asc_to_las(input_file, output_file):
    # Read the input ASC file
    cloud = PyntCloud.from_file(input_file, sep=" ", header=0, names=["x", "y", "z"])
    
    # Create a new LAS data with the appropriate point format
    las_data = laspy.create(point_format=3)

    # Set the scale and offset for the LAS file
    las_data.header.scale = [0.01, 0.01, 0.01]
    las_data.header.offset = [min(cloud.points["x"]), min(cloud.points["y"]), min(cloud.points["z"])]

    # Create and assign the point data
    point_count = len(cloud.points)
    las_data.X = np.array(cloud.points["x"] / las_data.header.scale[0], dtype=int)
    las_data.Y = np.array(cloud.points["y"] / las_data.header.scale[1], dtype=int)
    las_data.Z = np.array(cloud.points["z"] / las_data.header.scale[2], dtype=int)

    # Write the LAS file to disk
    las_data.write(output_file)

if __name__ == "__main__":
    input_file = "your_input_file.asc"  # Replace with your ASC file name
    output_file = "your_output_file.las"  # Replace with your desired LAS file name
    asc_to_las(input_file, output_file)
    print(f"Successfully converted {input_file} to {output_file}")
