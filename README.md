# Gray Scale Decomposer

The GrayScale decomposer converts images into grayscale and then decomposes
the image into 8 images. Each image respresents when a pixel is a 1 or 0 
at a particular bit value. For example the first image produced (0_bit_image)
contains an image where the pixels are either white or black depending on 
if at bit-0, there is a 1 or 0 value.

Bit-0 typically has the least information and is virtually random, however, 
bit-7 (MSB) tells you a lot of information typically. This is due to the 7 bit being
on if you have a intensity greater than 127. Whereas, the 0-bit or has to be even or odd.

## Code Example 
```python
from grayscale_decomposer import GrayScaleBitDecomposer

gs = GrayScaleBitDecomposer("test.jpg")
gs.produce_image(4, "4-bit-image.jpg") # produce just a 4 bit image example
gs.produce_all_8("folder-name") # creates all 8 images at that folder path
```

## Examples
We can grayscale decompose this image here

![image](https://github.com/user-attachments/assets/44356cbc-9ce5-4061-ba34-e733c313f595)

### bit-0 (LSB) image typically contains the least amount of information 

![image](https://github.com/user-attachments/assets/114f1304-44d8-4a3d-8a20-7825db46bdcf)

### bit-1 image

![image](https://github.com/user-attachments/assets/bee41f6d-e934-4875-8dcb-f20607fa43bb)

### bit-2 image

![image](https://github.com/user-attachments/assets/0ab7905a-adb3-46e4-b107-ffa3b4f6d313)

### bit-3 image

![image](https://github.com/user-attachments/assets/2e44bbf0-ef29-4757-97e0-970536483357)

### bit-4 image

![image](https://github.com/user-attachments/assets/45f9f929-194c-4664-bd52-bbc86160fc2b)

### bit-5 image

![image](https://github.com/user-attachments/assets/7f3daa51-0a28-439d-92e7-8146c9456a96)

### bit-6 image

![image](https://github.com/user-attachments/assets/6c5428e7-5885-4261-8803-513146570f59)

### bit-7 (MSB) image typically contains the most amount of information

![image](https://github.com/user-attachments/assets/0c928aa7-8b5d-4faa-911b-d88b2d396f40)

