from flask import Flask, render_template, request
import requests
import shutil

app = Flask(__name__)


@app.route('/download', methods=['POST','GET'])
def index():
    if request.method == "POST":
        try:
            data = request.form
            image_url = data['image']
            file_name =image_url.split('/')[-1]
            response = requests.get(image_url,allow_redirects=True, stream=True)
            if response.status_code == 200:
                with open(file_name, 'wb') as f:
                    f.write(response.content)
                    return render_template("app.html", message="successfully downloaded image")
            else:
                return render_template("app.html", message="Failed to  download")
        except Exception as  e:
            pass
        return render_template("app.html")
    else:
        return render_template("app.html")


if __name__ == '__main__':
    app.run(debug=True)
