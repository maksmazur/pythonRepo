CREATE TABLE Pracownicy (
    PracownikID INT AUTO_INCREMENT PRIMARY KEY,
    Imie VARCHAR(50),
    Nazwisko VARCHAR(50),
    DataUrodzenia DATE,
    Wynagrodzenie DECIMAL(10, 2),
    PoczatekZatrudnienia DATE,
    KoniecZatrudnienia DATE
);

INSERT INTO Pracownicy (Imie, Nazwisko, DataUrodzenia, Wynagrodzenie, PoczatekZatrudnienia, KoniecZatrudnienia)
VALUES
    ('Jan', 'Kowalski', '1990-01-15', 5000.00, '2022-01-01', NULL),
    ('Anna', 'Nowak', '1985-05-20', 6000.00, '2021-03-15', '2023-06-30'),
    ('Piotr', 'Wiśniewski', '1992-11-10', 4500.00, '2023-01-10', NULL);

CREATE VIEW AktualnieZatrudnieni AS
SELECT Imie, Nazwisko, Wynagrodzenie
FROM Pracownicy
WHERE KoniecZatrudnienia IS NULL;

CREATE VIEW RaportZatrudnienia AS
SELECT
    YEAR(PoczatekZatrudnienia) AS Rok,
    COUNT(*) AS LiczbaPracownikow
FROM Pracownicy
GROUP BY Rok
ORDER BY Rok;

SELECT * FROM AktualnieZatrudnieni;
SELECT * FROM RaportZatrudnienia;
