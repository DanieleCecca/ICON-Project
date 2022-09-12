:- dynamic(prop/3).
:- dynamic(prop/2).

% general class definition
prop(P, type, C) :- prop(S, subClassOf, C), prop(P, type, S).

% FACTS

% hostname (planetary system)
prop(k2_139_b, hostname, k2_139).
prop(k2_10_b, hostname, k2_10).
prop(k2_110_b, hostname, k2_110).
prop(k2_18_b, hostname, k2_18).
prop(k2_72_e, hostname, k2_72).
prop(wasp_118_b, hostname, wasp_118).
prop(wasp_75_b, hostname, wasp_75).
prop(wolf_503_b, hostname, wolf_503).
prop(trappist_1_b, hostname, trappist_1).
prop(trappist_1_c, hostname, trappist_1).
prop(trappist_1_f, hostname, trappist_1).
prop(trappist_1_g, hostname, trappist_1).
prop(hd_3167_d, hostname, hd_3167).
prop(ross_128_b, hostname, ross_128).
prop(gj_9827_b, hostname, gj_9827).

% discovery year
prop(k2_139_b, was_discovered_in, 2017).
prop(k2_10_b,was_discovered_in , 2016).
prop(k2_110_b, was_discovered_in ,2017).
prop(k2_18_b, was_discovered_in, 2016).
prop(k2_72_e, was_discovered_in , 2016).
prop(wasp_118_b, was_discovered_in, 2016).
prop(wasp_75_b,was_discovered_in ,  2013).
prop(wolf_503_b, was_discovered_in, 2018).
prop(trappist_1_b, was_discovered_in,2016).
prop(trappist_1_c, was_discovered_in, 2016).
prop(trappist_1_f,was_discovered_in , 2017).
prop(trappist_1_g,was_discovered_in ,2017).
prop(hd_3167_d,was_discovered_in ,2017).
prop(ross_128_b,was_discovered_in , 2017).
prop(gj_9827_b,was_discovered_in ,2017).

% radius in Earth Unit (6.371 km)
prop(k2_139_b, has_radius, 9.09).
prop(k2_10_b, has_radius, 4.24).
prop(k2_110_b, has_radius, 2.59).
prop(k2_18_b, has_radius, 2.24).
prop(k2_72_e, has_radius, 1.4).
prop(wasp_118_b, has_radius, 16.13).
prop(wasp_75_b, has_radius, 14.22).
prop(wolf_503_b, has_radius, 2.03).
prop(trappist_1_b,has_radius , 1.09).
prop(trappist_1_c, has_radius, 1.06).
prop(trappist_1_f, has_radius, 1.04).
prop(trappist_1_g, has_radius, 1.13).
prop(hd_3167_d,has_radius , 1.8).
prop(ross_128_b, has_radius, 1.15).
prop(gj_9827_b, has_radius, 1.04).

% mass in Earth Unit (5,9726×10e24 kg)
prop(k2_139_b, has_mass, 121.14).
prop(k2_10_b, has_mass, 27).
prop(k2_110_b,has_mass , 17.09).
prop(k2_18_b,has_mass , 16.46).
prop(k2_72_e,has_mass , 3.13).
prop(wasp_118_b, has_mass, 163.42).
prop(wasp_75_b,has_mass , 340.2).
prop(wolf_503_b, has_mass, 10.9).
prop(trappist_1_b,has_mass , 1.26).
prop(trappist_1_c, has_mass, 1.38).
prop(trappist_1_f, has_mass, 1.07).
prop(trappist_1_g, has_mass, 1.34).
prop(hd_3167_d,has_mass , 6.9).
prop(ross_128_b,has_mass , 1.4).
prop(gj_9827_b,has_mass , 8.2).

% density in Earth Unit (5,51 g/cm³)
prop(k2_139_b, has_density, 0.16).
prop(k2_10_b,has_density , 0.48).
prop(k2_110_b,has_density , 1.36).
prop(k2_18_b,has_density , 1.46).
prop(k2_72_e, has_density, 1.39).
prop(wasp_118_b, has_density, 0.04).
prop(wasp_75_b, has_density, 0.12).
prop(wolf_503_b,has_density , 1.31).
prop(trappist_1_b,has_density , 1.07).
prop(trappist_1_c,has_density , 1.17).
prop(trappist_1_f, has_density, 0.59).
prop(trappist_1_g,has_density , 1.34).
prop(hd_3167_d,has_density , 1.17).
prop(ross_128_b,has_density , 1.31).
prop(gj_9827_b, has_density, 2.28).

