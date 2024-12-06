# Antwoorden

## Hoofdstuk 1



## Hoofdstuk 2



## Hoofdstuk 3



## Hoofdstuk 4



## Hoofdstuk 5

1. 

	from microbit import *

	while True:
		if button_a.is_pressed():
			display.show(Image.HEART)
		elif button_b.is_pressed():
			display.show(Image.HAPPY)
		else:
			display.show("-")

Knop **A** krijgt voorrang, want als beide knoppen ingedrukt worden zie je een hart.


2. 

	from microbit import *

	while True:
		if button_a.is_pressed() and button_b.is_pressed():
			display.show(Image.HEART)
		elif button_a.is_pressed() or button_b.is_pressed():
			display.show(Image.HEART_SMALL)
		else:
			display.clear()

3.

from microbit import *

	while True:
		lichtniveau = display.read_light_level()
		if lichtniveau < 50:
			display.show(Image("99999:"
					    "99999:"
					    "99999:"
					    "99999:"
					    "99999:"))
	elif 50 <= lichtniveau <= 200:
		display.show(Image("55555:"
					    "55555:"
					    "55555:"
					    "55555:"
					    "55555:"))
	else:
		display.clear()

4.

	from maqueen import *

	init_maqueen()

	while True:
		if sensor_on_line(lijnsensor_m) == 4:
			motor_uit(motor_links)
			motor_uit(motor_rechts)
		else:
			motor_aan(motor_links, 100)
			motor_aan(motor_rechts, 100)

5.

	from maqueen import *

	init_maqueen()

	while True:
		if afstand_tot_voorwerp() < 30:
			motor_uit(motor_links)
			motor_uit(motor_rechts)
		else:
			motor_aan(motor_links, 100)
			motor_aan(motor_rechts, 100)

6. 

	from maqueen import *

	init_maqueen()

	while True:
		if sensor_on_line(lijnsensor_m) == 4 and afstand_tot_voorwerp() < 10:
			draaiRechts(1000)
		elif sensor_on_line(lijnsensor_m) == 4 and afstand_tot_voorwerp() >= 10:
			motor_uit(motor_links)
			motor_uit(motor_rechts)
			audio.play(Sound.GIGGLE)
		else:
			motor_aan(motor_links, 100)
			motor_aan(motor_rechts, 100)

7.

	from maqueen import *

	init_maqueen()

	while True:
		if afstand_tot_voorwerp() <= 10:
			motor_uit(motor_links)
			motor_uit(motor_rechts)
			set_underglow(rood)
		elif afstand_tot_voorwerp() > 10 and afstand_tot_voorwerp() < 30:
			motor_aan(motor_links, 16)
			motor_aan(motor_rechts, 16)
			set_underglow(geel)
		else:
			motor_aan(motor_links)
			motor_aan(motor_rechts)
			set_underglow(groen)

8. 

	from maqueen import *

	init_maqueen()

	while True:
		if afstand_tot_voorwerp() < 10:
			motor_uit(motor_links)
			motor_uit(motor_rechts)
			draaiLinks(900)  # Tijd kan verschillen per robot, zelf testen of dit ook echt ongeveer 90 graden is
		else:
			motor_aan(motor_links, 100)
			motor_aan(motor_rechts, 100)


## Hoofdstuk 6



## Hoofdstuk 7

