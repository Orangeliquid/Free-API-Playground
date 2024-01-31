import requests

# Delving into the free APIs found at "https://github.com/public-apis/public-apis"
# ------------------------------------------------------------------------------------------------- #

# Breaking bad API - gets 1 quote and author return json -

bb_endpoint = "https://api.breakingbadquotes.xyz/v1/quotes"
# quote_json = requests.get(url=bb_endpoint).json()
# dict_quote = quote_json[0]["quote"]
# dict_author = quote_json[0]["author"]
# print(f"{dict_quote} - {dict_author}")

# add "/{quantity}" to get multiple quotes
# quantity_of_quotes = 3
# bb_endpoint_multiple = f"{bb_endpoint}/{quantity_of_quotes}"
# quotes_json = requests.get(url=bb_endpoint_multiple).json()
# # print(quotes_json)
# for i in range(quantity_of_quotes):
#     print(f"{quotes_json[i]['quote']} - {quotes_json[i]['author']}\n")

# -------------------------------------------------------------------------- #

# This endpoint returns a json with a random emoji html code based on category
# chosen, there is also specific groups to further the search if need be

emoji_endpoint = "https://emojihub.yurace.pro/api"
# random_endpoint = f"{emoji_endpoint}/random/"
# all_endpoint = f"{emoji_endpoint}/all/"
# category_dict = {'category': ["smileys-and-people",
#                               "animals-and-nature",
#                               "food-and-drink",
#                               "travel-and-places",
#                               "activities",
#                               "objects",
#                               "symbols",
#                               "flags",
#                               ]
#                  }

# print(requests.get(url=f"{random_endpoint}category/{category_dict['category'][0]}").json())

# ---------------------------------------------------------------------------------- #

# PurgoMalum is a simple, free, RESTful web service for filtering and removing content of
# profanity, obscenity and other unwanted text.

purgo_endpoint = "https://www.purgomalum.com/service/json?text="
purgo_profanity_endpoint = "https://www.purgomalum.com/service/containsprofanity?text="

# text_input = input("Please enter a small sentence: ")
#
# adjusted_text = requests.get(url=f"{purgo_endpoint}{text_input}").json()['result']
# prof_test = requests.get(url=f"{purgo_profanity_endpoint}{text_input}").json()
#
#
# if prof_test:
#     print(f"\nYour text:'{text_input}' Contains profanity!\n")
#     print(f"Here is the fixed text '{adjusted_text}'")
# else:
#     print(f"\nNo profanity found in '{text_input}'")

# --------------------------------------------------------------------------------------------- #

# The Bored API - Let's find you something to do
bored_endpoint = "https://www.boredapi.com/api/activity/"
# bored_response = requests.get(url=bored_endpoint).json()
# for key, value in bored_response.items():
#     print(f"{key} / {value}")

# ---------------------------------------------------------------------------------------------- #

# Free dictionary API
dictionary_endpoint = "https://api.dictionaryapi.dev/api/v2/entries/en/"
# word_input = input("Please enter a word: ").lower()
# response = requests.get(url=f"{dictionary_endpoint}{word_input}")
# print(response.json())

# ---------------------------------------------------------------------------------------------- #

# an API for useless facts
useless_endpoint = "https://uselessfacts.jsph.pl/api/v2/facts/random"
# useless_response = requests.get(url=useless_endpoint).json()
# print(useless_response["text"])

# ------------------------------------------------------------------------------------------------ #

# an API for tech savy sounding phrases! - json or text can be placed at the end of the endpoint
techy_endpoint = "https://techy-api.vercel.app/api/json"
# techy_response = requests.get(url=techy_endpoint).json()
# print(techy_response["message"])

# ------------------------------------------------------------------------------------------------- #

# an API for Yo Mama jokes - Actual api is down on heruku
# yo_mama_endpoint = "https://yomamma-api.herokuapp.com/jokes"
# yo_mama_response = requests.get(url=yo_mama_endpoint)
# print(yo_mama_response.text)

# ------------------------------------------------------------------------------------------------- #

# Wall street bets api to get top 50 stocks discussed
wsb_endpoint = "https://tradestie.com/api/v1/apps/reddit"
# wsb_response = requests.get(url=wsb_endpoint).json()
# for stock_info in wsb_response:
#     print(stock_info)

