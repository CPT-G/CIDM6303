import sys


def track_package(location="Atlantis"):
    print("Package is located at " + location)


track_package("Electric city")
track_package("Okinawa")
track_package()
track_package("Mars")


x = [1977, 1980]
y = [2020, 2005]
combined = x + y
print(combined)

years = [1977, 1980]
print(len(years))

statehood = [
    ["V", 1788],
    ["NY", 1788],
    ["U", 1896],
    ["T", 1845]
]

print(statehood[2][1])

years = [1977, 1980, 1983, 1999, 2020, 2005, 2015, 2017, 2019]
modern_years = [year for year in years if year >= 2000]
print(modern_years)


def print_python_version():
    """Function printing python version."""
    print(sys.version)