% gravity in Earth Unit (9,807 m/s²)
prop(k2_139_b, has_gravity, 1.46).
prop(k2_10_b, has_gravity, 2.23).
prop(k2_110_b,has_gravity , 2.49).
prop(k2_18_b, has_gravity, 3.28).
prop(k2_72_e, has_gravity, 1.39).
prop(wasp_118_b,has_gravity , 1.03).
prop(wasp_75_b, has_gravity, 2.08).
prop(wolf_503_b,has_gravity , 3.05).
prop(trappist_1_b,has_gravity , 1.13).
prop(trappist_1_c,has_gravity , 1.24).
prop(trappist_1_f, has_gravity, 1.01).
prop(trappist_1_g,has_gravity , 1.06).
prop(hd_3167_d, has_gravity, 2.12).
prop(ross_128_b, has_gravity, 1.05).
prop(gj_9827_b,has_gravity , 3.07).

% equilibrium temperature in Kelvin
prop(k2_139_b, has_temp, 508.0).
prop(k2_10_b, has_temp,658.8).
prop(k2_110_b, has_temp, 583.5).
prop(k2_18_b, has_temp, 249.8).
prop(k2_72_e,has_temp, 280.1).
prop(wasp_118_b, has_temp, 1576.2).
prop(wasp_75_b, has_temp, 1437.5).
prop(wolf_503_b, has_temp, 722.8).
prop(trappist_1_b, has_temp, 364.9).
prop(trappist_1_c, has_temp, 311.8).
prop(trappist_1_f, has_temp, 199.7).
prop(trappist_1_g, has_temp, 181.1).
prop(hd_3167_d, has_temp, 766.7).
prop(ross_128_b, has_temp, 280.0).
prop(gj_9827_b, has_temp, 1042.1).

% composition
prop(k2_139_b, has_composition, gas).
prop(k2_10_b, has_composition, water_gas).
prop(k2_110_b,has_composition , rocky_water).
prop(k2_18_b, has_composition, rocky_iron).
prop(k2_72_e, has_composition, rocky_iron).
prop(wasp_118_b,has_composition , gas).
prop(wasp_75_b, has_composition, gas).
prop(wolf_503_b,has_composition, rocky_iron).
prop(trappist_1_b,has_composition , rocky_water).
prop(trappist_1_c,has_composition , rocky_iron).
prop(trappist_1_f, has_composition, rocky_water).
prop(trappist_1_g,has_composition , rocky_iron).
prop(hd_3167_d,has_composition , rocky_iron).
prop(ross_128_b, has_composition, rocky_iron).
prop(gj_9827_b,has_composition, rocky_iron).

% atmosphere type
prop(k2_139_b,has_atmosphere, hydrogene_rich).
prop(k2_10_b, has_atmosphere, metals_rich).
prop(k2_110_b,has_atmosphere,metals_rich ).
prop(k2_18_b,has_atmosphere , hydrogene_rich).
prop(k2_72_e,has_atmosphere ,metals_rich ).
prop(wasp_118_b,has_atmosphere , metals_rich).
prop(wasp_75_b,has_atmosphere , metals_rich).
prop(wolf_503_b,has_atmosphere, metals_rich).
prop(trappist_1_b, has_atmosphere, metals_rich).
prop(trappist_1_c,has_atmosphere ,metals_rich).
prop(trappist_1_f,has_atmosphere ,metals_rich).
prop(trappist_1_g, has_atmosphere, metals_rich).
prop(hd_3167_d,has_atmosphere , metals_rich).
prop(ross_128_b,has_atmosphere , metals_rich).
prop(gj_9827_b,has_atmosphere, metals_rich).

% eccentricity
prop(k2_139_b,has_eccentricity, 0.12).
prop(k2_10_b, has_eccentricity,0.31).
prop(k2_110_b,has_eccentricity,0.08).
prop(k2_18_b, has_eccentricity, 0.2).
prop(k2_72_e,has_eccentricity, 0.01).
prop(wasp_118_b,has_eccentricity, 0).
prop(wasp_75_b,has_eccentricity, 0).
prop(wolf_503_b,has_eccentricity,0.41).
prop(trappist_1_b,has_eccentricity, 0).
prop(trappist_1_c, has_eccentricity, 0).
prop(trappist_1_f,has_eccentricity , 1.03).
prop(trappist_1_g,has_eccentricity, 1.01).
prop(hd_3167_d,has_eccentricity ,0.36).
prop(ross_128_b,has_eccentricity ,0.12).
prop(gj_9827_b,has_eccentricity,0).

