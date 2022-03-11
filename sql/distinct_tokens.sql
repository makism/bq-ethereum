WITH tokens_filtered AS (
  SELECT
    address,
    name,
    UNIX_SECONDS(block_timestamp) AS block_timestamp
  FROM
    `bigquery-public-data.crypto_ethereum.tokens`
  WHERE
    DATE(block_timestamp) = "2021-08-31"
)
SELECT
  DISTINCT(name) AS distinct_name,
  address,
FROM
  tokens_filtered
ORDER BY
  name ASC