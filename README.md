# Data Art - The Sun #

![SW_1997-2017-animated](SW_1997-2017-animated.gif "Space Weather data collected over 20 years (1997-2017).")

Our Sun is living and beautiful. The Sun pulses with activity through its 11-year solar cycle and creates space weather. These images are "reconstructions" of our Sun using space weather data collected by the [Space Weather Prediction Centre (SWPC)](https://www.swpc.noaa.gov/) from 1997 to 2017.
Here is what each ring represents:
![SW-nomenclature](SW-nomenclature.png "SW-nomenclature")

Please refer to the SWPC website for further details on the parameters.


## Methodology ##
Daily space weather data was obtained from the [Space Weather Prediction Centre](https://www.swpc.noaa.gov/) warehouse. I compiled, cleaned and transformed the data to generate the final table: [SW\_1997-2017\_data.csv](SW_1997-2017_data.csv "SW_1997-2017_data.csv"). 
Briefly for data transformation, the parameters had to be scaled in the following manner for the plots:

* _x_/_max_: Radio\_Flux, Sunspot\_Number, Sunspot\_Area, S, O1, O2, O3, MLF\_A, HLC\_A, EP\_A
* log(_x_)/log(_max_): XRay\_Bkgd\_Flux, Flare\_tot, P\_1MeV, P\_10MeV, P\_100MeV, E\_06MeV, E\_2MeV

where _x_ is the reading, and _max_ is the maximum reading found in a parameter for all years. Transformed readings that were not within 0 - 1 were zeroed.

The circos plots were generated using [GraPhlAn](https://bitbucket.org/nsegata/graphlan/wiki/Home). Please refer to GraPhlAn documents on details about installing the program.
I have written a [Python 2](https://www.python.org) script that would take the following two starting files and generate a plot per year with GraPhlAn:

* [SW\_tree.txt](SW_tree.txt "SW_tree.txt")
* [SW\_1997-2017\_data.csv](SW_1997-2017_data.csv "SW_1997-2017_data.csv")

The command to run it is:
	`python plot_graphlan_SW.py SW_1997-2017_data.csv SW_tree.txt`

NOTE: To ensure that my plots follow strictly to the date order in the SW\_tree.txt file, I had to modify the *pyphlan.py* script in GraPhlAn in a similar way as Federico Abascal had done [here] (https://groups.google.com/forum/#!topic/graphlan-users/OrNMJuYxHIo).

Colour level adjustments and gif animation was processed with [GIMP](https://www.gimp.org/).



## AUTHOR ##
Created by Joel Z.B. Low on August 11th, 2018.
