-- Task Description: Create a stored procedure ComputeAverageWeightedScoreForUsers that computes and stores the average weighted score for all students.

-- Create the stored procedure
DELIMITER //
CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
    DECLARE done INT DEFAULT 0;
    DECLARE user_id INT;
    
    -- Cursor to iterate over user IDs
    DECLARE users_cursor CURSOR FOR SELECT id FROM users;
    
    -- Declare continue handler to exit loop
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = 1;
    
    -- Open the cursor
    OPEN users_cursor;
    
    -- Start looping
    users_loop: LOOP
        -- Fetch the next user ID
        FETCH users_cursor INTO user_id;
        
        -- Break the loop if no more records
        IF done THEN
            LEAVE users_loop;
        END IF;

        -- Calculate the weighted average score for the current user
        CALL ComputeAverageWeightedScoreForUser(user_id);
    END LOOP;

    -- Close the cursor
    CLOSE users_cursor;
END;
//
DELIMITER ;

-- Show procedures to confirm creation
SHOW PROCEDURE STATUS;
