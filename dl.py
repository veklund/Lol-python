import os
import requests
from clone import champion_roles, clean_champion_name

def download_champion_icons():
    """Download all champion icons"""
    # Create the directory if it doesn't exist
    if not os.path.exists('static/champions'):
        os.makedirs('static/champions')

    # Get latest version from Data Dragon
    versions_url = "https://ddragon.leagueoflegends.com/api/versions.json"
    versions = requests.get(versions_url).json()
    latest_version = versions[0]
    print(f"Using Data Dragon version: {latest_version}")

    # Download icons for each champion
    for champion in champion_roles.keys():
        clean_name = clean_champion_name(champion)
        icon_path = f"static/champions/{clean_name}.png"
        
        # Skip if already downloaded
        if os.path.exists(icon_path):
            print(f"Skipping {champion} (already exists)")
            continue

        # Download the icon
        url = f"https://ddragon.leagueoflegends.com/cdn/{latest_version}/img/champion/{clean_name}.png"
        response = requests.get(url)
        
        if response.status_code == 200:
            with open(icon_path, 'wb') as f:
                f.write(response.content)
            print(f"Downloaded {champion}")
        else:
            print(f"Failed to download {champion}: {response.status_code}")

if __name__ == "__main__":
    download_champion_icons()
