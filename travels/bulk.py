from models import Destination
import csv


with open('../city_data/cities_with_image.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    first_row = True
    for row in csv_reader:
        if first_row:
            first_row = False
            continue
        dest = Destination()
        dest.city = row[0]
        dest.country = row[1]
        dest.iso2 = row[2]
        dest.iso3 = row[3]
        dest.desc = row[4]
        dest.price = row[5]
        dest.img1 = row[6]
        dest.img2 = row[7]
        dest.img3 = row[8]
        dest.img4 = row[9]
        dest.save();
        input("One added")

