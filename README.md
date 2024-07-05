Kiah Johnson
CS536 - Homework Assignment One
Arbitrary Degree Bezier Curves

Bezier Curve Evaluator with an Inventor File Generator

Features
    This python script calculates a 3D arbitrary degree Bezier curve using control points from a text file and generates an inventor file containing the curve in polyline format.
    
    - Input: Control points from a text file
    - Output: An open inventor file with the Bezier curve

Environment
    - Language: Python 3
    - OS: Compatible with Windows, macOS, and Linux
    - Interpreter: Python interpreter

Usage
    Running the Script
        1. Clone or download the script with example inputs into local machine
        2. Open terminal with directory containing the script
        3. Run the script with the following structure:
            ./CG_hw1 -f filename -n n -r radius
        
        *You can replace 'filename', 'n', and 'radius' with desired filename, number of segments, and radius value*

    Arguments
        - '-f filename': The file containing the control points
        - '-n n': The number of segments for the curve (default is 20)
        - 'r radius': The radius of spheres for control points (default os 0.1)

    Output
        The script generates an open inventor file named 'out.iv' (unless specified) which is placed within the same directory as script.

Examples
    1. This command evaluates the Bezier curve using all of the default inputs, meaning the program will take points from the default text file 'cpts_in.txt', the number of segments will be 20, and the radius will be 0.1. It will also generate the iv file called 'out.iv':

        ./CG_hw1 -f filename -n n -r radius > out.iv

    2. This command evaluates the Bezier curve using the control points from 'my_points.txt', with 30 segments and a radius of 0.05. The output will be saved to a file called 'my_curve.iv':

        ./CG_hw1 -f my_points.txt -n 30 -r 0.05 > my_curve.iv