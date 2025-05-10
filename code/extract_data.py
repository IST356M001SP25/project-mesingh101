import requests

headers = {
    "Authorization": "Bearer 65bd66b3-f19b-464e-adc1-10131c37129a"
}

def get_all_players():
    all_players = {}
    url = "https://api.balldontlie.io/v1/players"
    headers = {"Authorization": "Bearer 65bd66b3-f19b-464e-adc1-10131c37129a"}
    cursor = None
    has_more = True

    while has_more:
        params = {"per_page": 100}
        if cursor:
            params["cursor"] = cursor

        response = requests.get(url, headers=headers, params=params)
        data = response.json()

        for player in data["data"]:
            full_name = f"{player['first_name']} {player['last_name']}"
            all_players[full_name] = player["id"]

        # Handle pagination
        cursor = data.get("meta", {}).get("next_cursor")
        has_more = bool(cursor)

    return all_players

def get_season_stats(player_id, season):
    url = "https://api.balldontlie.io/v1/season_averages"
    headers = {"Authorization": "Bearer 65bd66b3-f19b-464e-adc1-10131c37129a"}

    if not isinstance(player_id, int):  # Ensure it's a proper int
        print(f"[ERROR] Invalid player_id: {player_id}")
        return None

    params = {
        "season": season,
        "player_ids[]": player_id
    }
    print(f"Fetching stats for ID {player_id} in season {season}")

    response = requests.get(url, params=params, headers=headers)

    if response.status_code != 200:
        print(f"[ERROR] Stats API failed: {response.status_code}")
        print("Response text:", response.text)
        return None

    data = response.json()
    return data['data'][0] if data['data'] else None
