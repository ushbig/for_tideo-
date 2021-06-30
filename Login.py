@app.route('/admin log in', methods=['POST','GET'])
def AdminLogin():
    form =AdminLoginForm(request.form)
    if request.method == 'POST' and form.validate():
        user = Admin.query.filter_by(email = form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            session['email'] = form.email.data
            flash(f'Welcome {form.email.data} You are logged in now ','primary')
            return redirect(request.args.get('next') or url_for('AdminPage'))

        else:
            flash('Wrong email or password', 'danger')
        


    return render_template('adminH/login.html', form=form , title='Admin Log in Page')
