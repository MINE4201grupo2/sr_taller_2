DELIMITER $$
DROP PROCEDURE IF EXISTS `getRecomendation`;
CREATE PROCEDURE `getRecomendation`(IN par_user_id varchar(255),IN par_categoria VARCHAR(50), IN par_limit INT)
BEGIN
	IF (par_limit IS NOT NULL) THEN
		SELECT b.*, rb.recomendation_score FROM business b
        INNER JOIN recomendations_business rb
			ON rb.business_id = b.business_id
		WHERE rb.user_id = par_user_id
        ORDER BY rb.recomendation_scorE DESC
        LIMIT par_limit;
	ELSE
		SELECT b.*, rb.recomendation_score FROM business b
        INNER JOIN recomendations_business rb
			ON rb.business_id = b.business_id
		WHERE rb.user_id = par_user_id
			AND b.categories LIKE concat('%',par_categoria,'%')
		ORDER BY rb.recomendation_score DESC;
        
	END IF;
    
END$$

DELIMITER ;