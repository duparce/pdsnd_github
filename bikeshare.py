#coding:utf-8

import time 
import datetime
import pandas as pd
import numpy as np 
import copy 




CITY_DATA = { 'chicago': 'chicago.csv',
			  'new york': 'new_york_city.csv',
			  'washington': 'washington.csv' }

CITY_DATA_COMPARE = CITY_DATA.copy()
month_day_compare = {}

# for getting user input for city (chicago, new york city, washington), month and day
def get_filters():
		
	city = input("which data's town do you want to analyze chicago, new york or washington? type one of those towns :\n ") 

	while city not in ("chicago", "new york", "washington"):

		print("incorrect answer!! please type exactly one of the town's name given") 
		city = input("which data's town do you want to analyze chicago, new york or washington? type one of those towns :\n ")
		
	city_one = CITY_DATA_COMPARE.pop(city)

	# for getting user input for month (all, january, february, ... , june)

	month = input("which month do you want to analyze: January, February, March, April, May, June or all? type 'all' or one of those months (please respect the case...):\n ") 

	while month not in ("January", "February", "March", "April", "May", "June", "all"):

		print("incorrect answer!! please type exactly one of the months given or 'all' to analyze all the month") 
		month = input("which month do you want to analyze: January, February, March, April, May, June or all? type 'all' or one of those months (please respect the case...):\n ")  

	month_day_compare["month_compare"] = month 

	# for getting user input for day of week (all, monday, tuesday, ... sunday)
	
	day = input("which day do you want to analyze: Monday, Tuesday, Wednesday, Thurday, Friday, Saturday, Sunday or all of them? type 'all' or one of those days (please respect the case...):\n ")
	 
	while day not in ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday", "all"): 
		print("incorrect answer!! please type exactly one of the day given or type 'all' to analyze all the days") 
		day = input("which day do you want to analyze: Monday, Tuesday, Wednesday, Thurday, Friday, Saturday, Sunday or all of them? type 'all' or one of those days (please respect the case...):\n ?:\n  ")  
	
	month_day_compare["day_compare"] = day 

	print('\n''\n''\n''Hello! Let\'s explore some US bikeshare data!') 
	print('-'*40)
	return city, month, day



# load the data for all months and all the days
def load_data(city, month, day):
	
	if month == "all":
		if day == "all":
			df = pd. read_csv(CITY_DATA[city])  
			
		# load the data for all months but with a specific day	
		else:		 
			df = pd. read_csv(CITY_DATA[city])
			df['Start Time'] = pd.to_datetime(df['Start Time'])
			df['day_of_week'] = df['Start Time'].dt.weekday_name 
			df = df[df['day_of_week'] == day] 
	

	
	else: 
		if day =="all":  # load data for a specific month with all the days
			df = pd. read_csv(CITY_DATA[city]) 
			df['Start Time'] = pd.to_datetime(df['Start Time']) 
			df['month_of_year'] = df['Start Time'].dt.month 
			months = ["January", "February", "March", "April", "May", "June"] 
			month_index = months.index(month)+1 			
			df = df[df['month_of_year'] == month_index] 


		# load data for a specific month with a specific day
		else:
			df = pd. read_csv(CITY_DATA[city]) 
			df['Start Time'] = pd.to_datetime(df['Start Time']) 
			df['month_of_year'] = df['Start Time'].dt.month 
			df['day_of_week'] = df['Start Time'].dt.weekday_name
			months = ["January", "February", "March", "April", "May", "June"] 
			month_index = months.index(month)+1
			df = df[df["month_of_year"] == month_index]
			df = df[df['day_of_week'] == day.title()] 

	return df   
		

