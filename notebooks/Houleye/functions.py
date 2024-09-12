def calculate_completion_rates(df, steps):

    last_occurrences = {}
    clients_sets = {}

    for step in steps:
        last_occurrences[step] = df[df['process_step'] == step].groupby('client_id').last()
        clients_sets[step] = set(last_occurrences[step].index)

    total_clients_started = len(clients_sets[steps[0]])

    completion_rates = {}

    for i, step in enumerate(steps[1:], start=1):
        total_clients_step = len(clients_sets[step])
        completion_rate_step = total_clients_step / total_clients_started if total_clients_started > 0 else 0
        completion_rates[f" Completion Rate {step}"] = completion_rate_step

    return completion_rates


def calculate_avg_time_to_conversion(df, max_conversion_time_hours=1):

    # Explicit conversion of 'date_time' column to datetime format
    df['date_time'] = pd.to_datetime(df['date_time'])

    # Filter customers who have completed all steps up to 'confirm'.
    df_conversion = df[df['client_id'].isin(df[df['process_step'] == 'confirm']['client_id'])]

    # Filter data for 'start' and 'confirm' steps
    df_conversion_start = df_conversion[df_conversion['process_step'] == 'start']
    df_conversion_confirm = df_conversion[df_conversion['process_step'] == 'confirm']

    # Merge data to obtain start and confirmation dates for each customer
    df_time_to_conversion = pd.merge(df_conversion_start[['client_id', 'date_time']],
                                     df_conversion_confirm[['client_id', 'date_time']],
                                     on='client_id', suffixes=('_start', '_confirm'))

    # Calculate time to conversion in seconds
    df_time_to_conversion['time_to_conversion'] = (
        df_time_to_conversion['date_time_confirm'] - df_time_to_conversion['date_time_start']
    ).dt.total_seconds()

    # Filter out outliers (e.g. conversion time greater than max_conversion_time_hours)
    df_time_to_conversion = df_time_to_conversion[
        df_time_to_conversion['time_to_conversion'] < max_conversion_time_hours * 3600
    ]

    # Calculate average conversion time in minutes
    avg_time_to_conversion = df_time_to_conversion['time_to_conversion'].mean() / 60  # Conversion in minutes

    return avg_time_to_conversion


import pandas as pd

def time_spent_step(df, threshold=3600):
    df['date_time'] = pd.to_datetime(df['date_time'])
    df = df.sort_values(['client_id', 'date_time'])
    df['previous_time'] = df['date_time'].shift(1)
    df['previous_client'] = df['client_id'].shift(1)
    df['previous_step'] = df['process_step'].shift(1)

    df['time_spent'] = df.apply(
        lambda row: (row['date_time'] - row['previous_time']).total_seconds() if row['client_id'] == row['previous_client'] else None,
        axis=1
    )

    df = df[df['time_spent'] <= threshold]

    df_valid_transitions = df.dropna(subset=['time_spent'])

    avg_time_per_step = df_valid_transitions.groupby('previous_step')['time_spent'].mean()/60

    return avg_time_per_step

dataframes = {
    'Group Test': df_test,
    'Group Control': df_control,
    'Group No Participation': df_no_participation
}

time_spent_df = pd.DataFrame()

for name, df in dataframes.items():
    avg_time = time_spent_step(df)
    avg_time = avg_time.to_frame(name='avg_time_per_step')  
    time_spent_df = pd.concat([time_spent_df, avg_time], axis=1)


time_spent_df.to_csv('/Users/houleyeanne/Documents/GitHub/WEEK5/-vanguard_ab_test_week5_project/tableau/kpis/time_spent_df.csv', index=True)


print(time_spent_df)




#Defining the function that calculates error rate
def detect_backwards_steps(df):

    df['previous_step'] = df['process_step'].shift(1)

    df['previous_client'] = df['client_id'].shift(1)

    df['step_back'] = (df['client_id'] == df['previous_client']) & (df['process_step'] < df['previous_step'])

    backwards_steps = df[df['step_back']]

    clients_backwards = backwards_steps['client_id'].unique()

    clients_started = df[df['process_step'] == 'start']['client_id'].nunique()

    clients_with_errors = len(clients_backwards)

    error_rate = clients_with_errors / clients_started if clients_started > 0 else 0

    return error_rate


def calculate_error_recovery_rate(df):

    # Detect backward steps (previous step > current step)
    df['previous_step'] = df['process_step'].shift(1)
    df['previous_client'] = df['client_id'].shift(1)
    df['step_back'] = (df['client_id'] == df['previous_client']) & (df['process_step'] < df['previous_step'])

    # Clients who made a mistake (backward step)
    clients_with_errors = df[df['step_back']]['client_id'].nunique()

    # Clients who made a mistake and then completed the process
    clients_with_errors_completed = df[(df['client_id'].isin(df[df['step_back']]['client_id'])) &
                                       (df['process_step'] == 'confirm')]['client_id'].nunique()

    # Error recovery rate
    error_recovery_rate = (clients_with_errors_completed / clients_with_errors) if clients_with_errors > 0 else 0

    return error_recovery_rate


def drop_off_rate(df):

    drop_off_rates = {}
    steps = ['start', 'step_1', 'step_2', 'step_3', 'confirm']

    for i in range(len(steps) - 1):
        step_current = steps[i]
        step_next = steps[i + 1]

        clients_current = df[df['process_step'] == step_current]['client_id'].nunique()
        clients_next = df[df['process_step'] == step_next]['client_id'].nunique()

        drop_off_rate = (clients_current - clients_next) / clients_current if clients_current > 0 else 0
        drop_off_rates[step_current] = drop_off_rate

    return drop_off_rates

dataframes = {
    'Group Test': df_test,
    'Group Control': df_control,
    'Group No Participation': df_no_participation
}

print("Drop off rate per step :")

for name, df in dataframes.items():
    rates = drop_off_rate(df)
    print(f"{name}:")

    for step, rate in rates.items():
        print(f"  {step} -> {rate:.2%}")
    print()




