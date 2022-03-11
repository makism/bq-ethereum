class TokenTransfers:
    table = "token_transfers"
    query = """
        SELECT 
            token_address,
            from_address,
            to_address,
            CAST(value AS FLOAT64) AS value,
            transaction_hash,
            log_index,
            UNIX_SECONDS(block_timestamp) AS block_timestamp,
            block_number,
            block_hash
        FROM 
            bigquery-public-data.crypto_ethereum.token_transfers
        WHERE 
            DATE(block_timestamp) = "{0}"
    """


class Tokens:
    table = "tokens"
    query = """
        SELECT 
            token_address,
            CAST(name AS STRING) AS name,
            CAST(symbol AS STRING) AS symbol,
            CAST(decimals AS INT64) AS decimals,
            CAST(total_supply AS FLOAT64) AS total_supply
        FROM 
            bigquery-public-data.crypto_ethereum.tokens
        WHERE 
            DATE(block_timestamp) = "{0}"
    """
