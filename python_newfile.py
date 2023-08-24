class FlightTable:
    def __init__(self):
        self.locations = ["Mumbai", "Delhi", "Chennai", "Indore", "Mohali", "Delhi"]
        self.teams = ["Team 01", "India", "England", "India", "England", "Australia", "India",
                      "Team 02", "Sri Lanka", "Australia", "South Africa", "Sri Lanka", "South Africa", "Australia"]
        self.timings = ["DAY", "DAY-NIGHT", "DAY", "DAY-NIGHT", "DAY-NIGHT", "DAY"]

    def list_matches_by_team(self, team_name):
        matches = []
        for i in range(len(self.teams)):
            if self.teams[i] == team_name:
                matches.append((self.locations[i // 2], self.timings[i // 2]))
        return matches

    def list_matches_by_location(self, location_name):
        matches = []
        for i in range(len(self.locations)):
            if self.locations[i] == location_name:
                matches.append((self.teams[i * 2], self.teams[i * 2 + 1], self.timings[i]))
        return matches

    def list_matches_by_timing(self, timing):
        matches = []
        for i in range(len(self.timings)):
            if self.timings[i] == timing:
                matches.append((self.teams[i * 2], self.teams[i * 2 + 1], self.locations[i]))
        return matches


def main():
    flight_table = FlightTable()
    
    while True:
        print("Options:")
        print("1. List of all the matches of a Team")
        print("2. List of Matches on a Location")
        print("3. List of Matches based on timing")
        print("4. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            team_name = input("Enter the team name: ")
            matches = flight_table.list_matches_by_team(team_name)
            if matches:
                print(f"Matches for {team_name}:")
                for match in matches:
                    print(f"Location: {match[0]}, Timing: {match[1]}")
            else:
                print(f"No matches found for {team_name}")
        elif choice == '2':
            location_name = input("Enter the location name: ")
            matches = flight_table.list_matches_by_location(location_name)
            if matches:
                print(f"Matches at {location_name}:")
                for match in matches:
                    print(f"Team 1: {match[0]}, Team 2: {match[1]}, Timing: {match[2]}")
            else:
                print(f"No matches found at {location_name}")
        elif choice == '3':
            timing = input("Enter the timing (DAY, DAY-NIGHT): ")
            matches = flight_table.list_matches_by_timing(timing)
            if matches:
                print(f"Matches at {timing} timing:")
                for match in matches:
                    print(f"Team 1: {match[0]}, Team 2: {match[1]}, Location: {match[2]}")
            else:
                print(f"No matches found at {timing} timing")
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please choose a valid option.")


if __name__ == "__main__":
    main()
