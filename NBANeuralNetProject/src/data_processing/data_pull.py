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
    data = [];
    yamlfile = '../../data/Games/foldernames.yaml'
    with open(yamlfile, 'r') as file:
        foldernames = yaml.load(file, Loader=yaml.FullLoader)
        folders = foldernames['foldernames']


    for folder in folders:

        games_filepath = '../../data/Games/'+folder
        gamesyaml = games_filepath+'/filenames.yaml'
teamData = getTeamData()

print(teamData['2017-2018']['Philadelphia 76ers'])
print("############")
print(teamData['2017-2018']['Detroit Pistons'].keys())
print(len(gameData))

