def get_player_score(player_number, month):
	score = None 
	while not isinstance(score, int): 
		try: 
			score = input("What was Player %r's score for %r? " % (player_number, get_month[month]))
		except NameError, EOFError: 
			pass
	return score 

def scores_for_the_month_of(month):
	while True: 
		player_1 = get_player_score(1, month) 
		player_2 = get_player_score(2, month) 
		player_3 = get_player_score(3, month)
		if  player_1 + player_2 + player_3 == 0:
			return player_1, player_2, player_3 
		print "-----SCORES DON'T ADD UP-----"

def main(): 
	for month in range(12): 
		print "-----%r-----" % get_month[month]
		score_tally.insert(month, scores_for_the_month_of(month)) 
		player_1 = sum(score_tally[i][0] for i in range(month+1))
		player_2 = sum(score_tally[i][1] for i in range(month+1))
		player_3 = sum(score_tally[i][2] for i in range(month+1))
		print "Total: Player 1: %r, Player 2: %r, Player 3: %r" % (player_1, player_2, player_3)

if __name__ == '__main__': 
	score_tally = []
	get_month = { 0 : "January", 
		      1 : "February",
		      2 : "March",
		      3 : "April",
		      4 : "May", 
		      5 : "June",
	 	      6 : "July",
		      7 : "August",
		      8 : "September",
		      9 : "October",
		     10 : "November",
		     11 : "December" }
	main()



		


