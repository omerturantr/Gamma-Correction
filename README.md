Image Gamma Correction Project

This project is a Python application that applies gamma correction to an image using OpenCV and Matplotlib, visualizing the results with different gamma values. It demonstrates how gamma correction can be used to adjust the brightness and contrast of an image.

Table of Contents





Installation



Usage



Features



Requirements



Contributing



License



Contact

Installation

To run the project on your local machine, follow these steps:





Clone the repository:

git clone https://github.com/username/gamma-correction-project.git



Navigate to the project directory:

cd gamma-correction-project



Create a virtual environment (optional, but recommended):

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate



Install the required dependencies:

pip install opencv-python numpy matplotlib



Add the image file:





Place an image file named fruits.jpg in the project directory, or update the image path in the code to use your own image.



Run the project:





If using PyCharm Community Edition 2025.1:





Open the project in PyCharm.



Run the main.py file (right-click and select "Run").



Alternatively, you can run it from the terminal:

python main.py

Usage

The project applies gamma correction to the fruits.jpg image and visualizes the results with different gamma values (0.3, 1, 3) side by side. Follow these steps to run the project:





Add your image file to the project directory (e.g., fruits.jpg).



Run the code:

python main.py

The result will display the original image alongside three images with different gamma corrections, visualized using Matplotlib.

Example Output:





Original Image: Unmodified version.



Gamma = 0.3: The image becomes darker, with deeper colors.



Gamma = 1: Original brightness and contrast (no change).



Gamma = 3: The image becomes brighter, with lighter colors.

Features





Gamma Correction: Adjusts brightness and contrast by applying different gamma values to the image.



Visualization: Displays the original and corrected images side by side using Matplotlib.



Flexibility: Works with any image file (update the file path in the code).

Requirements





Python 3.6 or higher



PyCharm Community Edition 2025.1 (optional, can use another IDE or terminal)



Required libraries:





opencv-python



numpy



matplotlib

To install the dependencies:

pip install -r requirements.txt

requirements.txt file:

opencv-python
numpy
matplotlib

Contributing

If you'd like to contribute to the project, please follow these steps:





Fork the repository.



Create a new branch: git checkout -b new-feature



Make your changes and commit them: git commit -m "Feature description"



Push your branch: git push origin new-feature



Create a Pull Request.

For more details, refer to the CONTRIBUTING.md file (optional to add).

License

This project is licensed under the MIT License. See the LICENSE file for more details.

Contact

For questions or feedback, reach out to:





Email: omerturanpersonal@gmail.com	



GitHub: omerturantr