from flask import Flask, url_for, render_template, request, redirect, session
import os
from datetime import datetime
import secrets

app = Flask(__name__)
app.secret_key = secrets.token_urlsafe(10)
@app.route('/logout', methods=['GET','POST'])
def logout():
    if session.get('logged_in'):
        logged_in_users= open('logged_in.txt','rb')
        logged_in_users_after_logout=logged_in_users.read().decode('utf-8').replace(session['username']+'\n','')
        logged_in_users= open('logged_in.txt','w')
        logged_in_users.write(logged_in_users_after_logout)
        session['username']=''
        session['logged_in']=False
        return redirect(url_for('index'))
    else:
        return redirect(url_for('index'))


@app.route('/add', methods=['GET','POST'])
def add():
    if session.get('logged_in'):
        if request.method == 'GET':
            return render_template('add.html')
        else:
            id=secrets.token_urlsafe(10)
            title = request.form['title']
            price = request.form['price']
            start = request.form['start']
            end = request.form['end']
            if title=='':
                return render_template('add.html',message='No valid title sent')
            if price=='':
                return render_template('add.html',message='No valid price sent')
            start_date=datetime.strptime(start, '%Y-%m-%d')
            end_date=datetime.strptime(end, '%Y-%m-%d')
            total=str((end_date-start_date).days)
            with open(session['username']+'.txt','a') as file:
                file.write(id+'----------'+title+'----------'+price+'----------'+str(start_date)+'----------'+str(end_date)+'----------'+total+'\n')
            return redirect(url_for('index',message='Added successfully'))

            
    else:
        return redirect(url_for('index'))
        


        
@app.route('/', methods=['GET','POST'])
def index():
    if session.get('logged_in'):
        if request.method == 'GET':
            entries=[]
            with open(session['username']+'.txt','rb') as file:
                for line in file.readlines():
                    entries.append(line.decode('utf-8').replace('\n','').replace('\r','').split('----------'))
            print(entries)
            return render_template('home.html',entries=entries)
    else:
        if request.method == 'GET':
            return render_template('login.html')
        else:
            u = request.form['name']
            file= open('logged_in.txt','rb')
            if u in file.read().decode('utf-8'):
                return render_template('login.html',message='Error , user already signed in')
            else:
                file.close()
                file= open('logged_in.txt','a')
                file.write(u+'\n')
                file.close()
                if os.path.isfile(u+'.txt'):
                    pass
                else:
                    with open(u+'.txt','w') as file:
                        file.close()
                session['logged_in']=True
                session['username']=u
                return redirect(url_for('index'))
                
                
#adding update route:
@app.route('/edit', methods=['GET', 'POST'])
def edit():
    if session.get('logged_in'):
        if request.method == 'GET':
            id = request.args.get('id')
            with open(session['username']+'.txt','rb') as file:
                for line in file.readlines():
                    entry = line.decode('utf-8').replace('\n','').replace('\r','').split('----------')
                    if entry[0] == id:
                        return render_template('edit.html', entry=entry)
            return redirect(url_for('index'))
        else:
            id = request.form['id']
            title = request.form['title']
            price = request.form['price']
            start = request.form['start']
            end = request.form['end']
            start_date=datetime.strptime(start, '%Y-%m-%d')
            end_date=datetime.strptime(end, '%Y-%m-%d')
            total=str((end_date-start_date) * 4)
            with open(session['username']+'.txt','r+') as file:
                lines = file.readlines()
                file.seek(0)
                for line in lines:
                    entry = line.replace('\n','').replace('\r','').split('----------')
                    if entry[0] == id:
                        file.write(f"{id}----------{title}----------{price}----------{start}----------{end}----------{total}\n")
                    else:
                        file.write(line)
                file.truncate()
            return redirect(url_for('index', message='Updated successfully'))
    else:
        return redirect(url_for('index')) 


# delete route:
@app.route('/delete', methods=['GET', 'POST'])
def delete():
    if session.get('logged_in'):
        if request.method == 'GET':
            id = request.args.get('id')
            with open(session['username']+'.txt', 'r') as file:
                lines = file.readlines()
            with open(session['username']+'.txt', 'w') as file:
                for line in lines:
                    entry = line.replace('\n', '').replace('\r', '').split('----------')
                    if entry[0] != id:
                        file.write(line)
            return redirect(url_for('index', message='Deleted successfully'))
        else:
            return redirect(url_for('index'))
    else:
        return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080,threaded=True)