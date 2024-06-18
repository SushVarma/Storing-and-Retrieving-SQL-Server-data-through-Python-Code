#connection
import pyodbc 
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=DESKTOP-QFNB5IV;'
                      'Database=Devices;'
                      'Trusted_Connection=yes;')
cursor = conn.cursor()

creating  a new table
cursor.execute('''create table Dev (Dev_Id INT PRIMARY KEY IDENTITY(1,1),
                                                                 Dev_Name VARCHAR (50) NOT NULL,
                                                                 Dev_type  VARCHAR (50) NOT NULL,
                                                                 Dev_prob INT)''')
cursor.execute('''create table Own(Owner_Id INT PRIMARY KEY IDENTITY( 21,1),
                                                                   Owner_Name VARCHAR (50) NOT NULL,
                                                                   Owner_branch VARCHAR (50) NOT NULL,
                                                                   Dev_id INT foreign key references  Dev(Dev_ID),
                                                                   Admin_id INT foreign key references  Admin(Admin_ID),
                                                                   Issue_date   DATE  NOT NULL)''')
cursor.execute('''create table  Admin (Admin_Id INT PRIMARY KEY IDENTITY( 31,1),
                                                                       Admin_name VARCHAR (50) NOT NULL,
                                                                       Admin_branch VARCHAR (50) NOT NULL,
                                                                       Admin_pass  VARCHAR (50) NOT NULL)''')
cursor.execute('''create table home (User_Id INT PRIMARY KEY IDENTITY( 21,1),
                                                                   User_Name VARCHAR (50) NOT NULL,
                                                                   User_branch VARCHAR (50) NOT NULL,
                                                                   Dev_id INT foreign key references  Dev(Dev_ID),
                                                                   Admin_id INT foreign key references  Admin(Admin_ID),
                                                                   Issue_date   DATE  NOT NULL)''')

cursor.execute('''create table  Rental(renown_Id INT PRIMARY KEY IDENTITY( 21,1),
                                                                   renown_Name VARCHAR (50) NOT NULL,
                                                                   renown_branch VARCHAR (50) NOT NULL,
                                                                   Dev_id INT foreign key references  Dev(Dev_ID),
                                                                   Admin_id INT foreign key references  Admin(Admin_ID),
                                                                   Issue_date   DATE  NOT NULL,
                                                                 Return_date   DATE  NOT NULL)''')
cursor.execute('''create table Supp(Supp_Id INT PRIMARY KEY IDENTITY( 21,1),
                                                                   Supp_Name VARCHAR (50) NOT NULL,
                                                                   Supp_branch VARCHAR (50) NOT NULL,
                                                                   Dev_id INT foreign key references  Dev(Dev_ID),
                                                                   Admin_id INT foreign key references  Admin(Admin_ID),
                                                                   purch_date   DATE  NOT NULL)''')

conn.commit()
conn.close()

inserting rows 
cursor.execute(''' insert into  Dev (Dev_Name,Dev_type,Dev_prob) values ('lenovo','monitor',1),
                                                                                                                                       ('dell','mouse',0),
                                                                                                                                       ('Hp','keyboard USB',0),
                                                                                                                                       ('apple','monitor 3screen',1),
                                                                                                                                       ('lenovo','CPU',3),
                                                                                                                                       ('lenovo','monitor',1),
                                                                                                                                       ('dell','mouse',0),
                                                                                                                                       ('Hp','keyboard USB',0),
                                                                                                                                       ('apple','monitor 2screen',1),
                                                                                                                                       ('lenovo','CPU',3)''')
cursor.execute('select * from Dev')
print("\n\nContent of  Dev Table")
for row in cursor:
    print(row)
cursor.execute(''' insert into  Own(Owner_Name,Owner_branch,Dev_id,Issue_date) values ('Sonam','Powai',1,  '2022-12-02'),
                                                                                                                                                                                                ('Sonika','Powai',3,' 2022-04-05'),
                                                                                                                                                                                                ('Seokjin','Chennai',2,'2022-09-02'),
                                                                                                                                                                                                ('Suga','Pune',4, '2022-09-19'),
                                                                                                                                                                                                ('Hoseok','Noida',5,    ' 2022-01-25')''')