% orbit period (days)
prop(k2_139_b,has_orbit_period, 28.38).
prop(k2_10_b,has_orbit_period, 19.30).
prop(k2_110_b,has_orbit_period, 14.26).
prop(k2_18_b,has_orbit_period, 33.34).
prop(k2_72_e,has_orbit_period, 24.17).
prop(wasp_118_b,has_orbit_period, 4.05).
prop(wasp_75_b,has_orbit_period, 2.48).
prop(wolf_503_b,has_orbit_period, 6).
prop(trappist_1_b,has_orbit_period, 1.510).
prop(trappist_1_c,has_orbit_period, 2.42).
prop(trappist_1_f,has_orbit_period, 9.21).
prop(trappist_1_g, has_orbit_period, 12.35).
prop(hd_3167_d,has_orbit_period, 8.49).
prop(ross_128_b,has_orbit_period, 10.27).
prop(gj_9827_b,has_orbit_period, 1.21).

% habitability zone distance (from his star)
prop(k2_139_b, distance_from_star, -2.37).
prop(k2_10_b,distance_from_star, -2.17).
prop(k2_110_b,distance_from_star, -2.07).
prop(k2_18_b,distance_from_star, -0.12).
prop(k2_72_e,distance_from_star, -0.16).
prop(wasp_118_b,distance_from_star, -2.46).
prop(wasp_75_b,distance_from_star, -2.43).
prop(wolf_503_b,distance_from_star, -2.17).
prop(trappist_1_b,distance_from_star, -1.48).
prop(trappist_1_c,distance_from_star, -1.41).
prop(trappist_1_f,distance_from_star, 0.14).
prop(trappist_1_g, distance_from_star, 1.04).
prop(hd_3167_d,distance_from_star, -2.24).
prop(ross_128_b,distance_from_star, -1.39).
prop(gj_9827_b,distance_from_star, -2.23).

% number of stars in the system
prop(k2_139_b,has_stars_in_sys, 1).
prop(k2_10_b,has_stars_in_sys, 1).
prop(k2_110_b,has_stars_in_sys, 1).
prop(k2_18_b,has_stars_in_sys, 1).
prop(k2_72_e,has_stars_in_sys, 1).
prop(wasp_118_b,has_stars_in_sys, 1).
prop(wasp_75_b,has_stars_in_sys, 2).
prop(wolf_503_b,has_stars_in_sys, 1).
prop(trappist_1_b,has_stars_in_sys, 1).
prop(trappist_1_c,has_stars_in_sys, 7).
prop(trappist_1_f,has_stars_in_sys, 1).
prop(trappist_1_g, has_stars_in_sys,1).
prop(hd_3167_d,has_stars_in_sys, 1).
prop(ross_128_b,has_stars_in_sys, 1).
prop(gj_9827_b,has_stars_in_sys, 1).

% metallicity [star]
prop(k2_139_b,his_star_has_met, 0.23).
prop(k2_10_b,his_star_has_met, -0.07).
prop(k2_110_b, his_star_has_met, -0.3).
prop(k2_18_b,his_star_has_met, 0.12).
prop(k2_72_e, his_star_has_met, nan).
prop(wasp_118_b,his_star_has_met,0.16).
prop(wasp_75_b,his_star_has_met, 0.07).
prop(wolf_503_b,his_star_has_met, -0.47).
prop(trappist_1_b,his_star_has_met, 0.04).
prop(trappist_1_c,his_star_has_met, nan).
prop(trappist_1_f,his_star_has_met, 0.04).
prop(trappist_1_g,his_star_has_met, 0.04).
prop(hd_3167_d,his_star_has_met, 0.04).
prop(ross_128_b,his_star_has_met, -0.02).
prop(gj_9827_b,his_star_has_met, -0.028).

