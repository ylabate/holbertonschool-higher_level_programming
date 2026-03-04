create database if not exists hbtn_0d_usa;
use hbtn_0d_usa;
create table if not exists states (
	id int auto_increment primary key,
	name varchar(256) not null
	);
