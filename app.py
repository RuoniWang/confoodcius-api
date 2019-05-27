from flask import Flask
from flask import request
from watson_developer_cloud import VisualRecognitionV3
import base64



import json

app = Flask(__name__)

@app.route('/')
def main():
    return 'Welcome to Confoodcious\' API'

@app.route('/upload', methods=['POST'])
def upload():
    if request.method == 'POST':

        base64data = request.form['data']


        imgdata = base64.b64decode(base64data)
        filename = 'some_image.jpg'  # I assume you have a way of picking unique filenames
        with open(filename, 'wb') as f:
            f.write(imgdata)

        visual_recognition = VisualRecognitionV3(
            '2018-03-19',
            iam_apikey='PDH9x2MwWgNl0BJfIuDO5VuOfNaqNAxyawnvFNc_YFNr')

        with open('some_image.jpg', 'rb') as images_file:
            classes = visual_recognition.classify(
                images_file,
                threshold='0.6',
        	classifier_ids='DefaultCustomModel_267056391').get_result()

        return (json.dumps(classes))

    else:
        return("error")

if __name__ == '__main__':
    app.run(host='localhost', debug=True)