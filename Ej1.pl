/* Ejercicio 1 Tp : Sistema Experto para revision y mantenimiento de valvula de Gas*/

/* Rama Izquierda*/
verificar(thinckness_of_the_safety_valve_body) :- 
                estado(thinckness_of_the_safety_valve_body, yes),
                writeln('el estado del equipo debe ser reportado para una inspeccion tecnica de la unidad inmediatamente').
verificar(thinckness_of_the_safety_valve_body) :- 
                estado(thinckness_of_the_safety_valve_body, no),
                writeln('el estado del equipo es aceptable ').
               
verificar(thinckness_of_the_safety_valve_body) :- 
                estado(thinckness_of_the_safety_valve_body, desconocido),
                ((estado(safety_valve_body_has_deffect_of_dazzling_and_rusting, no), writeln('Verificar si el espesor de la valvula de seguridad es menor al umbral requerido')); 
                verificar(safety_valve_body_has_deffect_of_dazzling_and_rusting)).

verificar(thinckness_of_the_safety_valve_body) :- 
                estado(thinckness_of_the_safety_valve_body, desconocido),
                ((estado(safety_valve_body_has_deffect_of_dazzling_and_rusting, yes), writeln('se requiere coordinación para renderizar y colorear el equipo')); 
                verificar(safety_valve_body_has_deffect_of_dazzling_and_rusting)).
            
verificar(safety_valve_body_has_deffect_of_dazzling_and_rusting) :- 
                estado(safety_valve_body_has_deffect_of_dazzling_and_rusting, desconocido), 
                writeln('Verificar el cuerpo de la valvula de seguridad ').
/*  Rama Derecha    */
verificar(leakage_fixed_with_the_wrench) :- 
    estado(leakage_fixed_with_the_wrench, yes),
    writeln('Reportar para la inspeccion tecnica de la unidad').
verificar(leakage_fixed_with_the_wrench) :- 
    estado(leakage_fixed_with_the_wrench, no),
    writeln('el estado del equipo es aceptable ').
   
verificar(leakage_fixed_with_the_wrench) :- 
    estado(leakage_fixed_with_the_wrench, desconocido),
    (estado(gas_leakage_at_joint, no), writeln('enviar un reporte al departamento para arreglar la falla'));
    verificar(gas_leakage_at_joint).   

verificar(leakage_fixed_with_the_wrench) :- 
    estado(leakage_fixed_with_the_wrench, desconocido),
    (estado(gas_leakage_at_joint, yes), writeln('verificar si hay fuga de gas en la junta '));
    verificar(gas_leakage_at_joint).   
     
verificar(gas_leakage_at_joint) :- 
    estado(gas_leakage_at_joint, desconocido), 
    writeln('Verificar fuga de gas en la junta ').

/*  Rama Central Izquierda   */
verificar(piloto) :- 
    estado(piloto, yes), writeln('Setear la valvula de seguridad de acuerdo con las instrucciones').
verificar(piloto) :- 
    estado(piloto, no), writeln('Realizar un reparacion completa del piloto y reinstalarlo').

verificar(piloto) :- 
                estado(piloto, desconocido), 
                ((estado(leakage_prevention_between_sit_and_orifice, ok), writeln('Verificar Pilot'));
                verificar(leakage_prevention_between_sit_and_orifice)).

verificar(leakage_prevention_between_sit_and_orifice) :- 
                estado(leakage_prevention_between_sit_and_orifice, desconocido), 
                ((estado(safety_valve_spring, yes), writeln('Verificar leakage prevention between sit and orifice')); 
                verificar(safety_valve_spring)).

verificar(leakage_prevention_between_sit_and_orifice) :- 
                    estado(leakage_prevention_between_sit_and_orifice, desconocido), 
                    ((estado(safety_valve_spring, no), writeln('Reemplazar el asiento y el orificio y poner la valvula de seguridad en el circuito')); 
                    verificar(safety_valve_spring)).

verificar(safety_valve_spring) :- 
                estado(safety_valve_spring, desconocido), 
                ((estado(control_valve_sensors_blocked, no), writeln('Verificar safety valve spring')); 
                verificar(control_valve_sensors_blocked)).
verificar(safety_valve_spring) :- 
                estado(safety_valve_spring, desconocido), 
                ((estado(control_valve_sensors_blocked, yes), writeln('poner la valvula de seguridad y el resorte en servicio')); 
                verificar(control_valve_sensors_blocked)).
verificar(control_valve_sensors_blocked) :- 
                estado(control_valve_sensors_blocked, desconocido), 
                ((estado(valve_status_closed, no), writeln('Verificar control valve sensors blocked')); 
                verificar(valve_status_closed)).
verificar(control_valve_sensors_blocked) :- 
                estado(control_valve_sensors_blocked, desconocido), 
                ((estado(valve_status_closed, yes), writeln('limpiar y solucionar los problemas de sensado en las canerias')); 
                verificar(valve_status_closed)).
                
verificar(valve_status_closed) :- 
                estado(valve_status_closed, desconocido),
                ((estado(relief_valve_ok_with_10_percent_more_pressure, no), writeln('Verificar valve status "Close"'));
                verificar(relief_valve_ok_with_10_percent_more_pressure)).
verificar(valve_status_closed) :- 
                estado(valve_status_closed, desconocido),
                ((estado(relief_valve_ok_with_10_percent_more_pressure, yes), writeln('colocar la valvula de seguridad en posicion abierta'));
                verificar(relief_valve_ok_with_10_percent_more_pressure)).
                
verificar(relief_valve_ok_with_10_percent_more_pressure) :- 
                estado(relief_valve_ok_with_10_percent_more_pressure, desconocido),
                ((estado(safety_valve_has_continuous_evacuation, no), writeln('Verificar relief valve works correctly with +10% over regular pressure')); 
                verificar(safety_valve_has_continuous_evacuation)).
verificar(relief_valve_ok_with_10_percent_more_pressure) :- 
                estado(relief_valve_ok_with_10_percent_more_pressure, desconocido),
                ((estado(safety_valve_has_continuous_evacuation, yes), writeln('la funcion de seguridad es apropiada')); 
                verificar(safety_valve_has_continuous_evacuation)).
            
verificar(safety_valve_has_continuous_evacuation) :- 
                estado(safety_valve_has_continuous_evacuation, desconocido), 
                writeln('Verificar safety valve has continuous evacuation').

/* Ground Facts de instancia variables (podrian resolverse mediante sensado o agregando la informacion interactivamente a la base de conocimientos) */
estado(thinckness_of_the_safety_valve_body, desconocido).
estado(safety_valve_body_has_deffect_of_dazzling_and_rusting, desconocido).
estado(gas_leakage_at_joint,yes).
estado(leakage_fixed_with_the_wrench,yes).
estado(piloto, yes).
estado(leakage_prevention_between_sit_and_orifice, desconocido).
estado(safety_valve_spring, desconocido).
estado(control_valve_sensors_blocked, desconocido).
estado(valve_status_closed, no).
estado(relief_valve_ok_with_10_percent_more_pressure, no).
estado(safety_valve_has_continuous_evacuation, no).

