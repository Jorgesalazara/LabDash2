import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('ed_patient_data.csv')

fig, axes = plt.subplots(2, 2, figsize=(14, 9))
fig.suptitle('ED Patient Data — Overview', fontsize=15, fontweight='bold')

# 1. Wait time distribution per triage
for t in range(1, 6):
    subset = df[df['triage_level'] == t]['wait_time_minutes']
    axes[0,0].hist(subset, bins=30, alpha=0.6, label=f'Triage {t}')
axes[0,0].set_title('Wait Time Distribution by Triage Level')
axes[0,0].set_xlabel('Wait Time (minutes)')
axes[0,0].legend(fontsize=8)

# 2. Arrival volume by hour
df['hour'] = pd.to_datetime(df['arrival_datetime']).dt.hour
df.groupby('hour').size().plot(kind='bar', ax=axes[0,1], color='steelblue', edgecolor='white')
axes[0,1].set_title('Arrivals by Hour of Day')
axes[0,1].set_xlabel('Hour')
axes[0,1].set_ylabel('Count')

# 3. Disposition breakdown
df['disposition'].value_counts().plot(kind='barh', ax=axes[1,0], color='coral', edgecolor='white')
axes[1,0].set_title('Disposition Breakdown')
axes[1,0].set_xlabel('Count')

# 4. Staff on shift vs avg wait time
df.groupby('staff_on_shift')['wait_time_minutes'].mean().plot(
    kind='line', ax=axes[1,1], marker='o', color='green'
)
axes[1,1].set_title('Avg Wait Time vs Staff on Shift')
axes[1,1].set_xlabel('Staff Count')
axes[1,1].set_ylabel('Avg Wait (min)')

plt.tight_layout()
plt.savefig('ed_overview.png', dpi=150)
plt.show()
print(' Charts saved to ed_overview.png')