"""Displays statistics on the most frequent times of travel."""
def time_stats(df):
	
	time_stats_view = input("Would you like to view some time statistics? type 'yes' or 'no' \n")
	while time_stats_view not in ("yes", "no"):
		print("type 'yes' or 'no' please, thank you")
		time_stats_view = input("Would you like to view some time statistics? type 'yes' or 'no' \n")
	if time_stats_view == "yes":

		print('\nCalculating The Most Frequent Times of Travel...\n')
		start_time = time. time() 


		# display the month in the case where a specific month has been chosen
		if "month_of_year" in df.columns:
			months = ["January", "February", "March", "April", "May", "June"] 
			month_index = df["month_of_year"]-1 
			month_index = month_index.iloc[1] 
			month = months[month_index] 
			print("\nthe month choosed for analysis is the month of : {}".format(month)) 

		# display the most common month in the case where all the months have been choosen for analysis
		else:
			df["Start Time"] = pd.to_datetime(df["Start Time"]) 
			df["month_of_year"] = df["Start Time"].dt.month 
			common_month = df["month_of_year"].mode()[0]  
			months = ["January", "February", "March", "April", "May", "June"]  
			common_month = common_month-1  
			common_month = months[common_month]  
			print("\n\nthe most common month is the month of : {} ".format(common_month)) 
			

		# display the day in case of a specific day choosen	
		if "day_of_week" in df.columns:
			day_week = df.day_of_week.iloc[1] 
			print("\n\nthe day of analysis is: {}".format(day_week)) 

		# display the most common day in the case where all the days have been choosen for analysis	
		else:
			df['Start Time'] = pd.to_datetime(df['Start Time']) 
			df['day_of_week'] = df['Start Time'].dt.weekday_name 
			common_day = df["day_of_week"].mode()[0] 
			print("\n\nthe most common day of the week is: {}".format(common_day)) 

			
		# display the most common start hour for travel
		df["Start Time"] =  pd.to_datetime( df["Start Time"]) 
		df["start_hour"] = df["Start Time"].dt.hour 
		common_hour = df["start_hour"].mode()[0] 
		print ("\n\nthe most common start hour is: {}".format(common_hour)) 


		print("\nThis took %s seconds." % (time.time() - start_time))
		print('-'*40)




	

"""Displays statistics on the most popular stations and trip."""
def station_stats(df):
	
	station_stats_view = input("Would you like to view some station statistics? type 'yes' or 'no' \n")
	while station_stats_view not in ("yes", "no"):
		print("type 'yes' or 'no' please, thank you")
		station_stats_view = input("Would you like to view some station statistics? type 'yes' or 'no' \n")
	if station_stats_view == "yes":

		print('\nCalculating The Most Popular Stations and Trip...\n')
		start_time = time.time() 

		# display the start station used the most
		common_start_station = df["Start Station"].value_counts()   	 
		common_start = common_start_station[0:1] 
		print("\nthe most commonly used start station is the station of :\n  {} ".format(common_start)) 


		# display the end station used the most 
		common_end_station = df["End Station"].value_counts() 
		common_end = common_end_station[0:1] 
		print("\n\nthe most commonly used end station is the station of :\n  {} ".format(common_end)) 

		# display the  most frequent couple [start station, end station]
		concat_stations = pd.concat([df["Start Station"], df["End Station"]], axis=1) 
		concat_stations = pd.DataFrame(concat_stations) 	
		travel_stations = concat_stations.sort_values(by = ["Start Station", "End Station"])
		travel_stations = travel_stations.mode()
		travel_stations = pd.DataFrame(travel_stations).iloc[0] 
		print("\n\nThe most frequent couple of start station  -  end station is the following: \n\n", travel_stations) 

		print("\nThis took %s seconds." % (time.time() - start_time))
		print('-'*40)


# function to extract the time (hours, minutes and seconds) from a number
def convert_hms(sec):
	q,s = divmod(sec,60)
	h,m = divmod(q,60)
	return "%d hours : %d minutes : %d seconds" %(h,m,s)

"""Displays statistics on the total and average trip duration."""
def trip_duration_stats(df):
	
	trip_duration_stats_view = input("Would you like to view some trip duration statistics? type 'yes' or 'no' \n")
	while trip_duration_stats_view not in ("yes", "no"):
		print("type 'yes' or 'no' please, thank you")
		trip_duration_stats_view = input("Would you like to view some trip duration statistics? type 'yes' or 'no' \n")

	if trip_duration_stats_view == "yes":

		print('\nCalculating Trip Duration...\n')
		start_time = time.time() 


		# display the total travel time
		trip_time = df["Trip Duration"].sum() 
		print("\nThe total travel time is : ",convert_hms(trip_time))  

		# display the mean travel time
		trip_mean = df["Trip Duration"].mean() 
		print("\n\nThe mean tavel time is: ", convert_hms(trip_mean)) 

		print("\nThis took %s seconds." % (time.time() - start_time))
		print('-'*40)



"""Displays statistics on bikeshare users."""
def user_stats(df):
	

	user_stats_view = input("Would you like to view some users statistics? type 'yes' or 'no' \n")
	while user_stats_view not in ("yes", "no"):
		print("type 'yes' or 'no' please, thank you")
		user_stats_view = input("Would you like to view some user statistics? type 'yes' or 'no' \n")

	if user_stats_view == "yes":

		print('\nCalculating User Stats...\n')
		start_time = time.time() 

		# display counts of user types
		users_count = df["User Type"].value_counts() 
		print("\nThis is the count of user types: \n", users_count) 

		# display counts of gender if information about the gender is given in the data
		if "Gender" in df.columns:
			user_gender = df["Gender"].value_counts() 
			print("\n\nThis is the count of genders : \n\n", user_gender) 

		# if there is no Gender column
		else:
			print("\n\nThere is no information about gender of subscribers") 


		# display the most recent and the earliest and the most common year of birth
		if "Birth Year" in df.columns:		
			recent_year = df["Birth Year"].max()
			early_year = df["Birth Year"].min()

			print("\n\nThe most recent year of birth is : ", recent_year) 
			print("\n\nThe earliest year of birth is : ", early_year) 

			common_birth = df["Birth Year"].mode()[0] 
			print("\n\nthe most common year of birth is: ", common_birth) 


		# if there is no column about birth of year
		else:
			print("\n\nThere is no information about the year of birth of users")

		print("\nThis took %s seconds." % (time.time() - start_time))
		print('-'*40)


