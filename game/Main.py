import random

from game import Play_Game
from game.Conference import Conference
from game.Division import Division
from positions.Cornerback import Cornerback
from positions.DefensiveEnd import DefensiveEnd
from positions.DefensiveTackle import DefensiveTackle
from positions.Linebacker import Linebacker
from positions.OffensiveLineman import OffensiveLineman
from positions.Quarterback import Quarterback
from positions.RunningBack import RunningBack
from positions.Safety import Safety
from positions.TightEnd import TightEnd
from positions.WideReceiver import WideReceiver
from teams.Field import Field
from teams.Team import Team


class Main:
    def __init__(self):
        self.team_list = []
        self.create_team_list()
        self.league = []
        self.set_conferences()
        self.game = Play_Game.start(random.choice(self.team_list), self.get_team("Omaha Oblivion"))
        # self.game = Play_Game.start(self.create_iowa(), self.create_nebraska())

    def create_las_vegas_knights(self):
        field = Field(color_1=(0, 100, 0), color_2=(0, 128, 0), yard_number_font_path=f"../Teams/fonts/CLARENDO.ttf", endzone_font_path=f"../Teams/fonts/vegas.ttf",
                      endzone_font_size=80, yard_number_font_size=50, endzone_1_text="LAS VEGAS", endzone_2_text="KNIGHTS")
        team = Team("Las Vegas Knights", field, logo=f"../Teams/team_logos/Vegas.png")
        team.set_color((164, 120, 50))
        team.secondary_color = ((167, 32, 35))
        self.create_random_players(team)

        return team

    def create_orlando_rebels(self):
        field = Field(color_1=(4, 201, 60), color_2=(4, 184, 91), yard_number_font_path=f"../Teams/fonts/CLARENDO.ttf", endzone_font_path=f"../Teams/fonts/Star_Wars.ttf",
                      endzone_font_size=80, yard_number_font_size=40, endzone_1_text="orlando", endzone_2_text="Rebels")
        team = Team("Orlando Rebels", field, logo=f"../Teams/team_logos/Orlando.png")
        team.set_color((112,156,211))
        team.secondary_color = ((37,33,33))
        self.create_random_players(team)

        return team

    def create_chicago_stallions(self):
        field = Field(color_1=(0, 110, 31), color_2=(1, 77, 22), yard_number_font_path=f"../Teams/fonts/Horse.ttf", endzone_font_path=f"../Teams/fonts/Horse.ttf",
                      endzone_font_size=80, yard_number_font_size=40, endzone_1_text="chicago", endzone_2_text="stallions", symmetrical=False,
                      yard_number_color=(155, 176, 161), yard_numbers_spaced=True, endzone_text_offset=-13)
        team = Team("Chicago Stallions", field, logo=f"../Teams/team_logos/Chicago.png")
        team.set_color((210,31,67))
        team.secondary_color = ((241,88,37))
        self.create_random_players(team)

        return team

    def create_miami_monstars(self):
        field = Field(color_1=(135, 235, 255), color_2=(251, 143, 255), yard_number_font_path=f"../Teams/fonts/CLARENDO.ttf", endzone_font_path=f"../Teams/fonts/Vice.ttf",
                      endzone_font_size=80, yard_number_font_size=40, endzone_1_text="MIAMI", endzone_2_text="Monstars", symmetrical=True,
                      yard_number_color=(255,255,255), yard_numbers_spaced=True, endzone_text_offset=13, midfield_logo_size=300)
        team = Team("Miami Monstars", field, logo=f"../Teams/team_logos/Miami.png")
        team.set_color((37,170,224))
        team.secondary_color = ((218,60,150))
        self.create_random_players(team)

        return team

    def create_san_diego_inferno(self):
        field = Field(color_1=(0, 87, 16), color_2=(0, 112, 22), yard_number_font_path=f"../Teams/fonts/Inferno.ttf", endzone_font_path=f"../Teams/fonts/Inferno.ttf",
                      endzone_font_size=80, yard_number_font_size=40, endzone_1_text="San Diego", endzone_2_text="Inferno", symmetrical=False,
                      yard_number_color=(255,255,255), yard_numbers_spaced=True, endzone_text_offset=0, midfield_logo_size=175)
        team = Team("San Diego Inferno", field, logo=f"../Teams/team_logos/SanDiego.png")
        team.set_color((225,31,37))
        team.secondary_color = ((51,18,17))
        self.create_random_players(team)

        return team

    def create_sacramento_kingfishers(self):
        field = Field(color_1=(56,166,124), color_2=(56,166,124), yard_number_font_path=f"../Teams/fonts/CLARENDO.ttf", endzone_font_path=f"../Teams/fonts/Cali.otf",
                      endzone_font_size=70, yard_number_font_size=40, endzone_1_text="Sacramento", endzone_2_text="Kingfishers", symmetrical=False,
                      yard_number_color=(255,255,255), yard_numbers_spaced=True, endzone_text_offset=5, midfield_logo_size=175)
        team = Team("Sacramento Kingfishers", field, logo=f"../Teams/team_logos/Sacramento.png")
        team.set_color((80,199,235))
        team.secondary_color = ((26,24,76))
        self.create_random_players(team)

        return team

    def create_new_york_nightingales(self):
        field = Field(color_1=(7, 64, 22), color_2=(2, 99, 28), yard_number_font_path=f"../Teams/fonts/CLARENDO.ttf", endzone_font_path=f"../Teams/fonts/Manhattan.ttf",
                      endzone_font_size=90, yard_number_font_size=40, endzone_1_text="New York", endzone_2_text="Nightingales", symmetrical=False,
                      yard_number_color=(255,255,255), yard_numbers_spaced=True, endzone_text_offset=0, midfield_logo_size=150)
        team = Team("New York Nightingales", field, logo=f"../Teams/team_logos/NewYork.png")
        team.set_color((247,148,29))
        team.secondary_color = ((0,0,0))
        self.create_random_players(team)

        return team

    def create_gotham_rogues(self):
        field = Field(color_1=(7, 64, 22), color_2=(2, 99, 28), yard_number_font_path=f"../Teams/fonts/Batman.ttf", endzone_font_path=f"../Teams/fonts/Batman.ttf",
                      endzone_font_size=70, yard_number_font_size=30, endzone_1_text="Gotham", endzone_2_text="Rogues", symmetrical=True,
                      yard_number_color=(255,255,255), yard_numbers_spaced=False, endzone_text_offset=0, midfield_logo_size=150)
        team = Team("Gotham Rogues", field, logo=f"../Teams/team_logos/Gotham.png")
        team.set_color((243,208,54))
        team.secondary_color = ((19,20,22))
        self.create_random_players(team)

        return team

    def create_jacksonville_gladiators(self):
        field = Field(color_1=(0, 54, 5), color_2=(0, 77, 8), yard_number_font_path=f"../Teams/fonts/CLARENDO.ttf", endzone_font_path=f"../Teams/fonts/Spartan.ttf",
                      endzone_font_size=100, yard_number_font_size=30, endzone_1_text="For Glory", endzone_2_text="Fight On", symmetrical=True,
                      yard_number_color=(255,255,255), yard_numbers_spaced=True, endzone_text_offset=-13, midfield_logo_size=275)
        team = Team("Jacksonville Gladiators", field, logo=f"../Teams/team_logos/Jacksonville.png")
        team.set_color((244,162,60))
        team.secondary_color = ((29,29,27))
        self.create_random_players(team)

        return team

    def create_los_angeles_vigilantes(self):
        field = Field(color_1=(0, 90, 10), color_2=(3, 130, 15), yard_number_font_path=f"../Teams/fonts/CLARENDO.ttf", endzone_font_path=f"../Teams/fonts/tribal.ttf",
                      endzone_font_size=60, yard_number_font_size=30, endzone_1_text="Los Angeles", endzone_2_text="Vigilantes", symmetrical=False,
                      yard_number_color=(255,255,255), yard_numbers_spaced=True, endzone_text_offset=0, midfield_logo_size=150)
        team = Team("Los Angeles Vigilantes", field, logo=f"../Teams/team_logos/LAV.png")
        team.set_color((231,37,44))
        team.secondary_color = ((236,229,46))
        self.create_random_players(team)

        return team

    def create_los_angeles_sirens(self):
        field = Field(color_1=(1, 99, 60), color_2=(0, 153, 92), yard_number_font_path=f"../Teams/fonts/Siren.otf", endzone_font_path=f"../Teams/fonts/Siren.otf",
                      endzone_font_size=70, yard_number_font_size=50, endzone_1_text="Los Angeles Sirens", endzone_2_text="California's Team", symmetrical=False,
                      yard_number_color=(255,255,255), yard_numbers_spaced=True, endzone_text_offset=-4, midfield_logo_size=250)
        team = Team("Los Angeles Sirens", field, logo=f"../Teams/team_logos/LAS.png")
        team.set_color((171,34,110))
        team.secondary_color = ((254,254,254))
        self.create_random_players(team)

        return team

    def create_memphis_werewolves(self):
        field = Field(color_1=(2, 56, 29), color_2=(0, 36, 18), yard_number_font_path=f"../Teams/fonts/CLARENDO.ttf", endzone_font_path=f"../Teams/fonts/werewolf.ttf",
                      endzone_font_size=100, yard_number_font_size=30, endzone_1_text="Memphis", endzone_2_text="Werewolves", symmetrical=True,
                      yard_number_color=(255,255,255), yard_numbers_spaced=True, endzone_text_offset=-10, midfield_logo_size=150)
        team = Team("Memphis Werewolves", field, logo=f"../Teams/team_logos/Memphis.png")
        team.set_color((28,136,179))
        team.secondary_color = ((249,250,251))
        self.create_random_players(team)

        return team

    def create_new_orleans_scorpions(self):
        field = Field(color_1=(8, 191, 75), color_2=(1, 143, 53), yard_number_font_path=f"../Teams/fonts/charity.ttf", endzone_font_path=f"../Teams/fonts/charity.ttf",
                      endzone_font_size=62, yard_number_font_size=35, endzone_1_text="New Orleans", endzone_2_text="Scorpions", symmetrical=True,
                      yard_number_color=(255,255,255), yard_numbers_spaced=True, endzone_text_offset=0, midfield_logo_size=150)
        team = Team("New Orleans Scorpions", field, logo=f"../Teams/team_logos/NewOrleans.png")
        team.set_color((29,55,99))
        team.secondary_color = ((184,169,134))
        self.create_random_players(team)

        return team

    def create_philadelphia_blizzard(self):
        field = Field(color_1=(1, 117, 44), color_2=(1, 117, 44), yard_number_font_path=f"../Teams/fonts/CLARENDO.ttf", endzone_font_path=f"../Teams/fonts/blizzard.ttf",
                      endzone_font_size=67, yard_number_font_size=35, endzone_1_text="Philadelphia", endzone_2_text="Blizzard", symmetrical=True,
                      yard_number_color=(255,255,255), yard_numbers_spaced=True, endzone_text_offset=0, midfield_logo_size=200)
        team = Team("Philadelphia Blizzard", field, logo=f"../Teams/team_logos/Philadelphia.png")
        team.set_color((9,114,184))
        team.secondary_color = ((235,234,149))
        self.create_random_players(team)

        return team

    def create_salt_lake_city_sinners(self):
        field = Field(color_1=(251,225,182), color_2=(218,164,109), yard_number_font_path=f"../Teams/fonts/CLARENDO.ttf", endzone_font_path=f"../Teams/fonts/cowboy.ttf",
                      endzone_font_size=50, yard_number_font_size=30, endzone_1_text="Salt Lake", endzone_2_text="Sinners", symmetrical=True,
                      yard_number_color=(255,255,255), yard_numbers_spaced=True, endzone_text_offset=6, midfield_logo_size=200)
        team = Team("Salt Lake City Sinners", field, logo=f"../Teams/team_logos/SaltLakeCity.png")
        team.set_color((239,127,38))
        team.secondary_color = ((178,201,233))
        self.create_random_players(team)

        return team

    def create_tampa_toucans(self):
        field = Field(color_1=(125, 227, 0), color_2=(14, 163, 0), yard_number_font_path=f"../Teams/fonts/CLARENDO.ttf", endzone_font_path=f"../Teams/fonts/beach.ttf",
                      endzone_font_size=80, yard_number_font_size=40, endzone_1_text="Tampa", endzone_2_text="Toucans", symmetrical=True,
                      yard_number_color=(255,255,255), yard_numbers_spaced=True, endzone_text_offset=0, midfield_logo_size=200)
        team = Team("Tampa Toucans", field, logo=f"../Teams/team_logos/Tampa.png")
        team.set_color((248,164,32))
        team.secondary_color = ((238,33,105))
        self.create_random_players(team)

        return team

    def create_atlanta_ocelots(self):
        field = Field(color_1=(12, 143, 0), color_2=(51, 186, 2), yard_number_font_path=f"../Teams/fonts/CLARENDO.ttf", endzone_font_path=f"../Teams/fonts/tiger.otf",
                      endzone_font_size=100, yard_number_font_size=30, endzone_1_text="Atlanta", endzone_2_text="Ocelots", symmetrical=False,
                      yard_number_color=(255,255,255), yard_numbers_spaced=True, endzone_text_offset=0, midfield_logo_size=150)
        team = Team("Atlanta Ocelots", field, logo=f"../Teams/team_logos/Atlanta.png")
        team.set_color((220,32,49))
        team.secondary_color = ((248,242,243))
        self.create_random_players(team)

        return team

    def create_austin_infamous(self):
        field = Field(color_1=(24, 92, 0), color_2=(24, 92, 0), yard_number_font_path=f"../Teams/fonts/CLARENDO.ttf", endzone_font_path=f"../Teams/fonts/nightmare.otf",
                      endzone_font_size=88, yard_number_font_size=35, endzone_1_text="Welcome to Your", endzone_2_text="Worst Nightmare", symmetrical=False,
                      yard_number_color=(200,200,200), yard_numbers_spaced=True, endzone_text_offset=0, midfield_logo_size=250)
        team = Team("Austin Infamous", field, logo=f"../Teams/team_logos/Austin.png")
        team.set_color((206,125,54))
        team.secondary_color = ((249,177,52))
        self.create_random_players(team)

        return team

    def create_omaha_oblivion(self):
        field = Field(color_1=(33, 122, 1), color_2=(62, 128, 38), yard_number_font_path=f"../Teams/fonts/CLARENDO.ttf", endzone_font_path=f"../Teams/fonts/oblivion.ttf",
                      endzone_font_size=88, yard_number_font_size=30, endzone_1_text="Nebraska", endzone_2_text="Oblivion", symmetrical=False,
                      yard_number_color=(255, 255, 255), yard_numbers_spaced=True, endzone_text_offset=0, midfield_logo_size=0)
        team = Team("Omaha Oblivion", field, logo=f"../Teams/team_logos/Omaha.png")
        team.set_color((0, 0, 0))
        team.secondary_color = ((189,190,192))
        self.create_random_players(team)

        return team

    def create_phoenix_krakens(self):
        field = Field(color_1=(38, 117, 59), color_2=(4, 133, 38), yard_number_font_path=f"../Teams/fonts/CLARENDO.ttf", endzone_font_path=f"../Teams/fonts/kraken.ttf",
                      endzone_font_size=88, yard_number_font_size=34, endzone_1_text="BEWARE", endzone_2_text="THE KRAKENS", symmetrical=True,
                      yard_number_color=(255, 255, 255), yard_numbers_spaced=True, endzone_text_offset=-10, midfield_logo_size=200)
        team = Team("Phoenix Krakens", field, logo=f"../Teams/team_logos/Phoenix.png")
        team.set_color((141,74,157))
        team.secondary_color = ((243,239,244))
        self.create_random_players(team)

        return team

    def create_portland_pioneers(self):
        field = Field(color_1=(0, 87, 23), color_2=(12, 36, 1), yard_number_font_path=f"../Teams/fonts/pioneer.ttf", endzone_font_path=f"../Teams/fonts/pioneer.ttf",
                      endzone_font_size=80, yard_number_font_size=34, endzone_1_text="Portland", endzone_2_text="Pioneers", symmetrical=False,
                      yard_number_color=(255, 255, 255), yard_numbers_spaced=False, endzone_text_offset=0, midfield_logo_size=150)
        team = Team("Portland Pioneers", field, logo=f"../Teams/team_logos/Portland.png")
        team.set_color((202,32,44))
        team.secondary_color = ((254,254,253))
        self.create_random_players(team)

        return team

    def create_milwaukee_miners(self):
        field = Field(color_1=(27,107,53), color_2=(12, 50, 1), yard_number_font_path=f"../Teams/fonts/CLARENDO.ttf", endzone_font_path=f"../Teams/fonts/mine.ttf",
                      endzone_font_size=80, yard_number_font_size=40, endzone_1_text="Milwaukee", endzone_2_text="Miners", symmetrical=True,
                      yard_number_color=(80, 80, 80), yard_numbers_spaced=True, endzone_text_offset=0, midfield_logo_size=150)
        team = Team("Milwaukee Miners", field, logo=f"../Teams/team_logos/Milwaukee.png")
        team.set_color((27,107,53))
        team.secondary_color = ((74, 49, 19))
        self.create_random_players(team)

        return team

    def create_baltimore_phantoms(self):
        field = Field(color_1=(5, 89, 2), color_2=(12, 66, 1), yard_number_font_path=f"../Teams/fonts/CLARENDO.ttf", endzone_font_path=f"../Teams/fonts/phantom.ttf",
                      endzone_font_size=60, yard_number_font_size=34, endzone_1_text="Baltimore", endzone_2_text="Phantoms", symmetrical=True,
                      yard_number_color=(255, 255, 255), yard_numbers_spaced=True, endzone_text_offset=-12, midfield_logo_size=170)
        team = Team("Baltimore Phantoms", field, logo=f"../Teams/team_logos/Baltimore.png")
        team.set_color((152,27,30))
        team.secondary_color = ((5,7,7))
        self.create_random_players(team)

        return team

    def create_charlotte_spartans(self):
        field = Field(color_1=(11, 212, 4), color_2=(7, 156, 2), yard_number_font_path=f"../Teams/fonts/CLARENDO.ttf", endzone_font_path=f"../Teams/fonts/trojan.ttf",
                      endzone_font_size=130, yard_number_font_size=30, endzone_1_text="Charlotte", endzone_2_text="Spartans", symmetrical=True,
                      yard_number_color=(255, 255, 255), yard_numbers_spaced=True, endzone_text_offset=0, midfield_logo_size=150)
        team = Team("Charlotte Spartans", field, logo=f"../Teams/team_logos/Charlotte.png")
        team.set_color((244,180,33))
        team.secondary_color = ((167,32,34))
        self.create_random_players(team)

        return team

    def create_boston_bruisers(self):
        field = Field(color_1=(5, 112, 1), color_2=(5, 82, 2), yard_number_font_path=f"../Teams/fonts/CLARENDO.ttf", endzone_font_path=f"../Teams/fonts/lines.ttf",
                      endzone_font_size=100, yard_number_font_size=30, endzone_1_text="/ / / / / / /", endzone_2_text="/ / / / / / /", symmetrical=False,
                      yard_number_color=(255, 255, 255), yard_numbers_spaced=True, endzone_text_offset=-10, midfield_logo_size=150)
        team = Team("Boston Bruisers", field, logo=f"../Teams/team_logos/Boston.png")
        team.set_color((0,38,7))
        team.secondary_color = ((255, 255, 255))
        self.create_random_players(team)

        return team

    def create_cleveland_cannons(self):
        field = Field(color_1=(136,158,178), color_2=(88, 124, 168), yard_number_font_path=f"../Teams/fonts/CLARENDO.ttf", endzone_font_path=f"../Teams/fonts/war.ttf",
                      endzone_font_size=90, yard_number_font_size=34, endzone_1_text="Cleveland", endzone_2_text="Cannons", symmetrical=True,
                      yard_number_color=(25,45,88), yard_numbers_spaced=True, endzone_text_offset=-10, midfield_logo_size=225)
        team = Team("Cleveland Cannons", field, logo=f"../Teams/team_logos/Cleveland.png")
        team.set_color((25,45,88))
        team.secondary_color = ((205,31,59))
        self.create_random_players(team)

        return team

    def create_empire_state_terrors(self):
        field = Field(color_1=(0, 94, 0), color_2=(12, 138, 12), yard_number_font_path=f"../Teams/fonts/CLARENDO.ttf", endzone_font_path=f"../Teams/fonts/empire.ttf",
                      endzone_font_size=90, yard_number_font_size=40, endzone_1_text="EMPIRE", endzone_2_text="STATE", symmetrical=True,
                      yard_number_color=(255, 255, 255), yard_numbers_spaced=True, endzone_text_offset=0, midfield_logo_size=300)
        team = Team("Empire State Terrors", field, logo=f"../Teams/team_logos/Empire.png")
        team.set_color((243,206,34))
        team.secondary_color = ((0, 0, 0))
        self.create_random_players(team)

        return team

    def create_KC_mythics(self):
        field = Field(color_1=(0, 94, 0), color_2=(12, 138, 12), yard_number_font_path=f"../Teams/fonts/wizard.otf", endzone_font_path=f"../Teams/fonts/wizard.otf",
                      endzone_font_size=90, yard_number_font_size=40, endzone_1_text="Kansas City", endzone_2_text="Mythics", symmetrical=False,
                      yard_number_color=(255, 255, 255), yard_numbers_spaced=True, endzone_text_offset=-10, midfield_logo_size=150)
        team = Team("Kansas City Mythics", field, logo=f"../Teams/team_logos/KC.png")
        team.set_color((253,183,26))
        team.secondary_color = ((227,29,55))
        self.create_random_players(team)

        return team

    def create_OKC_flash(self):
        field = Field(color_1=(1, 138, 1), color_2=(1, 138, 1), yard_number_font_path=f"../Teams/fonts/CLARENDO.ttf", endzone_font_path=f"../Teams/fonts/flash.ttf",
                      endzone_font_size=60, yard_number_font_size=40, endzone_1_text="Oklahoma City Flash", endzone_2_text="Oklahoma City Flash", symmetrical=False,
                      yard_number_color=(255, 255, 255), yard_numbers_spaced=True, endzone_text_offset=-4, midfield_logo_size=430)
        team = Team("Oklahoma City Flash", field, logo=f"../Teams/team_logos/OKC.png")
        team.set_color((221,195,100))
        team.secondary_color = ((187,136,42))
        self.create_random_players(team)

        return team

    def create_toronto_manticore(self):
        field = Field(color_1=(1, 138, 1), color_2=(0, 102, 0), yard_number_font_path=f"../Teams/fonts/medieval.ttf", endzone_font_path=f"../Teams/fonts/medieval.ttf",
                      endzone_font_size=60, yard_number_font_size=45, endzone_1_text="TORONTO MANTICORE", endzone_2_text="TORONTO MANTICORE", symmetrical=True,
                      yard_number_color=(255, 255, 255), yard_numbers_spaced=False, endzone_text_offset=-4, midfield_logo_size=185)
        team = Team("Toronto Manticore", field, logo=f"../Teams/team_logos/Toronto.png")
        team.set_color((233,142,43))
        team.secondary_color = ((99,72,33))
        self.create_random_players(team)

        return team

    def create_san_francisco_stingers(self):
        field = Field(color_1=(28, 125, 6), color_2=(15, 77, 1), yard_number_font_path=f"../Teams/fonts/CLARENDO.ttf", endzone_font_path=f"../Teams/fonts/bee.ttf",
                      endzone_font_size=67, yard_number_font_size=30, endzone_1_text="San Francisco", endzone_2_text="Stingers", symmetrical=False,
                      yard_number_color=(255, 255, 255), yard_numbers_spaced=True, endzone_text_offset=-4, midfield_logo_size=200)
        team = Team("San Francisco Stingers", field, logo=f"../Teams/team_logos/SanFrancisco.png")
        team.set_color((248,191,20))
        team.secondary_color = ((24,54,48))
        self.create_random_players(team)

        return team

    def create_seattle_spiders(self):
        field = Field(color_1=(26, 99, 26), color_2=(17, 66, 17), yard_number_font_path=f"../Teams/fonts/CLARENDO.ttf", endzone_font_path=f"../Teams/fonts/spider.ttf",
                      endzone_font_size=100, yard_number_font_size=32, endzone_1_text="seattle", endzone_2_text="spiders", symmetrical=False,
                      yard_number_color=(255, 255, 255), yard_numbers_spaced=True, endzone_text_offset=0, midfield_logo_size=150)
        team = Team("Seattle Spiders", field, logo=f"../Teams/team_logos/Seattle.png")
        team.set_color((231,34,41))
        team.secondary_color = ((20,14,40))
        self.create_random_players(team)

        return team

    def create_washington_wardogs(self):
        field = Field(color_1=(82, 138, 54), color_2=(89, 120, 73), yard_number_font_path=f"../Teams/fonts/CLARENDO.ttf", endzone_font_path=f"../Teams/fonts/dog.ttf",
                      endzone_font_size=93, yard_number_font_size=32, endzone_1_text="Washington", endzone_2_text="Wardogs", symmetrical=True,
                      yard_number_color=(255, 255, 255), yard_numbers_spaced=True, endzone_text_offset=0, midfield_logo_size=200)
        team = Team("Washington Wardogs", field, logo=f"../Teams/team_logos/Washington.png")
        team.set_color((153,127,126))
        team.secondary_color = ((225,37,42))
        self.create_random_players(team)

        return team

    def create_tucson_twisters(self):
        field = Field(color_1=(40, 82, 19), color_2=(50, 135, 7), yard_number_font_path=f"../Teams/fonts/CLARENDO.ttf", endzone_font_path=f"../Teams/fonts/twister.ttf",
                      endzone_font_size=180, yard_number_font_size=32, endzone_1_text="Tucson", endzone_2_text="Twisters", symmetrical=True,
                      yard_number_color=(255, 255, 255), yard_numbers_spaced=True, endzone_text_offset=15, midfield_logo_size=240)
        team = Team("Tucson Twisters", field, logo=f"../Teams/team_logos/Tucson.png")
        team.set_color((167,169,172))
        team.secondary_color = ((32,0,0))
        self.create_random_players(team)

        return team

    def create_oakland_hogs(self):
        field = Field(color_1=(30, 87, 1), color_2=(30, 87, 1), yard_number_font_path=f"../Teams/fonts/CLARENDO.ttf", endzone_font_path=f"../Teams/fonts/mud.ttf",
                      endzone_font_size=60, yard_number_font_size=30, endzone_1_text="Oakland Hogs", endzone_2_text="Oakland Hogs", symmetrical=True,
                      yard_number_color=(255, 255, 255), yard_numbers_spaced=True, endzone_text_offset=-5, midfield_logo_size=180)
        team = Team("Oakland Hogs", field, logo=f"../Teams/team_logos/Oakland.png")
        team.set_color((223,33,38))
        team.secondary_color = ((251,251,251))
        self.create_random_players(team)

        return team

    def create_houston_hammerheads(self):
        field = Field(color_1=(16, 186, 13), color_2=(31, 138, 29), yard_number_font_path=f"../Teams/fonts/CLARENDO.ttf", endzone_font_path=f"../Teams/fonts/shark.ttf",
                      endzone_font_size=80, yard_number_font_size=40, endzone_1_text="HOUSTON", endzone_2_text="HAMMERHEADS", symmetrical=False,
                      yard_number_color=(255, 255, 255), yard_numbers_spaced=True, endzone_text_offset=-6, midfield_logo_size=250)
        team = Team("Houston Hammerheads", field, logo=f"../Teams/team_logos/Houston.png")
        team.set_color((1,30,64))
        team.secondary_color = ((252,254,251))
        self.create_random_players(team)

        return team
    
    def create_team_list(self):
        self.team_list.append(self.create_atlanta_ocelots())
        self.team_list.append(self.create_austin_infamous())
        self.team_list.append(self.create_baltimore_phantoms())
        self.team_list.append(self.create_boston_bruisers())
        self.team_list.append(self.create_charlotte_spartans())
        self.team_list.append(self.create_chicago_stallions())
        self.team_list.append(self.create_cleveland_cannons())
        self.team_list.append(self.create_empire_state_terrors())
        self.team_list.append(self.create_gotham_rogues())
        self.team_list.append(self.create_houston_hammerheads())
        self.team_list.append(self.create_jacksonville_gladiators())
        self.team_list.append(self.create_KC_mythics())
        self.team_list.append(self.create_las_vegas_knights())
        self.team_list.append(self.create_los_angeles_sirens())
        self.team_list.append(self.create_los_angeles_vigilantes())
        self.team_list.append(self.create_memphis_werewolves())
        self.team_list.append(self.create_miami_monstars())
        self.team_list.append(self.create_milwaukee_miners())
        self.team_list.append(self.create_new_orleans_scorpions())
        self.team_list.append(self.create_new_york_nightingales())
        self.team_list.append(self.create_oakland_hogs())
        self.team_list.append(self.create_OKC_flash())
        self.team_list.append(self.create_omaha_oblivion())
        self.team_list.append(self.create_orlando_rebels())
        self.team_list.append(self.create_philadelphia_blizzard())
        self.team_list.append(self.create_phoenix_krakens())
        self.team_list.append(self.create_portland_pioneers())
        self.team_list.append(self.create_sacramento_kingfishers())
        self.team_list.append(self.create_salt_lake_city_sinners())
        self.team_list.append(self.create_san_diego_inferno())
        self.team_list.append(self.create_san_francisco_stingers())
        self.team_list.append(self.create_seattle_spiders())
        self.team_list.append(self.create_tampa_toucans())
        self.team_list.append(self.create_toronto_manticore())
        self.team_list.append(self.create_tucson_twisters())
        self.team_list.append(self.create_las_vegas_knights())
        self.team_list.append(self.create_washington_wardogs())

    def create_nebraska(self):
        team = Team("Nebraska")
        team.set_color((227, 25, 55))
        team.secondary_color = ((253, 242, 217))

        # Offense
        qb = Quarterback("QB", "1", 99, 99, 99, 99, 99)
        team.add_player(qb)
        rb = RunningBack("RB", "1", 99, 99, 99, 99, 99)
        team.add_player(rb)
        wr1 = WideReceiver("WR", "1", 99, 99, 99, 99, 99)
        team.add_player(wr1)
        wr2 = WideReceiver("WR", "2", 99, 99, 99, 99, 99)
        team.add_player(wr2)
        wr3 = WideReceiver("WR", "3", 99, 99, 99, 99, 99)
        team.add_player(wr3)
        te = TightEnd("TE", "1", 99, 99, 99, 99, 99)
        team.add_player(te)
        ol1 = OffensiveLineman("OL", "1", 99, 99, 99, 99, 99)
        team.add_player(ol1)
        ol2 = OffensiveLineman("OL", "2", 99, 99, 99, 99, 99)
        team.add_player(ol2)
        ol3 = OffensiveLineman("OL", "3", 99, 99, 99, 99, 99)
        team.add_player(ol3)
        ol4 = OffensiveLineman("OL", "4", 99, 99, 99, 99, 99)
        team.add_player(ol4)
        ol5 = OffensiveLineman("OL", "5", 99, 99, 99, 99, 99)
        team.add_player(ol5)

        # Defense
        cb1 = Cornerback("CB", "1", 99, 99, 99, 99, 99)
        team.add_player(cb1)
        cb2 = Cornerback("CB", "2", 99, 99, 99, 99, 99)
        team.add_player(cb2)
        s1 = Safety("S", "1", 99, 99, 99, 99, 99)
        team.add_player(s1)
        s2 = Safety("S", "2", 99, 99, 99, 99, 99)
        team.add_player(s2)
        lb1 = Linebacker("LB", "1", 99, 99, 99, 99, 99)
        team.add_player(lb1)
        lb2 = Linebacker("LB", "2", 99, 99, 99, 99, 99)
        team.add_player(lb2)
        lb3 = Linebacker("LB", "3", 99, 99, 99, 99, 99)
        team.add_player(lb3)
        de1 = DefensiveEnd("DE", "1", 99, 99, 99, 99, 99)
        team.add_player(de1)
        de2 = DefensiveEnd("DE", "2", 99, 99, 99, 99, 99)
        team.add_player(de2)
        dt1 = DefensiveTackle("DT", "1", 99, 99, 99, 99, 99)
        team.add_player(dt1)
        dt2 = DefensiveTackle("DT", "2", 99, 99, 99, 99, 99)
        team.add_player(dt2)

        return team

    def create_iowa(self):
        team = Team("Iowa")
        team.set_color((0, 0, 0))
        team.secondary_color = ((255, 205, 0))

        # Offense
        qb = Quarterback("QB", "1", 50, 50, 50, 50, 50)
        team.add_player(qb)
        rb = RunningBack("RB", "1", 50, 50, 50, 50, 50)
        team.add_player(rb)
        wr1 = WideReceiver("WR", "1", 50, 50, 50, 50, 50)
        team.add_player(wr1)
        wr2 = WideReceiver("WR", "2", 50, 50, 50, 50, 50)
        team.add_player(wr2)
        wr3 = WideReceiver("WR", "3", 50, 50, 50, 50, 50)
        team.add_player(wr3)
        te = TightEnd("TE", "1", 50, 50, 50, 50, 50)
        team.add_player(te)
        ol1 = OffensiveLineman("OL", "1", 50, 50, 50, 50, 50)
        team.add_player(ol1)
        ol2 = OffensiveLineman("OL", "2", 50, 50, 50, 50, 50)
        team.add_player(ol2)
        ol3 = OffensiveLineman("OL", "3", 50, 50, 50, 50, 50)
        team.add_player(ol3)
        ol4 = OffensiveLineman("OL", "4", 50, 50, 50, 50, 50)
        team.add_player(ol4)
        ol5 = OffensiveLineman("OL", "5", 50, 50, 50, 50, 50)
        team.add_player(ol5)

        # Defense
        cb1 = Cornerback("CB", "1", 50, 50, 50, 50, 50)
        team.add_player(cb1)
        cb2 = Cornerback("CB", "2", 50, 50, 50, 50, 50)
        team.add_player(cb2)
        s1 = Safety("S", "1", 50, 50, 50, 50, 50)
        team.add_player(s1)
        s2 = Safety("S", "2", 50, 50, 50, 50, 50)
        team.add_player(s2)
        lb1 = Linebacker("LB", "1", 50, 50, 50, 50, 50)
        team.add_player(lb1)
        lb2 = Linebacker("LB", "2", 50, 50, 50, 50, 50)
        team.add_player(lb2)
        lb3 = Linebacker("LB", "3", 50, 50, 50, 50, 50)
        team.add_player(lb3)
        de1 = DefensiveEnd("DE", "1", 50, 50, 50, 50, 50)
        team.add_player(de1)
        de2 = DefensiveEnd("DE", "2", 50, 50, 50, 50, 50)
        team.add_player(de2)
        dt1 = DefensiveTackle("DT", "1", 50, 50, 50, 50, 50)
        team.add_player(dt1)
        dt2 = DefensiveTackle("DT", "2", 50, 50, 50, 50, 50)
        team.add_player(dt2)

        return team

    def create_random_players(self, team):
        # Offense
        qb = Quarterback("QB", "1", random.randint(50, 99), random.randint(50, 99), random.randint(50, 99), random.randint(50, 99), random.randint(50, 99))
        team.add_player(qb)
        rb = RunningBack("RB", "1", random.randint(50, 99), random.randint(50, 99), random.randint(50, 99), random.randint(50, 99), random.randint(50, 99))
        team.add_player(rb)
        wr1 = WideReceiver("WR", "1", random.randint(50, 99), random.randint(50, 99), random.randint(50, 99), random.randint(50, 99), random.randint(50, 99))
        team.add_player(wr1)
        wr2 = WideReceiver("WR", "2", random.randint(50, 99), random.randint(50, 99), random.randint(50, 99), random.randint(50, 99), random.randint(50, 99))
        team.add_player(wr2)
        wr3 = WideReceiver("WR", "3", random.randint(50, 99), random.randint(50, 99), random.randint(50, 99), random.randint(50, 99), random.randint(50, 99))
        team.add_player(wr3)
        te = TightEnd("TE", "1", random.randint(50, 99), random.randint(50, 99), random.randint(50, 99), random.randint(50, 99), random.randint(50, 99))
        team.add_player(te)
        ol1 = OffensiveLineman("OL", "1", random.randint(50, 99), random.randint(50, 99), random.randint(50, 99), random.randint(50, 99), random.randint(50, 99))
        team.add_player(ol1)
        ol2 = OffensiveLineman("OL", "2", random.randint(50, 99), random.randint(50, 99), random.randint(50, 99), random.randint(50, 99), random.randint(50, 99))
        team.add_player(ol2)
        ol3 = OffensiveLineman("OL", "3", random.randint(50, 99), random.randint(50, 99), random.randint(50, 99), random.randint(50, 99), random.randint(50, 99))
        team.add_player(ol3)
        ol4 = OffensiveLineman("OL", "4", random.randint(50, 99), random.randint(50, 99), random.randint(50, 99), random.randint(50, 99), random.randint(50, 99))
        team.add_player(ol4)
        ol5 = OffensiveLineman("OL", "5", random.randint(50, 99), random.randint(50, 99), random.randint(50, 99), random.randint(50, 99), random.randint(50, 99))
        team.add_player(ol5)

        # Defense
        cb1 = Cornerback("CB", "1", random.randint(50, 99), random.randint(50, 99), random.randint(50, 99), random.randint(50, 99), random.randint(50, 99))
        team.add_player(cb1)
        cb2 = Cornerback("CB", "2", random.randint(50, 99), random.randint(50, 99), random.randint(50, 99), random.randint(50, 99), random.randint(50, 99))
        team.add_player(cb2)
        s1 = Safety("S", "1", random.randint(50, 99), random.randint(50, 99), random.randint(50, 99), random.randint(50, 99), random.randint(50, 99))
        team.add_player(s1)
        s2 = Safety("S", "2", random.randint(50, 99), random.randint(50, 99), random.randint(50, 99), random.randint(50, 99), random.randint(50, 99))
        team.add_player(s2)
        lb1 = Linebacker("LB", "1", random.randint(50, 99), random.randint(50, 99), random.randint(50, 99), random.randint(50, 99), random.randint(50, 99))
        team.add_player(lb1)
        lb2 = Linebacker("LB", "2", random.randint(50, 99), random.randint(50, 99), random.randint(50, 99), random.randint(50, 99), random.randint(50, 99))
        team.add_player(lb2)
        lb3 = Linebacker("LB", "3", random.randint(50, 99), random.randint(50, 99), random.randint(50, 99), random.randint(50, 99), random.randint(50, 99))
        team.add_player(lb3)
        de1 = DefensiveEnd("DE", "1", random.randint(50, 99), random.randint(50, 99), random.randint(50, 99), random.randint(50, 99), random.randint(50, 99))
        team.add_player(de1)
        de2 = DefensiveEnd("DE", "2", random.randint(50, 99), random.randint(50, 99), random.randint(50, 99), random.randint(50, 99), random.randint(50, 99))
        team.add_player(de2)
        dt1 = DefensiveTackle("DT", "1", random.randint(50, 99), random.randint(50, 99), random.randint(50, 99), random.randint(50, 99), random.randint(50, 99))
        team.add_player(dt1)
        dt2 = DefensiveTackle("DT", "2", random.randint(50, 99), random.randint(50, 99), random.randint(50, 99), random.randint(50, 99), random.randint(50, 99))
        team.add_player(dt2)

    def get_team(self, name):
        for team in self.team_list:
            if team.name == name:
                return team

    def get_conference(self, name):
        for conference in self.league:
            if conference.name == name:
                return conference

    def set_conferences(self):
        self.league.append(Conference("Eastern"))
        self.league.append(Conference("Central"))
        self.league.append(Conference("Western"))

        self.get_conference("Western").add_division(Division("Pacific Northwest",
                                                             [self.get_team("Seattle Spiders"),
                                                              self.get_team("Portland Pioneers"),
                                                              self.get_team("Salt Lake City Sinners"),
                                                              self.get_team("Sacramento Kingfishers")]))
        self.get_conference("Western").add_division(Division("Sunbelt",
                                                             [self.get_team("San Francisco Stingers"),
                                                              self.get_team("Oakland Hogs"),
                                                              self.get_team("Las Vegas Knights"),
                                                              self.get_team("Los Angeles Vigilantes")]))
        self.get_conference("Western").add_division(Division("Desert",
                                                             [self.get_team("Los Angeles Sirens"),
                                                              self.get_team("Tucson Twisters"),
                                                              self.get_team("Phoenix Krakens"),
                                                              self.get_team("San Diego Inferno")]))
        self.get_conference("Central").add_division(Division("Great Lakes",
                                                             [self.get_team("Milwaukee Miners"),
                                                              self.get_team("Chicago Stallions"),
                                                              self.get_team("Cleveland Cannons"),
                                                              self.get_team("Toronto Manticore")]))
        self.get_conference("Central").add_division(Division("Heartland",
                                                             [self.get_team("Omaha Oblivion"),
                                                              self.get_team("Memphis Werewolves"),
                                                              self.get_team("Oklahoma City Flash"),
                                                              self.get_team("Kansas City Mythics")]))
        self.get_conference("Central").add_division(Division("Gulf Coast",
                                                             [self.get_team("Austin Infamous"),
                                                              self.get_team("Atlanta Ocelots"),
                                                              self.get_team("Houston Hammerheads"),
                                                              self.get_team("New Orleans Scorpions")]))
        self.get_conference("Eastern").add_division(Division("Florida",
                                                             [self.get_team("Miami Monstars"),
                                                              self.get_team("Jacksonville Gladiators"),
                                                              self.get_team("Tampa Toucans"),
                                                              self.get_team("Orlando Rebels")]))
        self.get_conference("Eastern").add_division(Division("Atlantic",
                                                             [self.get_team("Washington Wardogs"),
                                                              self.get_team("Baltimore Phantoms"),
                                                              self.get_team("Charlotte Spartans"),
                                                              self.get_team("Empire State Terrors")]))
        self.get_conference("Eastern").add_division(Division("Liberty",
                                                             [self.get_team("Gotham Rogues"),
                                                              self.get_team("New York Nightingales"),
                                                              self.get_team("Boston Bruisers"),
                                                              self.get_team("Philadelphia Blizzard")]))

        self.get_conference("Western").get_division("Pacific Northwest").logo_path = f"../Teams/division_logos/PNW.png"
        self.get_conference("Western").get_division("Sunbelt").logo_path = f"../Teams/division_logos/Sunbelt.png"
        self.get_conference("Western").get_division("Desert").logo_path = f"../Teams/division_logos/Desert.png"
        self.get_conference("Central").get_division("Great Lakes").logo_path = f"../Teams/division_logos/GreatLakes.png"
        self.get_conference("Central").get_division("Heartland").logo_path = f"../Teams/division_logos/Heartland.png"
        self.get_conference("Central").get_division("Gulf Coast").logo_path = f"../Teams/division_logos/GulfCoast.png"
        self.get_conference("Eastern").get_division("Florida").logo_path = f"../Teams/division_logos/Florida.png"
        self.get_conference("Eastern").get_division("Liberty").logo_path = f"../Teams/division_logos/Liberty.png"
        self.get_conference("Eastern").get_division("Atlantic").logo_path = f"../Teams/division_logos/Atlantic.png"

        for conference in self.league:
            for division in conference.divisions:
                for team in division.teams:
                    team.division = division

if __name__ == "__main__":
    Main()
