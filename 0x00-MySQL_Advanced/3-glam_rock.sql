-- Task Description: List all bands with Glam rock as their main style, ranked by their longevity

-- Import the metal_bands table dump (assuming the table is present in metal_bands.sql)
-- Make sure to import the table before running this script

-- List bands with Glam rock as their main style, ranked by their longevity

-- selects band_name and lifespan in descending order.
SELECT band_name,
CASE
    WHEN split IS NOT NULL THEN split - formed
    ELSE 2022 - formed
END AS lifespan
FROM metal_bands
WHERE style LIKE "%Glam rock%"
ORDER BY lifespan DESC;
