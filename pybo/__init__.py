from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm
#from lmsloader import Lmsloader

app = Flask(__name__)
app.config["SECRET_KEY"] = 'd2707fea9778e085491e2dbbc73ff30e'

@app.route('/', methods=["GET", "POST"])
def home():
    return render_template('layout.html')

@app.route('/register', methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        # 알람 카테고리에 따라 부트스트랩에서 다른 스타일을 적용 (success, danger)
        flash(f'{form.username.data} 님 동영상 다운로드.', 'success')
        userid = str(form.username.data)
        userpw = str(form.password.data)
        #Lmsloader(userid,userpw)
        return redirect(url_for('home'))
    return render_template('register.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)