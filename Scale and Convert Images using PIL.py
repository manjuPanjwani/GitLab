Download the file
Your design contractor sent you the zipped file through his team drive. Download the file from the drive using the following CURL request:

curl -c ./cookie -s -L "https://drive.google.com/uc?export=download&id=$11hg55-dKdHN63yJP20dMLAgPJ5oiTOHF" > /dev/null | curl -Lb ./cookie "https://drive.google.com/uc?export=download&confirm=`awk '/download/ {print $NF}' ./cookie`&id=11hg55-dKdHN63yJP20dMLAgPJ5oiTOHF" -o images.zip && sudo rm -rf cookie
Copied!
Output:

5fe50f874fc9b1f9.png

List files using the command:

ls
Copied!
Output:

bfeaf6a7d282dcf5.png

Unzip the file using the following command:

unzip images.zip
Copied!
To list images from the images folder use the following command:

ls ~/images
Copied!
The images received are in the wrong format:

.tiff format
Image resolution 192x192 pixel (too large)
Rotated 90° anti-clockwise
The images required for the launch should be in this format:

.jpeg format

Image resolution 128x128 pixel

Should be straight

Install Pillow
We should change the format and size of these pictures, and rotate them by 90° clockwise. To do this, we'll use Python Imaging Library (PIL). Install pillow library using the following command:

pip3 install pillow
Copied!
Python Imaging Library (known as Pillow in newer versions) is a library in Python that adds support for opening, manipulating, and saving lots of different image file formats.

Pillow offers several standard procedures for image manipulation. These include:

Per-pixel manipulations
Masking and transparency handling
Image filtering, such as blurring, contouring, smoothing, or edge finding
Image enhancing, like sharpening and adjusting brightness, contrast or color
Adding text to images (and much more!)
Click Check my progress to verify the objective.
Install Pillow

Write a Python script
This is the challenge section of the lab where you'll write a script that uses PIL to perform the following operations:

Iterate through each file in the folder
For each file:
Rotate the image 90° clockwise
Resize the image from 192x192 to 128x128
Save the image to a new folder in .jpeg format
Use a nano editor for this purpose. You can name the file however you'd like. And make sure to save the updated images in the folder: /opt/icons/

You'll use lots of methods from PIL to complete this exercise. You can refer to Pillow for detailed explanations and have a look at the tutorials to help you build the script and complete the task.

To save the file after editing, press Ctrl-O, Enter, and Ctrl-x.

Once your script is ready, grant executable permission to the script file.

chmod +x <script_name>.py
Copied!
Replace <script_name> with the name of your script.

Now, run the file.

./<script_name>.py
Copied!
Replace <script_name> with the name of your script.

On a successful run, this should produce images in the right format within the directory: /opt/icons/

To view the updated images use the following command:

ls /opt/icons
Copied!
Output:

ea9afeff1183c231.png

To check image properties, use the Python interpreter:

python3
Copied!
Once the interactive shell opens, import the Image module from PIL:

from PIL import Image
Copied!
Open any image from the folder, or you can use the following image:

img = Image.open("/opt/icons/ic_edit_location_black_48dp")
Copied!
To view the format and size of the image:

img.format, img.size
Copied!
Output:

b3a2965a9c783ec9.png

Type exit() to exit from the Python interpreter.
