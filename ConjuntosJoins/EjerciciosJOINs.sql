--Obtenga todos los libros y sus autores
select b.Name as BookName,
      COALESCE(a.Name,'') as AuthorName
from Books as b
JOIN Authors as a
 on b.author = a.ID;
 
--Obtenga todos los libros que no tienen autor
select b.Name as BookName_NoAuthor
from Books as b
LEFT JOIN Authors as a
 on b.author = a.ID
WHERE a.ID is null;


--Obtenga todos los autores que no tienen libros
select a.Name as Author_WithNoBooks
from Books as b
RIGHT JOIN Authors as a
 on b.author = a.ID
WHERE b.ID is null;

--Obtenga todos los libros que han sido rentados en algún momento
select DISTINCT b.Name as BookName
from Rents as r
INNER JOIN Books as b
 on b.ID = r.BookID;

--Obtenga todos los libros que nunca han sido rentados
select DISTINCT b.Name as BookName_NotRented
from Rents as r
RIGHT JOIN Books as b
 on b.ID = r.BookID
where r.BookID IS NULL;


--Obtenga todos los clientes que nunca han rentado un libro
select DISTINCT c.Name as ClientName
from Rents as r
RIGHT JOIN Customers as c
 on c.ID = r.CustomerID
where r.CustomerID IS NULL;


--Obtenga todos los libros que han sido rentados y están en estado “Overdue”
select DISTINCT b.Name as BookName_NotRented
from Rents as r
INNER JOIN Books as b
 on b.ID = r.BookID
where r.State = 'Overdue';


