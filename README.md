# PNG and GIF file Resize from ~~url~~ previous file

## Before
![DEMO IMAGE](https://github.com/DreamSky1996/png_or_gif_resize/blob/master/img/before.gif)
## after
![DEMO IMAGE](https://github.com/DreamSky1996/png_or_gif_resize/blob/master/img/after.gif)

### ~~Command~~
```
~~resize.py [-h] url w h~~
```


### code
You can use this function in other file.
```
# resize_to can be either:
# a tuple of two numbers, describing width and height, respectively
# or a single int, describing the desired maximum image size in MB
#		- The program shrinks the image by 4x on each iteration until it fits in the MB limit 

resize_gif_and_png(original_filepath, new_filename, resize_to)
```