cursor.execute('select * from Own')
print("\n\nContent of Own Table")
for row in cursor :
    print(row)
cursor.execute(''' insert into  Admin (Admin_name,Admin_branch,Admin_pass) values ('jungkook','powai',10214),
                                                                                                                                                                    ('taehyung','Bangalore',10215),
                                                                                                                                                                    ('kento yamada','Noida',10216),
                                                                                                                                                                    ('tanjiro ','Pune',10217),
                                                                                                                                                                    ('gojo satoru','Chennai',10218)''')
cursor.execute('select * from Admin')
print("\n\nContent of  Admin Table")
for row in cursor:
    print(row)
conn.commit()
conn.close()

cursor.execute(''' insert into  Home(User_name,User_branch,Dev_id,Issue_date) values ('junghoseok','powai',6,'2022-04-05'),
                                                                                                                                                                    ('taehyang','Bangalore',7,'2022-04-05'),
                                                                                                                                                                    ('kentaro yamada','Noida',8,'2022-04-05'),
                                                                                                                                                                    ('tanjiro yamazaki ','Pune',9,'2022-04-05'),
                                                                                                                                                                    ('Sasuke nichirin ','Chennai',10,'2022-04-05')''')
cursor.execute('select * from Home')
print("\n\nContent of  home Table")
for row in cursor:
    print(row)
                                                            
cursor.execute(''' insert into  Rental(  renown_Name ,renown_branch, Dev_id ,  Admin_id ,  Issue_date  ,Return_date)
                                                                                                                                                                values ('jungkook','powai',6,31,'2022-04-05',' 2022-04-05'),
                                                                                                                                                                                  ('taehyung','Bangalore',7,31,'2022-04-05',' 2022-04-05'),
                                                                                                                                                                    ('kento yamada','Noida',8,32,'2022-04-05',' 2022-04-05')''')
                                                                                                                                
                                                                                                                     
cursor.execute('select * from  Rental')
print("\n\nContent of  Rental Table")
for row in cursor:
    print(row)
conn.commit()
conn.close()
                                                                  
cursor.execute(''' insert into  Supp(Supp_Name ,Supp_branch , Dev_id , Admin_id ,  purch_date) values ('june','powai',9,34,' 2022-04-05'),
                                                                                                                                                                    ('taehyung','Bangalore',10,35,' 2022-04-05')''')
                                                                                                                                                                 
                                                                                                                                                                    
cursor.execute('select * from Supp')
print("\n\nContent of  Supp Table")
for row in cursor:
    print(row)
conn.commit()
conn.close()




update
cursor.execute(''' update Dev SET Dev_Name = 'Mac' WHERE Dev_Id= 2  ''')
cursor.execute('select * from Dev')
print("\n\nContent of Dev Table")
for row in cursor:
    print(row)
cursor.execute(''' update Admin SET Admin_branch = 'Mumbai'  WHERE  Admin_name= 'tanjiro'  ''')
cursor.execute('select * from Admin')
print("\n\nContent of AdminTable")
for row in cursor:
    print(row)
cursor.execute(''' update Own SET  Admin_id = 32  WHERE   Owner_ID= 21  ''')
cursor.execute('select * from Own')
print("\n\nContent of  Own Table")
for row in cursor:
    print(row)


#delete
cursor.execute('''  delete from Supp WHERE  Supp_id= 22  ''')
cursor.execute('select * from  Supp')
print("\n\nContent of  Supp Table")
for row in cursor:
    print(row)
cursor.execute('''  delete from  Own WHERE  Owner_name= 'Suga'  ''')
cursor.execute('select * from  Own')
print("\n\nContent of  Own Table")
for row in cursor:
    print(row)

conn.commit()
conn.close()

