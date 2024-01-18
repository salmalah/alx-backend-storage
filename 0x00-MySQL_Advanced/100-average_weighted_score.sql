-- Task Description: Create a stored procedure ComputeAverageWeightedScoreForUser that computes and stores the average weighted score for a student.

-- Create the stored procedure
DELIMITER //
CREATE PROCEDURE ComputeAverageWeightedScoreForUser(
    IN p_user_id INT
)
BEGIN
    DECLARE v_total_weighted_score FLOAT;
    DECLARE v_total_weight INT;

    -- Compute the total weighted score and total weight for the user
    SELECT
        SUM(score * weight) INTO v_total_weighted_score,
        SUM(weight) INTO v_total_weight
    FROM corrections
    JOIN projects ON corrections.project_id = projects.id
    WHERE user_id = p_user_id;

    -- Update the user's average_score
    IF v_total_weight > 0 THEN
        UPDATE users
        SET average_score = v_total_weighted_score / v_total_weight
        WHERE id = p_user_id;
    ELSE
        UPDATE users
        SET average_score = 0
        WHERE id = p_user_id;
    END IF;
END;
//
DELIMITER ;

-- Show procedures to confirm creation
SHOW PROCEDURE STATUS;
