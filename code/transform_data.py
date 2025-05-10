# transform_data.py

import pandas as pd

def convert_to_df(player_name, stats_dict):
    """
    Converts a single player's season stats dictionary into a DataFrame.
    Adds the player's name as a column for clarity.
    """
    if not stats_dict:
        print(f"[INFO] No stats to convert for {player_name}")
        return pd.DataFrame()

    df = pd.DataFrame([stats_dict])
    df['player_name'] = player_name
    return df


def merge_player_dfs(dfs):
    """
    Merges multiple player DataFrames into one combined DataFrame.
    Skips any that are empty.
    """
    non_empty_dfs = [df for df in dfs if not df.empty]
    if not non_empty_dfs:
        print("[INFO] No valid player data to merge.")
        return pd.DataFrame()

    return pd.concat(non_empty_dfs, ignore_index=True)
