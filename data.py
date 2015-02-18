DATA_PATH = "./data"
REGULAR_DATA_PATH = "%s/regular_season_detailed_results.csv" % DATA_PATH
TOURNEY_DATA_PATH = "%s/tourney_detailed_results.csv" % DATA_PATH
TEAM_MAPPING_PATH = "%s/teams.csv" % DATA_PATH
SEASONS_PATH = "%s/seasons.csv" % DATA_PATH

import pandas as pd


class MarchMadnessData:

    def __init__(self):
        self.load_team_mappings()
        self.load_seasons()
        self.load_regular_season_data()
        self.load_tourney_data()
        self.print_season_infos()

    def load_team_mappings(self):
        f = open(TEAM_MAPPING_PATH, 'r')
        self.team_code_to_id = {}
        self.team_codes = []
        for count, line in enumerate(f):
            if count == 0:
                continue
            team_code, team_name = line.rstrip().split(",")
            self.team_codes.append(team_code)
            self.team_code_to_id[team_code] = team_name

    def load_seasons(self):
        f = open(SEASONS_PATH, 'r')
        self.seasons = {}
        for count, line in enumerate(f):
            if count == 0:
                continue
            season, dayzero, region_w, region_x, region_y, region_z = \
                line.rstrip().split(",")
            self.seasons[season] = dayzero

    def load_regular_season_data(self):
        self.game_results_by_regular_season = {}
        total_regular_season_data = pd.read_csv(REGULAR_DATA_PATH)

        # group data by season.
        grouped = total_regular_season_data.groupby('season')
        for name, group in grouped:
            self.game_results_by_regular_season[name] = group

    def load_tourney_data(self):
        self.game_results_by_tourney_season = {}
        total_tourney_data = pd.read_csv(TOURNEY_DATA_PATH)

        # group data by tourney season
        grouped = total_tourney_data.groupby('season')
        for name, group in grouped:
            self.game_results_by_tourney_season[name] = group

    def print_season_infos(self):
        print "Regular season games - \n"
        print "\n".join(["%s: %s games" % (s, len(self.game_results_by_regular_season[s])) \
                         for s in sorted(self.game_results_by_regular_season)])
        print "Tourney games - \n"
        print "\n".join(["%s: %s games" % (s, len(self.game_results_by_tourney_season[s])) \
                         for s in sorted(self.game_results_by_tourney_season)])


if __name__ == "__main__":
    data = MarchMadnessData()
