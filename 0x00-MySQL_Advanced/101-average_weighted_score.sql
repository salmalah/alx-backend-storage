-- Task Description: Create a stored procedure ComputeAverageWeightedScoreForUsers that computes and stores the average weighted score for all students.

-- Create the stored procedure
-- average weighted score for all students.
DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUsers;
DELIMITER //

CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
    UPDATE users AS u
    JOIN (
        SELECT u.id, SUM(c.score * p.weight) / SUM(p.weight) AS weighted_avg
        FROM users AS u
        JOIN corrections AS c ON u.id = c.user_id
        JOIN projects AS p ON c.project_id = p.id
        GROUP BY u.id
    ) AS user_weighted_avg ON u.id = user_weighted_avg.id
    SET u.average_score = user_weighted_avg.weighted_avg;
END //

DELIMITER ;
