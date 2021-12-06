print('''
-----------------------------------
-----------------------------------
      ONLINE COURSE ENROLLMENT
-----------------------------------
-----------------------------------

     STUDENT OPTIONS:
     1. LOGIN
     2. REGISTER
     3. EXIT''')
e=input("enter your choice:")
if e=="1":
    q=input("enter your username")
    a=input("enter your password")
    if q=="shruti13" or q=="hitaishi04":
        if a=="dps":
            print('''
    You are successfully logged in.
    ----------------------------------------
        Student Menu:
          1. View result
          2. View courses
          3. Change course
          4. Drop course''')
            w=input("enter your choice:")
            if w=="2":
                import mysql.connector
                db=mysql.connector.connect(host="localhost",user="root",password="dps",database="school")
                cursor=db.cusor()
                query=("select * from courses")
                cursor.execute(query)
                db.commit()
                results=cursor.fetchall()
                for x in results:
                    print(x)
                cursor.close()
            elif w=="3":
                import mysql.connector
                name=("enter your name")
                co=input("enter the course you want to change")
                new=input("enter your new course")
                db=mysql.connector.connect(host="localhost",user="root",password="dps",database="school")
                cursor=db.cusor()
                query=("update table courses set course=new where course=co and student_name=name;")
                cursor.execute(query)
                db.commit()
                results=cursor.fetchall()
                for x in results:
                    print(x)
                cursor.close()
            elif w=="4":
                import mysql.connector
                delet=input("enter the course you  want to drop")
                db=mysql.connector.connect(host="localhost",user="root",password="dps",database="school")
                cursor=db.cusor()
                query=("delete from courses where course=delet;")
                cursor.execute(query)
                db.commit()
                results=cursor.fetchall()
                for x in results:
                    print(x)
                cursor.close()
elif e=="2":
    import mysql.connector
    a=8
    b=input("enter your name")
    c=input("enter your course")
    d=input("enter the teacher's name")
    e=input("enter the timings")
    db=mysql.connector.connect(host="localhost",user="root",password="dps",database="school")
    cursor=db.cusor()
    query=("insert into courses values(%s,%s,%s,%s,%s)")
    data=a,b,c,d,e
    cusor.execute(query,data)
    db.commit()
    results=cursor.fetchall()
    for x in results:
        print(x)
    cursor.close()
elif e=="3":
    exit

    
    
    
                       
                       
                       
                
                
                
                
            
    





 

    
        
