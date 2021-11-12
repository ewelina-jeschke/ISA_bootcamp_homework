Create database sklep

/*Tworzenie tabeli Uzytkownik*/
Create table Uzytkownik (
	Id_uzytkownika int not null,
	Imie varchar(50) not null,
	Nazwisko varchar(50) not null,
	primary key(Id_uzytkownika)
	)


/*Tworzenie tabeli Zamowienie*/
Create table Zamowienie (
	Id_zamowienia int not null,
	Numer_zamowienia varchar(50) not null,
	Data_zamowienia date not null,
	Wartosc_zamowienia int not null,
	primary key(Id_zamowienia),
	Id_uzytkownika int not null,
	Id_produktu int not null,
	foreign key (Id_uzytkownika) references Uzytkownik(Id_Uzytkownika),
	foreign key (Id_produktu) references Produkt(Id_produktu)
	)


/*Tworzenie tabeli Produkt*/
Create table Produkt (
	Id_produktu int not null,
	Nazwa_produktu varchar(50) not null,
	Cena_produktu int not null,
	primary key(Id_produktu)
	)


/*Dodanie Uzytkownikow*/
insert into Uzytkownik values (1,'Janusz','Kowalski');
insert into Uzytkownik values (2,'Ewa','Nowak');
insert into Uzytkownik values (3,'Tomasz','Kowal');


/*Dodanie Produktow*/
insert into Produkt values (1,'Krzeslo',200);
insert into Produkt values (2,'Stol',500);
insert into Produkt values (3,'Szafa',600);


/*Dodanie Zamowien*/
insert into Zamowienie values (1,'ZAM1','2021-01-01',700,1,2);
insert into Zamowienie values (2,'ZAM2','2021-10-01',900,1,3);
insert into Zamowienie values (3,'ZAM3','2021-11-05',2000,2,3);
insert into Zamowienie values (4,'ZAM4','2021-11-03',600,3,1);

/*do sprawdzenia*/
select * from Uzytkownik
select * from Produkt
select * from Zamowienie