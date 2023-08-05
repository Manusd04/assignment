from flask import Flask, render_template, request
from flask_nav import Nav
from flask_nav.elements import Navbar,View,Text,Link

application = Flask(__name__, template_folder='templates',static_folder='static')

@application.route('/')
def index():
   return render_template('index.html')

@application.route('/process_image', methods=['POST'])
def process_image():
   if 'image_file' not in request.files:
      return "No file part in the request", 400
   image = request.files['image_file']
   if image.filename == '':
      return "No selected file", 400
   image.save('uploads/' + image.filename)
   return "Image uploaded and processed successfully!"

if __name__ == '__main__':
   application.run(debug=True)
