.system clear
.bail on
.echo off
-- Uncomment the two lines below to start a web server 
-- that lets you browse the SQLite database
.system sh WEB/permissions.sh
.system WEB/server.sh

.open HCompSQLDemo.sqlite
PRAGMA foreign_keys = ON;

.echo on
.mode column
.headers on




















--1
SELECT hotelName, swimmingPool, resortName, resortType
FROM Hotel, Resort
WHERE Hotel.resortID = Resort.resortID AND resortName LIKE
'A%' AND resortType = 'coastal';

--2
SELECT firstname, surname, bookingNo, hotelName,
resortName, startDate
FROM Customer, Booking, Hotel, Resort
WHERE Customer.customerID=Booking.customerID AND
Booking.hotelRef=Hotel.hotelRef AND
Hotel.resortID=Resort.resortID AND surname LIKE '_h%'
ORDER BY surname ASC, startDate ASC;


--3
SELECT MIN(pricePersonNight) AS [Cheapest Price per
Night], MAX(pricePersonNight) AS [Dearest Price perNight]
FROM Hotel;

--4
SELECT ROUND(AVG(numberNights),2)
FROM Booking;

--5
SELECT resortType, COUNT(*)
FROM Resort
GROUP BY resortType;

--6
SELECT SUM(numberInParty) AS [People on holiday in July]
FROM Booking
WHERE startDate LIKE '%-07-%';

--7
SELECT resortType, COUNT(*) AS [Number of Bookings]
FROM Resort, Hotel, Booking
WHERE Resort.resortID = Hotel.resortID AND Hotel.hotelRef
= Booking.hotelRef AND resortType = 'coastal'
GROUP BY resortType;

--8
SELECT mealPlan, COUNT(*)
FROM Hotel, Booking
WHERE Hotel.hotelRef = Booking.hotelRef
GROUP BY mealPlan
ORDER BY COUNT(*) ASC;

--9
UPDATE Customer
SET address = '31 Pike Place', postcode = 'PH31 31P'
WHERE firstname = 'Omar' AND surname = 'Shaheed';

--10
UPDATE Hotel
SET pricePersonNight = ROUND(pricePersonNight * 1.04,2),
starRating = starRating + 1
WHERE hotelRef LIKE 'FW%';