import pandas as pd
from google.cloud import bigquery
from tqdm import tqdm


from queries import Tokens


if __name__ == "__main__":
    partitions = list(
        map(
            lambda dt: dt.strftime("%Y-%m-%d"),
            pd.date_range(start="2021-08-01", end="2021-08-31", freq="D")
            .to_pydatetime()
            .tolist(),
        )
    )

    client = bigquery.Client()

    with tqdm(
        bar_format="{postfix[0]} {postfix[1][value]}",
        postfix=["Fetching partition", dict(value=0)],
    ) as t:
        table = Tokens.table
        query = Tokens.query

        for i, partition in enumerate(partitions):
            query = Tokens.query.format(partition)
            # dataframe = (
            #     client.query(query_string)
            #     .result()
            #     .to_dataframe(
            #         create_bqstorage_client=True,
            #     )
            # )
            # dataframe.to_csv(f"raw/{table}/{date}.csv")

            t.postfix[1]["value"] = partition
            t.update()
