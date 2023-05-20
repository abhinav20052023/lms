import streamlit as st
import mysql.connector
import pandas as pd
import datetime
st.set_page_config(page_title="Library Management System",page_icon="https://www.pngitem.com/pimgs/m/32-327951_events-learning-circle-icon-library-management-system-icon.png")
st.title("LIBRARY MANAGEMENT SYSTEM")
choice=st.sidebar.selectbox("My Menu",("HOME","USER","ADMIN"))
if(choice=="HOME"):
    st.image("https://www.skoolbeep.com/blog/wp-content/uploads/2020/12/WHAT-IS-THE-PURPOSE-OF-A-LIBRARY-MANAGEMENT-SYSTEM-min.png")
    st.write("1.It is a data management application which can add, delete, update the data of books,users,admin,issue.")
    st.write("2.This Application provides features such as Login Form, View all Books, Add new book , delete old book , add new account , issue book , etc.")
    st.write("3.It uses MySQL as a DataBase Management System.")
    st.write("4.It is a web application which can accessible over a LAN.")
elif(choice=="USER"):
    if 'login' not in st.session_state:
        st.session_state['login']=False   
    uid=st.text_input("Enter Your User ID")
    pwd=st.text_input("Enter User Password")
    btn=st.button("Login")
    if btn:
        mydb=mysql.connector.connect(host="localhost",user="root",password="12345678",database="lms")
        c=mydb.cursor()
        c.execute("select * from users")
        for row in c:
            if(row[0]==uid and row[1]==pwd):
                st.session_state['login']=True
        if not st.session_state['login']:
            st.header("Incorrect ID and Password")
    if st.session_state['login']:
        st.header("Login Successfull")
        choice2=st.selectbox("Select the Feature",("None","View All Books","Issue a Book"))
        if(choice2=="View All Books"):
            mydb=mysql.connector.connect(host="localhost",user="root",password="12345678",database="lms")
            c=mydb.cursor()
            c.execute("select * from books")
            l=[]
            for row in c:
                l.append(row)
            df=pd.DataFrame(data=l,columns=c.column_names)
            st.dataframe(df)
        elif(choice2=="Issue a Book"):
            bid=st.text_input("Enter Book ID")
            usid=st.text_input("Enter your User ID")
            btn2=st.button("Issue Book")
            if btn2:
                mydb=mysql.connector.connect(host="localhost",user="root",password="12345678",database="lms")
                c=mydb.cursor()
                dt=str(datetime.datetime.now())
                c.execute("insert into issue values(%s,%s,%s)",(dt,bid,usid))
                mydb.commit()
                st.write("Book Issued Sucessfully at issueid :",dt)

elif(choice=="ADMIN"):
    if 'alogin' not in st.session_state:
        st.session_state['alogin']=False    
    aid=st.text_input("Enter Your Admin ID")
    pwd=st.text_input("Enter Admin Password")
    btn=st.button("Login")
    if btn:
        mydb=mysql.connector.connect(host="localhost",user="root",password="12345678",database="lms")
        c=mydb.cursor()
        c.execute("select * from admins")
        for row in c:
            if(row[0]==aid and row[1]==pwd):
                st.session_state['alogin']=True
        if not st.session_state['alogin']:
            st.header("Incorrect ID and Password")
    if st.session_state['alogin']:
        st.header("Login Successfull")
        choice2=st.selectbox("Select the Feature",("None","View Issue Books","Add New Book","Delete Book"))
        if(choice2=="View Issue Books"):
            mydb=mysql.connector.connect(host="localhost",user="root",password="12345678",database="lms")
            c=mydb.cursor()
            c.execute("select * from issue")
            l=[]
            for row in c:
                l.append(row)
            df=pd.DataFrame(data=l,columns=c.column_names)
            st.dataframe(df)
        elif(choice2=="Add New Book"):
            bid=st.text_input("Enter Book ID")
            bname=st.text_input("Enter Book Name")
            aname=st.text_input("Enter Author Name")
            btn2=st.button("Add Book")
            if btn2:
                mydb=mysql.connector.connect(host="localhost",user="root",password="12345678",database="lms")
                c=mydb.cursor()
                c.execute("insert into books values(%s,%s,%s)",(bid,bname,aname))
                mydb.commit()
                st.write("Book Added Sucessfully")
        elif(choice2=="Delete Book"):
            bid=st.text_input("Enter Book ID")            
            btn2=st.button("Delete Book")
            if btn2:
                mydb=mysql.connector.connect(host="localhost",user="root",password="12345678",database="lms")
                c=mydb.cursor()
                c.execute("delete from books where book_id=%s",(bid,))
                mydb.commit()
                st.write("Book Deleted Sucessfully")








        

