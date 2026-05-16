from flask import Flask, render_template

app = Flask(__name__)

# 1. الصفحة الرئيسية (الشاشة الترحيبية المؤقتة 4 ثوانٍ)
@app.route('/')
def index():
    return render_template('index.html')

# 2. الصفحة الثانية اللي ينتقل لها تلقائياً (Welcome)
@app.route('/welcome')
def welcome():
    return render_template('welcome.html')

# 3. صفحة التسجيل
@app.route('/register')
def register():
    return render_template('register.html')

# 4. صفحة البروفايل
@app.route('/profile')
def profile():
    return render_template('profile.html')

# صفحة مدخلات الصوت (المايك)
@app.route('/voice-input')
def voice_input():
    return render_template('voice-input.html') # تأكدي أن اسم ملف الـ HTML كذا بالملي

# صفحة الهوم الرئيسية (اللي فيها الأيجنت)
@app.route('/home')
def home():
    return render_template('home.html') # تأكدي أن اسم ملف الـ HTML كذا بالملي بحروف صغيرة
if __name__ == '__main__':
    app.run(debug=True, port=5000)