#compare some statistics with another town on the same months and days choosed above 

def compare_towns():
	towns_set = []
	compare_test = input("would you like to compare statistics with another town? type 'yes' or 'no' \n")
	while compare_test not in ("yes", "no"):
		print("type 'yes' or 'no' please, thank you")
		compare_test = input("would you like to compare statistics with another town? type 'yes' or 'no' \n")

	# display towns except the one choosed before
	if compare_test == "yes":
		print("\n\nType one of the town below to compare with")
		for val in CITY_DATA_COMPARE.keys():
			print("\n",val)
			towns_set.append(val) 

		town_compare = input("\n")

		while town_compare not in towns_set[:]:
			print("\nIncorrect entry please type one of those towns below ") 
			print("\n",towns_set[:])
			town_compare = input("\n")

		
		# keep the month and day choosen above and the town name 
		month2 = month_day_compare["month_compare"]
		day2 = month_day_compare["day_compare"]
		for k in CITY_DATA.keys():
			if k not in CITY_DATA_COMPARE.keys():
				city_one = k

		# load data with months and day choosed
		df2 = load_data(town_compare, month2, day2)
		df1 = load_data(city_one, month2, day2) 

		# calculation of statistics to be compare
		users_count1 = df1["User Type"].value_counts()
		users_count2 = df2["User Type"].value_counts()


		df1["Start Time"] =  pd.to_datetime( df1["Start Time"]) 
		df1["start_hour"] = df1["Start Time"].dt.hour 
		common_hour1 = df1["start_hour"].mode()[0]

		df2["Start Time"] =  pd.to_datetime( df2["Start Time"]) 
		df2["start_hour"] = df2["Start Time"].dt.hour 
		common_hour2 = df2["start_hour"].mode()[0]


		df1["End Time"] =  pd.to_datetime( df1["End Time"]) 
		df1["End_hour"] = df1["End Time"].dt.hour 
		common_End_hour1 = df1["End_hour"].mode()[0]

		df2["End Time"] =  pd.to_datetime( df2["End Time"]) 
		df2["End_hour"] = df2["End Time"].dt.hour 
		common_End_hour2 = df2["End_hour"].mode()[0]


		trip_time1 = df1["Trip Duration"].sum()
		trip_time1 = convert_hms(trip_time1) 
		trip_time2 = df2["Trip Duration"].sum() 
		trip_time2 = convert_hms(trip_time2) 


		trip_mean1 = df1["Trip Duration"].mean()
		trip_mean1 = convert_hms(trip_mean1) 
		trip_mean2 = df2["Trip Duration"].mean()
		trip_mean2 = convert_hms(trip_mean2)  

		# display those statistics
		compare1 = {("User counts", city_one) : users_count1} 
		compare2 = {("User counts", town_compare) : users_count2}
		compare3 = {("Common start hour", city_one) : common_hour1}
		compare4 = {("Common start hour", town_compare) : common_hour2}
		compare5 = {("Common end hour", city_one) : common_End_hour1}
		compare6 = {("Common end hour", town_compare) : common_End_hour2}
		compare7 = {("Total travel time", city_one) : trip_time1}
		compare8 = {("Total travel time", town_compare) : trip_time2}
		compare9 = {("Mean travel time", city_one) : trip_mean1}
		compare10 = {("Mean travel time", town_compare) : trip_mean2}

		print("\n",compare1) 
		print("\n",compare2)
		print('_'*40)
		print(compare3) 
		print("\n",compare4)
		print('_'*40)
		print(compare5) 
		print("\n",compare6)
		print('_'*40)
		print(compare7) 
		print("\n",compare8)
		print('_'*40)
		print(compare9) 
		print("\n",compare10)
		print('_'*40)


		
		



# The main method
def main():
	while True:
		city, month, day = get_filters()
		df = load_data(city, month, day)
		
		time_stats(df)
		station_stats(df)
		trip_duration_stats(df)
		user_stats(df)
		compare_towns() 

		restart = input('\nThank you. Would you like to restart? Enter yes or no.\n')
		if restart.lower() != 'yes':
			break


if __name__ == "__main__":
	main()
