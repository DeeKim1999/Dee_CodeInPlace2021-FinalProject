# for loading files with nested data -- dee
import csv
# for making pretty graphs
import seaborn as sns
import matplotlib.pyplot as plt

# Name of the file to read in!
FILE_NAME = 'datasheet02.csv'

def main():
    #load data (csv file) and print it
    with open(FILE_NAME) as f:
        reader = csv.DictReader(f)

        americas_total = 0
        no_of_countries_americas = 0
        am_new = 0
        am_deaths = 0
        am_com_trans = 0
        am_cluster = 0
        am_sporadic = 0
        am_no_active = 0
        am_no_cases = 0
        am_unknown = 0

        africa_total = 0
        no_of_countries_africa = 0
        afr_new = 0
        afr_deaths = 0
        afr_com_trans = 0
        afr_cluster = 0
        afr_sporadic = 0
        afr_no_active = 0
        afr_no_cases = 0
        afr_unknown = 0

        eastmed_total = 0
        no_of_countries_eastmed = 0
        eastmed_new = 0
        eastmed_deaths = 0
        eastmed_com_trans = 0
        eastmed_cluster = 0
        eastmed_sporadic = 0
        eastmed_no_active = 0
        eastmed_no_cases = 0
        eastmed_unknown = 0

        europe_total = 0
        no_of_countries_europe = 0
        eur_new = 0
        eur_deaths = 0
        eur_com_trans = 0
        eur_cluster = 0
        eur_sporadic = 0
        eur_no_active = 0
        eur_no_cases = 0
        eur_unknown = 0

        southeastasia_total = 0
        no_of_countries_southeastasia = 0
        sea_new = 0
        sea_deaths = 0
        sea_com_trans = 0
        sea_cluster = 0
        sea_sporadic = 0
        sea_no_active = 0
        sea_no_cases = 0
        sea_unknown = 0

        westernpacific_total = 0
        no_of_countries_westernpacific = 0
        wpa_new = 0
        wpa_deaths = 0
        wpa_com_trans = 0
        wpa_cluster = 0
        wpa_sporadic = 0
        wpa_no_active = 0
        wpa_no_cases = 0
        wpa_unknown = 0


        for line in reader:
            country_region = line['region']
            # Region: Americas
            if country_region == 'Americas':
                cumulative_cases = line['total']
                # to keep track of total cases
                americas_total += int(cumulative_cases)
                # to keep track of the number of countries per region
                no_of_countries_americas += 1
                # to keep track of the new number of cases
                am_new_cases = line['new']
                am_new += int(am_new_cases)
                # to keep track of the number of deaths
                am_death_cases = line['deaths']
                am_deaths += int(am_death_cases)
                # to keep track of the number of the cause of contamination
                am_transmission = line['transmission classification']
                if am_transmission == 'Community Transmission':
                    am_com_trans += 1
                elif am_transmission == 'Cluster of Cases':
                    am_cluster += 1
                elif am_transmission == 'Sporadic Cases':
                    am_sporadic += 1
                elif am_transmission == 'No Active Cases':
                    am_no_active += 1
                elif am_transmission == 'No Cases':
                    am_no_cases += 1
                else:
                    am_unknown += 1

            # Region: Africa
            if country_region == 'Africa':
                cumulative_cases = line['total']
                # to keep track of total cases
                africa_total += int(cumulative_cases)
                # to keep track of the number of countries per region
                no_of_countries_africa += 1
                # to keep track of the new number of cases
                afr_new_cases = line['new']
                afr_new += int(afr_new_cases)
                # to keep track of the number of deaths
                afr_death_cases = line['deaths']
                afr_deaths += int(afr_death_cases)
                # to keep track of the number of the cause of contamination
                afr_transmission = line['transmission classification']
                if afr_transmission == 'Community Transmission':
                    afr_com_trans += 1
                elif afr_transmission == 'Cluster of Cases':
                    afr_cluster += 1
                elif afr_transmission == 'Sporadic Cases':
                    afr_sporadic += 1
                elif afr_transmission == 'No Active Cases':
                    afr_no_active += 1
                elif afr_transmission == 'No Cases':
                    afr_no_cases += 1
                else:
                    afr_unknown += 1

            # Region: Eastern Mediterranean
            if country_region == 'Eastern Mediterranean':
                cumulative_cases = line['total']
                # to keep track of total cases
                eastmed_total += int(cumulative_cases)
                # to keep track of the number of countries per region
                no_of_countries_eastmed += 1
                # to keep track of the new number of cases
                eastmed_new_cases = line['new']
                eastmed_new += int(eastmed_new_cases)
                # to keep track of the number of deaths
                eastmed_death_cases = line['deaths']
                eastmed_deaths += int(eastmed_death_cases)
                # to keep track of the number of the cause of contamination
                eastmed_transmission = line['transmission classification']
                if eastmed_transmission == 'Community Transmission':
                    eastmed_com_trans += 1
                elif eastmed_transmission == 'Cluster of Cases':
                    eastmed_cluster += 1
                elif eastmed_transmission == 'Sporadic Cases':
                    eastmed_sporadic += 1
                elif eastmed_transmission == 'No Active Cases':
                    eastmed_no_active += 1
                elif eastmed_transmission == 'No Cases':
                    eastmed_no_cases += 1
                else:
                    eastmed_unknown += 1

            # Region: Europe
            if country_region == 'Europe':
                cumulative_cases = line['total']
                # to keep track of total cases
                europe_total += int(cumulative_cases)
                # to keep track of the number of countries per region
                no_of_countries_europe += 1
                # to keep track of the new number of cases
                eur_new_cases = line['new']
                eur_new += int(eur_new_cases)
                # to keep track of the number of deaths
                eur_death_cases = line['deaths']
                eur_deaths += int(eur_death_cases)
                # to keep track of the number of the cause of contamination
                eur_transmission = line['transmission classification']
                if eur_transmission == 'Community Transmission':
                    eur_com_trans += 1
                elif eur_transmission == 'Cluster of Cases':
                    eur_cluster += 1
                elif eur_transmission == 'Sporadic Cases':
                    eur_sporadic += 1
                elif eur_transmission == 'No Active Cases':
                    eur_no_active += 1
                elif eur_transmission == 'No Cases':
                    eur_no_cases += 1
                else:
                    eur_unknown += 1

            # Region: South-East Asia
            if country_region == 'South-East Asia':
                cumulative_cases = line['total']
                # to keep track of total cases
                southeastasia_total += int(cumulative_cases)
                # to keep track of the number of countries per region
                no_of_countries_southeastasia += 1
                # to keep track of the new number of cases
                sea_new_cases = line['new']
                sea_new += int(sea_new_cases)
                # to keep track of the number of deaths
                sea_death_cases = line['deaths']
                sea_deaths += int(sea_death_cases)
                # to keep track of the number of the cause of contamination
                sea_transmission = line['transmission classification']
                if sea_transmission == 'Community Transmission':
                    sea_com_trans += 1
                elif sea_transmission == 'Cluster of Cases':
                    sea_cluster += 1
                elif sea_transmission == 'Sporadic Cases':
                    sea_sporadic += 1
                elif sea_transmission == 'No Active Cases':
                    sea_no_active += 1
                elif sea_transmission == 'No Cases':
                    sea_no_cases += 1
                else:
                    sea_unknown += 1

            # Region: Western Pacific
            if country_region == 'Western Pacific':
                cumulative_cases = line['total']
                # to keep track of total cases
                westernpacific_total += int(cumulative_cases)
                # to keep track of the number of countries per region
                no_of_countries_westernpacific += 1
                # to keep track of the new number of cases
                wpa_new_cases = line['new']
                wpa_new += int(wpa_new_cases)
                # to keep track of the number of deaths
                wpa_death_cases = line['deaths']
                wpa_deaths += int(wpa_death_cases)
                # to keep track of the number of the cause of contamination
                wpa_transmission = line['transmission classification']
                if wpa_transmission == 'Community Transmission':
                    wpa_com_trans += 1
                elif wpa_transmission == 'Cluster of Cases':
                    wpa_cluster += 1
                elif wpa_transmission == 'Sporadic Cases':
                    wpa_sporadic += 1
                elif wpa_transmission == 'No Active Cases':
                    wpa_no_active += 1
                elif wpa_transmission == 'No Cases':
                    wpa_no_cases += 1
                else:
                    wpa_unknown += 1

        ## PART 02
        # Cumulative Cases (Americas)
        a = americas_total
        print('')
        print('Cumulative Cases in Americas:', americas_total)
        # Number of Countries per region
        print('Total Number of Countries in Americas:', no_of_countries_americas)

        # Calculates for the average (Americas)
        a = americas_total
        b = no_of_countries_americas
        am_ave = average(a, b)
        print('Average Cases in Americas:', am_ave)

        # Number of New Cases (Americas)
        a = americas_total
        print('Cumulative New Cases in Americas:', am_new)
        # Number of Deaths (Americas)
        a = americas_total
        print('Cumulative Deaths in Americas:', am_deaths)
        print('')
        # Transmission Classification (Americas)
        a = americas_total
        print('Types of Transmission evaluated per country in Americas:')
        print('Community Transmission:', am_com_trans)
        print('Cluster of Cases:', am_cluster)
        print('Sporadic Cases:', am_sporadic)
        print('No Active Cases:', am_no_active)
        print('No Cases:', am_no_cases)
        print('Unknown:', am_unknown)
        print('')
        print('----------------------------------------------------')
        print('')

        # Cumulative Cases (Africa)
        a = africa_total
        print('Cumulative Cases in Africa:', africa_total)
        # Number of Countries per region
        print('Total Number of Countries in Africa:', no_of_countries_africa)

        # Calculates for the average (Africa)
        a = africa_total
        b = no_of_countries_africa
        afr_ave = average(a, b)
        print('Average Cases in Africa:', afr_ave)

        # Number of New Cases (Africa)
        a = africa_total
        print('Cumulative New Cases in Africa:', afr_new)
        # Number of Deaths (Africa)
        a = africa_total
        print('Cumulative Deaths in Africa:', afr_deaths)
        print('')
        # Transmission Classification (Africa)
        a = africa_total
        print('Types of Transmission evaluated per country in Africa:')
        print('Community Transmission:', afr_com_trans)
        print('Cluster of Cases:', afr_cluster)
        print('Sporadic Cases:', afr_sporadic)
        print('No Active Cases:', afr_no_active)
        print('No Cases:', afr_no_cases)
        print('Unknown:', afr_unknown)
        print('')
        print('----------------------------------------------------')
        print('')

        # Cumulative Cases (East Mediterranean)
        a = eastmed_total
        print('Cumulative Cases in East Mediterranean:', eastmed_total)
        # Number of Countries per region
        print('Total Number of Countries in East Mediterranean:', no_of_countries_eastmed)

        # Calculates for the average (East Mediterranean)
        a = eastmed_total
        b = no_of_countries_eastmed
        eastmed_ave = average(a, b)
        print('Average Cases in East Mediterranean:', eastmed_ave)

        # Number of New Cases (East Mediterranean)
        a = eastmed_total
        print('Cumulative New Cases in East Mediterranean:', eastmed_new)
        # Number of Deaths (East Mediterranean)
        a = eastmed_total
        print('Cumulative Deaths in East Mediterranean:', eastmed_deaths)
        print('')
        # Transmission Classification (East Mediterranean)
        a = eastmed_total
        print('Types of Transmission evaluated per country in East Mediterranean:')
        print('Community Transmission:', eastmed_com_trans)
        print('Cluster of Cases:', eastmed_cluster)
        print('Sporadic Cases:', eastmed_sporadic)
        print('No Active Cases:', eastmed_no_active)
        print('No Cases:', eastmed_no_cases)
        print('Unknown:', eastmed_unknown)
        print('')
        print('----------------------------------------------------')
        print('')

        # Cumulative Cases (Europe)
        a = europe_total
        print('Cumulative Cases in Europe:', europe_total)
        # Number of Countries per region
        print('Total Number of Countries in Europe:', no_of_countries_europe)

        # Calculates for the average (Europe)
        a = europe_total
        b = no_of_countries_europe
        eur_ave = average(a, b)
        print('Average Cases in Europe:', eur_ave)

        # Number of New Cases (Europe)
        a = europe_total
        print('Cumulative New Cases in Europe:', eur_new)
        # Number of Deaths (Europe)
        a = europe_total
        print('Cumulative Deaths in Europe:', eur_deaths)
        print('')
        # Transmission Classification (Europe)
        a = europe_total
        print('Types of Transmission evaluated per country in Europe:')
        print('Community Transmission:', eur_com_trans)
        print('Cluster of Cases:', eur_cluster)
        print('Sporadic Cases:', eur_sporadic)
        print('No Active Cases:', eur_no_active)
        print('No Cases:', eur_no_cases)
        print('Unknown:', eur_unknown)
        print('')
        print('----------------------------------------------------')
        print('')

        # Cumulative Cases (South-East Asia)
        a = southeastasia_total
        print('Cumulative Cases in South-East Asia:', southeastasia_total)
        # Number of Countries per region
        print('Total Number of Countries in South-East Asia:', no_of_countries_southeastasia)

        # Calculates for the average (South-East Asia)
        a = southeastasia_total
        b = no_of_countries_southeastasia
        sea_ave = average(a, b)
        print('Average Cases in South-East Asia:', sea_ave)

        # Number of New Cases (South-East Asia)
        a = southeastasia_total
        print('Cumulative New Cases in South-East Asia:', sea_new)
        # Number of Deaths (South-East Asia)
        a = southeastasia_total
        print('Cumulative Deaths in South-East Asia:', sea_deaths)
        print('')
        # Transmission Classification (South-East Asia)
        a = southeastasia_total
        print('Types of Transmission evaluated per country in South-East Asia:')
        print('Community Transmission:', sea_com_trans)
        print('Cluster of Cases:', sea_cluster)
        print('Sporadic Cases:', sea_sporadic)
        print('No Active Cases:', sea_no_active)
        print('No Cases:', sea_no_cases)
        print('Unknown:', sea_unknown)
        print('')
        print('----------------------------------------------------')
        print('')

        # Cumulative Cases (Western Pacific)
        a = westernpacific_total
        print('Cumulative Cases in Western Pacific:', westernpacific_total)
        # Number of Countries per region
        print('Total Number of Countries in Western Pacific:', no_of_countries_westernpacific)

        # Calculates for the average (Western Pacific)
        a = westernpacific_total
        b = no_of_countries_westernpacific
        wpa_ave = average(a, b)
        print('Average Cases in Western Pacific:', wpa_ave)

        # Number of New Cases (Western Pacific)
        a = westernpacific_total
        print('Cumulative New Cases in Western Pacific:', wpa_new)
        # Number of Deaths (Western Pacific)
        a = westernpacific_total
        print('Cumulative Deaths in Western Pacific:', wpa_deaths)
        print('')
        # Transmission Classification (Western Pacific)
        a = westernpacific_total
        print('Types of Transmission evaluated per country in Western Pacific:')
        print('Community Transmission:', wpa_com_trans)
        print('Cluster of Cases:', wpa_cluster)
        print('Sporadic Cases:', wpa_sporadic)
        print('No Active Cases:', wpa_no_active)
        print('No Cases:', wpa_no_cases)
        print('Unknown:', wpa_unknown)
        print('')
        print('----------------------------------------------------')
        print('')


        # Data Compilation
        cummulative = {
            'Americas': americas_total,
            'Africa': africa_total,
            'East Med': eastmed_total,
            'Europe': europe_total,
            'SE Asia': southeastasia_total,
            'West Pacific': westernpacific_total
        }

        new = {
            'Americas': am_new,
            'Africa': afr_new,
            'East Med': eastmed_new,
            'Europe': eur_new,
            'SE Asia': sea_new,
            'Western Pacific': wpa_new
        }

        deaths = {
            'Americas': am_deaths,
            'Africa': afr_deaths,
            'East Med': eastmed_deaths,
            'Europe': eur_deaths,
            'SE Asia': sea_deaths,
            'Western Pacific': wpa_deaths
        }

        make_bar_plot(cummulative)
        #make_bar_plot(new)
        #make_bar_plot(deaths)

# Additional Helper Functions
def make_bar_plot(count_map):
    """
    Turns a dictionary (where values are numbers) into a bar plot.
    Labels gives the order of the bars! Uses a package called seaborn
    for making graphs.
    """
    # turn the counts into a list
    counts = []
    # loop over the labels, in order
    for label in count_map:
        counts.append(count_map[label])
    # format the data in the way that seaborn wants
    data = {
        'x':list(count_map.keys()),
        'y':counts
    }
    sns.barplot(x = 'x',y = 'y', data= data)
    plt.savefig("plot.png")


def average(total, length):
    ave = int(total) / int(length)
    return ave

# Authored by: Daniella Kim :))
# References: https://doh.gov.ph/2019-nCoV ; https://github.com/CSSEGISandData/COVID-19/blob/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv ; https://covid19.who.int/table ; 


if __name__ == '__main__':
    main()
