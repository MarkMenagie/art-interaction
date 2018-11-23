#!flask/bin/python
from flask import Flask, jsonify, Response, send_file
import flask
from PIL import Image
import evaluate

app = Flask(__name__)

#
# @app.route('/getimage', methods=['GET'])
# def upload():
#     try:
#         return Response(flask.request.files.get('/home/mmenagie/Documents/AICE/fast-style-transfer/examples/test/test1.jpeg', ''))
#     except Exception as err:
#         print('exception')




@app.route("/run_style_transfer", methods=["POST"])
def home():
    input_img = Image.open(flask.request.files['file'])
    input_img.save("input.jpg", "JPEG", quality=80, optimize=True, progressive=True)

    ## RUN STYLE TRANSFER CODE HERE
    # run evaluate.py from here with arguments like the following (in command line):
    # python evaluate.py --checkpoint /models/scream.ckpt
    # --in-path path_to_input_img
    # --out-path path_to_output_img

    #output_img = Image.open('/home/mmenagie/Documents/AICE/fast-style-transfer/results/test1.jpeg')

    return send_file(path_to_output_img, mimetype='image/jpeg')




if __name__ == '__main__':
    app.run(debug=True)