from PIL import Image, ImageFont, ImageDraw
import sys
sys.path.append('')
import logging
from wizard.vars import defaults

def convert_image(image_file, string):
	image = Image.open(image_file).convert('RGBA')
	im_width, im_height = image.size


	font_size = int((im_width*1)/100)

	font = ImageFont.truetype('cour.ttf', font_size)
	font_width, font_height = font.getsize(string)

	margin_percent = int((im_height*1)/100)

	text_position = ( margin_percent, im_height - (font_height + margin_percent) )

	wizard_icon = Image.open(defaults._wizard_ico_).convert('RGBA')
	wizard_icon.thumbnail((font_height, font_height), Image.ANTIALIAS)
	wizard_icon_width, wizard_icon_height = wizard_icon.size
	over_image_wizard = Image.new('RGBA', image.size, (255,255,255,0))
	over_image_wizard.paste(wizard_icon, (im_width-(margin_percent+wizard_icon_width), im_height-(margin_percent + wizard_icon_height)))

	bg_image = Image.new('RGBA', image.size, (92,92,92,255))

	over_image = Image.new('RGBA', image.size, (255,255,255,0))

	draw = ImageDraw.Draw(over_image)

	rectangle_xy = [im_width, im_height, 0, im_height-(margin_percent*2+font_height)]
	draw.rectangle(rectangle_xy, fill=(0,0,0,120), outline=None)
	draw.text(text_position, string, font = font, fill = "white")

	out = Image.alpha_composite(bg_image, image)
	out = Image.alpha_composite(out, over_image)
	out = Image.alpha_composite(out, over_image_wizard)

	out.save(image_file.replace('.jpg', '.png'))