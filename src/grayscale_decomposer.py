from PIL import Image
import os

"""The GrayScale decomposer converts images into grayscale and then decomposes
the image into 8 images. Each image respresents when a pixel is a 1 or 0 
at a particular bit value. For example the first image produced (0_bit_image)
contains an image where the pixels are either white or black depending on 
if at bit-0, there is a 1 or 0 value.

Bit-0 typically has the least information and is virtually random, however, 
bit-7 (MSB) tells you a lot of information typically """
class GrayScaleBitDecomposer:

    def __init__(self, image_path: str) -> None:
        self.im = Image.open(image_path, "r",).convert("L")  # Grayscale Image
        self.width, self.height = self.im.size
        self.file_extension = os.path.splitext(image_path)[-1]

    def produce_image(self, bit_position: int, image_path: str = None) -> None:
        """
        Produces the decomposed image with a bit position taken into consideration

        :param bit_position: the bit position that you would like to decompose the image at
        :param image_path: the image name that you would like to see
        """
        assert 0 <= bit_position <= 7  # this should give a warning if you provide an bit values no in range (0 to 7)

        temp = Image.new("L", self.im.size)

        for row in range(self.width):
            for col in range(self.height):

                pixel_value = self.im.getpixel((row, col))

                binary_value = self._convert_int_8bit_binary(pixel_value)
                is_on = binary_value[7-bit_position]

                if is_on == '1':
                    temp.putpixel((row, col), 255)
                else:
                    temp.putpixel((row, col), 0)

        temp.save(
            f"Bit-{bit_position}{self.file_extension}" if not image_path else image_path)

    def produce_all_8_images(self, path_name: str) -> None:
        """
        Produces a folder with all 8 image decompositions.

        :param path_name: the path name that you would like to store the images at
        """
        os.mkdir(path_name)
        for bit_position in range(8):
            self.produce_image(bit_position, os.path.join(
                path_name, f"Bit-{bit_position}{self.file_extension}"))

    def _convert_int_8bit_binary(self, n: int) -> str:
        """
        Converts an integer value be 0 and 255 to an 8 bit string

        :param n: the number to be converted to 8 bit binary
        :throws AssertionError: if you provide an integer that is not in the range (0 to 255)
        :return: a string of the binary number in 8-bit form ie (00101101)
        """
        assert 0 <= n < 256
        binary = str(bin(n))[2:]
        final_res = ""
        for _ in range(8-len(binary)):
            final_res += "0"
        final_res += binary

        return final_res
