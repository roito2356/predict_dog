import os
from flask import (
     Flask, 
     request, 
     render_template)
from model import predict

#画像のアップロード先のディレクトリ
UPLOAD_FOLDER='./static/dog_image'

#FlaskでAPIを書くときのおまじない
app = Flask(__name__)

# トップページ
@app.route('/')
def index():
    return render_template('index.html')
  
# 受け取った画像をディレクトリに保存する
@app.route('/upload', methods=['GET', 'POST'])
def upload_user_files():
    if request.method == 'POST':
        upload_file = request.files['upload_file']
        img_path = os.path.join(UPLOAD_FOLDER,upload_file.filename)
        upload_file.save(img_path)
        # dog_imageからパスを取得
        result, score = predict(img_path)
        # 画像のパスとモデルの予測結果を送信
        return render_template('result.html', score=int(score*100),result=result, img_path=img_path)

# アプリをスクリプトから起動できるようにする
if __name__ == '__main__':
  app.run(debug=True)