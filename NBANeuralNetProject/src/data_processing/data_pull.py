import yaml
import csv



def getTeamData():
#creates the dictionary the data will be stored in
#Schema is data[year][team][#statName]
#statnames:
    #'H/A' - Home/Away, 1 is home 0 is away
    #'MOV' - Adjusted margin of victory for strength of schedule of opponent
    #'ORtg' - Adjusted Offensive Rating for strength of opponent defense
    #'DRtg' - Adjusted Defensive Rating for strength of opponent offense
    #'Pace' - Estimate of Possessions per 48 minutes
    data = dict()

    #Gets an array of file names in miscellaneous_stats, store in variable 'files'
    yamlfile = '../../data/miscellaneous_stats/filenames.yaml'
    with open(yamlfile, 'r') as file:
        filenames = yaml.load(file, Loader=yaml.FullLoader)
        files = filenames['filenames'].split()

        miscellaneous_stats_filepath = "../../data/miscellaneous_stats/"

        for file in files:

            year = file.split("_")[0]
            data[year] = {}
            data[year]['Golden State Warriors'] = {}
            data[year]['San Antonio Spurs'] = {}
            data[year]['Cleveland Cavaliers'] = {}
            data[year]['Toronto Raptors'] = {}
            data[year]['Oklahoma City Thunder'] = {}
            data[year]['Los Angeles Clippers'] = {}
            data[year]['Atlanta Hawks'] = {}
            data[year]['Boston Celtics'] = {}
            data[year]['Charlotte Hornets'] = {}
            data[year]['Miami Heat'] = {}
            data[year]['Indiana Pacers'] = {}
            data[year]['Detroit Pistons'] = {}
            data[year]['Portland Trail Blazers'] = {}
            data[year]['Dallas Mavericks'] = {}
            data[year]['Memphis Grizzlies'] = {}
            data[year]['Chicago Bulls'] = {}
            data[year]['Houston Rockets'] = {}
            data[year]['Washington Wizards'] = {}
            data[year]['Utah Jazz'] = {}
            data[year]['Orlando Magic'] = {}
            data[year]['Denver Nuggets'] = {}
            data[year]['Milwaukee Bucks'] = {}
            data[year]['Sacramento Kings'] = {}
            data[year]['New York Knicks'] = {}
            data[year]['New Orleans Pelicans'] = {}
            data[year]['Minnesota Timberwolves'] = {}
            data[year]['Phoenix Suns'] = {}
            data[year]['Brooklyn Nets'] = {}
            data[year]['Los Angeles Lakers'] = {}
            data[year]['Philadelphia 76ers'] = {}
            data[year]['Seattle SuperSonics'] = {}
            data[year]['Vancouver Grizzlies'] = {}
            data[year]['New Jersey Nets'] = {}
            data[year]['New Orleans Hornets'] = {}
            data[year]['Charlotte Bobcats'] = {}
            data[year]['New Orleans/Oklahoma City Hornets'] = {}
            data[year]['League Average'] = {}



            with open(miscellaneous_stats_filepath+file, 'r') as csvfile:

                readCSV = csv.reader(csvfile)

                #set up the data dictionary, put pace by team into data
                for row in readCSV:

                    if(row[0]!= 'Rk'):

                        #store the team and pace
                        team = row[1]
                        team = team.replace("*","")
                        pace = row[13]

                        #create the dictionary data to store all the game data by year and team and store pace
                        data[year][team]["pace"] = pace

    yamlfile = '../../data/team_stats/filenames.yaml'
    with open(yamlfile, 'r') as file:
        filenames = yaml.load(file, Loader=yaml.FullLoader)
        files = filenames['filenames'].split()

        team_stats_filepath = "../../data/team_stats/"

        for file in files:
            year = file.split("_")[0]
            with open(team_stats_filepath + file, 'r') as csvfile:
                readCSV = csv.reader(csvfile)

                for row in readCSV:
                    #11,12,13 - MOV/A, ORtg, DRtg
                    if row[0] != 'Rk':
                        team = row[1]
                        data[year][team]["MOV"] = row[11]
                        data[year][team]["ORtg"] = row[12]
                        data[year][team]["DRtg"] = row[13]



    return data
#Returns an array of games which are stored as arrays of "Year, away, away_points, home, home_points
def getGameData():
    data = {}
    yamlfile = '../../data/Games/foldernames.yaml'
    with open(yamlfile, 'r') as file:
        foldernames = yaml.load(file, Loader=yaml.FullLoader)
        folders = foldernames['foldernames']


    for year in folders:
        data[year]=[]

        games_filepath = '../../data/Games/'+year
        gamesyaml = games_filepath+'/filenames.yaml'
        with open(gamesyaml, 'r') as year_yaml:
            csv_names = yaml.load(year_yaml, Loader=yaml.FullLoader)
            game_files= csv_names['filenames']
            for game_file in game_files:
                
                with open(games_filepath+'/'+game_file, 'r') as games:
                    readCSV = csv.reader(games)

                    for row in readCSV:
                        if row[0] != 'Date':
                            visitor = row[2]
                            visitor_score = row[3]
                            home=row[4]
                            home_score= row[5]
                            data[year].append((home, home_score,visitor,visitor_score))

    return data


def write_data(filename):
    teamData=getTeamData()
    gameData=getGameData()
    
    path = '../../data/combined_data'

    #Set the fields for the CSV file
    fields = ["home","home_score","home_MOV", "home_ORtg", "home_DRtg", "home_pace", "away", "away_score", "away_MOV", "away_ORtg", "away_DRtg", "away_pace", "year"]

    with open(path+'/'+filename, 'w') as csvfile:
        csvwriter =csv.writer(csvfile, lineterminator="\n")

        #write the fields 
        csvwriter.writerow(fields)

        for year in gameData:
            for game in gameData[year]:
                home = game[0]
                home_score = game[1]
                home_MOV = teamData[year][home]["MOV"]
                home_ORtg= teamData[year][home]["ORtg"]
                home_DRtg = teamData[year][home]["DRtg"]
                home_pace = teamData[year][home]["pace"]
                away = game[2]
                away_score=game[3]
                away_MOV = teamData[year][away]["MOV"]
                away_ORtg= teamData[year][away]["ORtg"]
                away_DRtg = teamData[year][away]["DRtg"]
                away_pace = teamData[year][away]["pace"]
                row =[home, home_score, home_MOV, home_DRtg, home_ORtg, home_pace, away, away_score, away_MOV, away_ORtg, away_DRtg, away_pace, year]
                csvwriter.writerow(row)

    
write_data("all_games.csv")
