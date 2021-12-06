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
#main menu asking for identification of the user’ identity

e=input("enter your choice:")
#selecting your choice from the menu

if e=="1":
    q=input("enter your username")
    a=input("enter your password")

    if q=="shruti13" or q=="hitaishi04": 
#when the username and password loaded in the server matches, the user gets logged in like any normal online system

        if a=="dps":
            print('''
            You are successfully logged in.
            ----------------------------------------
            Student Menu:
             1. View result
             2. View courses
             3. Change course
             4. Drop course''')
           #login menu for current students
             
           w=input("enter your choice:")

            if w=="1":
                print(''' Press 1 for term one result
                 Press 2 for preboard results
                
               The result will be in a pie chart form with all the subjects you applied for.''')
                jo=input("Which result do you want?")


#the results of the student for term one and term two shown separately in pyplot form for their analysis

                if jo=="1":
                    import matplotlib.pyplot as plt
       
                    subjects='english','maths','physics','chemistry','computer science'
                    sizes=[15.77,13.58,7.21,5.80,5.26]
                    cols=['c','m','r','b','y']
    
                        plt.pie(sizes,labels=subjects,colors=cols,startangle=90,shadow=True,explode=(0,0.1,0,0,0),autopct='%1.1f%%')
                    
                    plt.title('First Term Result',fontsize=20)
                    
                    plt.legend()
                    
                    plt.show() 

#using matplotlib module by importing it for pie chart description

                if jo=='2':
                    
                    import  matplotlib.pyplot as plt
                    
                    subjects='english','maths','physics','chemistry','computer science'      
                    #labels
                    sizes=[16.77,14.58,6.21,6.80,4.26] #sizes
                    cols=['c','m','r','b','y']
                    plt.pie(sizes,labels=subjects,colors=cols,startangle=90,shadow=True,
                    explode=(0,0.1,0,0,0),autopct='%1.1f%%')
                    
                    plt.title('First Term Result', fontsize=20)
                    
                    plt.legend()
 #labeling existing plots, providing legend to the graph
                    plt.show()
                    
                    

            elif w=="2":
                import mysql.connector           
                              db=mysql.connector.connect(host="localhost”,user=”root”,database=”jon”,
                password=”dps”)
                
               cursor=db.cursor()
#cursor establishes connection between python and mysql
                
                query=("select * from courses")
                cursor.execute(query)
                results=cursor.fetchall()
                
                for x in results:
                    print(x)
                cursor.close()

            elif w=="3":
                
                import mysql.connector

                name=input("enter your name")
                co=input("enter the course you want to change")
   
                new=input("enter your new course")
                        db=mysql.connector.connect(host="localhost",user="root",password="dps",database="school")
                 
                cursor=db.cursor()
                query=("update courses set subject=%s where subject=%s and student_name=%s;")
                
               cursor.execute(query,(new,co,name))
                db.commit() 
                
#commit function is used to save changes that we make to the           database
                
                cursor.execute('select * from courses;')
                results=cursor.fetchall()
                
               for x in results:
                       print(x)
               
               cursor.close()

           elif w=="4":
                
                import mysql.connector
               
                delet=input("enter the course you  want to drop")
                 wdb=mysql.connector.connect(host="localhost",user="root",password="dps" database="school")
                
                cursor=db.cursor()
                query=("delete from courses where subject='%s';")
                cursor.execute(query,(delet))
                 
                db.commit()
                cursor.execute('select * from courses;')
                results=cursor.fetchall()
                 
              
               for x in results:
                    print(x)
                
               cursor.close()

elif e=="2":

#for student who isn’t currently studying there, they have a registration facility which requires them to fill a form giving necessary details

       print("

Welcome to our institution. you just need to fill up the following details to register. Payments will be done in person at our institute.
")
    
    import mysql.connector
    a=8
#taking inputs from the user for new registration
    
    b=input("enter your name")
   
    c=input("enter your course")
 
    d=input("enter the teacher's name")
    e=input("enter the timings")
    wdb=mysql.connector.connect(host="localhost",user="root",password="  dps",database="school")
    cursor=db.cursor()
    
    query=("insert into courses values(%s,%s,%s,%s,%s)")
    data=a,b,c,d,e
    cursor.execute(query,data)
    
    db.commit()
    cursor.execute('select * from courses;')
    results=cursor.fetchall()
    
  for x in results:
        print(x)
    cursor.close()


elif e=="3":
    exit
