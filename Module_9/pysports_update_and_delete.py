import mysql.connector


db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'mrDCep2014',
    'database': 'pysports',
}

def execute_query(connection, query):
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()
    cursor.close()

def display_players(connection):

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
    cursor = connection.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    cursor.close()
    for row in results:
        player_id, first_name, last_name, team_name = row
        print(f"Player ID: {player_id}, First Name: {first_name}, Last Name: {last_name}, Team Name: {team_name}")
    print("-" * 40)

def main():
    # Establish a connection to the database
    connection = mysql.connector.connect(**db_config)

    # Insert a new record for Team Gandalf
    insert_query = "INSERT INTO players (first_name, last_name, team_id) VALUES ('New', 'Player', 1);"
    execute_query(connection, insert_query)

    # Display player records after inserting new record
    print("--Player records after inserting new record--")
    display_players(connection)

    # Update the newly inserted record to Team Sauron
    update_query = "UPDATE players SET team_id = 2 WHERE first_name = 'New' AND last_name = 'Player';"
    execute_query(connection, update_query)

    # Display updated player record
    print("--Player record after update--")
    display_players(connection)

    # Delete the updated record
    delete_query = "DELETE FROM players WHERE first_name = 'New' AND last_name = 'Player';"
    execute_query(connection, delete_query)

    # Display all player records after deletion
    print("--Player records after deletion--")
    display_players(connection)

    # Close the connection
    connection.close()

if __name__ == "__main__":
    main()