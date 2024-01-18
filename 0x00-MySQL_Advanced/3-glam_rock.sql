-- Task Description: List all bands with Glam rock as their main style, ranked by their longevity

-- Import the metal_bands table dump (assuming the table is present in metal_bands.sql)
-- Make sure to import the table before running this script

-- List bands with Glam rock as their main style, ranked by their longevity
SELECT
    band_name,
    IFNULL(
        IFNULL(YEAR(CURDATE()) - SUBSTRING_INDEX(sub.band_formed, '-', 1), 0),
        IFNULL(YEAR(CURDATE()) - SUBSTRING_INDEX(sub.band_split, '-', 1), 0)
    ) AS lifespan
FROM (
    SELECT
        band_name,
        IFNULL(SUBSTRING_INDEX(main_styles, ',', 1), main_styles) AS main_style,
        band_formed,
        band_split
    FROM metal_bands
) AS sub
WHERE main_style = 'Glam rock'
ORDER BY lifespan DESC;
