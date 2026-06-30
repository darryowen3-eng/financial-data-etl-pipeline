SELECT
	Currency_Code,
	SUM(Exchange_Rate) AS Total_exchange_rate
FROM clean_local_disaster_data
WHERE Currency_Code != 'UNKNOWN'
GROUP BY Currency_Code
ORDER BY Total_exchange_rate DESC;


SELECT
	Currency_Code,
	SUM(Exchange_Rate) AS total_exchange_rate,
	CASE
		WHEN SUM(Exchange_Rate ) > (
			SELECT AVG(total_per_currency)
			FROM (
				SELECT SUM(Exchange_Rate) AS total_per_currency
				FROM clean_local_disaster_data
				GROUP BY Currency_Code
			) subquery
		) THEN 'Premier'
		ELSE 'Standard'
	END AS Classifying_Currency_Code
FROM clean_local_disaster_data
GROUP BY Currency_Code
ORDER BY total_exchange_rate DESC;
