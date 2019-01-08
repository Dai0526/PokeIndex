import scrapy
import PokemonObject.Pokemon
# That's the Web crawler for the English version
# Implement the English ver first so that it can avoid some encoding problem
class PokeBall(scrapy.Spider):
	name = "PokeBall"

	def start_requests(self):
		urls = [
		'https://pokemondb.net/pokedex/bulbasaur',
		]
		
		for url in urls:
			yield scrapy.Request(url = url, callback=self.parse)

	def parse(self, response):
		wildPokemon = Pokemon()


