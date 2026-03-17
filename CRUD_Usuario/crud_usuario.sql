create database crud_usuario;

use crud_usuario;

 create table usuario(
id int primary key auto_increment,
nome varchar(50),
email varchar(100),
endereco varchar(100)
 );
 
 select * from usuario;