create database management;
use management;
show tables;
desc prisoner;
desc crime;

CREATE TABLE `prisoner`(
 prisoner_id VARCHAR(45)  NOT NULL,
 Name VARCHAR(45) NOT NULL ,
 Address text NULL ,
 age int(16) NULL ,
 Jail_id int(20) NOT NULL,
  PRIMARY KEY (`prisoner_id`),
  FOREIGN KEY (Jail_id) references Jail(Jail_id));
  

CREATE TABLE login (
  `userid` VARCHAR(10) NOT NULL,
  `password` VARCHAR(20) NOT NULL,
  PRIMARY KEY (`userid`));

CREATE TABLE Crime(
   prisoner_id VARCHAR(45),
   crime_id int(16) NOT NULL,
   Type VARCHAR(40) NOT NULL,
   Crime_details longtext NULL,
   Location text NULL,
   PRIMARY KEY (crime_id),
   FOREIGN KEY (prisoner_id) references prisoner(prisoner_id));

CREATE TABLE Jail(
   Jail_id int(20) NOT NULL,
   Jail_name VARCHAR(40) NOT NULL,
   Jail_Address text NULL,
   Prisoners_count int(20) NULL,
   PRIMARY KEY (Jail_id));
drop table staff;
CREATE TABLE staff(
   Name VARCHAR(45) NOT NULL,
   Age int(10) NOT NULL,
   Gender varchar(30) NULL,
   Designation varchar(45) NOT NULL,
   staff_id int(16) NOT NULL,
   Jail_id int(16) NOT NULL,
   login_id VARCHAR(45) NOT NULL,
   password VARCHAR(45) NOT NULL,
   FOREIGN KEY (Jail_id) references Jail(Jail_id),
   PRIMARY KEY(Jail_id,staff_id));
   
CREATE TABLE Punishments(
   Type varchar(45) NOT NULL,
   Details longtext NULL,
   Duration VARCHAR(45) NULL,
   IPC_Rule text NOT NULL,
   prisoner_id VARCHAR(45) NOT NULL,
   FOREIGN KEY (prisoner_id) references prisoner(prisoner_id));
 
show tables;

insert into login values("root","Aniket@62");
SELECT * FROM login;
select * from prisoner;
insert into jail values(21,"California Jail","California",23);
insert into jail values(23,"Ohio Jail","Ohio",65);
insert into prisoner values(5,"John","LA",45,21);
insert into prisoner values(6,"Davies","LA",43,21);
insert into prisoner values(87,"Anthony","LA",43,23);
insert into prisoner values(43,"Mavi","California",59,23);
insert into staff values("James",27,"Male","Cleaner",1,21);
insert into crime values(2,55,"Murder","Shooting at School","Ohio");
insert into punishments values("Life Imprisonment","Under High Court","Till death","320A","2");
select * from prisoner;

# Natural Join
select jail.jail_id, jail.jail_name, prisoner.Name, prisoner.prisoner_id from jail natural join prisoner order by jail_id;

# Self join
select t1.prisoner_id, t1.Name, t2.age from prisoner as t1, prisoner as t2 where t1.prisoner_id=t2.prisoner_id and t1.age>45;

# Equi Join
select jail.jail_id, jail.jail_name, staff.jail_id,staff.name, staff.Designation from jail,staff where jail.jail_id=staff.jail_id;

select * from prisoner;
select Address, Count(prisoner_id) as count from prisoner group by Address;










select Address,max(age) as oldest from prisoner group by Address;
select Address,min(age) as youngest from prisoner group by Address;


select prisoner.Name,prisoner.age,prisoner.prisoner_id, Crime.prisoner_id,Crime.Location from prisoner,Crime where prisoner.prisoner_id=Crime.prisoner_id and prisoner.Name="Adam";


create view v88 as select prisoner.name,prisoner.age,prisoner.address,Crime.prisoner_id,Crime.Location from prisoner,Crime where prisoner.prisoner_id=Crime.Prisoner_id;
select * from v88;
create view v91 as select prisoner.prisoner_id,prisoner.name,prisoner.age,prisoner.address,punishments.Details,punishments.Duration,Crime.Location from prisoner,Crime,punishments where prisoner.prisoner_id=Crime.prisoner_id;
select * from v91 where name="Adam";
drop view v91;

insert into staff values("Dwayne",43,"Male","Sweeper",1,21,"Dwayne@43","Dwayne12345");


delete from prisoner where prisoner_id=4;
select * from prisoner;

create table deletion_backup(action varchar(40),old_id int(40),old_name varchar(60),date date);
create table insertion_details(action varchar(40),new_id int(40),name varchar(60),date date);

# Triggers
# deletion Backup
delimiter $$
drop trigger if exists deletion_backup $$
create trigger deletion_backup
before delete on prisoner for each row
begin
insert into deletion_backup set action='delete',old_id=old.Prisoner_id,old_name=old.Name,date=now();
end $$
delimiter ;

# Insertion Backup
delimiter $$
drop trigger if exists insertion_backup $$
create trigger insertion_backup
before insert on prisoner for each row
begin
insert into insertion_details set action='insert',new_id=New.Prisoner_id,name=New.name,date=now();
end $$
delimiter ;

select * from insertion_details;
select * from deletion_backup;
