import mysql.connector

# Replace these with your actual database credentials
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'mrDCep2014',
    'database': 'pysports',
}

# Establish a connection to the database
connection = mysql.connector.connect(**db_config)
cursor = connection.cursor()

# Define the INNER JOIN query with the updated table name and alias
query = """
SELECT
    player_id AS 'Player ID:',
    players.first_name AS 'First Name:',
    players.last_name AS 'Last Name:',
    players.team_id AS 'Team Name:'
FROM
    players
INNER JOIN
    team ON players.team_id = team.team_id;
"""

# Execute the query
cursor.execute(query)

# Fetch all the results
results = cursor.fetchall()

# Display the results
print("--Displaying player records--")
for row in results:
    player_id, first_name, last_name, team_name = row
    print(f"Player ID: {player_id}")
    print(f"First Name: {first_name}")
    print(f"Last Name: {last_name}")
    print(f"Team Name: {team_name}")
    print("-" * 20)

# Close the cursor and connection
cursor.close()
connection.close()