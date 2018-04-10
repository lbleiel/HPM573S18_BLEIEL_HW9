import ParameterClasses as P
import MarkovModelClasses as MarkovCls
import SupportMarkovModel as SupportMarkov
import scr.SamplePathClasses as PathCls
import scr.FigureSupport as Figs
import InputData as I

# create a cohort
cohort = MarkovCls.Cohort(
    id=0,
    therapy=P.Therapies.MONO)

# simulate the cohort
simOutputs = cohort.simulate()

print("PROBLEM 3:")
SupportMarkov.print_outcomes(simOutputs, 'No therapy:')

cohort2 = MarkovCls.Cohort(
    id=0,
    therapy=P.Therapies.COMBO)

# simulate the cohort
simOutputs2 = cohort2.simulate()

print("PROBLEM 4:")
print(P.calculate_prob_matrix())

print("PROBLEM 5:")
SupportMarkov.print_outcomes(simOutputs2, 'Anticoagulation therapy:')

print("PROBLEM 6:")
print("With no therapy:")
PathCls.graph_sample_path(
    sample_path=simOutputs.get_survival_curve(),
    title='Survival curve',
    x_label='Simulation time step',
    y_label='Number of alive patients'
    )
print("With anticoagulation therapy:")
PathCls.graph_sample_path(
    sample_path=simOutputs2.get_survival_curve(),
    title='Survival curve',
    x_label='Simulation time step',
    y_label='Number of alive patients'
    )

print("PROBLEM 7:")
print("With no therapy:")
Figs.graph_histogram(
    data=simOutputs.get_survival_times(),
    title='Survival times of patients without coagulation therapy',
    x_label='Survival time (years)',
    y_label='Counts',
    bin_width=1
)
print("With anticoagulation therapy:")
Figs.graph_histogram(
    data=simOutputs2.get_survival_times(),
    title='Survival times of patients with coagulation therapy',
    x_label='Survival time (years)',
    y_label='Counts',
    bin_width=1
)
