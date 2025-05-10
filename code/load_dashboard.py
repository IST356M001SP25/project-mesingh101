import streamlit as st
from extract_data import get_all_players, get_season_stats
from transform_data import convert_to_df, merge_player_dfs
import plotly.express as px

# App Title
st.title("🏀 NBA Player Stats Comparison")

# Load all players and build dropdown choices
player_choices = get_all_players()
player_names = list(player_choices.keys())

# Sidebar Inputs (Dropdowns)
player1_name = st.sidebar.selectbox("Select first player:", player_names)
player2_name = st.sidebar.selectbox("Select second player:", player_names)
season = st.sidebar.selectbox("Select season:", list(range(2000, 2024))[::-1])

# Button to run comparison
if st.sidebar.button("Compare Players"):
    with st.spinner("Fetching player data..."):

        pid1 = player_choices[player1_name]
        pid2 = player_choices[player2_name]

        # Get stats
        stats1 = get_season_stats(pid1, season)
        stats2 = get_season_stats(pid2, season)

        # Display debug info
        st.markdown("### 🔍 Retrieved Info")
        st.write(f"**Player 1:** {player1_name} (ID: {pid1})")
        st.write(f"**Player 2:** {player2_name} (ID: {pid2})")

        # Convert to DataFrames
        df1 = convert_to_df(player1_name, stats1)
        df2 = convert_to_df(player2_name, stats2)

        # Merge player stats
        final_df = merge_player_dfs([df1, df2])

    # Display output
    if not final_df.empty:
        st.subheader(f"📊 {season} Season Stat Comparison")

        # Choose stats to display
        stats_to_show = ['pts', 'ast', 'reb', 'stl', 'blk', 'turnover', 'fg_pct', 'fg3_pct', 'ft_pct']
        display_df = final_df[["player_name"] + stats_to_show]

        # Bar Chart
        fig = px.bar(display_df.melt(id_vars='player_name', var_name='Stat', value_name='Value'),
                     x='Stat', y='Value', color='player_name',
                     barmode='group', title='Stat Comparison')
        st.plotly_chart(fig, use_container_width=True)

        # Table
        st.markdown("### 🧾 Raw Stats")
        st.dataframe(display_df)

    else:
        st.warning("Could not retrieve data for one or both players. Try picking another season.")
