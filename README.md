# micro-reactor
2021 Summer internship project in the University of Liverpool's Chemistry department

Starting with zero programming language experience I have been tasked with essentially learning python from scratch.


The project aims to create modular code/programs that will monitor and control the conditions within a photochemical microreactor
Monitoring will be achieved using 1Wire temperature sensors, a PiCamera v2.0 Noir and 3 (at present) adafruit light sensors (VEML6070, VEML7700 and TSL2591)
  PiCamera is intended for dual usage as either a photospectrometer (if I can make it work...) and primarily for direct viewing (leaks, lamp issues, remote comnfirmation of error messages/system halts
  Temp sensors will monitor various pieces of hardware including:
    * 3 sensors inside the reactor housing --> controlling flow into reactor via on/off of pressure valve using a stepper motor
         (is temp above desired value AND below value that will damage PTFE, polycarbonate, sensors etc --> theoret max = appr. 110 oC
    * 1 sensor measuring temp of reagent bottle (chemistry in) --> bypasses PTFE excellent thermal insulation properties
          Also providing ON/OFF control of flow --> single temp val for ideal reaction conditions (initial approx. 50 oC)
    * 1 sensor measuring lamp temperature
          Lamp comes with inbuilt active cooling, however the lamp LED shield has been shown to reach temps in excess of 100 oC, combined with active heating of reactor and vertical arranegment (lamp at top), overheating is innevitable...
              Planning to use this sensor to:
              detect temp inside lamp body, then (in order):
                1. first temp level hit --> sound alarm and auto power on/up 5v potentiometer (analog atm --> digitial coming soon) controlled 4x 30mm reactor cooling fans
                2. second temp level hit --> sound diff alarm and power on 5v potentiometer controlled 2x 50mm lamp cooling fans
                  after X mins and/or no decrease in temp, increase fan power (maybe 3-5 power levels)
                3. if all warnings and remedial actions above fail to lower lamp temp
                    Kill lamp power, all fans to full, kill reactant flow, sound V loud/obvious alarm, (maybe send notification emails to supervisor about the error.
                
                trigger flow OFF after *2-10mins* of excess temp detected inside lamp
             
