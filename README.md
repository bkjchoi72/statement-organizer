# statement-organizer

## Creating a config file
- Create a directory called ~/Desktop/statement_organizer
- Create a file called `config.txt` in the directory created above
  - Create rules in the config (example below)

## Exmple config file
```
Food/Drink=CHICKEN
Food/Drink=STARBUCKS
Food/Drink=MITSUWA-SANUKI
Food/Drink=PORTOS
Food/Drink=BOILING POINT
Food/Drink=RESTAURANT
Food/Drink=GRILL
Food/Drink=THE BUTCHER
Food/Drink=SAIGON DISH
Food/Drink=SQ *
Food/Drink=TST*
Food/Drink=DOORDASH
Food/Drink=TACO
Food/Drink=DIN TAI FUNG
Food/Drink=BAKERY
Food/Drink=BBQ
Food/Drink=PANDA EXPRESS
Food/Drink=CHICK-FIL-A
Food/Drink=CAFE
Food/Drink=HONG KONG BANJUM
Food/Drink=Pizza
Food/Drink=BOBA
Food/Drink=DOUGHNUTS
Food/Drink=Subway
Food/Drink=SEAFOOD
Food/Drink=BURGER
Food/Drink=TONKATSU
Food/Drink=PAPA JOHN'S
Food/Drink=YOGURTLAND
Food/Drink=SUSHI
Food/Drink=BEARD PAPAS
Food/Drink=MISASA
Food/Drink=DONUT
Food/Drink=PHO
Food/Drink=YUCHUN
Food/Drink=7-ELEVEN
Food/Drink=MCDONALD'S
Food/Drink=CHIPOTLE
Food/Drink=MIRAK
Food/Drink=MY PROTEIN
Food/Drink=POTBELLY
Food/Drink=MIYABITEI
Food/Drink=KIMBAP
Food/Drink=NOODLE
Food/Drink=WINGS
Food/Drink=RAISING CANE'S
Food/Drink=7 LEAVES
Food/Drink=MAPLE BLOCK
Food/Drink=DUNKIN
Food/Drink=MASTRO'S
Food/Drink=LITTLE CAESARS
Food/Drink=CHERRY ON TOP
Groceries=TRADER JOE'S
Groceries=RITE AID
Groceries=LOS ANGELES AFB COMM
Groceries=COSTCO WHSE
Groceries=MITSUWA MRKTPLACE
Groceries=RALPHS
Groceries=GALLERIA MARKET
Groceries=VONS
Groceries=SUPERMARKET
Groceries=H MART
Groceries=NIJIYA MARKET
Groceries=ZION MART
Groceries=CVS
Groceries=99 RANCH
Groceries=PAVILION
Groceries=SPROUTS
Groceries=MARKET
Groceries=ALBERTSONS
Groceries=AAFES LOS ANGELES MAIN S
Groceries=WALGREENS
Groceries=TARGET
Groceries=HANNAM CHAIN
Groceries=AMZNGrcy
Shopping=Amazon.com
Shopping=VICTORIASSECRET
Shopping=STAPLES
Shopping=UNIQLO
Shopping=DAISO
Shopping=APPLE.COM
Shopping=KIM'S HOME CENTER
Shopping=JCPENNEY
Shopping=ESTEE LAUDER
Shopping=SAMPLESALE
Shopping=SAMPLE SALE
Shopping=E-COMMERC
Shopping=CDKEYS
Shopping=Farfetch
Shopping=EBAY
Shopping=MARSHALLS
Shopping=ROSS STORES
Shopping=ZARA
Shopping=STAUD
Shopping=AMZN Mktp
Shopping=WALMART.COM
Shopping=JOANN.COM
Shopping=DUTY FREE
Shopping=TINT SHOP
Gas/Auto=GAS
Gas/Auto=AUTO REPA
Gas/Auto=TOYOTA
Gas/Auto=CHEVRON
Gas/Auto=DMV
Gas/Auto=SMOG
Gas/Auto=SHELL OIL
Travel/Entertainment=AIRLINE
Travel/Entertainment=TRAVEL
Travel/Entertainment=ADVENTURE
Travel/Entertainment=RESIDENCE INN
Travel/Entertainment=PARKING
Travel/Entertainment=OCULUS
Travel/Entertainment=PLAYSTATION
Travel/Entertainment=PRO SHOP
Travel/Entertainment=HERTZ
Travel/Entertainment=LYFT
Travel/Entertainment=UBER
Travel/Entertainment=LA QUINTA
Travel/Entertainment=AIRBNB
Travel/Entertainment=MARRIOTT
Travel/Entertainment=BOULEVARD MUSIC
Bills/Utilities=UNITED CONCORDIA
Bills/Utilities=SPECTRUM
Bills/Utilities=TMOBILE*AUTO PAY
Bills/Utilities=DENTAL
Bills/Utilities=GEICO
Bills/Utilities=HNFSWEST
Bills/Utilities=UCLA PHYSICIANS
Bills/Utilities=FITNESS
Bills/Utilities=Membership Renewal
Personal=LACCD
Personal=EDUCATIVEINC
```

## How to build an executable
(from the main repo directory)
make build

This will create a dist/ and build/ directories. The executable is located inside the /dist directory

## How to run tests
make test
