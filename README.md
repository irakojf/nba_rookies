# StatMamba
StatMamba scrapes and visualizes granular data from Basketball Reference.

Written in Python, StatMamba uses Selenium and BeautifulSoup to pull player and team data. Users can represent and manipulate data as Pandas dataframes or export tables as .csv files.

## High Level
1. [Prerequisites](#Prerequisites)
2. [Scraping player data](#scrape)
3. [Scraping team data](#teamquery)
4. [Plotting data](#plot)
5. [Plotting change over time](#plotavg)

<a name='Prerequisites'></a>
### Prerequisites

StatMamba automatically imports BeautifulSoup and Pandas, but you can get Selenium [here](http://www.seleniumhq.org/download/).

StatMamba works best with [Spyder](https://github.com/spyder-ide/spyder).

To use StatMamba, simply open `statmamba.py` in the Spyder IDE and call any of the sample queries.

<a name='scrape'></a>

## Scraping Player Data
### scrape( players, div )

The **scrape** function takes two parameters: (1) a list of player names and (2) the name of the of table being scraped, represented by the 'id' value in the `<div id=' '>` tag.

The function saves the table as a Pandas dataframe or .csv file.

For example, calling `scrape( [ 'Kobe Bryant' ] , 'per_game' )` will produce a comma separated value file with Kobe Bryant's Per Game stats in the following directory path:

  `.../per_game_exports/kobe bryant.csv`

Proper usage of scrape is as below:

  `scrape(['Michael Jordan', 'Kobe Bryant'], 'advanced')`

This code will generate multiple .csv files of Michael Jordan and Kobe Bryant's Per Game statistics.

  ![alt text](https://github.com/irakojf/statmamba/blob/master/readme%20imgs/scrape.png?raw=true "scrape")

### Parameter Details

#### players:

Player names must be formatted as strings in the list data structure.

	e.g. `[ 'Kobe Bryant', 'Michael Jordan', 'Lebron James' ]`

For single player queries, put the player as the only element in the list.

	e.g. `[ 'Kobe Bryant' ]`

#### div:

On Basketball Reference, stat tables are typically enclosed in `<div>` tags that look like this:

	`<div id = 'div_per_game'>`

The scrape function takes the value of the div id, excluding the string 'div_'. So for the example above, a valid parameter would be **'per_game'**.

Below is a list of generally acceptable div parameters.

  | Statistic           | Parameter      | `<div id = ' '>` |
  | ------------------- | -------------- | ---------------- |
  | Per Game            | per_game       | div_per_game     |
  | Totals              | totals         | div_totals       |
  | Per 36 Minutes      | per_minutes    | div_per_minutes  |
  | Per 100 Possessions | per_poss       | div_per_poss     |
  | Advanced Stats      | advanced       | div_advanced     |
  | Shooting            | shooting       | div_shooting     |
  | Play-by-Play        | advanced_pbp   | div_advanced_pbp |

If the table can be found on Basketball Reference, it can most-likely be scraped. For tables outside of this list, you can use Chrome Development Tools to find the `div id` name.

<a name='teamquery'></a>
## Scraping Team Data
### team_query( team, year, div )

StatMamba can collect aggregate team data for any team for any given time period (in years).

The team_query function takes three parameters: (1) the team name, represented by the official team acronym, (2) year, and (3) the name of the of table being scraped, represented by the 'id' value in the `<div id=' '>` tag.

The function saves the table as a Pandas dataframe or .csv file.

For example, calling `team_query( 'LAL, '2013', 'per_game' )` will produce a comma separated value file with the Los Angeles Lakers' per game stats in the following directory path:

	`.../LAL_per_game_exports/LAL2013.csv`

Proper usage of team_query is as below:

	`team_query('NYK', '2013', 'per_game')`

Repeat the functional call with different parameters for different years or teams.

  ![alt text](https://raw.githubusercontent.com/irakojf/statmamba/master/readme%20imgs/team_query.png "team query")

### Parameter Details

#### team:

The team parameter must be a string containing the abbreviated version of the team name.

  e.g. `'LAL'` or `'NYK'`

#### year:

The year parameter is a string and not an integer.

#### div:

On Basketball Reference, stat tables are typically enclosed in `<div>` tags that look like this:

	`<div id = 'div_per_game'>`

The scrape function takes the value of the div id, excluding the string 'div_'. So for the example above, a valid parameter would be **'per_game'**.

| Statistic           | Parameter      | `<div id = ' '>` |
| ------------------- | -------------- | ---------------- |
| Per Game            | per_game       | div_per_game     |
| Totals              | totals         | div_totals       |
| Advanced Stats      | advanced       | div_advanced     |

If the table can be found on Basketball Reference, it can most-likely be scraped. For tables outside of this list, you can use Chrome Development Tools to find the `div id` name.

<a name='plot'></a>
## Plotting Data
### plot( players, div, stat, perchange )

StatMamba can also create line charts for a player's statistical data. The **plot** function produces a line graph of a player's stat over time (e.g. Assists per season).

**Note:** In order to use **plot**, you must have already called the **scrape** function for that particular player. Thus, plot must be used in conjunction with scrape and cannot be called on its own.

Proper usage of **scrape** and **plot** is as such:

	`scrape(['Michael Jordan'], 'advanced')
	plot('Michael Jordan', 'advanced', 'PER', True)`

This code generates a .csv file of Michael Jordan's advanced stats, and plots his percent change in PER over time.

  ![alt text](https://raw.githubusercontent.com/irakojf/statmamba/master/readme%20imgs/plot.png "plot")

### Parameter Details

#### player:

A player's first and last name, in string format.

#### div:

The div parameter for **plot** is same as that of **scrape**.

#### stat:

A variable representing the type of statistic in question such as 'PER' or 'AST', dependent on the type of table being scraped. For example, 'PER' can only be accessed if parameter (2) == 'advanced'.

#### perchange:

A binary variable equal to `True` or `False`. The **perchange** parameter acts a switch, such that if `perchange == True`, the plot function produces a line graph with the stat variable's percent change over time. If `perchange == False`, the plot function simply produces a regular line graph of the stat over time.

<a name='plotavg'></a>
## Plotting Change over Time
### plot_with_avg ( players, div, stat, perchange )

You can find a stat's change over time with an average trendline using the function **plot_with_avg**, which takes the same parameters as the **plot** function.

Proper usage of the **plot_with_avg** function:

  `scrape(['Kobe Bryant'], 'advanced')
  plot_with_avg('Kobe Bryant', 'advanced', 'PER', True)`

This code produces Kobe Bryant's percent change in PER over time and indicates the average percent change across all seasons.

  ![alt text](https://raw.githubusercontent.com/irakojf/statmamba/master/readme%20imgs/plot.png "plot with average")

### Interpretation using plot_with_avg

By the looking at the graph produced by the **plot_with_avg** function, you can get a sense of a player's consistency for that particular statistic.

For example, calling the **plot_with_avg** function with Isaiah Thomas and DeAndre Jordan produces the following charts.

	`plot_with_avg('Isaiah Thomas', 'advanced', 'PER', True)
	plot_with_avg('DeAndre Jordan, 'advanced', 'PER', True)`

  ![alt text](https://raw.githubusercontent.com/irakojf/statmamba/master/readme%20imgs/it.png "Isaiah Thomas")
  ![alt text](https://raw.githubusercontent.com/irakojf/statmamba/master/readme%20imgs/dj.png "DeAndre Jordan")

The small range of values on the y-axis indicates that the player efficiency ratios of both Isaiah Thomas and DeAndre Jordan have generally remained consistent over time. With the exception of Isaiah Thomas's breakout performance in 2016-17, his PER variance has changed (improved) at a consistent rate.

This is observation is corroborated by external sources;  [eDraft.com](http://edraft.com/nba/fantasy-basketball/tools/player-consistency/) lists Isaiah Thomas and DeAndre Jordan as two of the most consistent players in the NBA.

## Usage with Pandas

StatMamba creates Pandas dataframes for easy manipulation. Most Pandas functions like .iloc work with StatMamba. Learn more about [Pandas](http://pandas.pydata.org/).

## Built With

* [SeleniumHQ](http://www.seleniumhq.org/)
* [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
* [Pandas](http://pandas.pydata.org/)
* [Basketball Reference](http://www.basketball-reference.com/)
* [Spyder](https://github.com/spyder-ide/spyder)

## Acknowledgments

* Thanks to [Basketball Reference](http://www.basketball-reference.com/) for its excellent work on basketball data collection.
* Thanks to [Scott Rome](http://srome.github.io/) for his excellent article on parsing HTML Tables with Python.
