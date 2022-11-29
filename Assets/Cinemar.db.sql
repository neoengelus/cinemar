BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "pelicula" (
	"id_pelicula"	INTEGER NOT NULL,
	"duracion"		TEXT(45),
	"director"		TEXT(45),
	"titulo"		TEXT(45),
	"clasificacion"	TEXT(45),
	PRIMARY KEY("id_pelicula" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "funcion" (
	"id_funcion"	INTEGER NOT NULL,
	"id_pelicula"	INTEGER,
	"horario"		TEXT(45),
	"dia_funcion"	TEXT(45),
	"id_sala"		INTEGER,
	FOREIGN KEY("id_sala") REFERENCES "sala"("id_sala") ON DELETE NO ACTION ON UPDATE NO ACTION,
	FOREIGN KEY("id_pelicula") REFERENCES "pelicula"("id_pelicula") ON DELETE NO ACTION ON UPDATE NO ACTION,
	PRIMARY KEY("id_funcion" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "sala" (
	"id_sala"			INTEGER NOT NULL,
	"tipo_sala"			BOOLEAN,
	"butaca_max"		INTEGER,
	"butaca_ocupada"	INTEGER,
	"costo"				FLOAT,
	"id_pelicula"		INTEGER,
	FOREIGN KEY("id_pelicula") REFERENCES "pelicula"("id_pelicula") ON DELETE NO ACTION ON UPDATE NO ACTION,
	PRIMARY KEY("id_sala" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "reserva" (
	"id_reserva"	INTEGER NOT NULL,
	"id_funcion"	INTEGER,
	"dni"			TEXT(45),
	"fecha_reserva"	TEXT(45),
	"cant_asiento"	INTEGER,
	"costo"			FLOAT,
	"dias"			TEXT(45),
	"id_butaca"		TEXT(45),
	FOREIGN KEY("id_funcion") REFERENCES "funcion"("id_funcion") ON DELETE NO ACTION ON UPDATE NO ACTION,
	FOREIGN KEY("dni") REFERENCES "usuario"("dni") ON DELETE NO ACTION ON UPDATE NO ACTION,
	FOREIGN KEY("dias") REFERENCES "descuento"("dias") ON DELETE NO ACTION ON UPDATE NO ACTION,
	FOREIGN KEY("id_butaca") REFERENCES "butaca"("id_butaca") ON DELETE NO ACTION ON UPDATE NO ACTION,
	PRIMARY KEY("id_reserva" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "descuento" (
	"dias"			TEXT(45) NOT NULL,
	"porcentaje"	FLOAT,
	PRIMARY KEY("dias")
);
CREATE TABLE IF NOT EXISTS "butaca" (
	"fila"		TEXT(45) NOT NULL,
	"asiento"	TEXT(45) NOT NULL,
	"id_sala"	INTEGER,
	FOREIGN KEY("id_sala") REFERENCES "sala"("id_sala") ON DELETE NO ACTION ON UPDATE NO ACTION,
	PRIMARY KEY("id_sala","asiento","fila"),
);
CREATE TABLE IF NOT EXISTS "usuario" (
	"dni"	T	EXT(45) NOT NULL,
	"nombre"	TEXT(45),
	"mail"		TEXT(45),
	"apellido"	TEXT(45),
	"edad"		INTEGER,
	"passw"		TEXT(45),
	"tipo"		INTEGER NOT NULL,
	PRIMARY KEY("dni")
);
INSERT INTO "pelicula" ("id_pelicula","duracion","director","titulo","clasificacion") VALUES (1,'162','James Cameron','Avatar','PG-13'),
 (2,'101','Francis Lawrence','Soy Leyenda','PG-13'),
 (3,'117','Zack Snyder','300','R'),
 (4,'143','Joss Whedon','Los Vengadores','PG-13'),
 (5,'169','Christopher Nolan','Intersellar','PG-13'),
 (6,'121','George Lucas','Star Wars: Episode IV - A New Hope','PG'),
 (7,'179','Peter Jackson','El Señor de Los Anillos - Las Dos Torres','PG-13'),
 (8,'103','James Wan','Insidious','PG-3'),
 (9,'81','John Lasseter','Toy Story','G'),
 (10,'81','John Lasseter','Cars','G');
INSERT INTO "sala" ("id_sala","tipo_sala","butaca_max","butaca_ocupada","costo","id_pelicula") VALUES (1,0,50,0,300.0,NULL),
 (2,1,60,0,600.0,NULL);
INSERT INTO "descuento" ("dias","porcentaje") VALUES ('Lunes',20.0),
 ('Martes',15.0),
 ('Miercoles',20.0),
 ('Juves',15.0),
 ('Viernes',10.0),
 ('Sabado',10.0),
 ('Domingo',10.0);
INSERT INTO "usuario" ("dni","nombre","mail","apellido","edad","passw","tipo") VALUES ('123456','Jorge','algo@gmail.com','Surate',NULL,'admin',0),
 ('678901','Ariel','algo@gmail.com','Chocobar',NULL,'admin',0),
 ('458796','Yanina','algo@gmail.com','Aban',NULL,'admin',0),
 ('124789','Johana','algo@gmail.com','',NULL,'admin',0),
 ('235879','Juan','algo@gmail.com','Perez',NULL,'user',1),
 ('578963','Julio','algo@gmail.com','Iglesias',NULL,'user',1);
COMMIT;