# -------------------------------------------------------------------------------------------------- #

# An API for breweries - I have selected city as a parameter
brewery_endpoint = "https://api.openbrewerydb.org/v1/breweries/?by_city=columbus&per_page=5"
# brewery_response = requests.get(url=brewery_endpoint).json()
# for brewery in brewery_response:
#     print(f"Name: {brewery['name']}")
#     print(f"Type: {brewery['brewery_type']}")
#     print(f"Address: {brewery['address_1']}")
#     print(f"Phone #: {brewery['phone']}")
#     print(f"Website: {brewery['website_url']}")
#     print("\n")

# --------------------------------------------------------------------------------------------------- #

# an API for cheap games called Cheapshark API
deals_endpoint = "https://www.cheapshark.com/api/1.0/deals?storeID=1&upperPrice=15"
# deals_response = requests.get(url=deals_endpoint).json()
# for deals in deals_response:
#     print(f"Title: {deals['title']}")
#     print(f"Normal Price: {deals['normalPrice']}")
#     print(f"Sale Price: {deals['salePrice']}")
#     print(f"Savings Percent: {deals['savings']}")
#     print(f"Metacritic Score: {deals['metacriticScore']}")
#     print(f"Steam Rating Text: {deals['steamRatingText']}")
#     print(f"Steam Rating Percent: {deals['steamRatingPercent']}")
#     print(f"Steam App Id: {deals['steamAppID']}")
#     print(f"Deal Rating: {deals['dealRating']}")
#     print(f"Thumbnail: {deals['thumb']}\n")

# ----------------------------------------------------------------------------------------------------- #

# Chess.com API - I am using to look at users - cannot get this to work yet - 403 error
username = 'Hardymj'
chess_endpoint = "https://api.chess.com/"
# # chess_endpoint = f"https://api.chess.com/pub/player/{username}/stats"
# chess_response = requests.get(url=chess_endpoint)
# print(chess_response)

# ----------------------------------------------------------------------------------------------------- #

# Corporate buzz word API
corp_endpoint = "https://corporatebs-generator.sameerkumar.website/"
# corp_response = requests.get(url=corp_endpoint).json()
# print(corp_response["phrase"])

# ----------------------------------------------------------------------------------------------------- #

# Currently service is down - 503 error
# Website carbon footprint API
footprint_url = "https://google.com/"
carbon_footprint_endpoint = f"https://api.websitecarbon.com/site?url={footprint_url}"
# carbon_footprint_response = requests.get(url=carbon_footprint_endpoint)
# print(carbon_footprint_response)

# ------------------------------------------------------------------------------------------------------ #

# Gov Treasury API
treasury_endpoint = "https://api.fiscaldata.treasury.gov/services/api/fiscal_service"
daily_treasury_stmt = "/v1/accounting/dts/deposits_withdrawals_operating_cash"
# testing_treasury_enpoint = f"{treasury_endpoint}{daily_treasury_stmt}"
# treasury_response = requests.get(url=testing_treasury_enpoint).json()
# # print(type(treasury_response["data"]))
# for info in treasury_response["data"]:
#     print(info)

# ------------------------------------------------------------------------------------------------------ #

# Dark Joke API - Any Jokes is on so all categories are available(dark stuff)
djoke_endpoint = "https://v2.jokeapi.dev/joke/Any"
djoke_response = requests.get(url=djoke_endpoint).json()
# print(djoke_response)
# if djoke_response['setup']:
#     print(f"Setup: {djoke_response['setup']}")
#     print(f"Delivery: {djoke_response['delivery']}")
# else:
#     print(djoke_response["joke"])

# ----------------------------------------------------------------------------------------------------- #

# Trivia Questions API
trivia_endpoint = "https://opentdb.com/api.php?amount=1&type=boolean"
# trivia_response = requests.get(url=trivia_endpoint).json()
# print(trivia_response['results'][0]["question"])
# ready_input = input("True of False? (Type T or F): ").upper()
# if ready_input[0] == trivia_response['results'][0]["correct_answer"][0]:
#     print("Correct")
# else:
#     print("Wrong, The correct answer is....")
#     print(trivia_response['results'][0]["correct_answer"])

