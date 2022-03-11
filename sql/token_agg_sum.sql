WITH token_transfers AS (
  SELECT
    token_address,
    from_address,
    to_address,
    CAST(value AS FLOAT64) AS value,
    transaction_hash,
    block_hash,
    UNIX_SECONDS(block_timestamp) AS block_timestamp
  FROM
    `bigquery-public-data.crypto_ethereum.token_transfers`
  WHERE
    DATE(block_timestamp) = "2021-08-31"
),
tokens AS (
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
  SUM(token_transfers.value) AS total_sum,
  COUNT(*) AS num_tx,
  tokens.name,
FROM
  token_transfers
  JOIN tokens ON token_transfers.token_address = tokens.address
GROUP BY
  tokens.name
ORDER BY
  total_sum DESC
LIMIT
  1000