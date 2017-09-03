from image_utils import ImageText
import subprocess

color = (229, 255, 204)
f = open("input/textData.txt", "r")
text = f.read()
#lines = text.split(". ")
lines = text.split("\n")

font = './Fonts/SFNSText.ttf'
f.close()

#write_text_box will split the text in many lines, based on box_width
#`place` can be 'left' (default), 'right', 'center' or 'justify'
#write_text_box will return (box_width, box_calculed_height) so you can
#know the size of the wrote text
i = 1;
for line in lines:
    img = ImageText("input/IMG_9263_b.JPG", background=(255, 255, 255, 100)) # 200 = alpha
    img.write_text_box((200, 159), line, box_width=2800, font_filename=font,
                           font_size=120, color=color)
    img.save('output/frame'+ str(i) + '.jpg')
    i += 1

cmd = ['ffmpeg', '-r', '0.25', '-start_number', '1', '-i', 'output/frame%01d.jpg', '-pix_fmt', 'yuv420p', '-vf', 'fps=24', #'framerate=fps=24:interp_start=0:interp_end=255:scene=100',
 'output/wealth_info.mp4']
print (cmd)
subprocess.Popen(cmd).wait()
