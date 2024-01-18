-- Task Description: Create a trigger to reset valid_email only when the email has been changed

-- Create the trigger
DELIMITER //
CREATE TRIGGER reset_valid_email
BEFORE UPDATE ON users
FOR EACH ROW
BEGIN
    IF NEW.email <> OLD.email THEN
        SET NEW.valid_email = 0;
    END IF;
END;
//
DELIMITER ;

-- Show triggers to confirm creation
SHOW TRIGGERS;

-- Note: This trigger assumes that the email field is the one being updated.

