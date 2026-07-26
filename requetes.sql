--Question 3a-Chiffre d’affaires total 

SELECT SUM(c3*c4)AS chiffre_affaires_total
FROM ventes;


--Question 3b-Ventes par produit 

SELECT c2, SUM(c3*c4) As Chiffre_affaires
FROM ventes
WHERE c2 <> 'produit' 
GROUP BY c2;



--Question 3c-Ventes par région

SELECT c5 , SUM (c3*c4) AS chiffres_region
FROM ventes
WHERE c5 <>  'region'
GROUP BY c5;


 
