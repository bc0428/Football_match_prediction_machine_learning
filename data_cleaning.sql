-- create base table for each year data and import from local csv
create table 2021epl(
    match_date date,
    home_team varchar(15),
    away_team varchar(15),
    Home_Team_Goals int,
    Away_Team_Goals int,
    Full_Time_Result varchar(1),
    Home_Team_Shots int,
    Away_Team_Shots int,
    Bet365_home_win_odds decimal(3,2),
    Bet365_draw_odds decimal(3,2),
    Bet365_away_win_odds decimal(3,2),
    over_2_5 decimal(3,2),
    under_2_5 decimal(3,2)
);

load data local infile '21.csv' 
into table 2021epl  
fields terminated by ',' 
ignore 1 lines;


-- data cleaning by creating view
-- home_win_index: away odds / home odds
-- goal_difference: goals by home - goals by away
-- SOT_difference: shot on target difference, SOT by home - away
-- over_under_2_5_index: odds of under 2.5 goals / odds of over 2.5 goals
create view temp21 as
select match_date,
bet365_home_win_odds as home_odds, bet365_away_win_odds as away_odds,
bet365_away_win_odds/bet365_home_win_odds as H_win_index,
Bet365_draw_odds as draw_odds,Full_Time_Result as result,
Home_Team_Goals - Away_Team_Goals as goal_difference,
Home_Team_Shots - Away_Team_Shots as SOT_difference,
Home_Team_Goals + Away_Team_Goals as total_goal,
over_2_5 as over_2_5_odds, under_2_5 as under_2_5_odds,
under_2_5/over_2_5 as over_under_2_5_index
from 2021epl
limit 400;



-- merge years of csv
create view all_temp as
select * from temp21 
union
select * from temp20 
union
select * from temp19 
union
select * from temp18 
union
select * from temp17 
union
select * from temp16
limit 2500;



-- quick compare between averages over years to particular years to evaluate frequency of outliers
create view compare as
select (all_temp.h_win_index) as win_index, (all_temp.draw_odds) as draw_odds, all_temp.result as result,
(temp21.h_win_index) as 21_win_index, (temp21.draw_odds) as 21_draw_odds
from all_temp 
inner join temp21
on all_temp.result = temp21.result;

select avg(win_index), avg(draw_odds), result, avg(21_win_index), avg(21_draw_odds) from compare group by result;



-- analyse over/under 2.5 goals reliability for goals prediction
-- mean under-to-over 2.5 goals index(uto index) for 3 goals: 1.1901315941, goals>3 also show indices>1.19
select (total_goal), avg(over_under_2_5_index), count(result) from all_temp group by total_goal  order by total_goal desc limit 2500;



-- matches with uto index>1.19 compared to actual goals in reality
-- true positive: 0.2492
select (select count(*) from all_temp where total_goal >=3 and over_under_2_5_index>1.19) / (select count(*) from all_temp);
-- false positive: 0.1688 
select (select count(*) from all_temp where total_goal <3 and over_under_2_5_index>1.19) / (select count(*) from all_temp);
-- true negative: 0.3088
select (select count(*) from all_temp where total_goal <3 and over_under_2_5_index<1.19) / (select count(*) from all_temp);
-- false negative: 0.2726 
select (select count(*) from all_temp where total_goal >=3 and over_under_2_5_index<1.19) / (select count(*) from all_temp);
-- accuracy: 0.558  

select * from all_temp limit 2500;


