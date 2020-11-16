from flask import Flask,render_template,request,redirect,url_for

app = Flask(__name__,template_folder='template')


@app.route('/', methods=('GET','POST'))
def index():
    return render_template('index_page.html')


t=0

@app.route('/water', methods=('GET','POST'))

def water():
    if request.method == 'POST':
        water_level = int(request.form['level'])
        global t
        if water_level<5:
            #No water case
            signal1 = 0
            signal2 = 0
            t=0
        elif 5<=water_level<13:
            #Fill or Use Tank case
            signal1 = 0
            signal2 = 1
        elif water_level>=13:
            #Overflowing case
            signal1 = 1
            signal2 = 1
            t=1
        
        posts = {
            'signal1':signal1,
            'signal2':signal2,
            't':t
        }
        #print(posts,t)
        return render_template('index_page.html',posts=posts)
    return redirect(url_for('/'))