# ----------------------------------------------------------------------------------------------------- #

# Pokemon API! Fetch info about Pokemon! This will fetch a massive amount of info on specific Pokemon
pokemon_endpoint = "https://pokeapi.co/api/v2/pokemon/"
# pokemon_select = input("Please enter the name of a Pokemon: ").lower()
# pokemon_select_endpoint = f"https://pokeapi.co/api/v2/pokemon/{pokemon_select}"
# pokemon_response = requests.get(url=pokemon_select_endpoint).json()
# print(pokemon_response)

# ----------------------------------------------------------------------------------------------------- #

# Tronald Dump API for Donny T worst quotes
tronald_endpoint = "https://api.tronalddump.io/random/quote"
# tronald_response = requests.get(url=tronald_endpoint).json()
# print(tronald_response['value'])

# ----------------------------------------------------------------------------------------------------- #

# FBI most wanted list - params for Cleveland Field office
fbi_endpoint = "https://api.fbi.gov/wanted/v1/list"
# fbi_response = requests.get(url=fbi_endpoint, params={'field_offices': 'cleveland'}).json()
# print(fbi_response)

# ----------------------------------------------------------------------------------------------------- #

# Corona virus data API - massive json return of data
corona_endpoint = "https://coronavirus.m.pipedream.net/"
# corona_response = requests.get(url=corona_endpoint).json()
# print(corona_response)

# ----------------------------------------------------------------------------------------------------- #

# Binary Jazz API - generates a genre of music - most likely fictional
bjazz_genre_endpoint = "https://binaryjazz.us/wp-json/genrenator/v1/genre/"  # for genre
# bjazz_genre_response = requests.get(url=bjazz_genre_endpoint).json()
# print(bjazz_genre_response)
# This endpoint is for story
bjazz_story_endpoint = "https://binaryjazz.us/wp-json/genrenator/v1/story/"  # for story
# bjazz_story_response = requests.get(url=bjazz_story_endpoint).json()
# print(bjazz_story_response)

# Combined the random genre with a random story!
# print(f"{bjazz_genre_response}...{bjazz_story_response}")

# ------------------------------------------------------------------------------------------------- #

# Wayback Machine APIs - checks most recent archive of url entered
# wbm_url = input("Enter a url to check: ")
# wbm_endpoint = f"http://archive.org/wayback/available?url={wbm_url}"
# wbm_response = requests.get(url=wbm_endpoint).json()
# print(wbm_response)

# ------------------------------------------------------------------------------------------------- #

# Nobel Peace Prizes - Laureates
# usd_conversion = 0.1
# npp_year_input = input("Please enter a year: ")
# npp_endpoint = f"https://api.nobelprize.org/2.1/nobelPrizes?nobelPrizeYear={npp_year_input}"
# npp_response = requests.get(url=npp_endpoint).json()
# npp_narrowed = npp_response['nobelPrizes']
# npp_laureates = npp_narrowed[2]['laureates']
# category_count = 0
#
# for nobel_prize in npp_narrowed:
#     # print(nobel_prize)
#     print(f"\nCategory: {nobel_prize['category']['en']}")
#     print(f"Award Year: {nobel_prize['awardYear']}")
#     print(f"Date Awarded: {nobel_prize['dateAwarded']}")
#     print(f"Prize Amount: ${nobel_prize['prizeAmountAdjusted'] * usd_conversion}(Converted to USD)")
#
#     for winner in npp_narrowed[category_count]['laureates']:
#         # print(winner)
#         if 'fullName' in winner and winner['fullName']['en']:
#             print(f"Laureate Name: {winner['fullName']['en']}, ID: {winner['id']}")
#         elif 'orgName' in winner and winner['orgName']['en']:
#             print(f"Organization Name: {winner['orgName']['en']}, ID: {winner['id']}")
#         else:
#             continue
#
#         print(f"Motivation: {winner['motivation']['en']}")
#         print(f"Link: {winner['links'][0]['href']}\n")
#
#     category_count += 1

# ------------------------------------------------------------------------------------------------- #
