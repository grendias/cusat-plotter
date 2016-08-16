# UPSat telemetry data plotter
A quick and dirty matplotlib script to graph extend telemetry data from [UPsat](https://upsat.gr).

## Requirements
You will need matplotlib and numpy python libraries

## Usage
* Add all the EX_WOD in json format you want in the EX_WOD_RX data folder (some are included as examples)
* Add all the WOD decoded files in json format in the WOD_RX data folder (some are included as examples)
* Fire up the script with the data you want as arguments.

## Examples

`./upsat-plotter.py -t EXT_WOD ADCS Time OBC Time COMMS Time`

`./upsat-plotter.py -t WOD VBAT IBAT TEPS`

## License

&copy; 2016 [Libre Space Foundation](http://librespacefoundation.org) & Commiters.

Licensed under the [GPLv3](LICENSE).
