import pymysql

# Function to connect to the MySQL database
def connect_to_database():
    try:
        # Modify the connection parameters based on your MySQL configuration
        connection = pymysql.connect(
            host='localhost',
            user='root',
            password='mrDCep2014',
            database='pysports'
        )
        print("Connected to the database successfully.")
        return connection
    except pymysql.Error as e:
        print(f"Error connecting to the database: {e}")
        return None

# Function to execute and display the select query results
def execute_select_query(connection, query):
    try:
        with connection.cursor() as cursor:
            cursor.execute(query)
            results = cursor.fetchall()

            for row in results:
                # Modify the index numbers based on the select query columns
                team_id, team_name, mascot = row[0], row[1], row[2]
                print(f"Team ID: {team_id}, Team Name: {team_name}, Mascot: {mascot}")
    except pymysql.Error as e:
        print(f"Error executing the query: {e}")

# Main function
if __name__ == "__main__":
    # Connect to the database
    db_connection = connect_to_database()

    if db_connection:
        # Define the select queries for the team and player tables
        team_query = "SELECT team_id, team_name, mascot FROM team;"
        players_query = "SELECT player_id, first_name, last_name FROM players;"

        # Execute and display the results for the team table
        print("Results from the Team table:")
        execute_select_query(db_connection, team_query)

        # Execute and display the results for the player table
        print("\nResults from the Player table:")
        execute_select_query(db_connection, players_query)

        # Close the database connection
        db_connection.close()
