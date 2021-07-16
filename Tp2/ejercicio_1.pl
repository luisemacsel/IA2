/* Axiomas */

verificar(leaked_fixed_wrench_joints) :-
                estado(leaked_fixed_wrench_joints, x),
                ((estado(gas_leakage_at_joint, ok), writeln('Verificar leaked_fixed_wrench_joints'));
                verificar(gas_leakage_at_joint)).

verificar(gas_leakage_at_joint) :-
                estado(gas_leakage_at_joint, x),
                writeln('Verificar gas_leakage_at_joint').

%----------------------------------

verificar(thickness_treshold_limit) :-
                estado(thickness_treshold_limit, x),
                ((estado(valve_dazzling_and_rusting, ok), writeln('Verificar thickness_treshold_limit'));
                verificar(valve_dazzling_and_rusting)).

verificar(valve_dazzling_and_rusting) :-
                estado(valve_dazzling_and_rusting, x),
                writeln('Verificar valve_dazzling_and_rusting').

%-----------------------------------

verificar(preventable_leakage_between_sit_n_orifice) :-
                estado(preventable_leakage_between_sit_n_orifice, x),
                ((estado(safety_spring_effective, ok), writeln('Verificar preventable leakage between sit n orifice'));
                verificar(safety_spring_effective)).

verificar(safety_spring_effective) :-
                estado(safety_spring_effective, x),
                ((estado(control_preasure_sensor_pipes_blocked, ok), writeln('Verificar safety spring effective'));
                verificar(control_preasure_sensor_pipes_blocked)).

verificar(control_preasure_sensor_pipes_blocked) :-
                estado(control_preasure_sensor_pipes_blocked, x),
                ((estado(line_gas_pressure_appropriate, ok), writeln('Verificar control preasure sensor pipes blocked'));
                verificar(line_gas_pressure_appropriate)).

verificar(line_gas_pressure_appropriate) :-
                estado(line_gas_pressure_appropriate, x),
                ((estado(safety_valve_has_continuous_evacuation, ok), writeln('Verificar line gas pressure appropriate'));
                verificar(safety_valve_has_continuous_evacuation)).

%-----------------------------------

verificar(pilot_works_properly) :-
                estado(pilot_works_properly,  x),
                ((estado(leakage_prevention_between_sit_and_orifice, ok), writeln('Verificar Pilot'));
                verificar(leakage_prevention_between_sit_and_orifice)).

verificar(leakage_prevention_between_sit_and_orifice) :-
                estado(leakage_prevention_between_sit_and_orifice,  x),
                ((estado(safety_valve_spring, ok), writeln('Verificar leakage prevention between sit and orifice'));
                verificar(safety_valve_spring)).

verificar(safety_valve_spring) :-
                estado(safety_valve_spring,  x),
                ((estado(control_valve_sensors_blocked, no), writeln('Verificar safety valve spring'));
                verificar(control_valve_sensors_blocked)).

verificar(control_valve_sensors_blocked) :-
                estado(control_valve_sensors_blocked,  x),
                ((estado(valve_status_closed, no), writeln('Verificar control valve sensors blocked'));
                verificar(valve_status_closed)).

verificar(valve_status_closed) :-
                estado(valve_status_closed,  x),
                ((estado(relief_valve_ok_with_10_percent_more_pressure, no), writeln('Verificar valve status "Close"'));
                verificar(relief_valve_ok_with_10_percent_more_pressure)).

verificar(relief_valve_ok_with_10_percent_more_pressure) :-
                estado(relief_valve_ok_with_10_percent_more_pressure,  x),
                ((estado(safety_valve_has_continuous_evacuation, no), writeln('Verificar relief valve works correctly with +10% over regular pressure'));
                verificar(safety_valve_has_continuous_evacuation)).
            
verificar(safety_valve_has_continuous_evacuation) :-
                estado(safety_valve_has_continuous_evacuation,  x),
                writeln('Verificar safety valve has continuous evacuation').


:- dynamic(estado/2).

/* Ground Facts (se pueden modificar dinamicamente con assert y retract)*/
estado(pilot_works_properly,  x).
estado(leakage_prevention_between_sit_and_orifice,  x).
estado(safety_valve_spring,  x).
estado(control_valve_sensors_blocked,  x).
estado(valve_status_closed,  x).
estado(relief_valve_ok_with_10_percent_more_pressure,  x).
estado(safety_valve_has_continuous_evacuation,  x).
estado(preventable_leakage_between_sit_n_orifice, x).
estado(safety_spring_effective, x).
estado(control_preasure_sensor_pipes_blocked, x).
estado(line_gas_pressure_appropriate, x).
estado(thickness_treshold_limit, x).
estado(valve_dazzling_and_rusting, x).
estado(gas_leakage_at_joint, x).
estado(leaked_fixed_wrench_joints, x).
