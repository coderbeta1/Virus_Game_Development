# Variable Explanation:
# 1. R0 = Basic Reproduction Number (R₀)
    # The average number of secondary infections produced by an infected individual in a completely susceptible
    # population.

# 2. infectionRate = Infection Rate
    # The probability of transmitting the virus from an infected person to a susceptible person during a
    # contact.

# 3. incubationPeriod = Incubation Period
    # The time between exposure to the virus and the onset of symptoms.

# 4. latencyPeriod = Latency Period
    # The time between exposure and when an infected person becomes capable of transmitting the virus.

# 5. infectiousPeriod = Infectious Period
    # The duration during which an infected individual is capable of transmitting the virus to others.

# 6. asymptomaticTransmission = Asymptomatic Transmission
    # The ability of asymptomatic or presymptomatic individuals to transmit the virus.

# 7. symptomSeverity = Symptom Severity
    # How severely infected individuals experience symptoms can influence their interactions and transmission dynamics.

# 8. populationDensity = Population Density
    # High population density can lead to more frequent and closer interactions, facilitating faster virus spread.

# 9. mobilityPatterns = Mobility Patterns
    # Movement of people between areas can introduce the virus to new regions and impact local transmission rates.

# 10. transportRoutes = Air Travel and Transportation
    # International and domestic travel can rapidly spread the virus across regions.

# 11. contactPattern = Contact Patterns
    # The frequency and nature of interactions between individuals, such as within households, workplaces, schools, and social gatherings.

# 12. hygienePractices = Hygiene Practices
    # Hand hygiene, mask-wearing, and respiratory etiquette can reduce virus transmission.

# 13. vaccinationCoverage = Vaccination Coverage
    # Higher vaccination rates can create herd immunity, slowing down virus spread.

# 14. immunitylevels = Immunity Levels
    # Prior immunity due to previous infection or vaccination can affect the susceptibility of individuals.

# 15. ageDistribution = Age Distribution
    # Different age groups may have varying susceptibility and severity of illness, affecting transmission rates.

# 16. healthcareCapacity = Healthcare Capacity
    # The availability of medical resources can influence the ability to manage and treat infected individuals.

# 17. PHI = Public Health Interventions
    # Measures like quarantine, isolation, social distancing, and lockdowns can limit virus transmission.

# 18. climate = Climate and Weather
    # Environmental factors can affect virus survival and transmission.

# 19. culture = Cultural and Social Factors
    # Cultural norms, beliefs, and behaviors can impact adherence to preventive measures.

# 20. govt_practice = Government Policies and Communication
    # Clear and timely communication from authorities can influence public compliance with preventive measures.

# 21. UR_setting = Urban vs. Rural Settings
    # Transmission dynamics can vary significantly between urban and rural areas.

# 22. economyFactors = Economic Factors
    # Economic disparities can affect the ability of individuals to follow preventive measures.

# 23. virusOrigin = Zoonotic Origins
    # The initial transmission from animals to humans can influence the virus's behavior in the human population.

# 24. mutationRate = Mutation Rate
    # Viral mutations can lead to changes in transmissibility and virulence.

# 25. superSpreadEvents = Super-Spreading Events
    # Large gatherings or events where many people are exposed to the virus by a single individual can lead to rapid transmission.

# 26. behavior = Behavioral Changes
    # Public perception, fear, and changes in behavior due to awareness of the virus can affect transmission.

# 27. healthcareAccess = Healthcare Access
    # Access to healthcare services can impact testing, treatment, and containment efforts.
    
# ptrans = Transmission probability.
# population = Total population within all containers.
# progression_period = Average number of days until a patient seeks treatment.
# progression_sd = Standard deviation of progression_period.
# interactions = Average number of interactions per person per day (decreases with social distancing).
# reinfection_rate = Probability of becoming susceptible again after recovery.
# I0 = Initial probability of being infected.
# death_rate = Probability of dying after being infected after progression_period and before recovery_days.
# recovery_days = Average number of days until recovery.
# recovery_sd = Standard deviation of recovery_days.
# severe = Probability of developing severe, symptomatic disease.
# steps = number of days in siimulation.

parameters = {'I0':0.01,
              'ptrans':0.25,
              'progression_period':3,
              'progression_sd':2,
              'population':1000,
              'interactions':12,
              'reinfection_rate':0.00,
              'death_rate':0.0193,
              'recovery_days':21,
              'recovery_sd':7,
              'severe':0.18,
              'steps':90}
