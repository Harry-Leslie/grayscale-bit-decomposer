from grayscale_decomposer import GrayScaleBitDecomposer

gs = GrayScaleBitDecomposer("test.jpg")
gs.produce_image(4, "4-bit-image.jpg") # produce just a 4 bit image example
gs.produce_all_8("folder-name") # creates all 8 images at that folder path