% effective temperature [star]
prop(k2_139_b, his_star_has_temp, 5287).
prop(k2_10_b, his_star_has_temp, 5620).
prop(k2_110_b, his_star_has_temp , 5010).
prop(k2_18_b, his_star_has_temp, 3503).
prop(k2_72_e, his_star_has_temp , 3497).
prop(wasp_118_b, his_star_has_temp, 6410).
prop(wasp_75_b, his_star_has_temp,  6100).
prop(wolf_503_b, his_star_has_temp, 4716).
prop(trappist_1_b, his_star_has_temp, 2550).
prop(trappist_1_c, his_star_has_temp, 2550).
prop(trappist_1_f, his_star_has_temp, 2550).
prop(trappist_1_g, his_star_has_temp, 2550).
prop(hd_3167_d, his_star_has_temp, 5367).
prop(ross_128_b, his_star_has_temp, 3192).
prop(gj_9827_b, his_star_has_temp, 4255).


% RULES
prop(P, has_volume, V) :-
    prop(P, has_density, D),
    prop(P, has_mass, M),
    V is M/D,
    write('(mass is in Earth Unit)').

% mass classification
prop(P, is_mass_class, T):-
    prop(P, has_mass, M),
    prop(M, defines, T).

prop(M, defines, terran) :-
    M > 0.5, M < 2.

prop(M, defines, superterran) :-
    M > 2, M < 10.

prop(M, defines, neptunian) :-
    M > 10, M < 50.

prop(M, defines, jovian) :-
    prop(P, has_mass, M),
    prop(P, has_composition, gas),
    M > 50, M < 5000.

% spectral classification [star]
prop(P, his_star_is_class, C) :-
    prop(P, his_star_has_temp, T),
    prop(T, defines, C).

prop(T, defines, f) :-
    T > 6000, T < 7500.

prop(T, defines, g)  :-
    T > 5200, T < 6000.

prop(T, defines, k) :-
    T > 3700, T < 5200.

prop(T, defines, m) :-
    T > 2400, T < 3700.

% zone classification (habitability)
prop(P, is_in_zone, Z):-
    prop(P, distance_from_star, D),
    prop(D, implies, Z).

prop(D, implies, hot) :-
    D < -1.40.

prop(D, implies, warm) :-
    D > -1.40.

% is an exoplanet made of rock?
prop(P, has_composition, rocky) :-
    prop(P, has_composition, rocky_iron);
    prop(P, has_composition, rocky_water).

% habitable exoplanets classification
prop(P, is_in_habitable_class, C) :-
    prop(P, is_habitable, true),
    prop(P, has_temp, T),
    prop(T, states, C).

prop(T, states, hypopsychroplanet) :-
    T < 190.

prop(T, states, psychroplanet) :-
    T > 190, T < 240.

prop(T, states, mesoplanet) :-
    T > 240, T < 300.

% habitable function
prop(P, is_habitable, X) :-
    prop(P, is_in_zone, warm),
    prop(P, has_composition, rocky),
    prop(P, has_eccentricity, E),
    prop(P, has_temp, T),
    prop(P, has_stars_in_sys, N),
    E > 0.00, T < 3500,  N is 1
    -> X = true; X = false.

% in-habitable function
prop(P, is_inhabitable, X) :-
    prop(P, has_critic_conditions),
    X = true.

prop(P, has_critic_conditions) :-
    prop(P, is_in_zone, hot);
    prop(P, is_mass_class, jovian);
    prop(P, has_more_than_one_star).

prop(P, has_more_than_one_star):-
    prop(P, has_stars_in_sys, N),
    N > 1.

% description
get_info_about(Planet) :-
    prop(Planet, hostname, Star),
    write(Planet),
    write(' is an exoplanet in a planetary system whose star is '),
    write(Star),
    prop(Planet, is_mass_class, Class),
    write(', it was classified by mass as a '),
    write(Class),
    prop(Planet, was_discovered_in, Year),
    write(' and it was discovered in '),
    write(Year).

get_systems :-
    prop(_, hostname, Star),
    write(Star).

% get all the exoplanets (tutti quelli che hanno un hostname, quindi
% tutti, nonostante si sarebbe potuto usare qls altro predicato perché
% sono tutti 'avvalorati')
get_exoplanets :-
    prop(Planet, hostname, _),
    write(Planet).

is_habitable(P) :-
    prop(P, is_in_zone, warm),
    prop(P, has_composition, rocky),
    prop(P, has_eccentricity, E),
    prop(P, has_temp, T),
    prop(P, has_stars_in_sys, N),
    E > 0.00, T < 3500,  N is 1,
    true.


