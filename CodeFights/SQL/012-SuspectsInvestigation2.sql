/*Please add ; after each select statement*/
/* For PostgreSQL LIKE is Case SENSITIVE use ILIKE For CASE INSENSITIVE*/
/* can convert to lower like LOWER(name) NOT LIKE */
CREATE PROCEDURE suspectsInvestigation2()
BEGIN
SELECT id,name,surname FROM Suspect
WHERE height <= 170 OR name NOT LIKE 'B%' OR surname NOT LIKE 'Gre_n'
ORDER BY id;
END
