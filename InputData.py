# SIMULATION SETTINGS
POP_SIZE = 2000
SIM_LENGTH = 50
ALPHA = 0.05
DISCOUNT = 0.03

ADD_BACKGROUND_MORT = True
DELTA_T = 1/4

PSA_ON = False

# TRANSITION MATRIX = 2000*annual transition probability
TRANS_MATRIX = [
    [1500, 300, 0, 200], #WELL
    [0, 0, 2000, 0], #STROKE
    [0, 500, 1100, 400],
]

# annual cost of each health state
ANNUAL_STATE_COST = [
    2756.0,   # CD4_200to500
    3025.0,   # CD4_200
    9007.0    # AIDS
    ]

# annual health utility of each health state
ANNUAL_STATE_UTILITY = [
    0.75,   # CD4_200to500
    0.50,   # CD4_200
    0.25    # AIDS
    ]

# annual drug costs
Zidovudine_COST = 2278.0
Lamivudine_COST = 2086.0

ANNUAL_PROB_BACKGROUND_MORT = 8.15 / 1000

TREATMENT_RR_anticoag = 1.05
TREATMENT_RR_CI = 1.05, 1.05 # lower 95% CI, upper 95% CI
