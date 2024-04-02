from IPython.core.magic import register_cell_magic
from sqlalchemy import create_engine
import pandas as pd
from google.colab import userdata
from sqlalchemy import text



# connection_string = userdata.get('DO_Postgres')
connection_string = userdata.get('postgres_key')
# Create an SQLAlchemy engine
engine = create_engine(connection_string)

# Initialize a global dictionary to hold the results
results_dict = {}

@register_cell_magic
def sql(line, cell):
    """
    Harness the data, with DOOM's mask and flair,
    Where SQL meets Python, a most villainous pair.
    A script so cunning, with pandas in lair,
    Executing queries with a magic rare.

    Parameters:
    - line (str): The unique identifier for the dataframe stored,
                  A tag, a label, on which results are boarded.
    - cell (str): The SQL command, a query accorded,
                  In plain text penned, where logic is sorded.

    Returns:
    - None: But witness the console, for it shall declare,
            The name of the key where results breathe air,
            In `results_dict`, a global layer,
            Where dataframes reside, with care.

    Example:
    %%sql my_label
    SELECT * FROM villains WHERE cunning > 100
    
    This spell, when cast, through notebooks it tears,
    Collects from the database, what the query ensnares.
    `my_label` as the tag, in `results_dict` it pairs,
    A new dataframe born, with data it shares.

    A global dictionary, `results_dict` by name,
    Holds the treasure of queries, in the Villain's game.
    Each run of the magic, its contents frame,
    A growing collection, of SQL's acclaim.

    So, scribe your queries, with DOOM's mask in sight,
    Let the data flow freely, from the depths to the light.
    Through SQLAlchemy's engine, to PostgreSQL's might,
    Our script runs the magic, with all its might.
    """

    global results_dict  # Refer to the global dictionary
    query = text(cell)
    with engine.connect() as conn:
        result = pd.read_sql_query(query, conn)
    dict_name = f'df{line}{len(results_dict)+1}'
    results_dict[dict_name] = result
    print(f'saved to results_dict[{dict_name}]')
    
