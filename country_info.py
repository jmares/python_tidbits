from countryinfo import CountryInfo

country = input("Enter your country: ")
info = CountryInfo(country)

print("Capital:", info.capital())
print("Currencies:", info.currencies())
print("Languages:", info.languages())
print("Neighbors:", info.borders())
print("Population:", info.population())
