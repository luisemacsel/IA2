(define (problem carga2)
  	(:domain aviones)
    (:objects
     	AA01
     	AA02
     	AA03
     	PSS
     	MDZ
     	BRC
     	VINO
     	YERBA
     	CHOCOLATES
    )
	(:init
     	(avion AA01)
     	(avion AA02)
     	(avion AA03)
     	(carga VINO)
     	(carga YERBA)
     	(carga CHOCOLATES)
     	(aeropuerto PSS)
     	(aeropuerto MDZ)
     	(aeropuerto BRC)
     	(en CHOCOLATES BRC )
     	(en VINO MDZ)
     	(en YERBA PSS)
     	(en AA01 PSS)
     	(en AA02 MDZ)
     	(en AA03 BRC)
     )
  	(:goal
     	(and
     		(en YERBA BRC)
     		(en CHOCOLATES MDZ)
     		(en VINO PSS)
         )
    )
)

