import mysql.connector
from doctorial import app, cnx
from flask import render_template, flash, redirect, url_for
from doctorial.forms import insertForm, updateForm, displayForm
from datetime import datetime


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')

@app.route("/Insert", methods=['GET','POST'])
def insert():
    form = insertForm()
    if form.validate_on_submit():
        ins_id = form.InstructorId.data
        fname = form.FName.data
        lname = form.LName.data
        startdate = datetime.strptime(form.StartDate.data, '%Y-%m-%d')
        degree = form.Degree.data
        rank = form.Rank.data
        ins_type = form.Type.data
        cid =form.CId.data
        sid = form.SId.data
        cur = cnx.cursor()
        try:
            cur.execute('INSERT INTO Instrcutor (ID, FName, LName, StartDate, Degree, Rank, Type) VALUES(%s,%s,%s,%s,%s,%s,%s)',
                        (ins_id,fname,lname, startdate, degree,rank,ins_type))
            #cur.execute("INSERT INTO COURSESTAUGHT VALUES(%s, %s)", (cid, iid) )
            #cur.execute("INSERT INTO COURSESTAUGHT VALUES(%s, %s)", (cid, iid) )
            #cur.execute("INSERT INTO PHDCOMMITTEE VALUES(%s, %s)", (sid, ins_id))

            #mysql.connection.commit()
            cnx.commit()
            cur.close()
            #cnx.close()
            #mysql.connection.commit()
            flash(f'New Instructor have been inserted successfully!', 'success')
            return redirect(url_for('home'))
        except mysql.connector.Error as err:
            flash(f'Fail to insert new instructor', 'danger')
            return render_template('error.html', result =err, title='Error')
    return render_template('insert.html', tilte = 'Insert', form = form)

@app.route("/Update", methods=['GET','POST'])
def update():
    form = updateForm()
    if form.validate_on_submit():
        try:
            studentId= form.StudentId.data
            fname = form.FName.data
            lname = form.LName.data
            #print(fname, lname, studentId)
            cur = cnx.cursor()
            cur.execute("UPDATE Instrcutor SET FName= %s, LName = %s WHERE ID =%s", (fname, lname, studentId) )
            cnx.commit()
            cur.close()
            flash(f'Student have been updated successfully!', 'success')
            return redirect(url_for('home'))
        except mysql.connector.Error as err:
            flash(f'Fail to update student', 'danger')
            return render_template('error.html', result =err, title='Error') 
    return render_template('update.html', tilte = 'Update', form = form)

@app.route("/Display", methods=['GET','POST'])
def display():
    form = displayForm()
    if form.validate_on_submit():
        try:
            studentId = form.StudentId.data
            cur = cnx.cursor()
            cur.execute("SELECT FName, LName FROM Instructor WHERE ID = %s", (studentId,))
            result = cur.fetchall()
            cnx.commit()
            cur.close()
            flash(f'Students have been displayed successfully!', 'success')
            return render_template('display.html', results = result)
        except mysql.connector.Error as err:
            flash(f'Fail to displaystudent', 'danger')
            return render_template('error.html', result =err, title='Error') 
    return render_template('display.html', title='Display', form = form)

@app.route("/Delete", methods=['GET','POST'])
def delete():
    cur = cnx.cursor()
    try:
        query = ("DELETE SELFSUPPORT, PHDSTUDENT"
                "FROM SELFSUPPORT INNER JOIN PHDSTUDENT ON PHDSTUDENT.StudentId = SELFSUPPORT.StudentId"
                "WHERE SELFSUPPORT.StudentId NOT IN (SELECT M.StudentID FROM MILESTONESPASSED M)")
        cur.execute(query)
        rv = cur.fetchall()
        cnx.commit()
        cur.close()
        flash(f'Students have been deleted', 'success')
    except mysql.connector.Error as err:
        flash(f'Fail to delete student', 'danger')
        return render_template('error.html', result =err, title='Error') 
    return render_template('home.html')

