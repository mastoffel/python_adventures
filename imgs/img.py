from PIL import Image, ImageDraw, ImageFont

im = Image.open('imgs/out.jpg')
draw = ImageDraw.Draw(im)
fnt = ImageFont.truetype()

def generate_postcard(in_path, out_path, crop=None, width=None):
    """Create a Postcard With a Text Greeting

    Arguments:
        in_path {str} -- the file location for the input image.
        out_path {str} -- the desired location for the output image.
        crop {tuple} -- The crop rectangle, as a (left, upper, right, lower)-tuple. Default=None.
        width {int} -- The pixel width value. Default=None.
    Returns:
        str -- the file path to the output image.
    """
    im = Image.open(in_path)
    if crop is not None:
        im = im.crop(crop)
        
    if width is not None:
        ratio = width/float(im.size[0])
        height = int(ratio*float(im.size[1]))
        im = im.resize((width, height), Image.NEAREST)
    im.save(out_path)
    return out_path

if __name__=='__main__':
    print(generate_postcard('img.jpeg', 'out.jpg', (450, 900, 900, 1300), 200))

1+1