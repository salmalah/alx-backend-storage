-- Task Description: Create a stored procedure ComputeAverageScoreForUser that computes and stores the average score for a student

-- Create the stored procedure
DELIMITER //
CREATE PROCEDURE ComputeAverageScoreForUser(
    IN p_user_id INT
)
BEGIN
    DECLARE v_total_score FLOAT;
    DECLARE v_total_projects INT;

    -- Compute the total score and total projects for the user
    SELECT
        SUM(score) INTO v_total_score,
        COUNT(DISTINCT project_id) INTO v_total_projects
    FROM corrections
    WHERE user_id = p_user_id;

    -- Update the user's average_score
    IF v_total_projects > 0 THEN
        UPDATE users
        SET average_score = v_total_score / v_total_projects
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
