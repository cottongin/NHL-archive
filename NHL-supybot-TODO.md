# NHL Plugin for supybot/limnoria TODO List

List of functions to implement in NHL plugin for supybot.  This is intended to mostly mimic functionality of existing code but *may* exclude features or include new/different ones.

"API" exists (mostly just json data). See http://hfboards.hockeysfuture.com/showthread.php?t=1596119

**Function**                    |   **Description**                                                                       | **Status**
--------------------------------|-----------------------------------------------------------------------------------------|--------------------------------------------
stats <player> [year]           |   player's season stats                                                                 | TODO (API?)
stats2 <player> [year]          |   use this for older players                                                            | TODO (API?) (oldstats)
stats <player> career           |   player's career nhl totals                                                            | TODO (API?)
stats2 <player> career          |   ^                                                                                     | TODO (API?) (oldstats)
pstats <player> [year/career]   |   ^ same as stats but for playoffs                                                      | TODO (combine/simplify into stats?)
gstats <player>                 |   player's game stats for games in progress/recently finished                           | TODO (API?)
tstats <team>                   |   team's seasonal stats                                                                 | TODO (API?)
nhlstandings <div/conf> [-p]    |   standings for division/conference use -p for wildcard                                 | TODO (API/scrape?)
nhlleaders <category>           |   seasonal stat leaders. g, a, pts, +/-, wins, gaa, sv%, shutouts                       | TODO (API?)
cap <player/team>               |   player's salary info or team's cap situation [uses capgeek.com]                       | TODO (http://www.generalfanager.com/)
summary <team> [date]           |   game's summary (score, attendance, shots, goals)                                      | TODO
playoffs <team>                 |   up until playoffs: shows team's chances at making playoffs                            | TODO (is this an API thing?)
playoffs [team]                 |   during playofs: shows playoff matches/outcome                                         | TODO (see above)
nhlnews <player>                |   latest news involving player [uses rotowire.com]                                      | TODO (google news too?)
sched <team> [opponent] [count] |   finds next games involing team (oponnent for only vs that team)                       | exclude (just use next/last?)
next# <team> [opponent]         |   like sched, but easier syntax (ie next3 toronto)                                      | TODO
last# <team> [opponent]         |   ^ results from last # games (ie last3 leafs)                                          | TODO
nhl [team] [date]               |   scores/results from the nhl, use '*' for all, use blank for only games in progress    | exclude (built-in to Scores plugin already)
hockey [team] [date]            |   lots of hockey scores (OHL/AHL/NHL/etc/etc)                                           | TODO
<league> [team] [date]          |   other league scores (NBA/MLB/NFL/Nascar?) [uses yahoo.com]                            | exclude (implemented by Scores plugin)
goalie <team> [date]            |   find which goalie will start for a team [uses dailyfaceoff.com]                       | TODO
daily [date]                    |   daily leaders, top 5 skaters                                                          | exclude? (is this useful?)
odds <league> <team> [date]     |   betting odds [uses yahoo.com]                                                         | exclude (implemented by Odds plugin)
goal <team> <index> [date]      |   find the video clip for a goal                                                        | TODO
--------------------------------|-----------------------------------------------------------------------------------------|--------------------------------------------
live scoring (GoalBot)          |   provides live scores and other major plays                                            | TODO (API)