# from scripts.label_image import get_img_category
from predictor import get_image_category
from flask import Flask, request
from werkzeug.utils import secure_filename
from PIL import Image

app = Flask(__name__)


UPLOAD_FOLDER = 'temp'
IMAGE_AUX = 'in.jpg'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'BMP'}


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/category', methods=["POST"])
def cat():
    if request.method == 'POST':
        if 'file' not in request.files:
            return 'No file part'
    file = request.files['file']
    if file.filename == '':
        return 'No selected file'
    if file:
        filename = secure_filename(file.filename)
        saved_image_path = "{}/{}".format(UPLOAD_FOLDER, filename)
        file.save(saved_image_path)
        img = Image.open(saved_image_path)
        img.save(IMAGE_AUX)
        category = get_image_category(IMAGE_AUX)
        return category
    return "None"


if __name__ == '__main__':
    app.run(port=5000, host='0.0.0.0')
