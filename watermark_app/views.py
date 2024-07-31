from django.shortcuts import render, redirect
from watermark_app.models import ImageModel

import uuid
from PIL import Image, ImageDraw, ImageFont

# Create your views here.


def water_apply(image, text):
    input_path = f"media_root/{image}"
    image = Image.open(input_path)

    width, height = image.size

    draw = ImageDraw.Draw(image)

    font = ImageFont.truetype('static/font/FontsFree-Net-arial-bold.ttf', 36)
    textwidth, textheight = draw.textsize(f"©{text}", font)

    margin = 50
    x = width - textwidth - margin
    y = height - textheight - margin

    draw.text((x, y), f"©{text}", font=font, fill="red")
    output_path = f"watermark_images/{uuid.uuid4()}.jpg"
    image.save(f"media_root/{output_path}")

    # image.show()
    return f"media/{output_path}"


def index_view(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        image = request.FILES['image']
        image = ImageModel.objects.create(title=title, image=image)

        # print('image path:', image.image)
        output_path = water_apply(image.image, title)

        return redirect(f"http://127.0.0.1:8000/{output_path}")

    return render(request, 'watermark_app/index.html')




